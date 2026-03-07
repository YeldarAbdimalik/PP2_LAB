import re

text = "Hello world My Name Is Python"

pattern = r"[A-Z][a-z]+"

print(re.findall(pattern, text))