from rest_framework import permissions, generics

from .serializers import DocSerializer
from .models import Doc

# Create your views here.


class DocList(generics.ListCreateAPIView):
    """
    List all docs and create a new doc
    """
    serializer_class = DocSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Doc.objects.all()


class DocDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, Edit and Delete a Doc instance
    """
    serializer_class = DocSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Doc.objects.all()
