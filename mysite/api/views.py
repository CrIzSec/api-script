import base64
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers

class InputSerializer(serializers.Serializer):
    input_text = serializers.CharField()

class DecodeSerializer(serializers.Serializer):
    input_text = serializers.CharField()

class RunScriptView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = InputSerializer(data=request.data)
        if serializer.is_valid():
            input_text = serializer.validated_data.get('input_text')
            result = self.run_script(input_text)
            return Response({'result': result}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def run_script(self, input_text):
        # Jalankan skrip Python di sini
        text_bytes = input_text.encode('utf-8')
        base64_bytes = base64.b64encode(text_bytes)
        base32_bytes = base64.b32encode(base64_bytes)
        base32_string = base32_bytes.decode('utf-8')
        return base32_string

class RunDecodeView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = DecodeSerializer(data=request.data)
        if serializer.is_valid():
            input_text = serializer.validated_data.get('input_text')
            results = self.run_script(input_text)
            return Response({'results': results}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def run_script(self, input_text):
        try:
            base32_bytes = base64.b32decode(input_text)
            base64_bytes = base64.b64decode(base32_bytes)
            original_text = base64_bytes.decode('utf-8')
            return original_text
        except Exception as e:
            print(f"Error in run_script: {e}")
            return str(e)
