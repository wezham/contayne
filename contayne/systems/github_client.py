from github import Github as GithubClient


class Github:
    def __init__(self, organisation_name: str, api_token: str) -> None:
        self.client = GithubClient(api_token)
        self.org = self.client.get_organization(organisation_name)

    def list_all_users(self):
        """Fetch all users in your github org."""
        for user in self.org.get_members():
            yield user

    def remove_user_from_organisation(self, username: str):
        """Remove a user."""
        headers, data = self.client.__requester.requestJsonAndCheck(
            "DELETE", f"/orgs/{self.org.login}/members/{username}"
        )
        return headers, data

    def add_user_to_organisation(self, username: str, role_type: str = "member"):
        """Add a user."""
        headers, data = self.client.__requester.requestJsonAndCheck(
            "PUT", f"/orgs/{self.org.login}/memberships/{username}", parameters={"role": role_type}
        )
        return headers, data

    def remove_all_org_roles_from_user(self, username: str):
        headers, data = self.client.__requester.requestJsonAndCheck(
            "DELETE",
            f"/{self.org}/organization-roles/users/{username}",
        )
        return headers, data
