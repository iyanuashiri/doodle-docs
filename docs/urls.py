from django.urls import path, include

from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.schemas import get_schema_view

from . import viewsets, views


schema_view = get_schema_view(title='Docs API')


router = DefaultRouter()
router.register('', viewsets.DocViewset)

app_name = 'docs'
urlpatterns = [
    path('v1/', include(router.urls)),
    path('schema/', schema_view),

    path('v2/', views.DocList.as_view()),
    path('v2/<int:pk>/', views.DocDetail.as_view(), name='detail'),
    path('v2/<user_id>/share/<doc_id>/', views.DocShare.as_view()),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
