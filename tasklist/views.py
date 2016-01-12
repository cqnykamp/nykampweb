from django.shortcuts import render
from django.views.generic import ListView, View
from django.http import JsonResponse

from .models import Item

class TaskIndexView (ListView):
	queryset = Item.objects.order_by('start_date')
	template_name='tasklist/index.html'


class ToggleCompletedView (View):
	
	def post(self, request, *args, **kwargs):
	
		try:
			item_id = request.POST['id']
		except KeyError:
			return JsonResponse({})
	
		try:
			item = Item.objects.get(id = item_id)
		except Item.DoesNotExist:
			return JsonResponse({})
		
		item.completed = not item.completed
		item.save()
		
		return JsonResponse({'item_id': item_id, 'completed': item.completed})
