import os
import django


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'biblioteca_books.settings')


django.setup()


from back_login.models import User 
from django.contrib.auth.models import User


users = User.objects.all()

for user in users:
    user.set_password(user.password_user) 
    user.save()  
