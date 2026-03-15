from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Certification
from .serializers import CertificationSerializer
from drf_yasg.utils import swagger_auto_schema

class CertificationListCreate(APIView):

    def get(self, request):
        objects = Certification.objects.all()
        serializer = CertificationSerializer(objects, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=CertificationSerializer)
    def post(self, request):
        serializer = CertificationSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CertificationDetail(APIView):

    def get_object(self, id):
        return Certification.objects.get(id=id)

    def get(self, request, id):
        obj = self.get_object(id)
        serializer = CertificationSerializer(obj)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=CertificationSerializer)
    def put(self, request, id):
        obj = self.get_object(id)
        serializer = CertificationSerializer(obj, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)

    def delete(self, request, id):
        obj = self.get_object(id)
        obj.delete()
        return Response({"message": "deleted"})