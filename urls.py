from django.conf.urls import url, patterns
import views

urlpatterns = patterns(
    '',
    url(r'^hello$', views.hello, name = 'hello'),
	url(r'^updateprofile$', views.updateprofile, name='updateprofile'),
)
