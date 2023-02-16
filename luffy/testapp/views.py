import logging
import requests
import json
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from rest_framework import serializers, viewsets
from testapp.models import ElasticNews
from .documents import NewsDocument
from .serializers import NewsDocumentSerializer
from django_elasticsearch_dsl_drf.filter_backends import FilteringFilterBackend, CompoundSearchFilterBackend, OrderingFilterBackend
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet


def testlog(request):
    # 进行日志配置的测试
    logger = logging.getLogger('django')
    logger.info('loading url')
    logger.error('error')
    logger.debug('debug')
    return HttpResponse("Hello world ! ")


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


def generate_random_data():
    url = 'http://localhost:3000/news'
    r = requests.get(url)
    payload = json.loads(r.text)
    print("type of payload is: ", type(payload))
    for data in payload:
        ElasticNews.objects.create(title=data['title'],
                                   content=data['content'])


def index(request):
    generate_random_data()
    return JsonResponse({'status': 200})


class PublisherDocumentView(DocumentViewSet):
    document = NewsDocument
    serializer_class = NewsDocumentSerializer
    lookup_field = 'first_name'
    fielddata = True
    filter_backends = [
        FilteringFilterBackend,
        OrderingFilterBackend,
        CompoundSearchFilterBackend,
    ]

    search_fields = (
        'title',
        'content',
    )
    multi_match_search_fields = (
        'title',
        'content',
    )
    filter_fields = {
        'title': 'title',
        'content': 'content',
    }
    ordering_fields = {
        'id': None,
    }
    ordering = ('id', )
