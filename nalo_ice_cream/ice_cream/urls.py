from django.urls import path

from . import views

app_name = "ice_cream"
urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name="create"),
    path('detail/', views.detail, name='detail'),
    path('admin/', views.admin, name='admin')
]
