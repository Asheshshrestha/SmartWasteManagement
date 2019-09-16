from django.urls import path, include
from blogs.views import BlogCreateView,Display_blogs
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
   
    path('create/', BlogCreateView.as_view(), name='create_blogs'),
    path('blog_list/',Display_blogs,name='blog_list'),
    # path('<str:category>/<int:pk>/', NewsDetail.as_view(), name='news_detail'),
    # path('<int:pk>/delete', NewsDeleteView.as_view(), name='delete_news'),
    # path('<int:pk>/update', NewsUpdateView.as_view(), name='update_news'),
    # path('category/<str:category>', CategoryListView.as_view(), name='news-cat'),
    # path('<str:category>/<int:post_id>/comment', comment, name='comment'),
    # # path('<str:category>/<int:pk>', CategoryListView.as_view(), name='news-category'),

   
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)