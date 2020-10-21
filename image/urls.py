from django.conf.urls import url
from . import views
from .views import PostListview,PostCreateview,PostUpdateview,PostDeleteview
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
  url(r'^$',PostListview.as_view(),name='index'),
  url(r'^image/(?P<image_id>\d+)/$',views.one_image,name='one_image'),
  url(r'^newpost/',PostCreateview.as_view(),name='post_create'),
  url(r'^image/(?P<pk>\d+)/update/',PostUpdateview.as_view(),name='post_update'),
  url(r'^image/(?P<pk>\d+)/delete/',PostDeleteview.as_view(),name='post_delete'),


]

if settings.DEBUG:
  urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)