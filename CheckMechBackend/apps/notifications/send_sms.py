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