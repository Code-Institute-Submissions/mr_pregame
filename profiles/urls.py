from django.urls import path
from . import views


urlpatterns = [
    path('', views.profile, name='profile'),
    path('get_membership', views.get_membership, name='get_membership'),
    path('update_membership/<subscription_id>/',
         views.update_membership, name='update_membership'),
]