from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action

from .serializers import DocSerializer
from .models import Doc


class DocViewset(viewsets.ModelViewSet):
    """
    This endpoint provides list, detail, retrieve, create and delete actions for Doc
    """

    queryset = Doc.objects.all()
    serializer_class = DocSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(detail=True, methods=['post'])
    def shared_docs(self, request, *args, **kwargs):
        docs = self.get_queryset().filter(authors_shared=self.request.user)
        return Response(docs)
