from django.shortcuts import render
from scrapers import baby
import json

def childcare(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        babysitters = baby.get_babysitters(city)
        babysitters = json.loads(babysitters)
        print(babysitters)
    else:
         babysitters = baby.get_babysitters('delhi') 
         babysitters = json.loads(babysitters)  
    return render(request, 'childcare/childcare.html', {'babysitters':babysitters})
