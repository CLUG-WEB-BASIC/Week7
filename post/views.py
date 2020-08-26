from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from django.utils import timezone
from django.core.paginator import Paginator

def read_blog_list(request):
    blogs = Blog.objects.all()  # 쿼리셋 = 전달받은 모델의 객체 목록 # 쿼리셋을 템플릿으로 보내기
    #몇 개씩?
    paginator = Paginator(blogs,2)
    #지금 보려는 페이지는?
    page = request.GET.get('page')
    #새로 담아서 보내주자
    posts = paginator.get_page(page)
    return render(request, 'post/blog_list.html', {'posts': posts})

def read_blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'post/blog_detail.html', {'blog': blog})

def blog_new(request):
    return render(request, 'post/blog_new.html')

def create_blog(request):
    blog = Blog()
    blog.title = request.POST['title'] #get과 post의 차이는 ppt에서 참고
    blog.body = request.POST['body']
    blog.pub_date = timezone.datetime.now()
    blog.save() #쿼리 메소드
    return redirect('read_blog_list')

def update_blog(request, blog_id):  #url, html 에서도 처리해주기
    #객체 탐색
    blog = get_object_or_404(Blog, pk=blog_id)
    #data 입력
    if request.method == "POST":
        blog.title = request.POST['title']
        blog.body = request.POST['body']
        blog.pub_date = timezone.datetime.now()
        #data 저장
        blog.save()

        return redirect('read_blog_detail', blog_id)
    else:
        return render(request, 'post/blog_edit.html',  {'blog': blog})

def delete_blog(request, blog_id):  #url, html 에서도 처리해주기
    #객체 탐색
    blog = get_object_or_404(Blog, pk =blog_id)
    # 삭제
    blog.delete()
    # 리스트 페이지로 ㄱㄱ
    return redirect('read_blog_list')
