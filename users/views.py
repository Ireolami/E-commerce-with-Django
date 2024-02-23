from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import *
from django.contrib.auth.decorators import login_required
# Create your views here.
def create_user(request):
    if request.method == 'POST':
        form =UserRegistrationForm(request.POST)
        

        if form.is_valid():
            form.save()
            
            messages.success(request, "Account created successfully")

            return redirect('login')
    else:
        form =UserRegistrationForm()
      
    
    context = {'form': form}

    return render(request, 'users/signup.html', context)

# @login_required
# def profile(request):
#     if request.method == 'POST':
#         u_form = UserUpdateForm(request.POST, instance=request.user)
#         p_form = ProfileUpdateForm(request.POST,
#         request.FILES,
#         instance=request.user.profile)
#         if u_form.is_valid() and p_form.is_valid():
#             u_form.save()
#             p_form.save()
#             messages.success(request, "Profile updated successfully")
#             return redirect('profile')
#     else:
#         u_form = UserUpdateForm(instance=request.user)
#         p_form = ProfileUpdateForm(instance=request.user.profile)
#     update_dict={'u_form': u_form, 'p_form': p_form}
#     return render(request, 'users/profile.html', context=update_dict)
@login_required
def profile(request):
   return render(request, 'users/profile.html')

def update_profile(request):
    if request.method == 'POST':
        u_form =UserUpdateForm(request.POST, instance=request.user)
        p_form =ProfileUpdateForm(request.POST, request.FILES, instance = request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            profile, created = Profile.objects.get_or_create(user=request.user)
            p_form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
            
            p_form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect('profile')
        context ={"u_form": u_form, 'p_form': p_form}
    else:
        u_form=UserUpdateForm(instance=request.user)
     
        profile, created = Profile.objects.get_or_create(user=request.user)
        p_form = ProfileUpdateForm(instance=profile)
    
    context ={"u_form": u_form, 'p_form': p_form}
    return render(request, 'users/profile_update.html', context)

# def update_profile(request):
#     if request.method == 'POST':
#         u_form =UserUpdateForm(request.POST, instance=request.user)
#         p_form =ProfileUpdateForm(request.POST, request.FILES, instance = request.user.profile)
#         if u_form.is_valid() and p_form.is_valid():
#             # u_form.save()
#             # if not hasattr(request.user, 'profile'):
#             #     profile = p_form.save(commit=False)
#             #     profile.user = request.user
#             #     profile.save()
#             # else:
#             #     p_form.save()
#             profile, created = Profile.objects.get_or_create(user=request.user)
#             p_form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
            
#             p_form.save()
#             messages.success(request, 'Profile updated successfully')
#             redirect('profile')
#         context ={"u_form": u_form, 'p_form': p_form}
#     else:
#         u_form=UserUpdateForm(instance=request.user)
#         # if not hasattr(request.user, 'profile'):
#         #     p_form = ProfileUpdateForm()
#         # else:
#         #     p_form = ProfileUpdateForm(instance=request.user.profile)
#         profile, created = Profile.objects.get_or_create(user=request.user)
#         p_form = ProfileUpdateForm(instance=profile)
    
#     context ={"u_form": u_form, 'p_form': p_form}
#     return render(request, 'users/profile_update.html', context)