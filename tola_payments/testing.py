""" from tola_payments import TolaPayements

pym = TolaPayements(is_sandbox=False)

resp = pym.charge_costomer(amount="1000",phone_number="+25561189850", sourcereference='4546f56543poF66')
try:
   print(resp.text)
except Exception as e:
    print(e) """