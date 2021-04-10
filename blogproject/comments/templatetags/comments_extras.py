#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :comments_extras.py
# @Time      :2021/4/10 16:54
# @Author    :Willbur

from django import template
from ..forms import CommentForm

register = template.Library()


@register.inclusion_tag('comments/inclusions/_form.html', takes_context=True)
def show_comment_form(context, post, form=None):
    if form is None:
        form = CommentForm()
    return {
        'form': form,
        'post': post,
    }