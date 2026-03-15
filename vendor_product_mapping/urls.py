from django.urls import path
from .views import VendorProductMappingListCreate, VendorProductMappingDetail

urlpatterns = [
    path("VendorProductMappings/", VendorProductMappingListCreate.as_view()),
    path("VendorProductMappings/<int:id>/", VendorProductMappingDetail.as_view()),
]