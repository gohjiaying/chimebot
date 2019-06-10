import json
import requests
import sys
import os

WEBHOOK_URI = os.environ['uri']
GIPHY_API = os.environ['api_key']

def post_message(event, content):
    response = None
    msg = format_chime_msg(get_random_dog_image())
    print (msg)
    try:
        response = requests.post(
            url=WEBHOOK_URI,
            json={"Content": msg})
        return json.loads(response.text)
    except:
        return response.text


def get_random_dog_image():
    giphy_url = "http://api.giphy.com/v1/gifs/random"
    response = None
    PARAMS = {
            "api_key":GIPHY_API,
            "tag" : "dog"
        }
    response = requests.get(
        url = giphy_url,
        params = PARAMS
    )

    dog_gif_url = json.loads(response.text)["data"]["image_url"]
    return dog_gif_url

def format_chime_msg(url):
    return "/md **Good Morning Ariel!** &nbsp; ![Alt Text](" + url + ") &nbsp; Here is your daily dog dose: " + url


# def main():
#     post_message("test", "test")


# main()
