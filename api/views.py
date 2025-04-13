from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.request import Request
from home.models import Project, Technology
from .serilizers import ProjectSerializer, TechnologySerializer
from rest_framework import generics, mixins
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class PaginationCustom(PageNumberPagination):
    page_size = 3
# class ProjectListView(generics.ListCreateAPIView):

#     queryset = Project.objects.all()
#     serializer_class = ProjectSerializer
    

class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer



class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    pagination_class = PaginationCustom
    # authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


    def create(self, request, *args, **kwargs):
        is_many = isinstance(request.data, list)
        
        serializer = self.get_serializer(data=request.data, many=is_many)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class TechnologyListView(generics.ListCreateAPIView):
    queryset = Technology.objects.all()
    serializer_class = TechnologySerializer


class TechnologyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Technology.objects.prefetch_related('projects')
    serializer_class = TechnologySerializer