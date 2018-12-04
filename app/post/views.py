from django.shortcuts import render

from django.http import JsonResponse

from .models import Post


# def my_view(request):
#     posts = Post.objects.all().values('id', 'text')
#     return JsonResponse(list(posts), safe=False)



#  caching적용 위해 view부분 변경하자.

from django.core.cache import cache


def my_view(request):
    posts = cache.get_or_set('posts', Post.objects.all().values('id', 'text'))
    return JsonResponse(list(posts), safe=False)