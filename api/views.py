from django.http import JsonResponse
from django.forms.models import model_to_dict

from .models import Hack
from .utils.apiResponse import apiResponse
from .utils.format import format_hacks


# Create your views here.
def index(request):
	return apiResponse(
		'success',
		'Welcome to the Hacks-API'
	)


def get_all_hacks(request):
	try:
		hacks = Hack.objects.all().select_related()
	except:
		return apiResponse(
			'error',
			'Error fetching hacks!'
		)
	return apiResponse(
		'success',
		format_hacks(hacks)
	)
