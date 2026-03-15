from rest_framework import serializers
from .models import ProductCourseMapping


class ProductCourseMappingSerializer(serializers.ModelSerializer):
    class Meta :
        model = ProductCourseMapping
        fields = "__all__"

    def validate(self, data):

        
        product = data["product"]
        course = data["course"]
        primary = data["primary_mapping"]

        if ProductCourseMapping.objects.filter(product = product , course = course).exists:
            raise serializers.ValidationError("This Product-Course mapping already Exists.")
        
        if primary:
            if ProductCourseMapping.objects.filter(product = product, primary_mapping = True).exists():
                raise serializers.ValidationError("Prouct already has a Primary Course.")

        return data