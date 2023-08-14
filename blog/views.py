from django.shortcuts import render, get_object_or_404, redirect
from .forms import BlogPost
from .models import Post
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.decorators import login_required


# 기본 화면
def index(request):
    # 입력 단자
    page = request.GET.get("page", 1)  # 페이지

    # POST 모델 정보 list에 담기
    post_list = Post.objects.order_by("-created_at")

    # 페이징 처리
    paginator = Paginator(post_list, 5)  # 페이지당 5개씩 보여주기
    page_obj = paginator.get_page(page)

    # 화면단에 보여줄 수 있게 담기
    context = {"post_list": page_obj}

    return render(request, "blog/list.html", context)


#  상세 조회
def detail(request, pid):
    list = get_object_or_404(Post, id=pid)

    context = {"list": list}

    return render(request, "blog/detail.html", context)


# 새글 올리기
@login_required
def post_create(request):
    # 글 등록
    if request.method == "POST":
        form = BlogPost(request.POST, request.FILES)  # 이미지 파일

        if form.is_valid():
            post = form.save(commit=False)
            post.author = User.objects.all()  # 로그인한 사용자
            post.save()
            return redirect("blog:index")
    else:
        form = BlogPost()

    context = {
        "form": form,
    }

    return render(request, "blog/post_create.html", context=context)


# 댓글 올리기


def comment_create(request, pid):
    """
    댓글 등록
    post.comment_set.create()
    """
    post = get_object_or_404(Post, id=pid)
    # save()명령어 안해도 됨
    post.comment_set.create(content=request.POST["content"], author=request.user)

    return redirect("blog:detail", pid=pid)


def comment_edit(request, cid):
    pass


def comment_delete(request, cid):
    pass


# def modify(request, pid):
#     """
#     질문 수정
#     """

#     question = get_object_or_404(Post, pk=pid)
#     if request.user != Post.author:
#         messages.error(request, "수정권한이 없습니다.")
#         return redirect("blog:detail", pid=pid)

#     if request.method == "POST":
#         form = BlogPost(request.POST, instance=question)
#         if form.is_valid():
#             question = form.save(commit=False)
#             question.author = request.user
#             question.modified_at = timezone.now()  # 수정날짜 저장
#             question.save()
#             return redirect("blog:detail", pid=pid)

#     else:
#         form = BlogPost(instance=question)
#     context = {
#         "form": form,
#     }
#     return render(request, "blog/detail.html", context)
