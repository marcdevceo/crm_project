from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin, Group, Permission
from django.contrib.auth.hashers import make_password, check_password
from django.utils import timezone

class CustomUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('You have not provided a valid email address')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, **extra_fields)

class Member(AbstractBaseUser, PermissionsMixin):
    DEPARTMENT = [
        ("EXECUTIVE", "Executive"),
        ("STAFFING", "HR"),
        ("PAYROLL", "Payroll"),
        ("ADMIN", "Admin"),
        ("SALES", "Sales"),
        ("SUPPORT", "Support"),
        ("MANAGER", "Manager"),
    ]
    member_id = models.AutoField(primary_key=True)
    password = models.CharField(max_length=128)

    first_name = models.CharField(max_length=50, blank=True, default='')
    last_name = models.CharField(max_length=50, blank=True, default='')
    email = models.EmailField(blank=True, default='', unique=True)
    department = models.CharField(max_length=50, choices=DEPARTMENT, blank=True, default='')
    date_joined = models.DateTimeField(default=timezone.now)
    last_updated = models.DateTimeField(default=timezone.now)

    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    last_login = models.DateTimeField(blank=True, null=True)

    groups = models.ManyToManyField(
        Group,
        related_name='member_groups', 
        blank=True,
        help_text='The groups this user belongs to.',
        related_query_name='member',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='member_permissions',  
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='member',
    )

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_short_name(self):
        return self.first_name

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def update(self, **kwargs):
        for field, value in kwargs.items():
            if hasattr(self, field):
                setattr(self, field, value)
        self.last_updated = timezone.now()
        self.save()

