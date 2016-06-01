from rest_framework import serializers
from smartp.models import park

class SmartSerializer(serializers.Serializer):
    
    parking_name = serializers.CharField(max_length=20)
    parking_no = serializers.IntegerField()
    status = serializers.IntegerField(default=0)
    
    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return park.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.parking_name = validated_data.get('parking_name', instance.parking_name)
        instance.parking_no = validated_data.get('parking_no', instance.parking_no)
        instance.status = validated_data.get('status', instance.status)
        
        instance.save()
        return instance