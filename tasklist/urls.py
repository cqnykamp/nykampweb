from django.conf.urls import include, url
from .views import TaskIndexView

urlpatterns = [
    url(r'^$', TaskIndexView.as_view(), name="index"),

]
