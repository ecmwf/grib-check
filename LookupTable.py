import pandas as pd
from Message import Message

class LookupTable:
    def __init__(self, filename: str):
        raise NotImplementedError

    def get_element(self, message: Message):
        raise NotImplementedError


class SimpleLookupTable(LookupTable):
    def __init__(self, filename: str):
        self.df = pd.read_json(filename, orient='records')

    def get_element(self, message: Message):
        for _, row in self.df.iterrows():
            count = 0
            for pair in row['pairs']:
                if pair['value'] == message.get(pair['key'], type(pair['value'])):
                    count += 1
            if count == len(row['pairs']):
                return row.to_dict()
       
        return None


class IndexedLookupTable(LookupTable):
    def __init__(self, filename: str):
        raise NotImplementedError

    def get_element(self, message: Message):
        raise NotImplementedError
