from django.shortcuts import render,get_object_or_404, redirect
from . import views
from .models import Profiles
from .forms import ProfileForm
# Create your views here.

def admin_console(request):
    profiles = Profiles.objects.all()
    return render(request, 'profiles/profiles_page.html', {'profiles': profiles})

def details(request, pk):
    pk = int(pk)
    item = get_object_or_404(Profiles, pk=pk)
    form = ProfileForm(data=request.POST or None, instance=item)
    if request.method =='POST':
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.save()
            return redirect('admin_console')
        else:
            print(form.errors)
    else:
        return render(request, 'profiles/present_profiles.html', {'form': form})
