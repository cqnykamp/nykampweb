from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

lowest_priority = 5
default_priority = 3

class Item(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField()
	start_date = models.DateTimeField()
	end_date = models.DateTimeField()
	priority = models.PositiveSmallIntegerField(
		default = default_priority)
	completed = models.BooleanField(default = False)
	user = models.ForeignKey(User)

	def __str__(self):
		return self.title
		
	def get_absolute_url(self):
		return reverse('tasks:detail', kwargs = {"task_id": str(self.id)})
		
	def get_edit_url(self):
		return reverse('tasks:edit', kwargs = {"task_id": str(self.id)})
