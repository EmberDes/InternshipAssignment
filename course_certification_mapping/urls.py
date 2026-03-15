from django.urls import path
from .views import CourseCertificationMappingListCreate, CourseCertificationMappingDetail

urlpatterns = [
    path("CourseCertificationMappings/", CourseCertificationMappingListCreate.as_view()),
    path("CourseCertificationMappings/<int:id>/", CourseCertificationMappingDetail.as_view()),
]