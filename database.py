from pymongo import MongoClient


class Database:
    host = "127.0.0.1:27017"
    db = None

    @classmethod
    def initialize(cls):
        client = MongoClient(cls.host)
        cls.db = client.get_database('personalDb')

    @classmethod
    def insert_one(cls, collection, record):
        cls.db[collection].insert_one(record)

    @classmethod
    def find_one(cls, collection, **kwargs):
        return cls.db[collection].find_one(kwargs)

    @classmethod
    def get_all(cls, collection):
        return cls.db[collection].find({})

    @classmethod
    def delete_one(cls, collection, record_id):
        if cls.find_one(collection, _id=record_id):
            cls.db[collection].delete_one({'_id': record_id})

    @classmethod
    def update_one(cls, collection, record_id, **kwargs):
        query = {'_id': record_id}
        new_values = {'$set': kwargs}
        cls.db[collection].update_one(query, new_values)

    @classmethod
    def paginate(cls, collection, per_page=1):
        records = [record for record in cls.get_all(collection)]
        total_length = len(records)
        pages = total_length // per_page
        current_index = 0
        data = []
        for page in range(pages):
            if page == 0:
                data.append({'index': page,
                             'items': records[current_index:current_index + per_page],
                             'has_prev': False,
                             'has_next': True, })
            else:
                data.append({'index': page,
                             'items': records[current_index:current_index + per_page],
                             'has_prev': True,
                             'has_next': True})
            current_index += per_page
        else:
            data.append({'index': 'last',
                         'items': records[current_index:current_index + per_page],
                         'has_prev': True,
                         'has_next': False, })
        return data

    @classmethod
    def find_many(cls, collection, **kwargs):
        return cls.db[collection].find(kwargs)
