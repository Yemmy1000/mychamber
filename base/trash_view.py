from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout,update_session_auth_hash
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import PasswordChangeForm
from django_datatables_view.base_datatable_view import BaseDatatableView
from .models import CustomUser, CustomUserProfile
from .forms import CustomUserCreationForm, UserForm, UserProfileForm, CustomUserForm
from django.contrib.auth.models import Group, User
from django.http import HttpResponse, JsonResponse


# User = get_user_model()

# Create your views here.
@login_required(login_url='login')
def home(request):
    ip = Get_IP(request)
    context = {'ip': ip}
    return render(request, 'base/home.html', context)



def registerView(request):
    if request.method == 'POST':
        if request.POST.get('username') and request.POST.get('password') and (request.POST.get('password') == request.POST.get('repeatpassword')):
            user = User()
            user.username = request.POST.get('username').lower()
            user.password = request.POST.get('password')
            user.save()
            login(request, user)
            return redirect('home') 
        else:
            messages.error(request, 'Error occured during registartion!')   
    return render(request, 'base/user-register.html')


def loginView(request):
    if request.user.is_authenticated:
        # if not checkProfileNames(request.user.id):
        #     return redirect('create-profile')
        if not checkUserInfo(request.user.id):
            return redirect('update-user')

        return redirect('home')

    if request.method == 'POST':
        email = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = CustomUser.objects.get(email=email)
        except:
            messages.error(request, 'User does not exist!')
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            if not checkUserInfo(request.user.id):
                return redirect('update-user')
            else:
                return redirect('home')
        else:
             messages.error(request, 'Username or Password does not exist!')
    context = {}
    return render(request, 'base/login.html', context)


def checkUserInfo(user_id):
    try:
        user = CustomUser.objects.get(user=user_id).values('first_name')
    except:
        return False
    # if user.first_name is None or user.last_name is None:
    else:
        return True


def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def User(request):
    # if request.user.is_authenticated:
    groups = Group.objects.all()
    context = {'groups': groups}
    return render(request, 'base/user_list.html', context) 

@login_required(login_url='login')
def CreateUserProfile(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        user = CustomUser.objects.get(id=id)
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        CustomUserProfile.objects.create(
            user = user,
            first_name = first_name,
            last_name = last_name, 
            )  
        # if form.is_valid():
        #     print(request.POST)
        #     form.save()
        return redirect('change-password')
    else:
        messages.error(request, 'Form error or element not valid!')

    # user = CustomUser.objects.get(id=pk)
    # print(user)
    # context = {'form': form}
    return render(request, 'base/create-profile.html') 


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


@login_required(login_url='login')
def UserProfile(request, pk):
    user = CustomUser.objects.get(id=pk)
    profile = CustomUserProfile.objects.get(user=user)
    # print(user)
    context = {
        'user':user,
        'profile': profile,
        }
    return render(request, 'base/user-profile.html', context) 

def UpdateProfile(request, pk):   
    user = CustomUser.objects.get(id=pk) 
    profile = CustomUserProfile.objects.get(user=user)
    form = UserProfileForm(instance=profile)
    # avatar = CustomUserProfile.objects.filter(user=user).values('avatar')
    pix = getattr(profile, 'avatar')
    # print(pix)
    if request.method == 'POST':
        profile = CustomUserProfile.objects.get(user=user)
        # print(user)
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()    
            return JsonResponse({'success': True})
        
            # messages.success(request, 'Profile updated successfully!')
        else:
            # messages.error(request, 'Profile updated failed!')
            return JsonResponse({'success': False}, status=400)

    context = {
        'form': form,
        'pix': pix,
        }
    return render(request, 'base/update-profile.html', context) 

# @login_required(login_url='login')
def UpdateUser(request):
    user_id = request.user.id
    # form = UserProfileForm(instance=user)  
    # print(user)  
    user = CustomUser.objects.get(id=user_id)
    if request.method == 'POST':
        form = CustomUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            CustomUserProfile.objects.create(user = user)
            # if request.POST.get('password') == 'password':
            # return redirect('change-password')
            # else:
            return redirect('update-user-info', pk=user_id)
        else:
            messages.error(request, 'Form error or element not valid!')
    return render(request, 'base/update-user.html')


# @login_required(login_url='login')
def UpdateUserInfo(request, pk):
    user = CustomUser.objects.get(id=pk)
    form = CustomUserForm(instance=user) 
    context={'form': form}

    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('change-password')
        else:
            messages.error(request, 'Form error or element not valid!')
    return render(request, 'base/update-user-info.html', context)


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
class UserListJson(BaseDatatableView):
    # The model we're going to show
    model = CustomUser

    # define the columns that will be returned
    columns = [ 'email', 'user_type', 'date_joined', 'last_login', 'action']  

    # define column names that will be used in sorting
    # order is important and should be same as order of columns
    # displayed by datatables. For non-sortable columns use empty
    # value like ''
    order_columns = [ 'email', 'user_type', 'date_joined', 'last_login', '' ]

    # set max limit of records returned, this is used to protect our site if someone tries to attack our site
    # and make it return huge amount of data
    max_display_length = 500


    # def filter_queryset(self, qs):
    #     sSearch = self.request.GET.get('sSearch', None)
    #     if sSearch:
    #         qs = qs.filter(Q(firstName__istartswith=sSearch) | Q(familyName__istartswith=sSearch))
    #     return qs

# class Get_IP():

def Get_IP(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')       

    return ip