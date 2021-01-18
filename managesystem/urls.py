
from django.contrib import admin
from django.urls import path, include
from main_app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),
    path('accounts/', include('allauth.urls')),
    path('email/', views.send_email),
    path('signup/', views.signup_view, name='signup'),
    path('signin/', views.signin_view, name='signin'),
    path('home/', views.onbuild_page, name='build'),





    *static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

]
