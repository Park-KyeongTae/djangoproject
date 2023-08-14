from django.urls import path
from blog import views

app_name = "blog"

urlpatterns = [
    # 기본 페이지
    path("", views.index, name="index"),
    # 새글 올리기
    path("create/", views.post_create, name="post_create"),
    # 상세 조회
    path("<int:pid>/", views.detail, name="detail"),
    # 게시글 수정
    # path("modify/<int:pid>/", views.modify, name="modify"),
    # 댓글 올리기
    # http://localhost:8000/blog/comment/create/질문번호
    path("comment/create/<int:pid>/", views.comment_create, name="comment_create"),
]
