from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User, auth, Group, User
from django.contrib.auth.forms import PasswordChangeForm
from django_datatables_view.base_datatable_view import BaseDatatableView
from .models import CustomUser, CustomUserProfile
from .forms import CustomUserCreationForm, UserForm, UserProfileForm, CustomUserForm
from django.http import HttpResponse, JsonResponse



@login_required(login_url='login')
def home(request):
    # ip = Get_IP(request)
    # context = {'ip': ip}
    return render(request, 'base/home.html')


def loginView(request):
    if request.user.is_authenticated:
        # if not checkUserInfo(request.user.id):
        if not check_Up_User(request.user.id).checkUserInfo():
            return redirect('update-user')
        if not check_Up_User(request.user.id).checkUserProfile():
            profile = CustomUserProfile.objects.get_or_create(user = request.user)
        return redirect('home')

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        # print(email)
        # print(password)
        try:
            user = CustomUser.objects.get(email=email)
        except:
            messages.error(request, 'User does not exist!')

        user = auth.authenticate(request, email=email, password=password)
        
        if user is not None:
            auth.login(request, user)
            # if not checkUserInfo(request.user.id):
            #     return redirect('update-user')
            if not check_Up_User(request.user.id).checkUserInfo():
                return redirect('update-user')
            if not check_Up_User(request.user.id).checkUserProfile():
                profile = CustomUserProfile.objects.get_or_create(user = user)
                return redirect('home')
            else:
                return redirect('home')
        else:
             messages.error(request, 'Username or Password does not exist!')
    return render(request, 'base/login.html')


def checkUserInfo(user_id):
    try:
        user = CustomUser.objects.get(id=user_id)
    except:
        return False

    if user.first_name is None or  user.first_name == '':
        return False
    else:
        return True

class check_Up_User:
    def __init__(self, user_id):
        self.user_id = user_id

    def checkUserInfo(self):
        try:
            user = CustomUser.objects.get(id=self.user_id)
        except:
            return False

        if user.first_name is None or  user.first_name == '':
            return False
        else:
            return True

    def checkUserProfile(self):
        try:
            userProfile = CustomUserProfile.objects.get(user=self.user_id)
        except:
            return False
        return True


# @login_required(login_url='login')
def UpdateUser(request):
    user_id = request.user.id
    user_mail = request.user.email
    user = CustomUser.objects.get(id=user_id)
    if request.method == 'POST':
        # form = CustomUserForm(request.POST, instance=user)
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.username = user_mail.split('@')[0]
        user.save()
        profile = CustomUserProfile.objects.get_or_create(user = user)
        # return redirect('update-user-info', pk=user_id)
        return redirect('home')            
    else:
        messages.error(request, 'Form error or element not valid!')
    return render(request, 'base/update-user.html')


# @login_required(login_url='login')
# def UserProfile(request, pk):
#     user = CustomUser.objects.get(id=pk)
#     profile = CustomUserProfile.objects.get(user=user)
#     context = {
#         'user':user,
#         'profile': profile,
#         }
#     return render(request, 'base/user-profile.html', context) 


@login_required(login_url='login')
def User(request):
    # if request.user.is_authenticated:
    groups = Group.objects.all()
    context = {'groups': groups}
    return render(request, 'base/user_list.html', context) 

def logoutUser(request):
    auth.logout(request)
    return redirect('login')

@login_required(login_url='login')
def UserProfile(request, pk):
    user = CustomUser.objects.get(id=pk)
    try:
        profile = CustomUserProfile.objects.get(user=user)
    except:
        redirect('update-user')
    # print(user)
    context = {
        'user':user,
        'profile': profile,
        }
    return render(request, 'base/user-profile.html', context) 

@login_required(login_url='login')
def UpdateUserInfo(request, pk):
    user = CustomUser.objects.get(id=pk)
    form = CustomUserForm(instance=user)
    if request.method == 'POST':
        # form = CustomUserForm(request.POST, instance=user)
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.dob = request.POST.get('dob')
        user.bio = request.POST.get('bio')
        user.phone = request.POST.get('phone')
        user.avatar = request.FILES.get('avatar')
        user.save()
        return redirect('user-profile', pk=pk)
        # return redirect('home')            
    else:
        messages.error(request, 'Form error or element not valid!')
    return render(request, 'base/update-user-info.html', {'form': form})

def UpdateProfile(request, pk):   
    user = CustomUser.objects.get(id=pk) 
    profile = CustomUserProfile.objects.get(user=user)
    form = UserProfileForm(instance=profile)
    context = {
        'form': form,
        }

    if request.method == 'POST':
        # profile = CustomUserProfile.objects.get(user=user)
        # print(user)
        print("nhdhd")
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()    
            return redirect('user-profile', pk=pk)
        else:
            print(form.errors)
            return render(request, 'base/update-profile.html', context) 
    return render(request, 'base/update-profile.html', context) 


@login_required(login_url='login')
def AddNewUser(request):
    if request.method == 'POST':
        # form = CustomUserCreationForm(request.POST)
        # print(request.POST)
        groups = Group.objects.all()
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        user_type=request.POST['usergroup']
        # if user_type == 'admin':
        if not CustomUser.objects.filter(email=email).exists():
            user = CustomUser.objects.create_user(
                username=username,
                email=email,
                password=password,
                user_type=user_type
            )
            # groups = Group.objects.get('Admin')
            user.groups.add(Group.objects.get(id=user_type))
            my_group = Group.objects.get(id=user_type) 
            my_group.user_set.add(user)
            # user.is_staff = True
            user.save()
            return JsonResponse({'success': True}, safe=False)
        else:
            return JsonResponse({'exist': True}, safe=False)
    context = {'groups': groups}

    return render(request, 'base/user_list.html', context)


# @login_required(login_url='login')
def ChangePassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            # update_session_auth_hash(request, user)  # Important!

            # return JsonResponse({'success': True}, safe=False)
            return render(request, 'base/change_password.html', {'form': form})
            # print(form)
            # return redirect('update-profile', pk=)
        else:
            # return JsonResponse({'success': False}, safe=False)
            return render(request, 'base/change_password.html', {'form': form})
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'base/change_password.html', {'form': form})
