import json


class PrefixesFileReader:
    def __init__(self):
        self.json_dir = './data/json/'

    def read_json_file(self, filename) -> dict:
        path = self.json_dir + filename + '.json'
        try:
            file = open(path)
            return json.load(file)
        except IOError:
            print(f'File {path} not found')
            exit(1)

    def get_ranges_from_file(self, filename) -> dict:
        return self.read_json_file(filename)
