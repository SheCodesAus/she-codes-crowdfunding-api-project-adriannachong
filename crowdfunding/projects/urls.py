from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views 

# best practice for name="project-list"
urlpatterns = [
    path('projects/', views.ProjectList.as_view(), name="project-list"),
    path('projects/<int:pk>/', views.ProjectDetail.as_view()),
    ] 

urlpatterns = format_suffix_patterns(urlpatterns) # 'format_suffix_patterns' function takes all your ursl and ability to tell it if yoy want JSON or HTML back, 'force it'

