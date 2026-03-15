from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Course
from .serializers import CourseSerializer
from drf_yasg.utils import swagger_auto_schema

class CourseListCreate(APIView):

    def get(self, request):
        objects = Course.objects.all()
        serializer = CourseSerializer(objects, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=CourseSerializer)
    def post(self, request):
        serializer = CourseSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CourseDetail(APIView):

    def get_object(self, id):
        return Course.objects.get(id=id)

    def get(self, request, id):
        obj = self.get_object(id)
        serializer = CourseSerializer(obj)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=CourseSerializer)
    def put(self, request, id):
        obj = self.get_object(id)
        serializer = CourseSerializer(obj, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)

    def delete(self, request, id):
        obj = self.get_object(id)
        obj.delete()
        return Response({"message": "deleted"})