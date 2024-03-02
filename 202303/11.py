





# views.py

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt  # Only use this decorator for testing purposes, consider CSRF protection in production
def your_view_function(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            json_data1 = data.get('json_data1')
            json_data2 = data.get('json_data2')

            # Process the JSON data as needed
            response_data = {
                'json_data1': json_data1,
                'json_data2': json_data2
            }
            return JsonResponse(response_data)
        except json.JSONDecodeError as e:
            return JsonResponse({'error': 'Invalid JSON format'}, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
        
        
        
        # api/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class YourAPIView(APIView):
    def get(self, request):
        # Handle GET request
        data = {'message': 'GET request received'}
        return Response(data, status=status.HTTP_200_OK)

    def post(self, request):
        # Handle POST request
        received_data = request.data
        # Process the received data
        # For example, if you expect 'key1' and 'key2' in the JSON data:
        key1_value = received_data.get('key1')
        key2_value = received_data.get('key2')
        # Process the data further as needed
        
        # Return a response
        response_data = {'message': 'POST request received and processed', 
                         'key1': key1_value,
                         'key2': key2_value}
        return Response(response_data, status=status.HTTP_201_CREATED)
        
        