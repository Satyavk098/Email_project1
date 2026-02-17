from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import RegistrationForm

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Send Welcome Email
            send_mail(
                subject='Welcome to Our Platform',
                message='Hello, your registration is successful.',
                from_email=None,  # uses EMAIL_HOST_USER
                recipient_list=[user.email],
                fail_silently=False,
            )

            return redirect('success')
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})


def success(request):
    return render(request, 'success.html')
