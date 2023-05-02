import json
import sys

from datetime import datetime

import requests

from wordcloud import WordCloud


GITHUB_API_URL = "https://api.github.com"


def get_stargazer_list(token, repository_name):
    """

    :param token:
    :param repository_name:
    :return:
    """

    stargazer_username_list = []
    page = 1
    while True:
        url = "%s/repos/%s/stargazers" % (GITHUB_API_URL, repository_name)
        print("%s?page=%i" % (url, page))
        r = requests.get(
            url=url,
            headers={
                "Accept": "application/vnd.github.v3.star+json",
                "Authorization": "token %s" % token,
            },
            params={"page": page},
        )
        stargazer_list = json.loads(r.text)
        for stargazer in stargazer_list:
            stargazer_username_list.append(stargazer["user"]["login"])

        if len(stargazer_list) != 30:
            break
        page = page + 1
    return stargazer_username_list


def get_userinfo_list(username_list, token):
    """

    :param username_list:
    :param token:
    :return:
    """

    userinfo_list = []
    size = len(username_list)
    for i, username in enumerate(username_list):
        url = "%s/users/%s" % (GITHUB_API_URL, username)
        print("%d/%d %s" % (i + 1, size, url))
        r = requests.get(url="%s" % url, headers={"Authorization": "token %s" % token})
        r_body = json.loads(r.text)
        bio = r_body["bio"]
        if bio is not None:
            bio = bio.replace("\n", " ")
        userinfo_list.append(
            {"username": username, "location": r_body["location"], "bio": bio}
        )
    return userinfo_list


def create_word_cloud(userinfo_list, image_file_name, target="bio"):
    """

    :param userinfo_list:
    :param image_file_name:
    :param target:
    :return:
    """

    word_list = ""
    for userinfo in userinfo_list:
        if userinfo[target] is not None:
            word_list += userinfo[target] + "\n"

    stop_words = [
        "am",
        "is",
        "of",
        "and",
        "the",
        "to",
        "it",
        "for",
        "in",
        "as",
        "or",
        "are",
        "be",
        "this",
        "that",
        "will",
        "there",
        "was",
    ]
    word_cloud = WordCloud(
        background_color="white",
        # font_path='/System/Library/Fonts/HelveticaNeue.ttc',
        width=900,
        height=500,
        stopwords=set(stop_words),
    ).generate(word_list)
    word_cloud.to_file(image_file_name)


def list_to_file(filename, store_list):
    with open(filename, mode="w") as f:
        f.write("\n".join(store_list))


def json_to_file(filename, json_str):
    with open(filename, "w") as f:
        json.dump(json_str, f, indent=4)


def file_to_list(filename):
    with open(filename) as f:
        return f.read().split("\n")


def file_to_json(filename):
    with open(filename) as f:
        return json.loads(f.read())


if __name__ == "__main__":
    USERS_FILENAME = "1_stargazer_username_list.txt"
    USERINFO_JSON_FILE = "2_userinfo.json"

    if len(sys.argv) != 3:
        print(
            "  Using: python main.py 'Repository Name' 'OAuth Token'\n"
            "Example: python main.py 'nomi-sec/PoC-in-GitHub' 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'"
        )
        exit(1)

    repository_name = sys.argv[1]
    oauth_token = sys.argv[2]

    # Store stargazer users.
    username_list = get_stargazer_list(oauth_token, repository_name)
    list_to_file(USERS_FILENAME, username_list)

    # Store user information.
    userinfo_list = get_userinfo_list(file_to_list(USERS_FILENAME), oauth_token)
    json_to_file(USERINFO_JSON_FILE, userinfo_list)

    # Store word-cloud image.
    now = datetime.now().strftime("%Y%m%d_%H%M%S")
    create_word_cloud(
        file_to_json(USERINFO_JSON_FILE), "word_cloud_%s.png" % now, target="bio"
    )
