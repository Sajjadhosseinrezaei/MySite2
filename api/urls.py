from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', views.ProjectViewSet)


app_name = 'api'
urlpatterns = [
    # path('projects/', views.ProjectListView.as_view(), name='project-list'),
    path('projects/<int:pk>/', views.ProjectDetailView.as_view(), name='project-detail'),
    path('viewset', include(router.urls)),
    path('technologies/', views.TechnologyListView.as_view(), name='technology-list'),
    path('technologies/<int:pk>/', views.TechnologyDetailView.as_view(), name='technology-detail'),
]
