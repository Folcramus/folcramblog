from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.http import *
from .forms import *

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail, send_mass_mail

from django.db.models import Q
from django.views.generic import ListView, DetailView ,CreateView , View

from contact.forms import ContactForm, EmailForm

from django.contrib import messages

def home(request):

    list_news = News.objects.all()
    paginator = Paginator(list_news, 15)  # 3 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)




    paginatiod = posts.has_other_pages()
    if posts.has_previous():
        prev_url = '?page={}'.format(posts.previous_page_number())

    else:
        prev_url = ''

    if posts.has_next():
        next_url = '?page={}'.format(posts.next_page_number())
    else:
        next_url = ''


    form = ContactForm(request.POST or None)

    if request.method == "POST" and form.is_valid() or 'email' in request.POST :
        data = form.cleaned_data['email']

        form.save()
        send_mail(
            'Вы подписались на рассылку',
            'Вечер в хату',
            'ponopaytov@Gmail.com',
            [data],
            fail_silently=False

        )

        messages.success(request, 'Спасибо, вы подписаны на рассылку!')


    return render(request, 'home.html', locals())




def news_page(request, id):

    news = News.objects.all()
    post = News.objects.get(id=id)
    new = get_object_or_404(News, id=id)
    comment = Comments.objects.filter(new=id)
    if request.method == "POST" and 'coment' in request.POST:

        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.new = new 
            form.save()
            return redirect(news_page, id)
    else:
        form = CommentForm()




    if request.method == "POST" and 'emal' in request.POST:
        form2 = EmailForm(request.POST)


        if form2.is_valid():
            data = form2.cleaned_data['email']

            form2.save()
            send_mail(
                'Вы подписались на рассылку',
                'Вечер в хату',
                'ponopaytov@Gmail.com',
                [data],
                fail_silently=False

            )
            messages.success(request, 'Спасибо, вы подписаны на рассылку!')
    else:
        form2 = EmailForm()

    if request.method == "POST" and 'del'  in request.POST and 'comment_id' in request.POST :
        pk = request.POST['comment_id']

        comment = get_object_or_404(Comments, pk=pk)
        comment.delete()
        messages.success(request, 'Ваш комментарий удален')
        return redirect(news_page, id)

    return render(request, 'news.html', locals())


class SearchResultsView(ListView):
    model=News

    template_name = 'search.html'
    def get_queryset(self):
        query = self.request.GET.get('q')

        if query is not None:
            object_list =  News.objects.filter(Q(name__icontains=query) | Q(author__icontains=query))

            return object_list





def search(request):
    query = request.GET.get('q')
    if query is not None:
        object_list = News.objects.filter(Q(name__icontains=query))

    form = ContactForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        data = form.cleaned_data['email']

        form.save()
        send_mail(
            'Вы подписались на рассылку',
            'Вечер в хату',
            'ponopaytov@Gmail.com',
            [data],
            fail_silently=False

        )

        messages.success(request, 'Спасибо, вы подписаны на рассылку!')





    return render(request, 'search.html', locals())





