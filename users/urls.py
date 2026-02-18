from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from users.apps import UsersConfig
from users.views import custom_login

# from users.views import UserCreateView, email_verification
# from users.forms import LoginForm
from . import views

app_name = UsersConfig.name  # 'users'

urlpatterns = [
    # path("", views.index, name="index"),
    path('login/', custom_login, name='login'),
    # path('login/', LoginView.as_view(template_name="login.html", redirect_authenticated_user=True, ), name='login'),
    # path('login/', LoginView.as_view(template_name="login.html"), name='login'),
    # path("login/", LoginView.as_view(authentication_form=LoginForm, template_name="login.html"), name="login"),
    # path("logout/", LogoutView.as_view(next_page='/'), name="logout"),
    path("logout/", LogoutView.as_view(), name="logout"),
    # path("register/", UserCreateView.as_view(), name="register"),
    # path("email-confirm/<str:token>/", email_verification, name="email-confirm"),
]
