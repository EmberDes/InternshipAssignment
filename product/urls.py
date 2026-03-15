from django.urls import path
from .views import ProductListCreate, ProductDetail

urlpatterns = [
    path("Products/", ProductListCreate.as_view()),
    path("Products/<int:id>/", ProductDetail.as_view()),
]