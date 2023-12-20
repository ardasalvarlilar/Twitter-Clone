from django.urls import path
from .views import *
urlpatterns = [
  path('home/', home_view, name="home_page"),
  path('/<slug:post_slug>/',post_detay_view,name="post_detay_page"),
  path('gündemler/<slug:hashtag_slug>/', hashtag_detay_view,name="hashtag_detay_page"),
  path('post-detay/post-edit/<slug:post_slug>/',post_edit_view,name="post_edit_page"),
  path('post-detay/yorum-edit/<slug:yorum_slug>/',yorum_edit_view,name="yorum_edit_page"),
  path('yorum-detay/<slug:yorum_slug>/',yorum_detay_view, name="yorum_detay_page"),
  path('post-delete/<slug:post_slug>/',post_delete_view,name="post_delete_page"),
  path('yorum-delete/<slug:yorum_slug>/',yorum_delete_view,name="yorum_delete_page")
]
