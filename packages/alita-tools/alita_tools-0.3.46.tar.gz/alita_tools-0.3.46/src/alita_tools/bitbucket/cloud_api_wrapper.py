from __future__ import annotations

import json
import logging
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Any

from atlassian.bitbucket import Bitbucket, Cloud
from langchain_core.tools import ToolException
from requests import Response
from ..ado.utils import extract_old_new_pairs

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

if TYPE_CHECKING:
    pass


class BitbucketApiAbstract(ABC):

    @abstractmethod
    def list_branches(self) -> str:
        pass

    @abstractmethod
    def create_branch(self, branch_name: str, branch_from: str) -> Response:
        pass

    @abstractmethod
    def create_pull_request(self, pr_json_data: str) -> Any:
        pass

    @abstractmethod
    def get_file(self, file_path: str, branch: str) -> str:
        pass

    @abstractmethod
    def create_file(self, file_path: str, file_contents: str, branch: str) -> str:
        pass


class BitbucketServerApi(BitbucketApiAbstract):
    api_client: Bitbucket

    def __init__(self, url, project, repository, username, password):
        self.url = url
        self.project = project
        self.repository = repository
        self.username = username
        self.password = password
        self.api_client = Bitbucket(url=url, username=username, password=password)

    def list_branches(self) -> str:
        branches = self.api_client.get_branches(project_key=self.project, repository_slug=self.repository)
        return json.dumps([branch['displayId'] for branch in branches])

    def create_branch(self, branch_name: str, branch_from: str) -> Response:
        return self.api_client.create_branch(
            self.project,
            self.repository,
            branch_name,
            branch_from
        )

    def create_pull_request(self, pr_json_data: str) -> Any:
        return self.api_client.create_pull_request(project_key=self.project,
                                                   repository_slug=self.repository,
                                                   data=json.loads(pr_json_data)
                                                   )

    def get_file(self, file_path: str, branch: str) -> str:
        return self.api_client.get_content_of_file(project_key=self.project, repository_slug=self.repository, at=branch,
                                                   filename=file_path).decode('utf-8')

    def create_file(self, file_path: str, file_contents: str, branch: str) -> str:
        return self.api_client.upload_file(
            project_key=self.project,
            repository_slug=self.repository,
            content=file_contents,
            message=f"Create {file_path}",
            branch=branch,
            filename=file_path
        )

    def update_file(self, file_path: str, update_query: str, branch: str) -> str:
        file_content = self.get_file(file_path = file_path, branch=branch)
        updated_file_content = file_content
        for old, new in extract_old_new_pairs(update_query):
            if not old.strip():
                continue
            updated_file_content = updated_file_content.replace(old, new)

        if file_content == updated_file_content:
            return (
                "File content was not updated because old content was not found or empty. "
                "It may be helpful to use the read_file action to get "
                "the current file contents."
            )


        source_commit_generator = self.api_client.get_commits(project_key=self.project, repository_slug=self.repository, hash_newest=branch, limit=1)
        source_commit = next(source_commit_generator)
        return self.api_client.update_file(
            project_key=self.project,
            repository_slug=self.repository,
            content=updated_file_content,
            message=f"Update {file_path}",
            branch=branch,
            filename=file_path,
            source_commit_id=source_commit['id']
        )

class BitbucketCloudApi(BitbucketApiAbstract):
    api_client: Cloud

    def __init__(self, url, workspace, repository, username, password):
        self.url = url
        self.workspace_name = workspace
        self.repository_name = repository
        self.username = username
        self.password = password
        self.api_client = Cloud(url=url, username=username, password=password)
        self.workspace = self.api_client.workspaces.get(self.workspace_name)
        try:
            self.repository = self.workspace.repositories.get(self.repository_name)
        except Exception as e:
            raise ToolException(f"Unable to connect to the repository '{self.repository_name}' due to error:\n{str(e)}")

    def list_branches(self) -> str:
        branches = self.repository.branches.each()
        branch_names = [branch.name for branch in branches]
        return ', '.join(branch_names)

    def _get_branch(self, branch_name: str) -> Response:
        return self.repository.branches.get(branch_name)

    def create_branch(self, branch_name: str, branch_from: str) -> Response:
        """
        Creates new branch from last commit branch
        """
        logger.info(f"Create new branch from '{branch_from}")
        commits_name = self._get_branch(branch_from).hash
        # create new branch from last commit
        return self.repository.branches.create(branch_name, commits_name)

    def create_pull_request(self, pr_json_data: str) -> Any:
        response = self.repository.pullrequests.post(None, data=json.loads(pr_json_data))
        return response['links']['self']['href']

    def get_file(self, file_path: str, branch: str) -> str:
        return self.repository.get(path=f'src/{branch}/{file_path}')

    def create_file(self, file_path: str, file_contents: str, branch: str) -> str:
        form_data = {
            'branch': f'{branch}',
            f'{file_path}': f'{file_contents}',
        }
        return self.repository.post(path='src', data=form_data, files={}, headers={'Content-Type': 'application/x-www-form-urlencoded'})

    def update_file(self, file_path: str, update_query: str, branch: str) -> str:

        file_content = self.get_file(file_path=file_path, branch=branch)
        updated_file_content = file_content
        for old, new in extract_old_new_pairs(file_query=update_query):
            if not old.strip():
                continue
            updated_file_content = updated_file_content.replace(old, new)

        if file_content == updated_file_content:
            return (
                "File content was not updated because old content was not found or empty. "
                "It may be helpful to use the read_file action to get "
                "the current file contents."
            )
        return self.create_file(file_path, updated_file_content, branch)