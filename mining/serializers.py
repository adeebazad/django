from rest_framework import serializers
from .models import MinedData


class MinedDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = MinedData
        fields ='__all__'#['order_id', 'system_order_id', 'order_date', 'order_total', 'customer_pincode', 'extra_details']