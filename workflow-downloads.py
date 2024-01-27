import utils.json_client as uf


files = uf.get_json_to_list("data/github/files.json")
for file in files:
    print(file)


