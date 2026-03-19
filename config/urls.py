from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from users.views import UserListView, UserUpdateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("mailing.urls", namespace="mailing")),
    path("users/", include("users.urls", namespace="users")),
    # # URL для менеджеров
    # path('managers/users/', UserListView.as_view(), name='users_list'),
    path('managers/users/<int:pk>/update/', UserUpdateView.as_view(), name='user_update'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
