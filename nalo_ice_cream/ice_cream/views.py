import json, random

from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render
from django.template import loader

from .models import Command, Flavour, Stock

SCOOP_PRICE = 2

def index(request):
    template = loader.get_template('ice_cream/index.html')
    return HttpResponse(template.render({}, request))

def new(request):
    template = loader.get_template('ice_cream/new.html')
    stocks = Stock.objects.all()
    return HttpResponse(template.render({"stocks": stocks}, request))

def create(request):
    template = loader.get_template('ice_cream/result.html')
    stocks = Stock.objects.all()

    content = {}
    price = 0
    for stock in stocks:
        if stock.flavour.name in request.POST and int(request.POST[stock.flavour.name])>0:
            nb_scoop = int(request.POST[stock.flavour.name])
            if stock.amount-nb_scoop >= 0:
                price = price + (nb_scoop*SCOOP_PRICE)
                content[stock.flavour.name] = nb_scoop

                # Update Stock amount
                stock.amount = stock.amount-nb_scoop
                stock.save()

                # Send mail if the current flavour is empty.
                if stock.amount == 0:
                    print('MAIL TOTALLY SEND, NOT JUST A PRINT : Failed to scoop %s, please refill.' % stock.flavour.name)

            else:
                return render(request,'ice_cream/new.html',{'stocks': stocks,'error_message': 'Not enougth ice cream for this flavour : %s'  % stock.flavour.name,})

    if len(content) > 0:
        content = json.dumps(content)
    else:
        return render(request,'ice_cream/new.html',{'stocks': stocks,'error_message': '!!! Command is empty !!!'})

    command = Command.objects.create(content=content, price=price)
    return HttpResponse(template.render({'command': command}, request))

def detail(request):
    template = loader.get_template('ice_cream/detail.html')
    code = request.POST['command_code']
    try:
        command = get_object_or_404(Command, code=code)
    except Http404:
        return render(request,'ice_cream/index.html',{'error_message': 'There is no command for this code.'})


    # List all ice cream scoops for an amazing graphical preview.
    flavours = Flavour.objects.all()
    scoops = []
    for key, value in json.loads(command.content).items():
        for i in range(value):
            scoops.append(flavours.get(name=key))
    random.shuffle(scoops)

    context = {
        "command": command,
        "scoops": scoops
    }
    return HttpResponse(template.render(context, request))

def admin(request):
    print(request.POST)
    template = loader.get_template('ice_cream/admin.html')

    stocks = Stock.objects.all()

    # Check if a refill is called
    for stock in stocks:
        if(stock.flavour.name in request.POST):
            stock.amount = 40
            stock.save()


    # Sum up revenue.
    revenue = 0
    for c in Command.objects.all():
        revenue = revenue + c.price

    context = {
        "stocks": stocks,
        "revenue": revenue
    }
    return HttpResponse(template.render(context, request))
