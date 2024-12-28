from django.urls import path
from .views import *

urlpatterns = [
    path('create/',create_job,name="createjob"),
    path('update/<int:id>/',update_job,name="updatejob"),
    
]
