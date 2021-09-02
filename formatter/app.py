#!/usr/bin/env python3
import sys

import pyperclip

import settings


def get_formatted_text(text):
    for regex in settings.FORMATTED_RULES:
        text = regex["regex"].sub(regex["to"], text)
    return text


def main(*args, **kwargs):
    # TODO: settings
    text = pyperclip.paste()
    while True:
        if text == pyperclip.paste():
            continue

        new_text = get_formatted_text(pyperclip.paste().strip())
        pyperclip.copy(new_text)
        text = new_text


if __name__ == '__main__':
    print("string-formatter running...")
    main(sys.argv)
