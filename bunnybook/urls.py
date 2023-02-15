from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('posts/', views.PostList.as_view(), name='post_list'),
    path('posts/<int:pk>/', csrf_exempt(views.PostDetail.as_view()), name='post_detail'),
    path('posts/<int:pk>/comments/', views.CommentList.as_view(), name='comment_list'),
    path('comments/<int:pk>/', csrf_exempt(views.CommentDetail.as_view()), name='comment_detail'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', csrf_exempt(views.LoginView.as_view()), name='login'),
]
