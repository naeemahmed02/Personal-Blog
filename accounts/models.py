from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils import timezone

# Custom Manager for User
class CustomUserManager(BaseUserManager):
    """Create and return a user with an email and password"""
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The email must be set")
        email = self.normalize_email(email)
        user = self.model(email = email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password = None, **extra_fields):
        """Create and return a superuser with an email and password"""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        return self.create_user(email, password, **extra_fields)

# Custom User Model
class CustomUser(AbstractUser):
    username = None             # Disable the username
    email = models.CharField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_joined = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False) # For admin access

    # Additional fields can be added here

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'  # Specify email as the unique login field
    REQUIRED_FIELDS = ['first_name', 'last_name'] # Fields required for creating a user

    def __str__(self):
        return self.email

    def get_full_name(self):
        return f"{self.first_name}{self.last_name}"

    def get_short_name(self):
        return self.first_name