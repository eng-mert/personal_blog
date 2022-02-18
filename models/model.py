import uuid
from abc import ABCMeta, abstractmethod
from database import Database


class Model(metaclass=ABCMeta):
    collection = "models"

    def __init__(self, _id=None, *args, **kwargs):
        self._id = _id or uuid.uuid4().hex

    @abstractmethod
    def to_json(self):
        raise NotImplementedError

    def save_to_db(self):
        Database.insert_one(collection=self.collection, record=self.to_json())
        pass

    def update(self, **kwargs):
        Database.update_one(collection=self.collection, record_id=self._id, **kwargs)
        pass

    def delete(self):
        Database.delete_one(collection=self.collection, record_id=self._id)
        pass

    @classmethod
    def get_all(cls):
        records = Database.get_all(cls.collection)
        return [cls(**record) for record in records]
        pass

    @classmethod
    def find_one(cls, **kwargs):
        record = Database.find_one(cls.collection, **kwargs)

        if record:
            return cls(**record)
        return None

    @classmethod
    def paginate(cls, per_page=1, page_index=0):
        records = Database.paginate(cls.collection, per_page=per_page)
        return {'current_page': records[page_index], 'total_pages': len(records),
                'has_next': records[page_index]['has_next'],
                'has_prev': records[page_index]['has_prev']}
