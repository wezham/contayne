from slack_sdk import WebClient


class Slack:
    """Implements common containment actions available via the Slack API."""

    def __init__(self, token: str):
        self.client = WebClient(token=token)

    def find_user_id_by_email(self, email: str) -> str | None:
        """Find a user's ID by their email address.

        Returns:
            The user's ID if found, otherwise None.
        """
        response = self.client.users_lookupByEmail(email=email)
        try:
            return response["user"]["id"]
        except KeyError:
            return None

    def fetch_all_users(self) -> list[dict]:
        """Fetch all users."""
        response = self.client.users_list()

        users = response.data["members"]
        while cursor := response.data["response_metadata"].get("next_cursor"):
            response = self.client.users_list(cursor=cursor)
            users.extend(response.data["members"])
        return users

    def find_team_id_for_user(self, user_id: str):
        """Find the team ID for a user.

        Returns:
            The team ID for the user.
        """
        response = self.client.users_info(user=user_id)
        return response["user"]["team_id"]

    def terminate_all_sessions(
        self, user_id: str, mobile_only: bool = True, web_only: bool = True
    ) -> bool:
        """Kill all sessions for a user.

        Raises:
            SlackApiError: If the API call fails.
        """
        return self.client.admin_users_session_reset(
            user_id=user_id, mobile_only=mobile_only, web_only=web_only
        ).validate()

    def remove_user_from_workspace(self, user_id: str, team_id: str) -> bool:
        """Remove a user from the workspace.

        Raises:
            SlackApiError: If the API call fails.
        """
        return self.client.admin_users_remove(user_id=user_id, team_id=team_id).validate()

    def readd_user_to_workspace(self, user_id: str, team_id: str):
        """Re-add a user to the workspace.

        Raises:
            SlackApiError: If the API call fails.
        """
        return self.client.admin_users_assign(user_id=user_id, team_id=team_id).validate()
