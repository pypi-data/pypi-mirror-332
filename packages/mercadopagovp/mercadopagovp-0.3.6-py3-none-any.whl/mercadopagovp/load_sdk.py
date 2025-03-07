import mercadopago
import os
from dotenv import load_dotenv
from mercadopagovp.error.error_token import ErrorTokenValue




class LoadSDK:
    """Class responsible for loading the MercadoPago SDK."""
    
    def __init__(self, key_env='TOKEN'):
        """
        Initializes the MercadoPago SDK.

        Args:
            key_env (str): Environment variable name containing the access token.
        """
        load_dotenv()
        self.sdk_main = os.getenv(key_env)
        if not self.sdk_main:
            raise ErrorTokenValue("Invalid or missing MercadoPago token.")
        
        self.sdk = mercadopago.SDK(access_token=self.sdk_main)
        print('Success: Token loaded!')
    
    def get_sdk(self):
        """
        Returns the MercadoPago SDK instance.

        Returns:
            mercadopago.SDK: SDK instance.
        """
        return self.sdk
