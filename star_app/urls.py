from django.urls import path
from . import views

urlpatterns = [
    path('stars', views.StarList.as_view(), name='star_list'),
    path('stars/<int:pk>', views.StarDetail.as_view(), name='star_detail')
]