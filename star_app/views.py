from rest_framework import generics
from .serializers import CrudSerializer
from .models import Crud

class CrudList(generics.ListCreateAPIView):
    queryset = Crud.objects.all().order_by('id')
    serializer_class = CrudSerializer

class CrudDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Crud.objects.all().order_by('id')
    serializer_class = CrudSerializer