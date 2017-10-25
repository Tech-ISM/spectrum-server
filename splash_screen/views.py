from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from customs.models import KeysData


@csrf_exempt
def splash_screen(request):
    print("================== Inside splash screen =====================")
    response_json = {}
    if request.method == 'GET':
        try:
            access_token1 = request.GET.get('access_token')
            fcm = request.GET.get('fcm')
            print(fcm)

            # if access_token == 'dsnbsmndjbmnx23' :
            #     print('b')
            #     p,created = FcmData.objects.get_or_create(fcm=fcm)
            #     print ('aman---------')
            #     if created:
            #         response_json['message'] = "fcm added"
            #     if not created:
            #         response_json['message'] = "fcm already exsists"

            # json = jwt.decode(str(access_token), keys.KEY_ACCESS_TOKEN_ENCRYPTION, algorithms=['HS256'])
            # mobile = str(json['mobile'])
            # company = CompanyData.objects.get(mobile= mobile)
            # fcm_instance= FcmData.objects.get(company=company)
            # fcm_instance.fcm=fcm
            # fcm_instance.save()
            # response_json['message'] = 'fcm linked to user'

            print("234")
            version = int(KeysData.objects.get(key='version').value)
            print(version)
            print ('a2')
            compulsory_update = KeysData.objects.get(key='compulsory_update').value
            print ('a5')
            response_json['version'] = version
            print ('a3')
            if int(compulsory_update) == 1:
                response_json['compulsory_update'] = True
                print ('a4')
            if int(compulsory_update) == 0:
                response_json['compulsory_update'] = False
                print ('a5')
            response_json['success'] = True
        except Exception as e:
            print("Exception Error", str(e))
            response_json['success'] = False
            response_json['message'] = "Something went Wrong" + str(e)
    else:
        response_json['success'] = False
        response_json['message'] = "Not get method"
    print("================== Close splash screen =====================")
    print(response_json)
    return JsonResponse(response_json)
