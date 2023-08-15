from django.shortcuts import render, get_object_or_404, redirect
from .forms import BlogPost, BlogComment
from .models import Post, Comment
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.decorators import login_required


# 기본 화면
def index(request):
    # 입력 단자
    page = request.GET.get("page", 1)  # 페이지
    # 카테 고리
    category = request.GET.get("category")  # 카테고리

    if category:
        # 카테고리 정보 list 담기
        post_list = Post.objects.filter(category=category).order_by("-created_at")
    else:
        # POST 모델 정보 list에 담기
        post_list = Post.objects.order_by("-created_at")

    # POST 모델 정보 list에 담기
    # post_list = Post.objects.order_by("-created_at")

    # 페이징 처리
    paginator = Paginator(post_list, 5)  # 페이지당 5개씩 보여주기
    page_obj = paginator.get_page(page)

    # 선택한 카테고리 활성화
    category_filter = request.GET.get("category")

    # 화면단에 보여줄 수 있게 담기
    context = {
        "post_list": page_obj,
        "category_list": Post.BLOG_CATE_CHOICES,
        "category": category_filter,  # 'category' 키를 추가
    }

    return render(request, "blog/list.html", context)


#  상세 조회
def detail(request, pid):
    list = get_object_or_404(Post, id=pid)

    context = {"list": list}

    return render(request, "blog/detail.html", context)


# 새글 올리기
@login_required(login_url="user:login")
def post_create(request):
    # 글 등록
    if request.method == "POST":
        form = BlogPost(request.POST, request.FILES)  # 이미지 파일

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # 로그인한 사용자
            post.save()
            return redirect("blog:index")
    else:
        form = BlogPost()

    context = {
        "form": form,
    }

    return render(request, "blog/post_create.html", context=context)


# 게시글 수정
@login_required(login_url="user:login")
def post_edit(request, pid):
    """
    게시글 수정
    """
    post = get_object_or_404(Post, id=pid)

    if request.method == "POST":
        form = BlogPost(request.POST, instance=post)

        if form.is_valid():
            # 수정날짜 추가해야됨
            post = form.save(commit=False)
            post.modifed_at = timezone.now()
            post.save()
            return redirect("blog:detail", pid=pid)
    else:
        form = BlogPost(instance=post)

    return render(
        request,
        "blog/post_edit.html",
        {"form": form},
    )


# 게시글 삭제
@login_required(login_url="user:login")
def post_delete(request, pid):
    """
    게시글 삭제
    """
    post = get_object_or_404(Post, id=pid)
    post.delete()

    return redirect("blog:index")


#################################################################################################################
# 댓글 등록
@login_required(login_url="user:login")
def comment_create(request, pid):
    """
    댓글 등록

    post.comment_set.create()
    """
    post = get_object_or_404(Post, id=pid)
    # save()명령어 안해도 됨
    post.comment_set.create(content=request.POST["content"], author=request.user)

    return redirect("blog:detail", pid=pid)


# 댓글 수정
@login_required(login_url="user:login")
def comment_edit(request, cid):
    # Comment 모델 찾기
    comment = get_object_or_404(Comment, id=cid)

    if request.method == "POST":
        form = BlogComment(request.POST, instance=comment)
        if form.is_valid():
            form = BlogComment(request.POST, instance=comment)
            comment = form.save(commit=False)
            comment.modified_at = timezone.now()
            comment.save()
            return redirect("blog:detail", pid=comment.post_id)
    else:
        form = BlogComment(instance=comment)

    return render(request, "blog/comment_edit.html", {"form": form})


# 댓글 삭제
@login_required(login_url="user:login")
def comment_delete(request, cid):
    print("댓글 삭제 함수 실행")  # print 문 추가
    # Comment 모델 찾기
    comment = get_object_or_404(Comment, id=cid)
    comment.delete()
    messages.success(request, "댓글이 삭제되었습니다.")
    return redirect("blog:detail", pid=comment.post_id)
