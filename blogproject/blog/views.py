from django.shortcuts import render

# Create your views here.
#from django.http import HttpResponse

from django.shortcuts import render,get_object_or_404
from django.utils.text import slugify
from .models import Post
import markdown
from markdown.extensions.toc import TocExtension
import re

def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    return render(request,'blog/index.html',context={'post_list':post_list})

def detail(request,pk):
    post = get_object_or_404(Post,pk=pk)
    md = markdown.Markdown(extensions=['markdown.extensions.extra',
                                       'markdown.extensions.codehilite',
                                       TocExtension(slugify=slugify),
                                       ])
    post.body = md.convert(post.body)
    post.toc = md.toc
    m = re.search(r'<div class="toc">\s*<ul>(.*)</ul>\s*</div>', md.toc, re.S)
    post.toc = m.group(1) if m is not None else ''

    '''post.body = markdown.markdown(post.body,extensions=['markdown.extensions.extra',
                                                        'markdown.extensions.codehilite',
                                                        'markdown.extensions.toc'])'''
    return render(request,'blog/detail.html',context={'post':post})