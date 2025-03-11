import requests

class AzureReservationCost:
    def __init__(self, subscription_id, token):
        self.subscription_id = subscription_id
        self.token = token
        self.base_url = "https://management.azure.com"

    def get_reservation_cost(self):
        """Fetch reservation cost details from Azure."""
        url = f"{self.base_url}/subscriptions/{self.subscription_id}/providers/Microsoft.Consumption/reservationSummaries?api-version=2022-10-01"
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
        }
        response = requests.get(url, headers=headers)
        return response.json() if response.status_code == 200 else {"error": response.text}

    def get_azure_reservation_order_details(self):
        """Fetch reservation order details from Azure."""
        url = f"{self.base_url}/providers/Microsoft.Capacity/reservationOrders?api-version=2022-11-01"
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
        }
        response = requests.get(url, headers=headers)
        return response.json() if response.status_code == 200 else {"error": response.text}
