from django.urls import path, include

from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view

from . import viewsets, views


schema_view = get_schema_view(title='Docs API')


router = DefaultRouter()
router.register('', viewsets.DocViewset)

app_name = 'docs'
urlpatterns = [
    path('v1/docs/', include(router.urls)),
    path('schema/', schema_view),

    path('v2/', views.DocList.as_view()),
    path('v2/<int:pk>/', views.DocDetail.as_view()),
    path('v1/<user_id>/share/<doc_id>/', views.DocShare.as_view()),
    path('v1/<user_id>/remove/<doc_id>/', views.DocRemove.as_view()),
    path('v1/v2/shared_docs/', views.DocSharedList.as_view()),
]
