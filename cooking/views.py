from django.shortcuts import render
from .models import Category, Post
from django.db.models import F
# from .forms import PostAddForms

def index(request):
    posts = Post.objects.all()

    context = {
        'title': 'Главная страница',
        'posts': posts,

    }
    return render (request, template_name='cooking/index.html', context=context)

def category_list(request, pk):
    posts = Post.objects.filter(category_id = pk)

    context = {
        'title': posts[0].category,
        'posts': posts,

    }
    return render (request, template_name='cooking/index.html', context=context)   

# def add_post(request):
#     if request.method == 'POST':
#         pass
#     else:
#         form = PostAddForms()

#     context = {
#         'form': form,
#         'title': 'Добавить статью'
#     }
#     return  render(request, 'cooking/article_add_form.html', context)
            # Страница статьи
def post_detail(request, pk):
    article = Post.objects.get(pk=pk)
            #счетчик
    Post.objects.filter(pk=pk).update(watched=F('watched') + 1)
            #текст статьи
    context = {
        'title': article.title,
        'post': article
    }
    return render(request, 'cooking/article_detail.html', context)