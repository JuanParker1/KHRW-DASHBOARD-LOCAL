from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def aquifer_hydrograph_view(request):
    return render(
        request=request,
        template_name='aquifer_hydrograph/aquifer_hydrograph.html',
        context={}
    )
