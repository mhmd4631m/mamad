from myapp import views
from django.urls import path

app_name = 'myapp'

urlpatterns = [
path('',views.index,name='index'),
path('users/',views.user,name='users'),
]
