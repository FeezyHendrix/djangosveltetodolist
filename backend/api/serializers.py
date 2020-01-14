from rest_framework import serializers

from .models import Todo, TodoList

class TodoListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TodoList
        fields = ('title', 'description')