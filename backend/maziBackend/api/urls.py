from django.urls import path, include
from rest_framework import routers
from api.views import Article_viewset


myrouter = routers.DefaultRouter()
myrouter.register('article', Article_viewset, base_name='article')

urlpatterns = [
 path('', include(myrouter.urls)),
 path('api-auth/', include('rest_framework.urls'))
]
