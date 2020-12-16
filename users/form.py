from django import forms
from django.contrib.auth.models import User

import re
from django.contrib.auth.hashers import check_password, make_password

class LoginForm(forms.Form):
    username = forms.CharField(
        error_messages={'required': '이메일를 입력해주세요'},
        max_length=64,
        label='아이디',
        widget=forms.TextInput(attrs={'placeholder': '이메일를 입력해주세요', 'data-width': '100%'})
    )
    password = forms.CharField(
        error_messages={'required': "비밀번호를 입력해주세요"},
        widget=forms.PasswordInput(attrs={'placeholder': '비밀번호를 입력해주세요', 'data-width': '100%'}),
        label="비밀번호",
    )

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                self.add_error('user_id', '아이디가 없습니다.')
                return

            if not check_password(password, user.password):
                self.add_error('password', '비밀번호를 틀렸습니다.')