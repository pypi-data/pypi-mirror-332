# Version: 1.0.1
# Author: Reinan Br
# Date: 2021-07-07
# This is the CreatePixPayment class that is responsible for creating PIX payments on MercadoPago.
# It contains the methods set_value, create_client, create_payment, and the constructor __init__.
# from mercadopago import mercadopago

import mercadopago
from datetime import datetime
from mercadopagovp.load_sdk import LoadSDK
from dataclasses import dataclass
from mercadopagovp.pix_payment import PixPayment





class CreatePixPayment:
    """Class responsible for creating PIX payments on MercadoPago."""
    
    def __init__(self, notification_url: str = None):
        """
        Initializes the CreatePixPayment class.

        Args:
            notification_url (str, optional): Notification URL for the payment.
        """
        self.sdk = LoadSDK().get_sdk()
        self.notification_url = notification_url
        self.first_name = None
        self.last_name = None
        self.value = None
        self.email = None
    
    def set_value(self, value: float) -> None:
        """
        Sets the payment amount.

        Args:
            value (float): Payment amount.

        Raises:
            ValueError: If the amount is less than R$2.00.
        """
        if value < 2.00:
            raise ValueError("The minimum allowed amount is R$2.00.")
        self.value = value
    
    def create_client(self, first_name: str, last_name: str, email: str) -> None:
        """
        Sets client details.

        Args:
            first_name (str): Client's first name.
            last_name (str): Client's last name.
            email (str): Client's email.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
    
    def create_payment(self, description: str) -> PixPayment:
        """
        Creates a PIX payment.

        Args:
            description (str): Payment description.

        Returns:
            PixPayment: Object representing the created payment.
        """
        if not all([self.first_name, self.last_name, self.email, self.value]):
            raise ValueError("All client details and value must be set before creating a payment.")
        
        data = {
            "payer": {
                "email": self.email,
                "first_name": self.first_name,
                "last_name": self.last_name
            },
            "payment_method_id": "pix",
            "transaction_amount": self.value,
            "description": description,
            "notification_url": self.notification_url
        }
        
        try:
            request_options = mercadopago.config.RequestOptions()
            payment_pix = self.sdk.payment().create(data, request_options)
            date_expiration = datetime.fromisoformat(payment_pix['response']['date_of_expiration'])
            date_created = datetime.fromisoformat(payment_pix['response']['date_created'])
            delta_time = (date_expiration - date_created).total_seconds()
            return PixPayment(
                id=payment_pix['response']['id'],
                amount=payment_pix['response']['transaction_amount'],
                qr_code=payment_pix['response']['point_of_interaction']['transaction_data']['qr_code'],
                description=payment_pix['response']['description'],
                currency_id=payment_pix['response']['currency_id'],
                date_last_updated=payment_pix['response']['date_last_updated'],
                ticket_url=payment_pix['response']['transaction_details']['external_resource_url'],
                date_init=payment_pix['response']['date_created'],
                date_end=payment_pix['response']['date_of_expiration'],
                status_code=payment_pix['response']['status'],
                status_payment=payment_pix['response']['status_detail'],
                time_to_end=delta_time
            )
        except Exception as e:
            print(f"Error creating payment: {e}")
            return None
