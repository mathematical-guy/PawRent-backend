from account_management.helpers import send_email_to_owner
from account_management.models import Contract
from backend.celery import app


@app.task()
def deactivate_all_contract():
    contracts = Contract.objects.filter(is_active=True)
    print(f"There are {contracts.count()} active contracts")
    contracts.update(is_active=False)
    print("All Contracts deactivated")
    send_email_to_owner()


