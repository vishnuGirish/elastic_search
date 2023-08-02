
from django.shortcuts import render
from elasticsearch_dsl import Search
from .documents import BlogPostIndex

def search_view(request):
    query = request.GET.get('q')
    if query:
        s = Search(index='blogpost_index').query('match', title=query)
        response = s.execute()
        hits = response.hits
    else:
        hits = []

    return render(request, 'blog/search_results.html', {'hits': hits, 'query': query})
