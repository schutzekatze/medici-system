from django.contrib.auth.models import User

import logging
import datetime
from decimal import Decimal

from ...models import MediciUser

logger = logging.getLogger(__name__)

def process_receipt_data(mediciuser, data):
    logger.info("Processing data.")

    mediciuser.balance -= Decimal(data['total'])
    mediciuser.save()

def user_create(user_data):
    logger.info("Creating user <" + user_data['username'] + ">.")

    user = User.objects.create_user(
                            username=user_data['username'],
                            password=user_data['password'],
                            email=user_data['email'],
                            )

    if 'balance' in user_data:
        user.mediciuser.balance = user_data['balance']
        user.mediciuser.save()

def user_update(mediciuser, user_data):
    logger.info("Updating user <" + mediciuser.user.username + ">.")

    if 'username' in user_data:
        mediciuser.user.username = user_data['username']
    if 'password' in user_data:
        mediciuser.user.set_password(user_data['password'])
    if 'email' in user_data:
        mediciuser.user.email = user_data['email']
    if 'balance' in user_data:
        mediciuser.balance = Decimal(user_data['balance'])
    mediciuser.last_updated = datetime.datetime.now()

    mediciuser.user.save()

def user_fetch(mediciuser, user_fields):
    logger.info("Fetching user <" + medici.user.username + ">.")

    data = {}

    if 'username' in user_fields:
        data['username'] = mediciuser.user.username
    if 'email' in user_fields:
        data['email'] = mediciuser.user.email
    if 'balance' in user_fields:
        data['balance'] = mediciuser.balance
    if 'last_updated' in user_fields:
        data['last_updated'] = mediciuser.last_updated

    return data
