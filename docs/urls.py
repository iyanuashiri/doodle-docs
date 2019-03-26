from django.urls import path, include

from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

from . import viewsets, views


router = DefaultRouter()
router.register('', viewsets.DocViewset)

app_name = 'docs'
urlpatterns = [
    path('v1/', include(router.urls)),

    path('v2/', views.DocList.as_view()),
    path('v2/<int:pk>/', views.DocDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
