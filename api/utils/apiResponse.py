from django.http import JsonResponse


def apiResponse(status, message):
	response = {
		'status': status,
	}
	if (status == 'success'):
		response['data'] = message
	else:
		response['message'] = message
	return JsonResponse(response)
