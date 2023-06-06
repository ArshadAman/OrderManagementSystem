from django.urls import path
from .views import check_quality, check_quality_login, check_quality_logout

urlpatterns = [
    path("check-quality/", view=check_quality, name="check-quality"),
    path("check-quality/login/", view=check_quality_login, name="login-quality"),
    path("check-quality/logout/", view=check_quality_logout, name="logout-quality"),
]
