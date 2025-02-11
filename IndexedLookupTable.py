import pandas as pd


class IndexedLookupTable:
    def __init__(self, filename: str):
        df = pd.read_json(filename, orient='records')

        # 0    {'stream': 'eefo', 'dataType': 'fcmean'}
        # 1      {'stream': 'eefo', 'dataType': 'taem'}
        # 2      {'stream': 'eefo', 'dataType': 'taes'}
        # 3        {'stream': 'enfo', 'dataType': 'pf'}
        stripped_keys = df['pairs'].apply(lambda row: {d['key']: d['value'] for d in row})

        #   stream dataType
        # 0   eefo   fcmean
        # 1   eefo     taem
        # 2   eefo     taes
        # 3   enfo       pf
        normalized_keys = pd.DataFrame(stripped_keys.tolist())

        keys=list(normalized_keys.columns.values)
        self.indexed_table = normalized_keys.join(df).set_index(keys)
        d = {k: self.indexed_table.index.get_level_values(k).dtype for k in keys}
        self.idx_keys = {k: str if str(v) == "object" else int for k, v in d.items()}

    def get_index_keys(self) -> dict:
        return self.idx_keys

    def get_element(self, index_kv: dict):
        index = tuple(index_kv[k] if k in index_kv else slice(None) for k in self.idx_keys)
        return self.indexed_table.loc[index].to_dict()
