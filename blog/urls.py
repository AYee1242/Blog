
from . import views
from django.urls import path

urlpatterns = [
    path('', views.Index.as_view(), name="index"),
    path('posts', views.Posts.as_view(), name="all-posts"),
    path('post/<slug:slug>', views.PostDetail.as_view(), name="post"),
    path('bookmark', views.ReadLaterView.as_view(), name="bookmark"),
    path('sign-up', views.SignUp.as_view(), name="sign-up"),
    path('sign-in', views.SignIn.as_view(), name="sign-in"),
    path('sign-out', views.sign_out, name="sign-out")
]
