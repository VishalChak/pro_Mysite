from django.conf.urls import url,include
from django.views.generic import ListView,DetailViews
from blog.models import Post

urlpatterns = [
	url(r'^$',ListView.asview(queryset=Post.objects.all().order_by("-date")[:25], tamplate_name = 'blog/blog.html'))]


