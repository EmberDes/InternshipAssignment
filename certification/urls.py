from django.urls import path
from .views import CertificationListCreate, CertificationDetail

urlpatterns = [
    path("Certifications/", CertificationListCreate.as_view()),
    path("Certifications/<int:id>/", CertificationDetail.as_view()),
]