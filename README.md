# Group 6 - Auth0 Tech Talk Demo

This sample demonstrates how to create a simple Python web app that shows comics to
authenticated users

# Set-up
1. Clone this git repository and navigate into it
```
    git clone https://github.com/hndo1220/auth0-techtalk-python-flask-demo.git
    cd auth0-techtalk-python-flask-demo
```
2. Make sure you have `python3` and `pip` installed
3. Run `pip install -r requirements.txt` to install the dependencies
4. Create an account
    * Go to [Auth0](https://auth0.com) and click Sign Up.
    * Use Google, GitHub or Microsoft Account to login.

5. Register and configure the Web App on Auth0
    * Navigate to your Auth0 Dashboard
    * Click Create Application
    * Set Application Name (ex: 'Auth0 Tech Talk Python Flask Demo')
    * Select Application type = 'Regular Web Applications'
    * Click on the 'Settings' tab
    * Note your Domain, Client ID and Client Secret
    * Copy `http://localhost:3000/callback` into the `Allowed Callback URLs` textbox
    * Copy `http://localhost:3000` into the `Allowed Logout URLs` textbox

6. Set up environment variables
    * Create an `.env` file in your project directory following the format of `.env template`
    * Copy your application's Auth0 Domain into the `AUTH0_DOMAIN` field
    * Copy your application's Client ID into the `AUTH0_CLIENT_ID` field
    * Copy your application's Client Secret into the `AUTH0_CLIENT_SECRET` field

# Running the App
7. Make sure you have `python3`, `pip` and the dependencies in `requirements.txt` installed
8. If you have not done so, navigate into the project's directory from the terminal 
`cd auth0-techtalk-python-flask-demo`
9. Run `python server.py`
10. Access the app at [http://localhost:3000/](http://localhost:3000/)

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
1. [Auth0's 'Add login to your Python Flask app' quickstart](https://auth0.com/docs/quickstart/webapp/python/interactive)
2. [Auth0's collection of Quickstart tutorials](https://auth0.com/docs/quickstarts)
3. [Intro to OpenIDConnect](https://auth0.com/resources/webinars/intro-openid-connect/thankyou)
4. [https://developer.okta.com/blog/2019/10/21/illustrated-guide-to-oauth-and-oidc](https://developer.okta.com/blog/2019/10/21/illustrated-guide-to-oauth-and-oidc)