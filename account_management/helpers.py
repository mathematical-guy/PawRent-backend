from account_management.models import Contract
from django.core.mail import send_mail


def send_email_to_owner():
    # try:
    #     contract = Contract.objects.get(id=contract_id)
    # except Contract.DoesNotExist:
    #     return f"Contract with {contract_id} does not exists"
    #
    # else:
    #     send_to = contract.owner.email

    send_mail(
        'Contract is about to Expire !',
        'Contract is about to Expire !',
        'mohittalrejaceh@gmail.com',
        ['mohittalreja57@gmail.com'],
        fail_silently=False,
    )
