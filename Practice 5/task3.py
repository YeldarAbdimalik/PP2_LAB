import re

text = "hello_world test_string Python_Test"

pattern = r"[a-z]+_[a-z]+"

print(re.findall(pattern, text))