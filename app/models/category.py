from app.models.model import Model


class Category(Model):
    collection = "categories"

    def __init__(self, title, parent_id=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title = title
        self.parent_id = parent_id

    def to_json(self):
        return {
            '_id': self._id,
            'title': self.title,
            'parent_id': self.parent_id
        }

    @property
    def children(self):
        return Category.find_many(parent_id=self._id)

    @property
    def articles(self):
        from .article import Article
        return Article.find_many(category_id = self._id)