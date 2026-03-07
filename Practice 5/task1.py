import re

pattern = r"ab*"

text = ["a", "ab", "abb", "ac"]

for t in text:
    if re.fullmatch(pattern, t):
        print(t, "-> Match")