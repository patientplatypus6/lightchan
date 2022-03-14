from django.urls import path
from django.conf.urls.static import static
# from django.conf import settings

from . import views

urlpatterns = [
  path('comment/<int:comment_id>/', views.comment, name='comment'),
  path('comments/<slug:board_mnemonic>/', views.comments, name='comments'),
  path('reply/<int:incoming_id>/', views.reply, name='reply')
]