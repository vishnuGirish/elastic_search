# ![Elasticsearch Logo](https://upload.wikimedia.org/wikipedia/commons/thumb/f/f4/Elasticsearch_logo.svg/320px-Elasticsearch_logo.svg.png)

# Elasticsearch Guide 📖

Welcome to the **Elasticsearch Guide**! 🚀 This document provides a comprehensive understanding of Elasticsearch, including installation, indexing, querying, and best practices.

---

## 📌 What is Elasticsearch?
Elasticsearch is a **highly scalable** open-source search and analytics engine. It is used for searching, logging, monitoring, and analyzing large amounts of structured and unstructured data in real time.

### 🏆 Key Features
- **Full-Text Search** 🔍
- **Scalability & High Availability** 🌍
- **Real-Time Data Indexing** ⚡
- **Powerful Query DSL** 📝
- **Analytics & Aggregations** 📊
- **Integration with Kibana & Logstash** 🔗

---

## 🛠 Installation Guide
### Using Docker 🐳
```bash
# Pull Elasticsearch Docker Image
docker pull docker.elastic.co/elasticsearch/elasticsearch:8.4.0

# Run Elasticsearch Container
docker run -d --name elasticsearch -p 9200:9200 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:8.4.0
```

### Manual Installation 🖥️
1. Download Elasticsearch from the official site: [Elastic Downloads](https://www.elastic.co/downloads/elasticsearch)
2. Extract the downloaded file.
3. Start Elasticsearch:
   ```bash
   ./bin/elasticsearch
   ```
4. Verify installation:
   ```bash
   curl -X GET "localhost:9200"
   ```

---

## 🏗️ Core Concepts
### 🔹 Index
An **index** is like a database in Elasticsearch. It contains documents.
```json
PUT /products
{
  "settings": {
    "number_of_shards": 3,
    "number_of_replicas": 1
  }
}
```

### 🔹 Document
A **document** is a unit of data stored in an index.
```json
POST /products/_doc/1
{
  "name": "Apple iPhone 15",
  "price": 999,
  "category": "smartphone"
}
```

### 🔹 Mapping
Defines the structure of documents inside an index.
```json
PUT /products/_mapping
{
  "properties": {
    "name": { "type": "text" },
    "price": { "type": "float" }
  }
}
```

### 🔹 Query DSL (Search)
Elasticsearch uses **Query DSL** for searching.
```json
GET /products/_search
{
  "query": {
    "match": {
      "name": "iPhone"
    }
  }
}
```

### 🔹 Aggregations
Powerful analytics feature for summarizing data.
```json
GET /products/_search
{
  "aggs": {
    "average_price": {
      "avg": {
        "field": "price"
      }
    }
  }
}
```

---

## 🔗 Integrating Elasticsearch with Django
### 📦 Installing Required Packages
To integrate Elasticsearch with Django, install the required libraries:
```bash
pip install elasticsearch-dsl django-elasticsearch-dsl
```

### 🔹 Configuring Elasticsearch in Django
Add the following settings in your Django **settings.py** file:
```python
ELASTICSEARCH_DSL = {
    'default': {
        'hosts': 'http://localhost:9200'
    }
}
```

### 🔹 Creating an Elasticsearch Document
Define a document using `django-elasticsearch-dsl`:
```python
from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from myapp.models import Product

@registry.register_document
class ProductDocument(Document):
    class Index:
        name = 'products'
    
    class Django:
        model = Product
        fields = ['name', 'price', 'category']
```

### 🔹 Running Elasticsearch Indexing
Run the following command to populate Elasticsearch with Django data:
```bash
python manage.py search_index --rebuild
```

### 🔹 Querying Elasticsearch in Django
Use `ProductDocument` to search in Elasticsearch:
```python
from myapp.documents import ProductDocument

results = ProductDocument.search().query("match", name="iPhone").execute()
for hit in results:
    print(hit.name, hit.price)
```

---

## 🚀 Best Practices
✅ Use proper **index mapping** to optimize queries.  
✅ **Monitor cluster health** using Kibana and X-Pack.  
✅ **Shard wisely** based on data size and query patterns.  
✅ Use **filters** instead of queries for faster performance.  
✅ **Enable caching** for frequently used queries.

---

## 📜 Useful Commands
Check cluster health:
```bash
GET _cluster/health
```

List all indices:
```bash
GET _cat/indices?v
```

Delete an index:
```bash
DELETE /products
```

---

## 📚 Additional Resources
- 🔗 [Elasticsearch Official Docs](https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html)
- 🔗 [Kibana for Visualization](https://www.elastic.co/kibana)
- 🔗 [Elasticsearch Query DSL](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl.html)
- 🔗 [Django Elasticsearch DSL](https://django-elasticsearch-dsl.readthedocs.io/en/latest/)

---

### 🛠 Created by: **Your Name**  
⚡ Powered by Elasticsearch & Django! 🎉

