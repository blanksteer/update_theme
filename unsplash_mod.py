from unsplash.api import Api
from unsplash.auth import Auth


def main():
    print("main function...do something")

def get_auth(client_id, client_secret, redirect_uri, code):
    auth = Auth(client_id, client_secret, redirect_uri, code=code)
    return Api(auth)


def keyword():
    print("keyword function...do something")
