from django.conf.urls import url
from django.urls import include, path
from basicapp import views

# TEMPLATE TAGGING

app_name = 'basicapp'

urlpatterns = [
    path('relative/', views.relative, name='relative'),
    path('other/', views.other, name='other'),

]
