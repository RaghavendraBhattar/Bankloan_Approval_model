from rest_framework import serializers
from .models import approvals


class approvalSerializer(serializers.Serializer):
    class Meta:
        model = approvals
        fields = '__all__'
