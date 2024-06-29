from django import forms
from .models import Member
from .validators import validate_password

DEPARTMENT = [
    ("EXECUTIVE", "Executive"),
    ("STAFFING", "Staffing"),
    ("PAYROLL", "Payroll"),
    ("ADMIN", "Admin"),
    ("SALES", "Sales"),
    ("SUPPORT", "Support"),
    ("MANAGER", "Manager"),
]

class SignUpForm(forms.ModelForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'text-black w-full'}), 
        validators=[validate_password],
        help_text=(
            "At Least 8 Characters, "
            "1 Uppercase Letter, 1 Lowercase Letter, "
            "1 Number, and 1 Special Character. "
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'text-black w-full'}), 
        validators=[validate_password])
    department = forms.ChoiceField(
        choices=DEPARTMENT,
        required=True,
        widget=forms.Select(attrs={'class': 'text-black w-full'})
    )

    class Meta:
        model = Member
        fields = ['first_name', 'last_name', 'email', 'department', 'password1', 'password2']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'text-black w-full'}),
            'last_name': forms.TextInput(attrs={'class': 'text-black w-full'}),
            'email': forms.EmailInput(attrs={'class': 'text-black w-full'}),
        }

   