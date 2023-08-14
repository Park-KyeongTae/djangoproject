from django.urls import path
from django.contrib.auth import views as auth_views
from user import views

app_name = "user"

urlpatterns = [
    # path("register/", views.register, name="register"),
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="user/login.html"
        ),  # LoginView 클래스를.as_view(함수)처럼 사용하겠다
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(),
        name="logout",
    ),
    path("register/", views.register, name="register"),
    # path(
    #     "password_change/",
    #     auth_views.PasswordChangeView.as_view(),
    #     name="password_change",
    # ),
    path(
        "password_change/",
        views.CustomPasswordChangeView.as_view(),
        name="password_change",
    ),
]
