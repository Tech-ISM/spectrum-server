import jwt
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from event.models import EventData, UserEventData
from register.models import UserData


@csrf_exempt
def get_events_list(request):
    response_json = {}
    if request.method == "GET":
        try:
            for x, y in request.GET.items():
                print(x, ":", y)
            # category_id= str(request.POST.get("category_id"))
            day = int(request.GET.get("day"))
            response_json["success"] = True
            response_json["message"] = " Event list Received "
            response_json["event_list"] = []
            for o in EventData.objects.filter(day=int(day), round=1):
                temp_json = {"event_id": int(o.id), "name": str(o.name),
                             "image_url": request.scheme + '://' + request.get_host() + '/media/' + str(o.image_landscape),
                             }
                response_json["event_list"].append(temp_json)
        except Exception as e:
            print("e@offer", e)
            response_json["success"] = False
            response_json["message"] = " offer_data not found"
    else:
        response_json['success'] = False
        response_json['message'] = "not get method"
    return JsonResponse(response_json)


@csrf_exempt
def get_events_details(request):
    response_json = {}
    if request.method == "GET":
        try:
            for x, y in request.GET.items():
                print(x, ":", y)
            event_id = int(request.GET.get("event_id"))
            event_instance = EventData.objects.get(id=event_id)
            response_json["name"] = event_instance.name
            response_json["image"] = request.scheme + '://' + request.get_host() + '/media/' + str(event_instance.image)
            response_json["image_blur"] = request.scheme + '://' + request.get_host() + '/media/' + str(event_instance.image_blur)
            response_json["time"] = event_instance.time
            response_json["date"] = event_instance.date
            response_json["type"] = event_instance.type
            response_json["location"] = event_instance.location
            response_json["day"] = event_instance.day
            response_json["attendees"] = event_instance.attendees
            response_json["description"] = event_instance.description
            response_json["prize_description"] = event_instance.prize_description
            response_json["message"] = "Event Details Received"
            response_json["success"] = True
        except Exception as e:
            print("e@offer", e)
            response_json["success"] = False
            response_json["message"] = " offer_data not found"
    else:
        response_json['success'] = False
        response_json['message'] = "not get method"
    return JsonResponse(response_json)


@csrf_exempt
def get_user_events_list(request):
    response_json = {}
    if request.method == "GET":
        try:
            for x, y in request.GET.items():
                print(x, ":", y)
            access_token = str(request.GET.get("access_token"))
            decoded = jwt.decode(access_token, '810810', algorithms=['HS256'])
            mobile = decoded['mobile']
            print (mobile)
            response_json["success"] = True
            response_json["message"] = " event_list recieved "
            response_json["event_list"] = []
            try:
                user_instance = UserData.objects.get(mobile=mobile)
                for o in UserEventData.objects.filter(user=user_instance):
                    temp_json = {"id": int(o.event.id), "type": int(o.event.type),
                                 "name": str(o.event.name), "participated": int(o.participated),
                                 }
                    response_json["event_list"].append(temp_json)
            except Exception as e:
                response_json["success"] = False
                response_json["message"] = "Something went wrong" + str(e)
        except Exception as e:
            print("e@usereventlist", e)
            response_json["success"] = False
            response_json["message"] = " user data not found"+str(e)
    else:
        response_json['success'] = False
        response_json['message'] = "not get method"
    print (response_json)
    return JsonResponse(response_json)


@csrf_exempt
def change_event_participated_status(request):
    response_json = {}
    if request.method == "POST":
        try:
            access_token = str(request.POST.get("access_token"))
            print('1')
            decoded = jwt.decode(access_token, '810810', algorithms=['HS256'])
            print('2')
            mobile = decoded['mobile']
            try:
                user_instance = UserData.objects.get(mobile=mobile)
                print(user_instance)
            except Exception as e:
                response_json["success"] = False
                response_json["message"] = "Something went wrong"+str(e)
            try:
                event_id = request.POST.get('event_id')
                event_instance = EventData.objects.get(id=event_id)
                user_event_instance = UserEventData.objects.get(event=event_instance, user=user_instance)
                flag_participated = request.POST.get('participated')
                print (flag_participated)
                try:
                    if user_event_instance.participated == 0:
                        user_event_instance.participated = 1
                        user_event_instance.save()
                        event_instance.save()
                        response_json["message"] = "You have Successfully Registered for this event"
                        response_json["success"] = True
                    else:
                        user_event_instance.participated = 0
                        user_event_instance.save()
                        event_instance.save()
                        response_json["message"] = "You have unregistered from this event"
                        response_json["success"] = True
                except Exception as e:
                    print(e)
                    response_json["message"] = "Some Error Occurred"+str(e)
                    response_json["success"] = False
            except Exception as e:
                print(e)
                response_json["message"] = "Some Error Occurred" + str(e)
                response_json["success"] = False
        except Exception as e:
            print(e)
            response_json["message"] = "Access token error" + str(e)
            response_json["success"] = False
        print(response_json)
        return JsonResponse(response_json)
