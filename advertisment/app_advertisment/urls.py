from django.urls import path
from .views import index, top_sellers, advertisement_post, register, login, profile, advertisement

urlpatterns = [
    path('index.html/', index, name="main-page"),
    path('top-sellers/', top_sellers, name="top-sellers"),
    path('advertisement-post.html/', advertisement_post, name="advertisement-post"),
    path('register.html/', register, name="register"),
    path('login.html/', login, name="login"),
    path('profile.html/', profile, name="profile"),
    path('advertisement.html/', advertisement, name="advertisement"),
]