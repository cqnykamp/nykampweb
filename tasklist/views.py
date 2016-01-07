from django.shortcuts import render
from django.views.generic import ListView
from .models import Item

class TaskIndexView (ListView):
	queryset = Item.objects.order_by('start_date').filter(completed=False)
	template_name='tasklist/index.html'
	
