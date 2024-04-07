# Description

Contayne is intended to be a library that implements common containment actions for SaaS products in your environment

# Services supported

1. Okta
1. Slack

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