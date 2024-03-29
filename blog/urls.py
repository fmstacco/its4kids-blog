from . import views
from django.urls import path
from .views import ActivitiesView, AddPostView, UpdatePostView, DeletePostView

urlpatterns = [
    path("", views.PostList.as_view(), name='home'),
    path('blog/', ActivitiesView.as_view(), name='blog'),
    path('add_post/', views.AddPostView.as_view(), name='add_post'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path(
        'update_post/<slug:slug>/',
        UpdatePostView.as_view(),
        name='update_post'
    ),
    path(
        'delete_post/<slug:slug>/',
        DeletePostView.as_view(),
        name='delete_post'
        ),

]
