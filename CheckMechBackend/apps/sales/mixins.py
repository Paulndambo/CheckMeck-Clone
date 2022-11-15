from django.contrib.auth.models import User
from datetime import datetime, timedelta
from django.db import transaction
from apps.garages.models import Garage
class GarageOnboardingMixin(object):

    def __init__(self, data):
        self.data = data

    def run(self):
        pass

    def __onboard_garage(self):
        pass

    def __create_garage_user(self):
        """
        This method creates the user for this garage
        """
        user_obj = self.data['owner']
        

    def __create_garage(self):
        pass

