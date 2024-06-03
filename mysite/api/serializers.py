from rest_framework import serializers

class InputSerializer(serializers.Serializer):
    input_text = serializers.CharField()

class DecodeSerializer(serializers.Serializer):
    input_text = serializers.CharField()