from rest_framework import viewsets, permissions
from rest_framework.response import Response

from .serializers import DocSerializer
from .models import Doc


class DocViewset(viewsets.ModelViewSet):
    """
    This endpoint provides list, detail, retrieve, create and delete actions for Doc
    """

    queryset = Doc.objects.all()
    serializer_class = DocSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        docs = self.queryset.filter(author=self.request.user)
        return docs

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def shared_docs(self, request, *args, **kwargs):
        docs = self.get_query.filter(authors_shared=self.request.user)
        return Response(docs)
