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
    # psw = User.objects.make_random_password(length=8, allowed_chars="abcdefghjkmnpqrstuvwxyz01234567889!@#$%^&*")
    # password1 = psw # Standard django password input
    # password2 = psw # Standard django password confirmation input
    # def __init__(self, *args, **kwargs):
    #      super(UserCreationForm, self).__init__(*args, **kwargs)
    
    #      self.fields['password1'].widget.attrs['autocomplete'] = 'off'
    #      self.fields['password2'].widget.attrs['autocomplete'] = 'off'
    #      del self.fields['password1']
    #      del self.fields['password2']

    class Meta:
        model =User
        fields =('username',
                 'email',
                 'first_name',
                 'last_name',
                 'password1',
                 'password2',
                 )

class UserUpdateForm(forms.ModelForm):
    
    class Meta:
        model =User
        fields =('email',
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
