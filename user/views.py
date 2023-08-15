from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy

from .forms import UserForm


# 회원등록
def register(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()

            # 회원가입 후 로그인 처리 해주기
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(request, username=username, password=password)

            if user is not None:
                # 세션에 정보가 담기게 됨
                login(request, user)
                return redirect("/")
    else:
        form = UserForm()
    return render(request, "user/register.html", {"form": form})


# 비밀번호 변경 구현
class CustomPasswordChangeView(PasswordChangeView):
    """
    PasswordChangeView 에서 정의한
    template_name 은 registration/password_change_form.html 을 찾게 되어 있음
    success_url 은 password_change_done 으로 이동함
    """

    template_name = "user/password_change.html"
    success_url = reverse_lazy("user:login")
