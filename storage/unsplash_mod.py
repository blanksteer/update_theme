from unsplash.api import Api
from unsplash.auth import Auth

def main():

def get_auth():
    auth = Auth(client_id, client_secret, redirect_uri, code=code)
    api = Api(auth)

def keyword():