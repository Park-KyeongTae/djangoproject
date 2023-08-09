from django.db import models
from django.contrib.auth.models import User


# 새글 테이블 작성
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
