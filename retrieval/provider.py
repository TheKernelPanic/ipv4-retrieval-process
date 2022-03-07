import json


class Ranges:
    def __init__(self):
        self.ranges = []
        self.json_dir = './data/json/'

    def read_json_file(self, filename) -> dict:
        file = open(self.json_dir + filename + '.json')
        return json.load(file)

    def get_data_from_decoded_file(self) -> None:
        raise NotImplementedError('Method not implemented')


class AWSRanges(Ranges):
    def get_data_from_decoded_file(self) -> None:
        data = self.read_json_file('aws')
        for element in data['prefixes']:
            self.ranges.append({
                'provider': 'AWS_' + element['service'],
                'range': element['ip_prefix'],
            })

    def get_ranges(self) -> list:
        self.get_data_from_decoded_file()
        return self.ranges
