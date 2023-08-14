from django.db import models
from django.contrib.auth.models import User


# 새글 테이블 작성
# 번호는 자동으로 생성됨
# verbose_name 화면에서 보여줄 이름
class Post(models.Model):
    BLOG_CATE_CHOICES = [
        ("0", "일상"),
        ("1", "유머"),
        ("2", "정보"),
    ]

    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="작성자")
    category = models.CharField(
        max_length=1,
        choices=BLOG_CATE_CHOICES,
        default="0",
    )
    subject = models.CharField(max_length=30, verbose_name="제목")
    content = models.TextField(verbose_name="내용")
    image = models.ImageField(blank=True, null=True, verbose_name="이미지")
    # auto_now_add : insert 시 한번
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="작성날짜")
    # auto_now : update 시 매번
    modified_at = models.DateTimeField(auto_now_add=True, verbose_name="수정날짜")

    def __str__(self) -> str:
        return self.subject


# 댓글 테이블
# 질문, 답변 댓글 모두 저장 ==> 구분은 어떻게 할 것인가?
# 번호(자동생성),작성자,댓글내용,작성날짜,수정날짜,외래키(질문,답변 구분을 위해)
class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="작성자")
    content = models.TextField(verbose_name="댓글내용")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="작성날짜")
    modified_at = models.DateTimeField(verbose_name="수정날짜", null=True, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
