from django.urls import path
from .views import view_orders, view_perticular_order, master_login, logout_master

urlpatterns = [
    path('master-login/', view=master_login, name='master-login'),
    path('master-logout/', view=logout_master, name='master-logout'),
    path('view-orders/', view=view_orders, name='view-orders'),
    path('<str:id>/', view=view_perticular_order, name='view-perticular-order'),
    # path('update-status/', view=status_of_order, name="update-status")
]
