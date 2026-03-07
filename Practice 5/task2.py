import re

pattern = r"ab{2,3}"

text = ["ab", "abb", "abbb", "abbbb"]

for t in text:
    if re.fullmatch(pattern, t):
        print(t, "-> Match")