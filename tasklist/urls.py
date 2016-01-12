from django.conf.urls import include, url
from .views import TaskIndexView, ToggleCompletedView

urlpatterns = [
    url(r'^$', TaskIndexView.as_view(), name="index"),
    url(r'^toggle_completed$', ToggleCompletedView.as_view(), name="toggle_completed"),

]
