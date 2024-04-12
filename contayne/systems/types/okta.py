from dataclasses import dataclass


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
