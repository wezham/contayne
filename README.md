# Problem statement

In the modern technology organisation, sensitive data lives in the cloud in tens or hundred of different applications.
Within your organisation, a user or entity has access to the data in these applications. As a security team, we want to be
able to respond and contain suspicious activity in these applications. To do this, we have tools like EDR solutions that help us contain on an endpoint. However, SAAS applications are still relatively new and suite of tools is less mature.

This library aims to solve the problem of containment in third party SaaS applications. It aims to be the building blocks for a more complex containment solution. This type of behaviour may already be bundled up in existing security solutions however this is intended for those without access to tools, or who want a more customisable option.

Containment can comee in many different forms. Some sceneraios and containment actions are listed below. Please raise issues for any more you would like to see:

| Event | Containment Action |
| ----- | ----- |
| A user session token is stolen | Revoking a user session |
| An api token looks like its being used to perform suspicious actions | Revoking an API Token |
| A user account has been confirmed as compromised | Suspending a user |


# Description

Contayne is intended to be a library that implements common containment actions for SaaS products in your environment

# Supported Services 
| Service | Containment Actions | Uncontain Actions | Supported |
| ------- | ------------------ | ----------------- | ----------- |
| Okta    | <ul><li>Revoking a user session</li><li>Revoking an API Token</li><li>Suspending a user</li></ul> | <li>Activate a user</li></ul> | Yes |
| Slack   | <ul><li>Revoke all user sessions</li><li>Suspend User</li> | <li>Activate User</li></ul>  | Yes |
| Github | <ul><li>Remove user from org</li><li>Remove org roles assigned to user</li></ul>| <ul><li>Add user to organisation</li></ul>| Yes |
| AWS | <ul><li>Detach policie(s) from IAM user</li><li>Delete IAM user</li><li>Remove user from all group(s)</li></ul>| | Yes |
| Workday | | | No |
| Azure AD | | | No |
| Salesforce | | | No |


# Usage

## Okta
```python
okta_client = Okta("sample.okta.com", API_TOKEN)
user_id = okta_client.find_user_id_by_email("test@test.com")
okta_client.terminate_user_sessions(user_id)
```
## Slack
```python
slack_client = Slack(API_TOKEN)
user_id = slack_client.find_user_id_by_email("test@test.com")
slack_client.terminate_all_sessions(user_id)
```

# How to

## Okta

1. Generate an API token
1. Provide that API token to the client in a secure fashion along with your tenant domain

## Slack

You will need an Enterprise Slack license. 

1. Choose how to authenticate to slack. I have used a Slack App
1. In the Oauth setup you'll need to grant your user token a few scopes. Those are:
    1. `admin.users:write`
    1. `users:read`
    1. `users:read.email`
    1. `admin` ?
1. Provide that API token in a secure fashion

## Jira

1. Create an API Token
2. Provide that API token in a secure fashion

## AWS

These are known required permissions:
```
"iam:ListUsers",
"iam:ListUserPolicies",
"iam:ListAttachedUserPolicies",
"iam:DeleteUserPolicy",
"iam:DetachUserPolicy",
"iam:ListGroupsForUser"
```

