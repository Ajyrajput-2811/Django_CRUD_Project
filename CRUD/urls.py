from django.urls import path
from CRUD import views

urlpatterns = [
    path('',views.home, name="showdata"),
    path('delete/<int:id>/',views.delete_data, name="deletedata"),
    path('<int:id>/',views.updated_data, name="updatedata"),

]