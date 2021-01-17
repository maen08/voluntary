
from django.contrib import admin
from django.urls import path
from main_app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),




    *static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

]