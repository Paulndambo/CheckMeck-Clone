from django.contrib.auth.models import User
from datetime import datetime, timedelta
from django.db import transaction
from apps.garages.models import Garage, GarageOwner, GarageSubscription, Service
class GarageOnboardingMixin(object):

    def __init__(self, data):
        self.data = data

    def run(self):
        self.__onboard_garage()

    @atomic
    def __onboard_garage(self):
        try:
            self.__create_garage_user()
            self.__create_garage_owner()
            self.__create_garage()
            self.__create_garage_services()
            self.__create_garage_subscription()
        except Exception as e:
            raise e


    def __create_garage_user(self):
        """
        This method creates the user for this garage
        """
        user_obj = self.data['user_obj']
        user = User()
        user.first_name = user_obj["first_name"]
        user.last_name = user_obj["last_name"]
        user.username = user_obj["first_name"].lower()
        user.email = user_obj["email"]
        user.set_password('1234')
        user.save()
        print("##########New User Created##########")
        

    def __create_garage_owner(self):
        user_email = self.data["user_obj"]["email"]
        garage_owner_obj = self.data["garage_owner_obj"]
        user = User.objects.get(email=user_email)
        print(f"Current User: {user.username}")
        garage_owner = GarageOwner.objects.create(user=user, **garage_owner_obj)
        garage_owner.save()
        print("################Garage Owner Created###########")


    def __create_garage(self):
        user_email = self.data["user_obj"]["email"]
        garage_obj = self.data['garage_obj']
        owner = GarageOwner.objects.get(user__email=user_email)
        garage = Garage.objects.create(owner=owner, **garage_obj)
        garage.save()
        print("##########Garage Created###############")


    def __create_garage_services(self):
        print("########No Services Addition Yet######")

    def __create_garage_subscription(self):
        user_email = self.data["user_obj"]["email"]
        garage = Garage.objects.get(owner__user__email=user_email)
        subscription_obj = self.data['subscription_obj']
        subscription = GarageSubscription.objects.create(garage=garage, **subscription_obj)

