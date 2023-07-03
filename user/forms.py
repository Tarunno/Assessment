from django import forms
from .models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from app.models import Item


class UserSignin(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput)

    def is_valid(self):
        super(UserSignin, self).is_valid()

        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        try:
            if User.objects.filter(email=email).exists():
                user = User.objects.get(email=email)
                user = authenticate(email=email, password=password)
                if user is not None:
                    if user.is_active:
                        return True
                    else:
                        self._errors["email"] = ["User is not active"]
                        return False
                else:
                    self._errors["email"] = ["Invalid password"]
                    return False
            else:
                password = make_password(password)
                User.objects.create(email=email, password=password)
                return True
        except:
            self._errors["password"] = ["Invalid password"]
            return False

    def save(self, request):
        email = self.cleaned_data.get('email')
        user = User.objects.get(email=email)
        login(request, user)


class AddAuction(forms.ModelForm):
    class Meta:
        model = Item 
        fields = '__all__'
