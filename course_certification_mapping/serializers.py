from rest_framework import serializers
from .models import CourseCertificationMapping


class CourseCertificationMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseCertificationMapping
        fields = "__all__"

    def validate(self, data):
        course = data["course"]
        certif = data["certification"]
        primary = data["primary_mapping"]

        if CourseCertificationMapping.objects.filter(course = course , certification = certif).exists():
            return serializers.ValidationError("This Course-Certification mapping already Exists. ")
        

        if primary :
            if CourseCertificationMapping.objects.filter(course = course , primary_mapping = True).exists():
                return serializers.ValidationError("Course Already have a primary Certification.")


        return super().validate(data)