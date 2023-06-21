from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
# def index(req):
#     return render(req, 'Base.html')

class Login(View):
    def get(self, request):
        return render(request, 'Login_Register/Login.html')
    def post(self, request):
        if request.method == "POST":
            username = request.POST.get('User_Name')
            Password = request.POST.get('Password')
            user = authenticate(username=username, password=Password)
            if user is not None:
                # Kiểm tra điều kiện hợp lệ ==> Đăng nhập thành công
                login(request, user)
                return redirect('/Login_Success')
            else:
                try:
                    # Kiểm tra điều kiện tên người dùng nhập vào có tồn tại hay không
                    User.objects.get(username=username)
                    # Nếu người dùng có tồn tại, nhưng mật khẩu sai ==> Reload lại trang web để người dùng đăng nhập lại
                    messages.error(request, "Sai thông tin đăng nhập!!!!")
                    return redirect('/')
                except User.DoesNotExist:
                    return redirect('/Register')


class Register(View):
    def get(self, request):
        messages.warning(request, "Không tìm thấy thông tin người dùng")
        return render(request, 'Login_Register/Register.html')
    def post(self, request):
        if request.method == "POST":
            email = request.POST.get('Email_Address')
            username = request.POST.get('User_Name')
            Password = request.POST.get('Password')
            Confirm_Password = request.POST.get('Confirm_Password')
            print(email)
            print(username)
            print(Password)
            print(Confirm_Password)
            # =============================== catch errors when registering ===============================
            if User.objects.filter(username=username):
                # messages.error(request, "Username already exist! Please try some other username")
                print("Người này đã tồn tại trước đó!")
                print("Không lưu")
                messages.warning(request, "Username đã tồn tại. Hãy sử dụng Username khác")
                return render(request, 'Login_Register/Register.html')
            
            if User.objects.filter(email=email).exists():
                # messages.error(request, "Email already Register")
                print("Email đã được đăng ký")
                print("Không lưu")
                messages.warning(request, "Email đã được đăng ký trước đó.")
                return render(request, 'Login_Register/Register.html')
            
            if Password!=Confirm_Password:
                # messages.error(request, "Password didn't match!")
                print("Mật khẩu không khớp")
                print('Chưa lưu')
                messages.warning(request, "Mật khẩu không khớp!")
                return render(request, 'Login_Register/Register.html')

            MyUser = User.objects.create_user(username, email, Password)
            MyUser.save()
            print('Email: ' + email)
            print('User Name: ' + username)
            print('Password: ' + Password)
            print('Config Password: ' + Confirm_Password)
        return redirect('/')

def Logout(request):
    logout(request)
    return render(request, 'Login_Register/Logout.html')


class Affter_Login(View):
    def get(self, request):
        # return HttpResponse("Đã đăng nhập thành công")
        logout(request)
        return render(request, 'Login_Register/Logout.html')