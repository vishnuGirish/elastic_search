
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from elasticsearch import Elasticsearch
from elasticsearch.exceptions import NotFoundError
from .models import BlogPost
from .documents import BlogPostIndex
from .serializers import BlogPostSerializer

@receiver(post_save, sender=BlogPost)
def index_blogpost_on_save(sender, instance, created, **kwargs):
    if created or not instance.is_deleted:
        es = Elasticsearch()
        index_name = BlogPostIndex._index._name
        try:
            serializer = BlogPostSerializer(instance)
            serialized_data = serializer.data
            es.index(index=index_name, id=instance.id, body=serialized_data)
            print(f"Data transferred to Elasticsearch: {instance.title}")
        except Exception as e:
            print(f"Error indexing blog post: {str(e)}")


@receiver(post_delete, sender=BlogPost)
def remove_blogpost_from_index(sender, instance, **kwargs):
    es = Elasticsearch()
    index_name = BlogPostIndex._index._name
    try:
        es.delete(index=index_name, id=instance.id)
        print(f"Data removed from Elasticsearch: {instance.title}")
    except NotFoundError:
        pass  # Index/document does not exist, no action needed
    except Exception as e:
        print(f"Error removing blog post from index: {str(e)}")
