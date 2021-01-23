
from django.contrib import admin
from django.urls import path, include
from main_app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),
    path('register/', views.register, name='register'),
    # path('signin/', views.signin_view, name='signin'),
    path('new-activity/', views.display_activity, name='new_activity'),
    path('create/', views.create_activity, name='create_activity'),
    path('applied/', views.applied_activity, name='applied_activity'),
    path('login/', views.login_view, name='login'),






    *static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

]
