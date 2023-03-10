from .models import ElasticNews
from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from .documents import NewsDocument


class NewsDocumentSerializer(DocumentSerializer):
    class Meta(object):
        """Meta options."""
        model = ElasticNews
        document = NewsDocument
        fields = (
            'title',
            'content',
        )

        def get_location(self, obj):
            """Represent location value."""
            try:
                return obj.location.to_dict()
            except:
                return {}