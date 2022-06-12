from photo.models import User  # 새로운 필드 추가한 User 사용
from django import forms

class RegisterForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'gender', 'birthdate']

        # clean_필드명(): 필드의 validation 방법 지정
        def clean_password2(self):
            cd = self.cleaned_data  # cleaned_data: 유효성 검사를 마친 후의 데이터
            if cd['password'] != cd['password2']:
                raise forms.ValidationError
            return cd['password2']  # 해당 필드의 데이터를 return하도록 구현
