import sys

lines = open("README.md", "r").readlines()

for line in lines:
    print(line, end="")

sys.exit(-1)

print("\nEverything is OK")

