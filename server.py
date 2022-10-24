"""
Auth0 Tech Talk Python Flask Example
"""
# Imports the necessary modules
import json
from os import environ as env
from urllib.parse import quote_plus, urlencode
from authlib.integrations.flask_client import OAuth
from dotenv import find_dotenv, load_dotenv
from flask import Flask, redirect, render_template, session, url_for
from secrets import token_bytes
from base64 import b64encode
import random

# List of comic images that /comic can display
comics = [
    'https://images.macrumors.com/t/-piFJMm-RGSkqx0ii-6SclOem9k=/400x0/article-new/2021/06/nathan-pyle-comic-2.jpg?lossy',
    'https://pbs.twimg.com/media/DzPIR5pWoAIoAr9.jpg:large',
    'https://cdn-images.threadless.com/threadless-media/artist_shops/shops/nathanwpyle/products/1087280/shirt-1563559370-6d30316cb3d3cacbb1f5acb60a756356.png?v=3&d=eyJvbmx5X21ldGEiOiBmYWxzZSwgImZvcmNlIjogZmFsc2UsICJvcHMiOiBbWyJ0cmltIiwgW2ZhbHNlLCBmYWxzZV0sIHt9XSwgWyJyZXNpemUiLCBbXSwgeyJ3aWR0aCI6IDk5Ni4wLCAiYWxsb3dfdXAiOiBmYWxzZSwgImhlaWdodCI6IDk5Ni4wfV0sIFsiY2FudmFzX2NlbnRlcmVkIiwgWzEyMDAsIDEyMDBdLCB7ImJhY2tncm91bmQiOiAiZmZmZmZmIn1dLCBbInJlc2l6ZSIsIFs4MDBdLCB7fV0sIFsiY2FudmFzX2NlbnRlcmVkIiwgWzgwMCwgODAwLCAiI2ZmZmZmZiJdLCB7fV0sIFsiZW5jb2RlIiwgWyJqcGciLCA4NV0sIHt9XV19',
    'https://images.squarespace-cdn.com/content/v1/5e746c6a3b9afb644bf2b580/1599059988924-OSRDUVNW6RKUYOS6CCEK/a1.png',
    'https://pbs.twimg.com/media/Dz9nY_jWwAEJQtp.jpg:large',
    'https://media.npr.org/assets/img/2019/12/12/imagine-pleasant-nonesense_custom-34cafb9feaaf590b0111a98033d8ddff361d215d-s800-c85.webp',
    'https://media.npr.org/assets/img/2019/12/12/1cb8aa81-2e51-4403-b67b-eb4d4ef4f949_custom-007b0efc510ca464c56115b36d45f55b9a9f7219-s800-c85.webp',
    'https://cdn-images.threadless.com/threadless-media/artist_shops/shops/nathanwpyle/products/978809/shirt-1554920343-214b8d695ff76938c20564b92839b88c.png?v=3&d=eyJvbmx5X21ldGEiOiBmYWxzZSwgImZvcmNlIjogZmFsc2UsICJvcHMiOiBbWyJ0cmltIiwgW2ZhbHNlLCBmYWxzZV0sIHt9XSwgWyJyZXNpemUiLCBbXSwgeyJ3aWR0aCI6IDk5Ni4wLCAiYWxsb3dfdXAiOiBmYWxzZSwgImhlaWdodCI6IDk5Ni4wfV0sIFsiY2FudmFzX2NlbnRlcmVkIiwgWzEyMDAsIDEyMDBdLCB7ImJhY2tncm91bmQiOiAiN2VhOGQ2In1dLCBbInJlc2l6ZSIsIFs4MDBdLCB7fV0sIFsiY2FudmFzX2NlbnRlcmVkIiwgWzgwMCwgODAwLCAiI2ZmZmZmZiJdLCB7fV0sIFsiZW5jb2RlIiwgWyJqcGciLCA4NV0sIHt9XV19'
]

# Load environment variables
ENV_FILE = find_dotenv()    # search for a .env file
if ENV_FILE:
    load_dotenv(ENV_FILE)   # load environment variables

# Initializes a Python web application(https://flask.palletsprojects.com/en/2.2.x/api/,
# https://www.fullstackpython.com/wsgi-servers.html)
app = Flask(__name__)

# Generates a long random 32 digit hexadecimal string to serve as a secret_key.
# A secret_key is used for securely signing the session cookie to make sure that data stored in
# the cookie has not been tampered with. 
app.secret_key = b64encode(token_bytes(32)).decode()
print("app.secret_key = {}".format(app.secret_key))

# Creates a registry for remote applications. 
oauth = OAuth(app)

# register a remote application on the OAuth registry
# https://connect2id.com/blog/oauth-openid-connect-client-registration-explained
oauth.register(
    name = "auth0",
    client_id=env.get("AUTH0_CLIENT_ID"),       
    client_secret=env.get("AUTH0_CLIENT_SECRET"),
    client_kwargs={
        "scope": "openid profile email",
    },
    server_metadata_url=f'https://{env.get("AUTH0_DOMAIN")}/.well-known/openid-configuration',
)


# Controllers API

# @app.route("/") maps the home() function with the base URL such that
# the output of home() will be rendered on the browser if one navigates to baseURL (aka home page).
# If the user is logged in, home() will render home.html with additional information about the user. 
@app.route("/")
def home():
    # https://flask.palletsprojects.com/en/2.2.x/api/#flask.render_template
    # template_name_or_list = name of template
    # session and pretty are variables to be made available in the template
    session_information = session.get("user")
    session_information_as_json = json.dumps(session.get("user"), indent=4)
    # print("Args passed to render_template():")
    # print("session = {}".format(session_information))
    # print("pretty = {}".format(session_information_as_json))
    return render_template(
        template_name_or_list = "home.html",
        session=session_information,
        pretty=session_information_as_json,
    )

@app.route("/comic")
def comic():
    return render_template(
        template_name_or_list = "comic.html",
        comic_url = random.choice(comics)
    )

# @app.route("/login") maps the login() function with the "/login path" such that
# the output of login() will be rendered on the browser if one navigates to baseURL/hello.
# Since login() , user will be redirected to Auth0 to begin the authentication flow.
# Once the user has authenticated, Auth0 will redirect the client to the redirect_uri, which
# in this case is the /callback path
@app.route("/login") 
def login():
    callback_URL = url_for("callback", _external=True)
    print("callback_URL = {}".format(callback_URL))
    return oauth.auth0.authorize_redirect(
        redirect_uri= callback_URL
    )

# This route is unseen by the user, as it is accessed after the user submits their 
# authentication credentials and before the user is redirected back to the homepage.
# The route first saves the session for the user (in the form of a token) so that 
# they don't have to sign back in again if they revisit this web app within 
# the allowed timeframe. After that, it'll redirect the user back to the homepage. 
@app.route("/callback", methods=["GET", "POST"])
def callback():
    token = oauth.auth0.authorize_access_token()
    session["user"] = token
    return redirect("/")


@app.route("/logout")
def logout():
    session.clear()
    return redirect(
        "https://"
        + env.get("AUTH0_DOMAIN")
        + "/v2/logout?"
        + urlencode(
            {
                "returnTo": url_for("home", _external=True),
                "client_id": env.get("AUTH0_CLIENT_ID"),
            },
            quote_via=quote_plus,
        )
    )


# When this server.py is executed, run the web app locally on port 3000
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=env.get("PORT", 3000))
