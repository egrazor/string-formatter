from regexps import regexps

FORMATTED = {
    "DOUBLE_SPACE": True,
    "SPACE_AND_COMMA": True,
    # TODO: other wrongs
}

FORMATTED_RULES = [regex for regex in regexps if FORMATTED.get(regex["name"].upper())]


