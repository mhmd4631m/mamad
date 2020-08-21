import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','myproject.settings')

import django
django.setup()

from myapp.models import User
from faker import Faker
f=Faker()

def populate(n):
    for x in range(n):
        fake_name = f.name().split()
        fake_firstname = fake_name[0]
        fake_lastname = fake_name[1]
        fake_email = f.email()

        us = User.objects.get_or_create(first_name=fake_firstname , last_name=fake_lastname , email=fake_email)[0]

if __name__=='__main__':
    print('start')
    populate(30)
    print('the end')
