from rest_framework import serializers

from .models import Todo, TodoList

class TodoListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TodoList
        fields = ('title', 'description')



class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'
        depth = 1
        lookup_field = 'todolist'
