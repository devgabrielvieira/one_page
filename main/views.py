from django.shortcuts import redirect, render
from . forms import ClientForm


def home(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ClientForm()

    return render(request, 'home.html', {'form': form})
