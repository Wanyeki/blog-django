from django.shortcuts import render
from django.views import generic
from message.models import Article,Comment
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.shortcuts import get_object_or_404

def home(request):
    return render(request,'messages/home.html',{})

class ArticlesView(generic.ListView):
    template_name='messages/articles.html'
    context_object_name='articles_list'
    def get_queryset(self):
        return Article.objects.all()

def show(request,article_id):
    article=get_object_or_404(Article,pk=article_id)
    comment_list=article.comment_set.all()
    return render(request,'messages/show.html',{'article':article,'comment_list':comment_list})

def add_article(request):
    if  request.POST :
        article=Article(body=request.POST['body'],title=request.POST['title'],pub_date=timezone.now())
        article.save()
        return HttpResponseRedirect(reverse('message:articles'))
    else:
        return render(request,'messages/add.html',{})

def edit_article(request,article_id):
    article=get_object_or_404(Article,pk=article_id)
    if request.POST:
        article.title=request.POST['title']
        article.body=request.POST['body']
        article.save()
        return HttpResponseRedirect(reverse('message:articles')) 
        
    else:
        return render(request,'messages/edit.html',{'article':article})

def delete_article(request,article_id):
    article=get_object_or_404(Article,pk=article_id)
    article.delete()
    return HttpResponseRedirect(reverse('message:articles'))

def comment(request,article_id):
    if request.POST:
        article=get_object_or_404(Article,pk=article_id)
        comment=article.comment_set.create(commenter=request.POST['commenter'],body=request.POST['body'],comment_date=timezone.now())
        comment.save()
        return HttpResponseRedirect(reverse('message:show',args=(article_id,)))
    else:
        return render(request,'messages/comment.html',{'article_id':article_id})

def delete_comment(request,article_id,comment_id):
    comment=get_object_or_404(Comment,pk=comment_id)
    comment.delete()
    return HttpResponseRedirect(reverse('message:show',args=(article_id,)))

def edit_comment(request,article_id,comment_id):
    comment=get_object_or_404(Comment,pk=comment_id)
    if request.POST:
        comment.commenter=request.POST['commenter']
        comment.body=request.POST['body']
        comment_date=timezone.now()
        comment.save()
        return HttpResponseRedirect(reverse('message:show',args=(article_id,)))
    else:
        return render(request,'messages/edit_comment.html',{'comment':comment,'article_id':article_id})

# Create your views here.
