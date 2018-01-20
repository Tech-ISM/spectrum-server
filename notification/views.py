import jwt
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from notification.models import NotificationData
from notifications import send_notification
from register.models import UserData


def notification_list(request):
    if request.method == 'GET':
        print ("\n\n-----------------Inside notification_list---------")
        response_json = {}
        try:
            access_token = request.GET.get('access_token')
            decoded_json = jwt.decode(str(access_token), '810810', algorithms=['HS256'])
            mobile = str(decoded_json['mobile'])
            print ("moblie = ", str(mobile))
            response_json['notification_list'] = []
            for obj in NotificationData.objects.all().order_by('-id'):
                temp_json = {}
                temp_json['title'] = obj.notification_title
                temp_json['message'] = obj.notification_message
                temp_json['date'] = obj.notification_date
                temp_json['time'] = obj.notification_time
                temp_json['event_id'] = int(obj.notification_event_id)
                response_json['notification_list'].append(temp_json)
            print (response_json)
            response_json['success'] = True
            response_json['message'] = "Successful"
            return JsonResponse(response_json)
        except Exception as e:
            print ("Exception " + str(e))
            response_json['success'] = False
            response_json['message'] = "Company does not exists, Please signup." + str(e)
            return JsonResponse(response_json)


@csrf_exempt
def admin_notification(request):
    if request.method == "GET":
        response_json = {}
        print ("===============Inside admin_notification GET method===============")
        for x, y in request.GET.items():
            print("key,value", x, ":", y)
        title = str(request.GET.get('title'))
        time = str(request.GET.get('time'))
        date = str(request.GET.get('date'))
        message = str(request.GET.get('message'))
        notifications = NotificationData(notification_title=str(title),
                                         notification_date=str(date),
                                         notification_time=str(time),
                                         notification_message=str(message))
        notifications.save()
        print ("Notification row created")
        # for row in UserData.objects.all():
        #     if UserData.objects.filter(fcm=row.fcm).count() > 1:
        #         row.delete()
        fcm_set = set()
        for user in UserData.objects.all():
            try:
                fcm_set.add(user.fcm)
            except Exception as e:
                print ("Exception " + str(e))
        print (fcm_set)
        for item in fcm_set:
            try:
                send_notification(item, notifications.notification_message)
            except Exception as e:
                print("Exception....", e)
        return HttpResponseRedirect('/adminpanel/notification/')
