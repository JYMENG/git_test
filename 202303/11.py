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