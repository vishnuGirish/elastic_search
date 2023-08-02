from elasticsearch_dsl import Document, Text, Date
from elasticsearch_dsl.connections import connections
from .models import BlogPost

connections.create_connection(hosts=['localhost'])

class BlogPostIndex(Document):
    title = Text()
    content = Text()
    publish_date = Date()

    class Index:
        name = 'blogpost_index'
