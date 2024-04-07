from dataclasses import dataclass

import requests


@dataclass
class OktaError:
    """Represents an error returned by the Okta API."""

    error_code: str | None
    error_summary: str | None
    error_id: str | None
    error_link: str | None
    error_causes: list[str] | None

    @staticmethod
    def from_dict(data: dict) -> "OktaError":
        """Create an OktaError instance from a dictionary."""
        return OktaError(
            error_code=data.get("errorCode"),
            error_summary=data.get("errorSummary"),
            error_id=data.get("errorId"),
            error_link=data.get("errorLink"),
            error_causes=data.get("errorCauses", []),
        )


class OktaApiException(Exception):
    """An exception raised when an Okta API call fails."""

    def __init__(self, error: OktaError):
        self.error = error
        super().__init__(error.error_summary)


class Okta:
    """Implements common containment actions available via the Okta API."""

    def __init__(self, tenant_domain: str, api_key):
        self.api_base_url = f"https://{tenant_domain}/api/v1"
        self.api_key = api_key

    def make_api_call(
        self,
        method: str,
        api_endpoint: str,
        params: dict | None = None,
        data: dict | None = None,
        parse_json: bool = True,
    ) -> dict | str:
        """Make an API call to Okta.

        Params:
            parse_json: If True, the response will be parsed as JSON.
        Raises:
            OktaApiException: If the API call fails.
        """
        url = f"{self.api_base_url}{api_endpoint}"
        headers = {"Authorization": f"SSWS {self.api_key}"}
        response = requests.request(method, url, params=params, json=data, headers=headers)
        if 400 <= response.status_code < 500:
            raise OktaApiException(OktaError.from_dict(response.json()))
        if parse_json is True:
            return response.json()
        return response.text

    def find_user_id_by_email(self, email: str) -> str | None:
        """Find a user's ID by their email address.

        Returns:
            The user's ID if found, otherwise None.
        """
        result = self.make_api_call("GET", f"/users/{email}")
        if isinstance(result, OktaError):
            return None
        return result["id"]

    def terminate_user_sessions(self, user_id: str) -> dict:
        """Kill session for a user.

        Raises:
            OktaApiException: If the API call fails.
        """
        return self.make_api_call("DELETE", f"/users/{user_id}/sessions", parse_json=False)

    def suspend_user(self, user_id: str) -> dict:
        """Suspend a user.

        Raises:
           OktaApiException: If the API call fails.
        """
        return self.make_api_call("POST", f"/users/{user_id}/lifecycle/suspend")
