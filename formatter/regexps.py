import re


double_space = {
    "name": "double_space",
    "regex": re.compile(r'\s{2,}'),
    "to": ' '
}
space_and_comma = {
    "name": "space_and_comma",
    "regex": re.compile(r'\s,'),
    "to": ','
}

regexps = (
    double_space,
    space_and_comma
)


