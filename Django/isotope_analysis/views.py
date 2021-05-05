from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def isotope_analysis_view(request):
    return render(
        request=request,
        template_name='isotope_analysis/isotope_analysis.html',
        context={}
    )
