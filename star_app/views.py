from rest_framework import generics
from .serializers import StarSerializer
from .models import Star

class StarList(generics.ListCreateAPIView):
    queryset = Star.objects.all().order_by('id')
    serializer_class = StarSerializer

class StarDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Star.objects.all().order_by('id')
    serializer_class = StarSerializer