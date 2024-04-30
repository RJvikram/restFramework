from rest_framework import serializers

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length = 150)
    roll = serializers.IntegerField()
    age = serializers.CharField(max_length = 150)