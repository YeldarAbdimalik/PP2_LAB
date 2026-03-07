import re

pattern = r"a.*b"

text = ["ab", "acb", "a123b", "ahello"]

for t in text:
    if re.fullmatch(pattern, t):
        print(t, "-> Match")