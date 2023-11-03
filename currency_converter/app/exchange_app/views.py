import requests
from django.shortcuts import render

def exchange(request):
    response = requests.get(url='https://v6.exchangerate-api.com/v6/6e5c495f837334f3e4f7f4d7/latest/USD').json()
    currencies = response.get('conversion_rates')
    if request.method == 'GET':
        context = {
            'currencies': currencies
        }
    if request.method == 'POST':
        from_amount = float(request.POST.get('from-amount'))
        from_curr = request.POST.get('from-curr')
        to_curr = request.POST.get('to-curr')
        
        converted_amount = round((currencies[to_curr] / currencies[from_curr]) * from_amount, 2)
        
        context = {
            'converted_amount': converted_amount,
            'currencies': currencies,
            'from_amount': from_amount,
            'from_curr': from_curr,
            'to_curr': to_curr
        }
    return render(request=request, template_name='exchange_app/index.html', context=context)
    
    
