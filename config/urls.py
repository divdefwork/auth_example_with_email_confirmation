from django.contrib import admin
from django.urls import path, include

from my_project_app.views import IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", IndexView.as_view(), name='index'),
    path("accounts/", include('accounts.urls'), )
]
