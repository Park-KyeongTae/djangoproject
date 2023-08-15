from django.urls import path
from blog import views

app_name = "blog"

urlpatterns = [
    # 기본 페이지
    path("", views.index, name="index"),
    # 상세 조회
    path("<int:pid>/", views.detail, name="detail"),
    # 게시글 등록
    path("post/create/", views.post_create, name="post_create"),
    # 게시글 수정
    path("post/modify/<int:pid>/", views.post_edit, name="post_modify"),
    # 게시글 삭제
    path("post/delete/<int:pid>/", views.post_delete, name="post_delete"),
    ###############################################################################################################
    # 댓글 등록
    path("comment/create/<int:pid>/", views.comment_create, name="comment_create"),
    # 댓글 수정
    path("comment/modify/<int:cid>/", views.comment_edit, name="comment_modify"),
    # 댓글 삭제
    path("comment/delete/<int:cid>/", views.comment_delete, name="comment_delete"),
]
