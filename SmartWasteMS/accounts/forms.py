from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from accounts.models import UserProfile


class EmailValidation(forms.EmailField):
    def validate(self, value):
        try:
            User.objects.get(email=value)
            raise forms.ValidationError("Email already Exists")
        except User.DoesNotExist as e:
            pass

        except Exception as e:
            raise forms.ValidationError("Email already Exists")


# messages


class SignUpForm(UserCreationForm):
    email = EmailValidation(required=True)
    
    class Meta:
        model =User
        fields =('username',
                 'email',
                 'first_name',
                 'last_name')

class UserUpdateForm(forms.ModelForm):
    
    class Meta:
        model =User
        fields =('username',
                 'first_name',
                 'last_name')

class CreateUserProfile(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
                "image",
                "phone_no",
                "age",
                "gender",
                "address",
                "van_no"]
