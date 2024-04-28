import requests
from django.shortcuts import render



def index(request):
    r1 = requests.get('	https://random-data-api.com/api/v2/addresses/full_address')
    data = r1.json()
    full_address = data['full_address']
  if  r1.status_code == requests.codes.ok:
    print(r1.text)
  else:
    print("Error:", r1.status_code, r1.text)    
 
    r2 = requests.get('https://random-data-api.com/api/v2/blood_types/type')
    blood_type = r2.json()
    type = blood_type['type']
  if  r2.status_code == requests.codes.ok:
    print(r2.text)
  else:
    print("Error:", r2.status_code, r2.text)

    r3 = requests.get('https://random-data-api.com/api/v2/credit_cards/credit_card_number')
    res3 = r3.json()
    card = res3['credit_card_number']
  if r3.status_code == requests.codes.ok:
    print(r3.text)
  else:
    print("Error:", r3.status_code, r3.text)
    
  return render(request, 'templates/index.html', {
      'full_address': full_address,
      'type': type,
      'card': card
  })

  
