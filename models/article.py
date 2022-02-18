from datetime import datetime
from models.model import Model


class Article(Model):
    collection = 'articles'

    def __init__(self, title, content, category_id, state=None, created_date=None, tags=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title = title
        self.content = content
        self.category_id = category_id
        self.state = state
        self.created_date = created_date or datetime.utcnow().strftime('%Y-%m-%d')
        self.tags = tags

    def to_json(self):
        return {
            '_id': self._id,
            'title': self.title,
            'content': self.content,
            'state': self.state,
            'tags': self.tags,
            'category_id': self.category_id,
        }
