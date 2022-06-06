from rest_framework import serializers
from . models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class BlogSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Blog
        fields = '__all__'


class OpportunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Opportunity
        fields = '__all__'