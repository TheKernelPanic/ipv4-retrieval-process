import json


class RangesFileReader:
    def __init__(self):
        self.json_dir = './data/json/'

    def read_json_file(self, filename) -> dict:
        file = open(self.json_dir + filename + '.json')
        return json.load(file)

    def get_ranges_from_file(self, filename) -> dict:
        return self.read_json_file(filename)
