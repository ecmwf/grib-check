import pandas as pd
from Message import Message


class LookupTable:
    def __init__(self, filename: str):
        raise NotImplementedError

    def get_element(self, message: Message):
        raise NotImplementedError


class SimpleLookupTable(LookupTable):
    '''
    A simple lookup table that uses a JSON file to store the data.
    '''
    def __init__(self, filename: str):
        assert filename is not None
        self.df = pd.read_json(filename, orient='records')

    def get_element(self, message: Message):
        params = list()
        for _, row in self.df.iterrows():
            count = 0
            for pair in row['pairs']:
                if pair['value'] == message.get(pair['key'], type(pair['value'])):
                    count += 1
            if count == len(row['pairs']):
                params.append((count, row))
                # return row.to_dict()
        if len(params) > 0:
            params.sort(key=lambda x: x[0], reverse=True)
            return params[0][1].to_dict()
       
        return None


class IndexedLookupTable(LookupTable):
    '''
    A lookup table that uses a dictionary to store the data.
    The dictionary is indexed by the keys in the data.

    TODO: Implement and replace SimpleLookupTable with this class.
    '''
    def __init__(self, filename: str):
        raise NotImplementedError

    def get_element(self, message: Message):
        raise NotImplementedError
