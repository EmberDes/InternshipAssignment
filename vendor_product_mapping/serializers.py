from rest_framework import serializers
from .models import VendorProductMapping


class VendorProductMappingSerializer(serializers.ModelSerializer):
    class Meta :
        model = VendorProductMapping
        fields = "__all__"

    def validate(self, data):

        vendor = data["vendor"]
        product = data["product"]
        primary = data["primary_mapping"]

        if VendorProductMapping.objects.filter(vendor=vendor, product = product).exists():
            raise serializers.ValidationError("This Vendor-Product mapping already Exists.")
        
        if primary:
            if VendorProductMapping.objects.filter(vendor = vendor, primary_mapping = True).exists():
                raise serializers.ValidationError("Vendor already has a Primary Product.")

        return data