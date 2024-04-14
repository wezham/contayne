import boto3

from contayne.systems.custom_types.aws import PoliciesDeleted


class AWS:
    def __init__(self, access_key: str, secret_key: str) -> None:
        self.client = boto3.client(
            "iam",
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key,
        )

    def list_users(self):
        paginator = self.client.get_paginator("list_users")
        response_iterator = paginator.paginate()

        users = []
        for response in response_iterator:
            if response.get("Users") is not None:
                users.extend(response["Users"])

        return users

    def delete_user(self, username: str):
        """Delete an IAM user."""
        return self.client.delete_user(UserName=username)

    def detach_user_policy(self, username: str, policy_arn: str):
        """Detach a policy from a user."""
        return self.client.detach_user_policy(UserName=username, PolicyArn=policy_arn)

    def detach_all_policies_for_user(self, username: str) -> PoliciesDeleted:
        """Detach all policies assigned to a user."""
        deleted_policies = PoliciesDeleted(attached_policies=[], inline_policies=[])

        attached_policies = self.client.list_attached_user_policies(UserName=username)
        for policy in attached_policies["AttachedPolicies"]:
            self.detach_user_policy(username, policy["PolicyArn"])
            deleted_policies["attached_policies"].append(policy["PolicyName"])

        policies = self.client.list_user_policies(UserName=username)

        for policy in policies["PolicyNames"]:
            self.detach_user_policy(username, policy["PolicyArn"])
            deleted_policies["inline_policies"].append(policy["PolicyName"])
        return deleted_policies

    def remove_user_from_group(self, username: str, group_name: str):
        """Remove a user from a group."""
        return self.client.remove_user_from_group(UserName=username, GroupName=group_name)

    def remove_user_from_all_groups(self, username: str) -> list[str]:
        """Remove a user from all groups."""
        groups = self.client.list_groups_for_user(UserName=username)

        removed_groups = []
        for group in groups["Groups"]:
            self.remove_user_from_group(username, group["GroupName"])
            removed_groups.append(group["GroupName"])
        return removed_groups
