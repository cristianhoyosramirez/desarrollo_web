from rest_framework import serializers
from .models import * 

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields= '__all__'

class PartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Part
        fields= '__all__'
        
class displacementSerializer(serializers.ModelSerializer):
    class Meta:
        model = displacement
        fields= '__all__'
        
class manufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = manufacturer
        fields= '__all__'
        

        


