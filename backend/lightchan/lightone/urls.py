from django.urls import path

from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('comment/<int:comment_id>/', views.comment, name='comment')
]