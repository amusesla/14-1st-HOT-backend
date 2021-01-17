import re

from django.urls import path
from .views      import RegisterView, LogInView, FollowView, UnFollowView, LikeView, UnLikeView, BookmarkView, UnBookmarkView, MyPageView, SampleView


urlpatterns = [
    path('/register', RegisterView.as_view()),
    path('/login', LogInView.as_view()),
    path('/friendships/{int:user_id}/follow', FollowView.as_view()),
    path('/friendships/{int:user_id}/unfollow', UnFollowView.as_view()),
    path('/bookmark', BookmarkView.as_view()),
    path('/unbookmark', UnBookmarkView.as_view()),
    path('/user_id', MyPageView.as_view()),
]
