from django.urls import path, include
#from . import views
from .views import HomeView, ArticleDetailViews, AddPostView, UpdatePostView, DeletePostView, AddCategoryView, CategoryView, CategoryListView, LikeView, AddCommentView


urlpatterns = [
    #path('', views.home, name='home')
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailViews.as_view(), name="article_detail"),
    path('addpost/', AddPostView.as_view(), name="add_post"),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name="update_post"),
    path('article/<int:pk>/delete', DeletePostView.as_view(), name="delete_post"),
    path('article/addcategory', AddCategoryView.as_view(), name="add_category"),
    path('category/<str:categorys>/', CategoryView, name='category'),
    path('category_list/', CategoryListView, name='category-list'),
    path('like/<int:pk>', LikeView, name="like_post"),
    path('article/<int:pk>/comment', AddCommentView.as_view(), name="add_comment"),
]
