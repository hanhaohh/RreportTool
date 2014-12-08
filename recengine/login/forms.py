__author__ = 'haohan'
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(forms.Form):

    username = forms.CharField(max_length = 30,required=True)
    password = forms.CharField(widget=forms.PasswordInput)
    # email = forms.EmailField(required=False)
    def __unicode__(self):
        return self.username
class CustomCreateUserForm(UserCreationForm):

    username = forms.RegexField(
    label=("Username"), max_length=30, regex=r"^[\w.@+-]+$",
    help_text=("Required. 30 characters or fewer. Letters, digits and "
                "@/./+/-/_ only."),
    error_messages={
        'invalid': ("This value may contain only letters, numbers and "
                     "@/./+/-/_ characters.")},
    widget=forms.TextInput(attrs={'class': 'form-control',
                            'required': 'true',
                            'placeholder': 'Login'
    })
    )
    first_name = forms.CharField(
    label=("Name"),
    widget=forms.TextInput(attrs={'class': 'form-control',
                                  'type': 'text',
                                  'required': 'true',
    }),
    help_text=("Enter user first and last name.")
    )

    password1 = forms.CharField(
    label=("Password"),
    widget=forms.PasswordInput(attrs={'class': 'form-control',
                                      'required': 'true',

    })
    )
    password2 = forms.CharField(
    label=("Password confirmation"),
    widget=forms.PasswordInput(attrs={'class': 'form-control',
                                      'type': 'password',
                                      'required': 'true',
    }),
    help_text=("Enter the same password as above, for verification.")
    )



    email = forms.CharField(
    label=("Email"),
    widget=forms.TextInput(attrs={'class': 'form-control',
                                  'type': 'email',
                                  'placeholder': 'Email address',
                                  'required': 'true'
    })
    )

