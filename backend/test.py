import json

with open("data/provider-alpha.json") as f:
	file = json.load(f)
	print(len(file))