# Group 6 - Auth0 Tech Talk Demo

This sample demonstrates how to create a simple Python web app that shows comics to
authenticated users

# Set-up
1. Clone this git repository and navigate into it
```
    
```
2. Create an account
    * Go to [Auth0](https://auth0.com) and click Sign Up.
    * Use Google, GitHub or Microsoft Account to login.
3. 

# Running the App

To run the sample, make sure you have `python3` and `pip` installed.

Rename `.env.example` to `.env` and populate it with the client ID, domain, secret, callback URL and audience for your
Auth0 app. If you are not implementing any API you can use `https://YOUR_DOMAIN.auth0.com/userinfo` as the audience.
Also, add the callback URL to the settings section of your Auth0 client.

Register `http://localhost:3000/callback` as `Allowed Callback URLs` and `http://localhost:3000`
as `Allowed Logout URLs` in your client settings.

Run `pip install -r requirements.txt` to install the dependencies and run `python server.py`.
The app will be served at [http://localhost:3000/](http://localhost:3000/).


## What is Auth0?

Auth0 helps you to:

* Add authentication with [multiple authentication sources](https://auth0.com/docs/identityproviders),
either social like **Google, Facebook, Microsoft Account, LinkedIn, GitHub, Twitter, Box, Salesforce, among others**,or
enterprise identity systems like **Windows Azure AD, Google Apps, Active Directory, ADFS or any SAML Identity Provider**.
* Add authentication through more traditional **[username/password databases](https://docs.auth0.com/mysql-connection-tutorial)**.
* Add support for **[linking different user accounts](https://auth0.com/docs/link-accounts)** with the same user.
* Support for generating signed [JSON Web Tokens](https://auth0.com/docs/jwt) to call your APIs and
**flow the user identity** securely.
* Analytics of how, when and where users are logging in.
* Pull data from other sources and add it to the user profile, through [JavaScript rules](https://auth0.com/docs/rules).

## Create a free account in Auth0

1. Go to [Auth0](https://auth0.com) and click Sign Up.
2. Use Google, GitHub or Microsoft Account to login.

## References and Resources:
1. [Auth0's 'Add login to your Python Flask app' quickstart] (https://auth0.com/docs/quickstart/webapp/python/interactive)
2. [Auth0's collection of Quickstart tutorials] (https://auth0.com/docs/quickstarts)
3. [Intro to OpenIDConnect] (https://auth0.com/resources/webinars/intro-openid-connect/thankyou)