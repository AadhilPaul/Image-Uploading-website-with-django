from django.urls import path
from . import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from .views import PostUpdateView
from django.views.static import serve
from .views import PostDeleteView, AddCommentView

# Create your urls here.

urlpatterns = [
    path("", views.home, name="home"),
    path("post/<int:id>", views.post_view, name="post-view"),
    path("search/<str:search>", views.search_results, name="search-results"),
    path("newpost/", views.post, name="new_post"),
    path("post/<int:pk>/comment", views.AddCommentView.as_view(), name="add-comment"),
    path("posts/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name="post-delete"),
    path('like/<int:pk>', views.LikeView, name="like-post"),
    url(r'^download/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]

# Allow media root to work 
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)