from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from users.apps import UsersConfig
from users.views import custom_login, UserListView, UserUpdateView

from users.views import UserCreateView, email_verification
# from users.forms import LoginForm

from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

app_name = UsersConfig.name  # 'users'

urlpatterns = [
    # path("", views.index, name="index"),
    path('login/', custom_login, name='login'),
    # path('login/', LoginView.as_view(template_name="login.html", redirect_authenticated_user=True, ), name='login'),
    # path('login/', LoginView.as_view(template_name="login.html"), name='login'),
    # path("login/", LoginView.as_view(authentication_form=LoginForm, template_name="login.html"), name="login"),
    # path("logout/", LogoutView.as_view(next_page='/'), name="logout"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", UserCreateView.as_view(), name="register"),
    path("email-confirm/<str:token>/", email_verification, name="email-confirm"),
    # Сброс пароля
    path('password-reset/',
         PasswordResetView.as_view(template_name='users/password_reset.html',
         email_template_name='registration/password_reset_email.html'),
         name='password_reset'),
    path('password-reset/done/',
         PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('reset/done/',
         PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),

    path('list/', UserListView.as_view(), name='users_list'),
    path('update/<int:pk>/', UserUpdateView.as_view(), name='user_update'),
]
