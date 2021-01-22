from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
# building here new custom model

class MyAccountManager(BaseUserManager):
    # put here all the required fields as per done below
    # this is create user method
    def create_user(self, email, username, password = None):
        if not email: 
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("User must have an username")
        
        # if everything is satisfied then create a model for the user
        user = self.model(
            email = self.normalize_email(email), # normalize will simply convert it to lowercase and it is available inside the base user
            username = username,
        )
        
        # now setting the password
        user.set_password(password)
        user.save(using = self._db)
        
        return user 
    
    # now creating a superUser
    def create_superuser(self, email, username, password):
        user = self.create_user(
            email = self.normalize_email(email), # normalize will simply convert it to lowercase and it is available inside the base user
            password = password,
            username = username,
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True

        user.save(using = self.db)
        return user



class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name = "Email", max_length = 60, unique = True)
    username = models.CharField(max_length = 30, unique = True)
    date_joined = models.DateTimeField(verbose_name = "date_joined", auto_now_add = True)
    last_login = models.DateTimeField(verbose_name = "last_login", auto_now = True)
    is_admin = models.BooleanField(default = False)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)
    is_superuser = models.BooleanField(default = False)

    # this are some mapping for the datafields
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username',]

    # telling user where is account manager
    objects = MyAccountManager()

    # implementing the two string method----please check the documentation for the reference once
    def __str__(self):
        return self.email + "," + self.username

    # below functions are required when we want to build a custom user model
    def has_perm(self, perm, obj = None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

# http://127.0.0.1:8000/admin/login/?next=/admin/
# above is default url for admin path registrations
'''
after creating search and filtering methods, getting admin or staff options is becoming ambigious
need to change and updated as soon as possible
'''

