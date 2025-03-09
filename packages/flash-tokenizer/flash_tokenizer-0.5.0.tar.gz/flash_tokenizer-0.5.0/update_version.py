import os
import re

with open("pyproject.toml", "rt", encoding="utf-8") as f:
    lines = f.read().splitlines()

for line in lines:
    if line.startswith("version"):
        version_toml = line.split("=")[1].strip()[1:-1]
        break

with open("CMakeLists.txt", "rt", encoding="utf-8") as f:
    lines = f.read().splitlines()
for line in lines:
    if "PROJECT_VERSION_STR" in line:
        tmp = re.findall('([^)]+)', line)[0]
        version_cmakelist = re.sub(r'[^0-9\.]', '', tmp)
        break

print(version_toml)
print(version_cmakelist)
