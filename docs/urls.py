from django.urls import path, include

from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

from . import viewsets, views


router = DefaultRouter()
router.register('', viewsets.DocViewset)

app_name = 'docs'
urlpatterns = [
    path('', include(router.urls)),

    path('', views.DocList.as_view()),
    path('/<int:pk>/', views.DocDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
