from rest_framework import serializers
from .models import News

#Serializers: encargados de serializar datos a JSON o viceversa.

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'
