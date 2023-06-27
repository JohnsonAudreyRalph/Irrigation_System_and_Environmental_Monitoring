from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

import requests

# Create your views here.
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
            if User.objects.filter(username=username):
                print("Người này đã tồn tại trước đó!")
                print("Không lưu")
                messages.warning(request, "Username đã tồn tại. Hãy sử dụng Username khác")
                return render(request, 'Login_Register/Register.html')
            
            if User.objects.filter(email=email).exists():
                print("Email đã được đăng ký")
                print("Không lưu")
                messages.warning(request, "Email đã được đăng ký trước đó.")
                return render(request, 'Login_Register/Register.html')
            
            if Password!=Confirm_Password:
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
    return redirect('/')

def Accounts_settings(request):
    return render(request, 'Accounts_settings.html')

class Affter_Login(View):
    def get(self, request):
        url = "http://solar-ctd.ddns.net/data/line"
        response = requests.get(url)
        data = response.json()

        line1_power = data["data"]["line1"]["power"]
        line1_volt = data["data"]["line1"]['volt']
        line1_perform = data["data"]["line1"]["perform"]
        line1_ampe = data["data"]["line1"]["ampe"]

        line2_power = data["data"]["line2"]["power"]
        line2_volt = data["data"]["line2"]['volt']
        line2_perform = data["data"]["line2"]["perform"]
        line2_ampe = data["data"]["line2"]["ampe"]

        print("Line 1 Power:", line1_power)
        print("Line 1 Volt: ", line1_volt)
        print("Line 1 Perform: ", line1_perform)
        print("Line 1 Ampe: ", line1_ampe)
        print("Line 2 Power:", line2_power)
        print("Line 2 Volt: ", line2_volt)
        print("Line 2 Perform: ", line2_perform)
        print("Line 2 Ampe: ", line2_ampe)
        conx = {
            'line1_power':line1_power,
            'line1_volt':line1_volt,
            'line1_perform':line1_perform,
            'line1_ampe':line1_ampe,
            'line2_power':line2_power,
            'line2_volt':line2_volt,
            'line2_perform':line2_perform,
            'line2_ampe':line2_ampe
        }
        return render(request, 'Login_Success.html', conx)