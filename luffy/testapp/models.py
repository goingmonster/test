from django.db import models


# Create your models here.
class ElasticNews(models.Model):
    # ES中索引的模型
    # 自动在索引中生成
    # "mappings": {
    #     "properties": {
    #         "content": {
    #             "type": "text",
    #             "fields": {
    #                 "keyword": {
    #                     "type": "keyword"
    #                 }
    #             }
    #         },
    #         "id": {
    #             "type": "integer"
    #         },
    #         "title": {
    #             "type": "text",
    #             "fields": {
    #                 "keyword": {
    #                     "type": "keyword"
    #                 }
    #             }
    #         }
    #     }
    # }
    title = models.CharField(max_length=100)
    content = models.TextField()