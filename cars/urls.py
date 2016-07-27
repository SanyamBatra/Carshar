from django.conf.urls import url
from.import views

app_name = 'cars'

urlpatterns = [

    url(r'^$', views.main, name='main'),
    url(r'^upcomingcars/$', views.upcoming, name='coming'),
    url(r'^carmodels/$', views.details, name='det'),
    url(r'^alert_me/(?P<which_car>[\w ]+)/$', views.formfill, name='fill'),
    url(r'^alert_me/(?P<which_car>[\w ]+)/sending_mail/$', views.mail, name='mail'),
    url(r'^used-cars\sin/(?P<city>[\w]+)/$', views.used, name="use")
]
