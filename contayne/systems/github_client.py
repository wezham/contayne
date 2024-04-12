from github import Github as GithubClient


class Github:
    def __init__(self, organisation_name: str, api_token: str) -> None:
        self.client = GithubClient(api_token)
        self.org = self.client.get_organization(organisation_name)

    def list_all_users(self):
        """Fetch all users in your github org."""
        for user in self.org.get_members():
            yield user

    def block_user(self, username: str):
        """Block a user."""
        headers, data = self.client.__requester.requestJsonAndCheck(
            "PUT", f"/orgs/{self.org.login}/blocks/{username}"
        )
        return headers, data

    def unblock_user(self, username: str):
        """Unblock a user."""
        headers, data = self.client.__requester.requestJsonAndCheck(
            "DELETE", f"/orgs/{self.org.login}/blocks/{username}"
        )
        return headers, data
