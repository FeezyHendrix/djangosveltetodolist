from django.shortcuts import render
from rest_framework import viewsets

from .serializers import TodoListSerializer, TodoSerializer
from .models import TodoList, Todo

class TodoListViewSet(viewsets.ModelViewSet):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    lookup_field = 'todolist'