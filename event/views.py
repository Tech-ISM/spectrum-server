from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from event.models import EventData


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
            response_json["message"] = " event_list recieved "
            response_json["event_list"] = []
            for o in EventData.objects.filter(day=int(day)):
                temp_json = {"event_id": int(o.id), "name": str(o.name),
                             "image_url": request.scheme + '://' + request.get_host() + '/media/' + str(o.image),
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
