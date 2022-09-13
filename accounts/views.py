from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect

# Create your views here.

#
# from accounts.forms import 21UserForm
#
# def signup(request):
#     if request.method == "POST":
#         form = UserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             email = form.cleaned_data.get('eamil')
#             login(request, email)
#             return redirect('/mainapp/mainapp')
#     else:
#         form = UserForm()
#     return render(request, 'accounts/register.html', {'form': form})

