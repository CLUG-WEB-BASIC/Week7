from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from django.utils import timezone

def read_blog_list(request):
    blogs = Blog.objects.all()  # 쿼리셋 = 전달받은 모델의 객체 목록 # 쿼리셋을 템플릿으로 보내기
    return render(request, 'post/blog_list.html', {'blogs': blogs})

def read_blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'post/blog_detail.html', {'hi': blog})

def blog_new(request):
    return render(request, 'post/blog_new.html')

def create_blog(request):
    blog = Blog()
    blog.title = request.POST['title'] #get과 post의 차이는 ppt에서 참고
    blog.body = request.POST['body']
    blog.pub_date = timezone.datetime.now()
    blog.save() #쿼리 메소드
    return redirect('read_blog_list')

def update_blog(request):
    return render(request, 'post/blog_edit.html')
