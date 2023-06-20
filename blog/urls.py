import blog.views
from django.urls import path

urlpatterns = [
    path('', blog.views.post_list, name='post_list'),
    # path('',blog.views.songs_list,name='wangyi')
]