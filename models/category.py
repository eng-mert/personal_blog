from models.model import Model


class Category(Model):
    collection = "categories"

    def __init__(self, title, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title = title

    def to_json(self):
        return {
            '_id': self._id,
            'title': self.title
        }