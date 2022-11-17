from django.http import request
from django.shortcuts import redirect, render
from django.utils import translation
from .models import Person, Transaction
from django.views.decorators.csrf import csrf_protect


@csrf_protect
# Create your views here.
def load_home(request):
    return render(request, 'index.html')

def load_transaction(request):
    return render(request, "transaction.html")

def load_history(request):
    transaction  = Transaction.objects.all()
    print(transaction)
    return render(request, "history.html",{'transaction':transaction})

def load_accounts(request):
    person_list = Person.objects.all()
    print("person_list=", person_list)
    return render(request, 'accounts.html', {'person_list': person_list})

def insert_transaction(request):
    sender_account_number = request.POST.get('senderAccountNumber')
    receiver_account_number = request.POST.get('receiverAccountNumber')
    amount = request.POST.get("amount")

    sender_data = Person.objects.get(person_account_number=sender_account_number)
    receiver_data = Person.objects.get(person_account_number=receiver_account_number)
        
    sender_data.person_balance -= float(amount)
    receiver_data.person_balance += float(amount)
    
    sender_data.save()
    receiver_data.save()

    transaction = Transaction()
    transaction.sender_id = sender_data
    transaction.receiver_id = receiver_data
    transaction.receiver_amount = amount

    transaction.save()

    return redirect('load_history')
