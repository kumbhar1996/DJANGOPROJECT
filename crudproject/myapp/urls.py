
from django.urls import path
from . import views
urlpatterns = [
    path('home/',views.home),
    path('',views.add_show,name='addandshow'),
    path('delete/<int:id>/',views.delete_data,name='deletedata'),
    path('<int:id>/',views.update_data,name='updatedata'),
]
