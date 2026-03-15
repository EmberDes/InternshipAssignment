from django.urls import path
from .views import ProductCourseMappingListCreate, ProductCourseMappingDetail

urlpatterns = [
    path("ProductCourseMappings/", ProductCourseMappingListCreate.as_view()),
    path("ProductCourseMappings/<int:id>/", ProductCourseMappingDetail.as_view()),
]