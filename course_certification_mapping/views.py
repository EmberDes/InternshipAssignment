from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CourseCertificationMapping
from .serializers import CourseCertificationMappingSerializer


class CourseCertificationMappingListCreate(APIView):

    def get(self, request):
        objects = CourseCertificationMapping.objects.all()
        serializer = CourseCertificationMappingSerializer(objects, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CourseCertificationMappingSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CourseCertificationMappingDetail(APIView):

    def get_object(self, id):
        return CourseCertificationMapping.objects.get(id=id)

    def get(self, request, id):
        obj = self.get_object(id)
        serializer = CourseCertificationMappingSerializer(obj)
        return Response(serializer.data)

    def put(self, request, id):
        obj = self.get_object(id)
        serializer = CourseCertificationMappingSerializer(obj, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)

    def delete(self, request, id):
        obj = self.get_object(id)
        obj.delete()
        return Response({"message": "deleted"})