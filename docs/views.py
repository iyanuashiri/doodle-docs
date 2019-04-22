from django.shortcuts import get_object_or_404

from rest_framework import permissions, generics
from rest_framework.views import APIView
from rest_framework.response import Response

from accounts.models import Account
from .serializers import DocSerializer
from .models import Doc

# Create your views here.


class DocList(generics.ListCreateAPIView):
    """
    List all docs and create a new doc
    """
    serializer_class = DocSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Doc.objects.all()

    def get_queryset(self):
        docs = self.queryset.filter(author=self.request.user)
        return docs


class DocDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, Edit and Delete a Doc instance
    """
    serializer_class = DocSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Doc.objects.all()


class DocShare(APIView):
    """
    Share a doc instance with another user
    """
    def put(self, request, user_id, doc_id):
        doc = get_object_or_404(Doc, pk=doc_id)
        user = get_object_or_404(Account, pk=user_id)
        user.docs_shared.add(doc)
        return Response({'shared': True})


class DocRemove(APIView):
    """
    Remove a doc instance from a shared user
    """
    def put(self, request, user_id, doc_id):
        doc = get_object_or_404(Doc, pk=doc_id)
        user = get_object_or_404(Account, pk=user_id)
        user.docs_shared.remove(doc)
        return Response({'removed': True})


class DocSharedList(generics.ListAPIView):
    """
    List of all shared docs
    """
    queryset = Doc.objects.all()
    serializer_class = DocSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        docs = self.queryset.filter(authors_shared=self.request.user)
        return docs
