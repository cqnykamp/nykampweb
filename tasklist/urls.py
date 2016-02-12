from django.conf.urls import include, url
from .views import TaskIndexView, ToggleCompletedView, TaskDetailView, TaskEditView

urlpatterns = [
    url(r'^$', TaskIndexView.as_view(), name="index"),
    url(r'^toggle_completed$', ToggleCompletedView.as_view(), name="toggle_completed"),
    url(r'^(?P<task_id>\d+)$', TaskDetailView.as_view(), name="detail"),
    url(r'^(?P<task_id>\d+)/edit$', TaskEditView.as_view(), name="edit"),

]
