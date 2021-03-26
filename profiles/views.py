from django.shortcuts import render
from .models import UserProfile

def profile(request):
    """ Display user's profile matafakka """

    template = 'profiles/profile.html'
    context = {
        'profile': profile,
    }

    return render(request, template, context)
