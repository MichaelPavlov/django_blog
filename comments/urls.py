from django.conf.urls import url, include

from comments.views import comment_thread

urlpatterns = [
	url(r'^(?P<id>\d+)/$', comment_thread, name="thread"),
	url(r'^posts/', include("posts.urls", namespace='posts')),
]
