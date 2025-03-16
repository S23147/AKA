from django.urls import path
from .views import assigner_role

urlpatterns = [
    path('assigner_role/<int:user_id>/<str:role>/', assigner_role, name='assigner_role'),
]
