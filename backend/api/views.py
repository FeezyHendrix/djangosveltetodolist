from django.shortcuts import render
from rest_framework import viewsets

from .serializers import TodoListSerializer, TodoSerializer
from .models import TodoList, Todo
from django.views.decorators.csrf import csrf_exempt

from django.views import View

class TodoListViewSet(viewsets.ModelViewSet):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    lookup_field = 'todolist'



class TodoListView(View):
    def get(self, request):
        todolists = TodoList.objects.all()
        serialize = TodoListSerializer(todolists, many=True)