from django.urls import include,path
from rest_framework import routers
from .views import * 

routers=routers.DefaultRouter()
routers.register(r'car',CarViewSet)
routers.register(r'part',PartViewSet)
routers.register(r'displacement',displacementViewSet)
routers.register(r'manufacturer',manufacturerViewSet)

urlpatterns=[
    path("api/v1/",include(routers.urls))
]