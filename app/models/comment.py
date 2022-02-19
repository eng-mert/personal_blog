from datetime import datetime

from app.models.model import Model


class Comment(Model):
    collection = "comments"
    def __init__(self, content, article_id=None, created_date=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.content = content
        self.article_id = article_id
        self.created_date = created_date or datetime.utcnow().strftime('%Y-%m-%d')

    def to_json(self):
        return {
            '_id': self._id,
            'content': self.content,
            'article_id': self.article_id,
            'created_date': self.created_date

        }

    @property
    def article(self):
        from .article import Article
        return Article.find_one(_id=self.article_id)
