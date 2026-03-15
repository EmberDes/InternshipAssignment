from django.urls import path
from .views import CourseListCreate, CourseDetail

urlpatterns = [
    path("Courses/", CourseListCreate.as_view()),
    path("Courses/<int:id>/", CourseDetail.as_view()),
]