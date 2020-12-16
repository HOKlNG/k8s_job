from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.http import JsonResponse
from django.views.generic.edit import FormView, View
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic.edit import FormView, View
from django.http import JsonResponse, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .form import LoginForm
# Create your views here.


def index(request):
    return render(request, 'index.html')


@method_decorator(csrf_exempt, name='dispatch')
class BaseView(View):
    @staticmethod
    def response(data={}, message='', status=200):
        result = {
            'data': data,
            'message': message,
        }
        return JsonResponse(result, status=status)


class LoginView(FormView):
    # 로그인 페이지 View
    template_name = 'user_login.html'
    form_class = LoginForm
    success_url = reverse_lazy('main')

class UserLoginView(BaseView):
    # login access view

    def post(self, request):

        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        try:
            username = User.objects.get(email=email).username
        except: #없는 이메일인 경우
            return JsonResponse({'message':'이메일 또는 비밀번호를 확인해주세요.'}, status=400)
        # authenticate에 email만넣으면 인증이 안됨 만들때 Username으로 생성
        user = authenticate(request,username=username, email=email, password=password)

        if user is None: #로그인 실패
            last_login = User.objects.get(email=email).last_login
            try:
                return JsonResponse({'message': '비밀번호를 회 잘못 입력하셨습니다.'}, status=400)
            except:
                return JsonResponse({'message': '비밀번호를 잘못 입력하셨습니다.'}, status=400)

        login(request, user)
        return self.response()

class UserLogoutView(BaseView):

    def get(self, request):
        logout(request)
        return redirect('/')