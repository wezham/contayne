from atlassian.jira import Jira as JiraClient


class Jira:
    def __init__(self, url: str, user, api_token: str) -> None:
        """Initialize the Jira client.

        Assume API token authentication for now.
        """
        self.client = JiraClient(url=url, username=user, password=api_token, cloud=True)

    def get_jira_version(self) -> str:
        """Get the version of Jira."""
        return self.client.get_server_info()

    def find_user_id_by_email(self, user_string: str) -> str | None:
        """Find a user's ID by their email address.

        Returns:
            The user's ID if found, otherwise None.
        """
        try:
            users_found = self.client.user_find_by_user_string(
                query=user_string, include_inactive_users=False
            )
            if users_found:
                return users_found[0]["accountId"]
        except Exception:
            return None

        return None

    def deactivate_user(self, user_id: str) -> dict:
        """Deactivate a user.

        According to this article, a user who is de-activated will have their sessions killed.
        https://jira.atlassian.com/browse/CONFSERVER-59978?page=com.atlassian.jira.plugin.system.issuetabpanels%3Aworklog-tabpanel


        Raises:
            JiraError: If the API call fails.
        """
        return {}

    def activate_user(self, user_id: str) -> dict:
        """Activate a user.

        Raises:
            JiraError: If the API call fails.
        """
        return {}
