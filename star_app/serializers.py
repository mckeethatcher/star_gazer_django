from rest_framework import serializers
from .models import Crud

class CrudSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crud
        fields = ( 'id','astronomer', 'location', 'coordinates', 'image', 'description' )