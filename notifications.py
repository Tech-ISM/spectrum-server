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
        "Authorization": "key=AAAAF0W9-0E:APA91bG-NxJFum5-F-uktwnBXMG5EKW_mcU5M5MrDHg3U-0ZICk6R4rgLGixQU4IJC867u518gKlrrr64h-GAVDfuh1PG2kVTnm9ZKwzp5UGT5Rndl1megRaJFCzk95N8clYa2sodWCH787_NvW61u85qGX0B1dTMg"
    }
    print ("--------2-----------")
    r = requests.post(url, headers=headers, json=json)
    for o in r:
        print("Notification : " + str(o))
    print ("\n*************** SEND NOTIFICATIONS CLOSE *************")