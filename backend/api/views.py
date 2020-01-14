from django.shortcuts import render
from rest_framework import viewsets

from .serializers import TodoListSerializer
from .models import TodoList

class TodoListViewSet(viewsets.ModelViewSet):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer
