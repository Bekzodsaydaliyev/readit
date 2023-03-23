import login as login
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import Article, Feedback, Category, Tag, Profile, Comment
from .form import ContactForm, CommentForm, SignUpForm
from django.contrib.auth import login, logout, authenticate


def index(request):
    articles = Article.objects.order_by('-id')
    page_number = request.GET.get('page', 1)
    paginator = Paginator(articles, 2)
    try:
        page_obj = paginator.page(page_number)
    except EmptyPage:
        page_obj = paginator.page(1)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    ctx = {
        'objects_list': page_obj,
    }
    return render(request, 'readit/index.html', ctx)


def detail(request, pk):
    article = get_object_or_404(Article, id=pk)
    recent_articles = Article.objects.order_by('id')[:3]
    categories = Category.objects.all()
    tags = Tag.objects.all()
    cat = request.GET.get('cat')
    tag = request.GET.get('tag')
    search = request.GET.get('search')
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(data=request.POST)
        if request.user.is_authenticated:
            if form.is_valid():
                obj = form.save(commit=False)
                obj.author_id = request.user.profile.id
                obj.article_id = article.id
                obj.save()
                return redirect('.')
        return redirect('blog:login')
    ctx = {
        'recent_articles': recent_articles,
        'object': article,
        'categories': categories,
        'tags': tags,
        'tag': tag,
        'cat': cat,
        'search': search,
        'form': form,
    }
    return render(request, 'readit/blog-single.html', ctx)


def list(request):
    articles = Article.objects.order_by('-id')
    cat = request.GET.get('cat')
    tag = request.GET.get('tag')
    search = request.GET.get('search')
    if cat:
        articles = articles.filter(category__title__exact=cat)
    if tag:
        articles = articles.filter(tag__title__exact=tag)
    if search:
        articles = articles.filter(title__icontains=search)
    page_number = request.GET.get('page', 1)
    paginator = Paginator(articles, 3)
    try:
        page_obj = paginator.page(page_number)
    except EmptyPage:
        page_obj = paginator.page(1)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    ctx = {
        'objects_list': page_obj,
        'tag': tag,
        'cat': cat,
        'search': search,
    }
    return render(request, 'readit/blog.html', ctx)


def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('.')
    ctx = {
        'form': form,
    }
    return render(request, 'readit/contact.html', ctx)


def about(request):
    feedbacks = Feedback.objects.order_by('-id')
    ctx = {
        'feedbacks': feedbacks,
    }
    return render(request, 'readit/about.html', ctx)


def footer(request):
    articles = Article.objects.order_by('-id')
    ctx = {
        'objects_list': articles,
    }
    return render(request, 'footer.html', ctx)


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('blog:index')
    return render(request, 'readit/login.html')


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('blog:index')
    return render(request, 'readit/logout.html')


class Register(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('blog:login')
    template_name = 'readit/register.html'


