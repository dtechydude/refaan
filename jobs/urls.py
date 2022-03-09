from django.urls import path
from .views import(
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
   # AddCategoryView
)
from . import views




urlpatterns = [

    #path('', views.blogpage, name='blog-home'),   --function-base biew
    path('post/', PostListView.as_view(), name='jobs-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    #path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'), #disabled because of using slug
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<slug:slug>/', PostDetailView.as_view(), name='post-detail'), #for using slug
    #path('category/new/', AddCategoryView.as_view(), name='add-category'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'), #used without slug
    #path('post/<slug:slug>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

]