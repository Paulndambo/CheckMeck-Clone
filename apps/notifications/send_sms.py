DEFAULT_NOTIFICATIONS_URL = "http://51.15.233.87:15432/message/queue"
SMS_SOURCE_ADDRESS = "SMSAfrica"
import requests


def send_sms(destinationAddress, content):
    data = {
        "destinationAddress": destinationAddress,
        "sourceAddress": "SMSAfrica",
        "message": content,
        "messageType": "SMS"
        }
    resp = requests.post(DEFAULT_NOTIFICATIONS_URL, json=data)
    data = resp.json()
    print(data)


def send_email(destinationAddress, content):
    data = {
        "destinationAddress": destinationAddress,
        "sourceAddress": "alerts@meliora.tech",
        "message": content,
        "messageType": "EMAIL"
    }
    resp = requests.post(DEFAULT_NOTIFICATIONS_URL, json=data)
    #data = resp.json()
    print(resp.text)


def send_notification(destinationAddress, content, notificationType):
    if notificationType.lower() == 'SMS'.lower():
        send_sms(destinationAddress, content)
    elif notificationType.lower() == 'EMAIL'.lower():
        send_email(destinationAddress, content)

def request_service(garage_name, garage_phone_number, driver_name, driver_phone_number):
    message = f"""
        Hello {garage_name},\n Am requesting for your service, My car had broken down. Call me ASAP please if you are available. \nCall me on {driver_phone_number}. \n\nFrom CheckMech Services
        """
    data = {
        "destinationAddress": garage_phone_number,
        "sourceAddress": "SMSAfrica",
        "message": message,
        "messageType": "SMS"
        
    }
    resp = requests.post(DEFAULT_NOTIFICATIONS_URL, json=data)
    data = resp.json()
    print(data)
