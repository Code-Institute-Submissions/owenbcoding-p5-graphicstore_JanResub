from django.shortcuts import render
from django import forms
from .forms import NewsletterForm
from django.shortcuts import get_object_or_404, redirect, render, reverse
from .models import Newsletter
from django.http import HttpResponseRedirect



def index(request): 
    """ A view to return the index page"""
    form = NewsletterForm()
    context = { 
        'form': form,
    }

    return render(request, 'home/index.html', context)


def about(request): 
    """ A view to return the about page"""
    return render(request, 'home/about.html')


def subscribe(request):
    """ Part of Custom model Crud for creating a newsletter by subscribing """
    form = NewsletterForm(request.POST)
    if form.is_valid():
        form = form.save(commit=False)
        if request.user.is_authenticated:
            form.user_id = request.user
        else:
            form.user_id = None
        form.save()
    return redirect('index')


def unsubscribe(request):
    """Part of Custom model Crud for news letter A user or guest can ubsubscribe / delete their email from updates"""
    form = NewsletterForm(request.POST)
    if request.user.is_authenticated:
        newsletter = Newsletter.objects.get(user_id=request.user)
        newsletter.delete()
    else:
        if form.is_valid():
            newsletter = Newsletter.objects.get(
                email=form.cleaned_data["email"]
            )
            newsletter.delete()
    return HttpResponseRedirect(reverse("index"))