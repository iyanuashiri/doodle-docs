from rest_framework import viewsets, permissions

from .serializers import DocSerializer
from .models import Doc


class DocViewset(viewsets.ModelViewSet):
    """
    This endpoint provides list, detail, retrieve, create and delete actions for Doc
    """

    queryset = Doc.objects.all()
    serializer_class = DocSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
