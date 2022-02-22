from django.urls import path

from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('comment/<int:comment_id>/', views.comment, name='comment'),
  path('comments/', views.comments, name='comments')
  
  # path('reply/<int:reply_id>/', views.reply, name='reply')
  # path('replies/', views.replies, name='replies')
]