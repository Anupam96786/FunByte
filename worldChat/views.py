from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'wc_index.html')


@login_required
def chat(request):
    return render(request, 'wc_chat.html')
