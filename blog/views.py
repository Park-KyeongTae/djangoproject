from django.shortcuts import render, get_object_or_404, redirect
from .forms import BlogPost
from .models import Post
from django.contrib.auth.models import User


# 기본 화면
def index(request):
    # POST 모델 정보 list에 담기
    list = Post.objects.all()
    # 화면단에 보여줄 수 있게 담기
    context = {"list": list}

    return render(request, "blog/list.html", context)


def detail(request, pid):
    list = get_object_or_404(Post, id=pid)

    context = {"list": list}

    return render(request, "blog/detail.html", context)


def samplepost(request):
    if request.method == "POST":
        form = BlogPost(request.POST, request.FILES)  # 이미지 파일
        print(form)

        user = User.objects.get(id=1)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = user
            post.save()
            return redirect("blog:index")
    else:
        form = BlogPost()

    context = {"form": form}

    return render(request, "blog/samplepost.html", context=context)
