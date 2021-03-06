# coding:utf-8
import random

# 並びは、挨拶, 国旗の絵文字
GREETING_LIST = [
    ("こんにちは！", ":jp:"),
    ("Hello!", ":us:"),
    ("ニーハオ!", ":cn:"),
]


def get_greeting() -> str:
    greetword, kokki = random.choice(GREETING_LIST)
    return "{}ノアイサツデス :robot_face: 「{}」".format(kokki, greetword)


def call_function(arg: str = "") -> str:
    return get_greeting()
