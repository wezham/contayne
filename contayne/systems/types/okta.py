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
            name=data.get("name"),
            user_id=data.get("userId"),
            token_window=data.get("tokenWindow"),
            id=data.get("id"),
            client_name=data.get("clientName"),
            expires_at=data.get("expiresAt"),
            created=data.get("created"),
            last_updated=data.get("lastUpdated"),
            _links=data.get("_links"),
        )
