# from django.shortcuts import render
# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .filters import ProjectFilter, TODOFilter
from .models import TODO, Project
from .serializers import ProjectSerializer, TODOSerializer


class ProjectPagination(PageNumberPagination):
    page_size = 10


class TODOPagination(PageNumberPagination):
    page_size = 20


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    pagination_class = ProjectPagination
    filterset_class = ProjectFilter

    def get_queryset(self):
        queryset = Project.objects.all()
        name = self.request.query_params.get("name", None)
        if name:
            queryset = queryset.filter(name__contains=name)
        return queryset


class TODOViewSet(ModelViewSet):
    queryset = TODO.objects.all()
    serializer_class = TODOSerializer
    pagination_class = TODOPagination
    # filter_backends = [DjangoFilterBackend]
    filterset_class = TODOFilter

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.is_active = False
            instance.save()
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)
