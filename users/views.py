# from django.shortcuts import render

from rest_framework import mixins, viewsets
from rest_framework.renderers import JSONRenderer

from .models import User
from .serializers import UserModelSerializer


class UserModelViewSet(
    mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet
):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    renderer_classes = [JSONRenderer]
