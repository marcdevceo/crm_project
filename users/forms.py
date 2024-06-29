from django import forms
from .models import Member

DEPARTMENT = [
    ("EXECUTIVE", "Executive"),
    ("Staffing", "HR"),
    ("PAYROLL", "Payroll"),
    ("ADMIN", "Admin"),
    ("SALES", "Sales"),
    ("SUPPORT", "Support"),
    ("MANAGER", "Manager"),
]

class SignUpForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'text-black w-full'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'text-black w-full'}))
    department = forms.ChoiceField(choices=DEPARTMENT, required=True, widget=forms.Select(attrs={'class': 'text-black w-full'}))

    class Meta:
        model = Member
        fields = ['first_name', 'last_name', 'email', 'department', 'password1', 'password2']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'text-black w-full'}),
            'last_name': forms.TextInput(attrs={'class': 'text-black w-full'}),
            'email': forms.EmailInput(attrs={'class': 'text-black w-full'}),
        }
       