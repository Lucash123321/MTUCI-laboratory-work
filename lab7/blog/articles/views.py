from .models import Article, User
from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth import login
from django.shortcuts import get_object_or_404


def archive(request):
    return render(request, 'archive.html', {"posts": Article.objects.all()})


def get_article(request, article_id):
    try:
        post = Article.objects.get(id=article_id)
        return render(request, 'article.html', {"post": post})
    except Article.DoesNotExist:
        raise Http404


def create_post(request):
    if not request.user.is_anonymous:
        if request.method == "POST":
            form = {
                'text': request.POST["text"], 'title': request.POST["title"]
            }
            if form["text"] and form["title"] and not({'title': form["title"]} in Article.objects.all().values('title')):
                Article.objects.create(text=form["text"], title=form["title"], author=request.user)
                article = Article.objects.get(title=form["title"])
                return redirect(get_article, article_id=article.id)
            else:
                if {'title': form["title"]} in Article.objects.all().values('title'):
                    form['errors'] = u"Ваш заголовок не уникален, придумайте другой заголовок."
                    return render(request, 'create_post.html', {'form': form})
                form['errors'] = u"Не все поля заполнены"
                return render(request, 'create_post.html', {'form': form})
        else:
            return render(request, 'create_post.html')

    else:
        raise Http404


def register(request):
    if request.method == "POST":
        form = {
            'username': request.POST["username"], 'password': request.POST["password"]
        }
        if form["username"] and form["password"] and not ({'username': form["username"]} in User.objects.all().values('username')):
            User.objects.create(password=form["password"], username=form["username"])
            user = User.objects.get(username=form["username"])
            login(request, user)
            return redirect('/')
        else:
            if {'username': form["username"]} in User.objects.all().values('username'):
                form['errors'] = u"Ваш логин занят, придумайте другой."
                return render(request, 'register.html', {'form': form})
            form['errors'] = u"Не все поля заполнены"
            return render(request, 'register.html', {'form': form})
    else:
        return render(request, 'register.html')


def authorize(request):
    if request.method == "POST":
        form = {
            'username': request.POST["username"], 'password': request.POST["password"]
        }
        if form["username"] and form["password"] and User.objects.filter(username=form["username"], password=form["password"]):
            user = User.objects.get(username=form["username"], password=form["password"])
            login(request, user)
            return redirect('/')
        else:
            if not form["password"] or not form["username"]:
                form['errors'] = u"Не все поля заполнены"
                return render(request, 'login.html', {'form': form})

            form['errors'] = u"Неправильный логин или пароль."
            return render(request, 'login.html', {'form': form})
    else:
        return render(request, 'login.html')