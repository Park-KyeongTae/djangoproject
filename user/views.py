from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.db import transaction

from .forms import UserForm


@transaction.atomic
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