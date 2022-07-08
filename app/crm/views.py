from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render, get_list_or_404
from .models import Client, ClientWallet
from .forms import ClientForm, UpdateWalletForm
from django.core.exceptions import ObjectDoesNotExist
from decimal import Decimal
from .api_formatter import create_json_response
from .populate_DB import populate_client_model
from .json_samples import sample_error_response, sample_success_response


# Create your views here.

#Do you update wallet when deleting etc.

def index(request, msg=False):
    #implement an if statement for this
    #populate_client_model(repeat=60*60)
    #populate_client_model()
    if msg:
        _, msg = msg.split('.')
        return render(request, 'app/crm/index.html', {'title': 'Welcome Page', 'messages': [msg]})
    return render(request, 'app/crm/index.html', {'title': 'Welcome Page'})

    
    
def list(request):    
    clients = get_list_or_404(Client)
    return render(request, 'app/crm/list.html', {'title': 'Clients List', 'clients': clients})

def details(request, cid):
    client = get_object_or_404(Client, cid= cid)
    try:
        client_wallet = ClientWallet.objects.get(client=client)
    except ObjectDoesNotExist:
        client_wallet = False
    return render(request, 'app/crm/details.html', {'title': f'{client.first_name} Details', 'client': client, "client_wallet": client_wallet})

def create_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            cid = form.cleaned_data.get('cid')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            country_code = form.cleaned_data.get('country_code')
            email = form.cleaned_data.get('email')
            address = form.cleaned_data.get('address')
            phone = form.cleaned_data.get('phone')
            
            new_client = Client(cid = cid, first_name = first_name, last_name = last_name, country_code = country_code, email = email, address = address, phone = phone)

            #will unique fiels be checj before here
            new_client.save()
            
            return redirect('details', cid=cid)
        else:
            #Send error msg use form.errors
            pass
    
    form = ClientForm()
    return render(request, 'app/crm/create_client.html', {'title': 'Create Client', 'form': form})


def update_client(request, cid):
    client = get_object_or_404(Client, cid= cid)

    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            cid = form.cleaned_data.get('cid')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            country_code = form.cleaned_data.get('country_code')
            email = form.cleaned_data.get('email')
            address = form.cleaned_data.get('address')
            phone = form.cleaned_data.get('phone')
            
            client = Client(cid = cid, 
                            first_name = first_name, 
                            last_name = last_name, 
                            country_code = country_code, 
                            email = email, 
                            address = address, 
                            phone = phone)

            client.save()           

            return redirect('details', cid=cid)
        else:
            #Send error msg form.errors
            pass

    form = ClientForm(initial={'cid': client.cid,
                                'first_name': client.first_name, 
                                'last_name' : client.last_name, 
                                'country_code': client.country_code, 
                                'email' : client.email, 
                                'address':  client.address, 
                                'phone':  client.phone})
    return render(request, 'app/crm/create_client.html', {'title': f'Update {client.first_name} Details', 'form': form})

def delete_client(request, cid):
    client = get_object_or_404(Client, cid= cid)
    try:
        client_wallet = ClientWallet.objects.get(client=client)
        client_wallet.delete()
    except:
        pass
    finally:
        client.delete()
        msg = f"--.{client.full_name} Deleted"
        return redirect('index', msg)


def update_wallet(request, cid):
    client = get_object_or_404(Client, cid= cid)
    try:
        client_wallet = ClientWallet.objects.get(client=client)
    except ObjectDoesNotExist:
        client_wallet = ClientWallet(client=client)
        client_wallet.save()

    if request.method == 'POST':
        form = UpdateWalletForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data.get('amount')
            #Updated both total and available
            client_wallet.total_balance += Decimal(amount)
            client_wallet.available_balance += Decimal(amount)

            client_wallet.save()
            return redirect('details', cid)
        else:
            #Send error msg``
            pass
    form = UpdateWalletForm()
    return render(request, 'app/crm/update_wallet.html', {'title': f'Update {client.first_name} Wallet','form': form})

#API ROUTES
def test_API(request):
    #json_object = json.dumps(sample_success_response, indent = 4)
    return JsonResponse(sample_success_response)

def API_single_client(request, cid):
    
    client = Client.objects.filter(cid=cid)

    if len(client) != 1:
        return JsonResponse(sample_error_response, status=404)
    
    client = client[0]

    client_wallet = ClientWallet.objects.filter(client=client)

    if len(client_wallet) != 1:
        created = True
    else:
        created = False
        client_wallet = client_wallet[0]

    response = create_json_response(client, client_wallet, created, sample_success_response)
    return JsonResponse(response)  


def client_websocket(request, cid):
    client = get_object_or_404(Client, cid=cid)

    try:
        wallet = ClientWallet.objects.get(client=client)
    except ObjectDoesNotExist:
        wallet = ClientWallet(client=client)
        wallet.save()

    return render(request, 'app/crm/client_websocket.html', {'title': 'Real-time Wallet Balance', 'client': client, 'wallet': wallet})