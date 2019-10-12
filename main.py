import os

from dotenv import load_dotenv
from mtnmomo.collection import Collection

load_dotenv()

config = {
    "ENVIRONMENT": os.environ.get("ENVIRONMENT"),
    "CALLBACK_HOST": os.environ.get("CALLBACK_HOST"),
    "COLLECTION_PRIMARY_KEY": os.environ.get("COLLECTION_PRIMARY_KEY"),
    "COLLECTION_USER_ID": os.environ.get("COLLECTION_USER_ID"),
    "COLLECTION_API_SECRET": os.environ.get("COLLECTION_API_SECRET")
}

client = Collection(config)
transaction_ref = client.requestToPay(
    mobile="256780249914",
    amount="600",
    external_id="123456789",
    payee_note="dd",
    payer_message="dd",
    currency="EUR"
    )

transaction_status = client.getTransactionStatus(
    transaction_ref['transaction_ref'])
print(transaction_status)
print(client.getBalance())
