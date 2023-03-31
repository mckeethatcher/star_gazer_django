from django.urls import path
from . import views

urlpatterns = [
    path('experiences', views.CrudList.as_view(), name='crud_list'),
    path('experiences/<int:pk>', views.CrudDetail.as_view(), name='crud_detail')
]