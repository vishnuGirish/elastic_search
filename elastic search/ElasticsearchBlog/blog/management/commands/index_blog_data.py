# NOTES

# THIS MANAGEMENT COMMANDS ARE USED TO MANUALLY UPDATE DATA IN ELASTIC SEARCH, NOT REQUIRED 
# IF SIGNALS ARE USED, SIGNALS AUTOMATICALLY UPDATE DATA IN ELASTIC SEARCH WHEN EVER A DATA 
# IS CREATED,DELETED OR UPDATED IN A MODEL

# This is just for reference


from django.core.management.base import BaseCommand
from blog.models import BlogPost
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
from blog.documents import BlogPostIndex

class Command(BaseCommand):
    help = 'Index blog data into Elasticsearch'

    def handle(self, *args, **options):
        # Get all BlogPost instances
        blog_posts = BlogPost.objects.all()

        # Initialize Elasticsearch client
        es = Elasticsearch()

        # Initialize Elasticsearch index
        index_name = BlogPostIndex._index._name
        es.indices.create(index=index_name, ignore=400)  # Ignore if index already exists

        # Prepare data for bulk indexing
        actions = [
            {
                "_index": index_name,
                "_id": blog_post.id,
                "_source": {
                    "title": blog_post.title,
                    "content": blog_post.content,
                    "publish_date": blog_post.publish_date,
                    # Add more fields as needed
                }
            }
            for blog_post in blog_posts
        ]

        # Bulk index data into Elasticsearch
        success, failed = bulk(es, actions)

        for blog_post in blog_posts:
            print(f"Transferring data for: {blog_post.title}")

        self.stdout.write(self.style.SUCCESS(f'Successfully indexed {success} blog data'))
        self.stdout.write(self.style.ERROR(f'Failed to index {failed} blog data'))


