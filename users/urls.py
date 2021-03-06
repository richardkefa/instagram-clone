from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns=[
  url('^newuser/',views.register,name='register'),
  url('^login/',auth_views.LoginView.as_view(template_name='login.html'),name='login'),
  url('^logout/',auth_views.LogoutView.as_view(template_name='logout.html'),name='logout'),
  url('^profiles/',views.profile,name='profile'),

]

if settings.DEBUG:
  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)