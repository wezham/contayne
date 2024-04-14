from typing import TypedDict


class PoliciesDeleted(TypedDict):
    attached_policies: list[str]
    inline_policies: list[str]
