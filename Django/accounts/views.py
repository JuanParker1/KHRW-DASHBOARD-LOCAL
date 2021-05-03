from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from home.models import App


def home(request):

    context = {
        'apps': App.objects.all().order_by('app_id')
    }

    return render(
        request=request,
        template_name='home/home.html',
        context=context
    )
