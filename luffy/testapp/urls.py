from django.urls import include, path
from rest_framework import routers

from testapp.views import UserViewSet, testlog

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'testlog', testlog)
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls',
                              namespace='rest_framework'))
]


print(urlpatterns)