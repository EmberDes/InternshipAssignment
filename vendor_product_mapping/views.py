from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import VendorProductMapping
from .serializers import VendorProductMappingSerializer
from drf_yasg.utils import swagger_auto_schema 

class VendorProductMappingListCreate(APIView):

    def get(self, request):
        objects = VendorProductMapping.objects.all()
        serializer = VendorProductMappingSerializer(objects, many=True)
        return Response(serializer.data)
    
    @swagger_auto_schema(request_body=VendorProductMappingSerializer)
    def post(self, request):
        serializer = VendorProductMappingSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VendorProductMappingDetail(APIView):

    def get_object(self, id):
        return VendorProductMapping.objects.get(id=id)

    def get(self, request, id):
        obj = self.get_object(id)
        serializer = VendorProductMappingSerializer(obj)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=VendorProductMappingSerializer)
    def put(self, request, id):
        obj = self.get_object(id)
        serializer = VendorProductMappingSerializer(obj, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)

    def delete(self, request, id):
        obj = self.get_object(id)
        obj.delete()
        return Response({"message": "deleted"})