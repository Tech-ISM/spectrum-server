from __future__ import print_function
import random

import jwt
from django.http import JsonResponse

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

import keys
from company.models import CompanyData
from referral.models import ReferCodeData, ReferData

# Create your views here.

def generateReferralCode(access_token):
    try:
        decoded = jwt.decode(access_token, keys.KEY_ACCESS_TOKEN_ENCRYPTION, algorithms=['HS256'])
        mobile = decoded[keys.KEY_JWT_ACCESS_TOKEN]
        company_instance = CompanyData.objects.get(username=mobile)
        first_three_letters = company_instance.name.upper()
        first_three_letters = first_three_letters.replace(" ", "")[:4]
        random_int = random.randint(100, 999)
        # company_id = str(company_instance.mobile)[:-8]
        refer_code = first_three_letters + str(random_int)
        try:
            ReferCodeData.objects.get(refer_code=refer_code)
            random_int = random.randint(100, 999)
            refer_code = first_three_letters + str(random_int)
        except Exception as e:
            print(str(e))
        referral_code_instance = ReferCodeData.objects.create(company_instance=company_instance, refer_code=refer_code)
        referral_code_instance.save()
        print(str(mobile))
    except Exception as e:
        print(str(e))
    return


@csrf_exempt
def showReferralCode(request):
    if request.method == 'GET':
        response = {}
        try:
            access_token = request.GET.get(keys.KEY_REQUEST_ACCESS_TOKEN)
            decoded = jwt.decode(access_token, keys.KEY_ACCESS_TOKEN_ENCRYPTION, algorithms=['HS256'])
            mobile = decoded[keys.KEY_JWT_ACCESS_TOKEN]
            company_instance = CompanyData.objects.get(username=mobile)
            try:
                referral_code_instance = ReferCodeData.objects.get(company_instance=company_instance)
            except Exception as e:
                generateReferralCode(access_token)
                referral_code_instance = ReferCodeData.objects.get(company_instance=company_instance)
            print(str(mobile))
            response[keys.KEY_COUNT_SIGNUP] = referral_code_instance.count_signup
            response[keys.KEY_COUNT_INVOICED] = referral_code_instance.count_invoice
            response[keys.KEY_COUNT_REDEEMED] = referral_code_instance.count_redeemed
            response[keys.KEY_REFERRAL_CODE] = referral_code_instance.refer_code
            response[keys.KEY_RESPONSE_SUCCESS] = True
            response[keys.KEY_RESPONSE_MESSAGE] = "Successful"
        except Exception as e:
            response[keys.KEY_RESPONSE_SUCCESS] = False
            response[keys.KEY_RESPONSE_MESSAGE] = "Error in showReferralCode:" + str(e)
            print(str(e))
        print(response)
        return JsonResponse(response)


def checkReferralCode(refer_code, mobile):
    try:
        company_instance = CompanyData.objects.get(username=mobile)
        refer_code_instance = ReferCodeData.objects.get(refer_code=refer_code)
        print(str(mobile))
        try:
            ReferData.objects.get(refer_code_instance=refer_code_instance, company_instance=company_instance)
        except Exception as e:
            ReferData.objects.create(refer_code_instance=refer_code_instance, company_instance=company_instance)
            refer_code_instance.count_signup += 1
            refer_code_instance.save()
            access_token = jwt.encode({keys.KEY_JWT_ACCESS_TOKEN: str(mobile)},
                                       keys.KEY_ACCESS_TOKEN_ENCRYPTION,
                                       algorithm='HS256')
            add_top_up_free_referral2(access_token)
            print(str(e))
        return True
    except Exception as e:
        print(str(e))
    return False


def increaseReferralInvoiceCount(access_token):
    try:
        decoded = jwt.decode(access_token, keys.KEY_ACCESS_TOKEN_ENCRYPTION, algorithms=['HS256'])
        mobile = decoded[keys.KEY_JWT_ACCESS_TOKEN]
        company_instance = CompanyData.objects.get(username=mobile)
        print(str(mobile))
        try:
            refer_instance = ReferData.objects.get(company_instance=company_instance)
            refer_instance.refer_code_instance.count_invoice += 1
            refer_instance.refer_code_instance.save()
            if refer_instance.refer_code_instance.count_invoice >= 2:
                print('1')
                mobile2 = refer_instance.refer_code_instance.company_instance.mobile
                access_token2 = jwt.encode({keys.KEY_JWT_ACCESS_TOKEN: str(mobile2)},
                                           keys.KEY_ACCESS_TOKEN_ENCRYPTION,
                                           algorithm='HS256')
                add_top_up_free_referral(access_token2)
                refer_instance.refer_code_instance.count_invoice -= 2
                refer_instance.refer_code_instance.count_redeemed += 2
                refer_instance.refer_code_instance.save()
        except Exception as e:
            print(str(e))
    except Exception as e:
        print(str(e))
    return
