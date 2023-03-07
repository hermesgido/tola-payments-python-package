import base64
import os
import phonenumbers
import requests
import random
import tanzania_mno
from decouple import config


class TolaPayements:
    def __init__(self,  is_sandbox=True, username: str =None, password=None, voda_target = None, tigo_target= None, airtel_target = None):
        self.__is_sandbox = is_sandbox
        self.__username = config("TOLA_USERNAME")
        self.__password = config('TOLA_PASSWORD')
        self.__voda_target = config("VODA_TARGET")
        self.__airtel_target = config("AIRTEL_TARGET")
        self.__tigo_target =config("TIGO_TARGET")

    
    def get_url(self):
        if self.__is_sandbox:
            return "https://stoplight.io/mocks/tolamobile/api-docs/39881367/transaction"
        else:
            return config("TOLA_LIVE_URL")
        
    def charge_costomer(self, phone_number, amount, sourcereference):
        parsed_number = phonenumbers.parse(phone_number, "TZ")
        phone_number_formated = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)
        phone_number_formated = phonenumbers.parse(phone_number_formated, "TZ").national_number
        phone_number_formated = '255' + str(phone_number_formated)
        mno = tanzania_mno.TanzaniaMNOChecker()
        mno_name = mno.get_mno_name(phone_number=phone_number)
        payload = {
            "msisdn": str(phone_number_formated),
            "type": "charge",
            "amount": amount,
            "sourcereference": sourcereference,
            "currency" :"TZS",

        }
     
        
        if mno_name == "Vodacom":
            payload["target"] = self.__voda_target
            payload["channel"] = "TANZANIA.VODACOM"
        elif mno_name == "Tigo":
            payload["target"] = self.__tigo_target
            payload["channel"] = "TANZANIA.AIRTEL"
        elif mno_name == "Airtel":
            payload["target"] = self.__airtel_target
            payload["channel"] = "TANZANIA.AIRTEL"
        else:
           pass
        ##print(payload)
       
        
        auth_credentials = (self.__username, self.__password)
        headers = { "Authorization": "Basic " + base64.b64encode(f"{auth_credentials[0]}:{auth_credentials[1]}".encode('utf-8')).decode('utf-8'), "Content-Type": "application/json"}
        resp =   requests.post(self.get_url(), json=payload, headers=headers)
        try:
            return resp
        except:
            return "Number Not allowed"



