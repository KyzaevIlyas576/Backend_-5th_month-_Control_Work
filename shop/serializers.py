from rest_framework import serializers
import models

class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = models.Post
        fields = '__all__'