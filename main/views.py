from django.contrib import messages
from django.shortcuts import redirect, render
from . forms import ClientForm
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def home(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect('home')
    else:
        form = ClientForm()

    return render(request, 'home.html', {'form': form})
