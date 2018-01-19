# from splash_screen.models import keys
import requests


def send_notification(fcm, message):
    print ("\n****************** SEND NOTIFICATIONS ***************")
    print (message)
    json = {
        "to": str(fcm),
        "data": {
            "message": str(message),
        }
    }
    print(json)
    url = "https://fcm.googleapis.com/fcm/send"
    print ("--------1-----------")
    headers = {
        'Content-Type': 'application/json',
        "Authorization": "key=AAAAYRe_QZI:APA91bFgbhh7wthjyKy3mPHCldAWjKaark5MjVWbDQD3eJKMpPr8dnFrnBUdMZv8VKbOiK21OIEZ-ICffFkXADXBBQUF69bzVHyPO4ExJGA-N8yryqvO4TX4aiIwlHzbhITi0s3Yf_ge"
    }
    print ("--------2-----------")
    r = requests.post(url, headers=headers, json=json)
    for o in r:
        print("Notification : " + str(o))
    print ("\n*************** SEND NOTIFICATIONS CLOSE *************")