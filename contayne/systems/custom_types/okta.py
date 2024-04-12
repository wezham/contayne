from dataclasses import dataclass


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


@dataclass
class OktaAPIToken:
    name: str
    user_id: str
    token_window: str
    id: str
    client_name: str
    expires_at: str
    created: str
    last_updated: str
    _links: dict

    @staticmethod
    def from_dict(data: dict) -> "OktaAPIToken":
        """Create an OktaAPIToken instance from a dictionary."""
        return OktaAPIToken(
            name=data["name"],
            user_id=data["userId"],
            token_window=data["tokenWindow"],
            id=data["id"],
            client_name=data["clientName"],
            expires_at=data["expiresAt"],
            created=data["created"],
            last_updated=data["lastUpdated"],
            _links=data["_links"],
        )
