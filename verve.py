import click
import os
import requests
from bs4 import BeautifulSoup

content = ""

text = []
curText = ""

def index():
    global content, text
    for i in content:
        if i.startswith("["):
            i = i[1:-1]
            filename = i
            i = os.path.normpath(i)
            with open(i, "r") as f:
                text.append([f.read(), filename])
        if i.startswith("{"):
            i = i[1:-1]
            res = BeautifulSoup(requests.get(i).content, "html.parser")
            text.append([res.get_text(), i])
    # print(text)
    repl()

def find(st):
    global curText
    return st in curText

def repl():
    while True:
        command = input(">>> ")
        if command == "exit": break
        for i in text:
            global curText
            curText = i[0]
            if eval(command):
                print(f"Find in {i[1]}")

@click.command()
@click.argument("filename")
def verve(filename):
    global content
    with open(filename, "r") as f:
        content = f.read()
    content = content.split("\n")
    index()

if __name__ == "__main__":
    verve()