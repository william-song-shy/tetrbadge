from flask import Flask, request, redirect
import requests

app = Flask(__name__)


@app.route('/')
def main():
    user = request.args.get('user')
    style = request.args.get('style', default='for-the-badge')
    st = request.args.get('st')

    if st == 'f1':
        style = 'flat'
    if st == 'f2':
        style = 'flat-square'

    url = f'https://ch.tetr.io/api/users/{user}'
    r = requests.get(url).json()

    appendix = f'?longCache=true&style={style}&logo=data:image/png;base64,' \
               'iVBORw0KGgoAAAANSUhEUgAAAQAAAAEABAMAAACuXLVVAAAALVBMVEVHcEwAAAAAAAAFBQUbVXofaJZ9VtCNL37JRJ+lOYQVkZ1+X' \
               '+PAQKrfTqovUaqjn7QgAAAACnRSTlMAIBEwc7rMdcFvX68ANQAAAeNJREFUeNrt3b1Nw0AYxnErG9i3gHMbWIQJCA0tsAIzUKRGNGwAC7ACPRUDhIKOmhkQBsUBvVzuzmfuwvt/HLnKxy/vk5OiKPJVLyNTjQ0AAAAA7D+gjT7SAGxssgOs+glQARVQQSpAPY84UlZQx6RJOYFYgO4JWCooYQIpAaauu5BT4go65RUcBCb5KogGtOoBVEAF+SbQFVbBtZQb6aXW4l3FV1ksPbLo0yNmn1+Ue1z/BHcS4Nn/bZ7ce2cLMFcPoAIAfAYAAAAAAAAAAAAAAAAAAAAAAABKAlxKP8peXUg5l3Im/TR7HABYPQl5fJDyJuVUGsshAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAE0A+U+t4v9fpwGIeR2uwLB9RaYsgKYEgFU9AUsF6leBpQImQAVUQAVUQAVUQAVUQAVUQAVUQAVU8J8qWHrnaBrA6IvlZgO06gFUQAVUIFZgvjY4uPUHBG+eYHZMYHJAXQrAqp9AYkDncdtseeKowEQAzGbxuNMN9yu7go9ZrfZzFRjnefcE7FhA4zz/tqHSFmBIAGD0xmrZAK4JtLkBVGCpQMUqKGsCs+r7EQD4+VD/w5UAQDVJAAAAAOAPAe84sSSYxpxAFAAAAABJRU5ErkJggg=='

    if not r.get('success'):
        return redirect(f'https://img.shields.io/badge/{user}-User does not exist-lightgrey.svg{appendix}')

    rating = int(r["data"]["user"]["league"]["rating"])
    rank = r["data"]["user"]["league"]["rank"]
    if rating == -1:
        win = r["data"]["user"]["league"]["gameswon"]
        play = r["data"]["user"]["league"]["gamesplayed"]
        rating = win + '/' + play

    if rank == "z":
        color = "-808080"
        rank = "%3F"
    elif rank == "d":
        color = "-9e81a1"
    elif rank == "d+":
        color = "-9a67a0"
    elif rank == "c-":
        color = "-84679b"
    elif rank == "c":
        color = "-7c4e9e"
    elif rank == "c+":
        color = "-5b3399"
    elif rank == "b-":
        color = "-5651c7"
    elif rank == "b":
        color = "-5b73df"
    elif rank == "b+":
        color = "-52a6c8"
    elif rank == "a-":
        color = "-49c38a"
    elif rank == "a":
        color = "-72d156"
    elif rank == "a+":
        color = "-23ab32"
    elif rank == "s-":
        color = "-e3e132"
    elif rank == "s":
        color = "-fbc90b"
    elif rank == "s+":
        color = "-ffe810"
    elif rank == "ss":
        color = "-fffb92"
    elif rank == "u":
        color = "-ff3013"
    elif rank == "x":
        color = "-ff5aff"
    else:
        color = "-black"
    rank.upper()

    url = f'https://img.shields.io/badge/{user}-{rank} {rating}{color}.svg{appendix}'
    # print(url)
    return redirect(url)
