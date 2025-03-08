import requests
from blockhouse.client.sor_connector import SORConnector
import uuid

class TradeClient:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.api_url = "https://go-api.blockhouse.app"
        # self.api_url = "http://localhost:8080/"
        self.sor_connector = None
        self.trade = None
        self.scheduled_orders = {}

    def fetch_sor_credentials(self) -> dict:
        """
        Fetch SOR credentials from the Go API.

        Returns:
            dict: SOR credentials including access key, secret key, region, and endpoint.
        """
        headers = {"x-api-key": self.api_key}
        response = requests.get(self.api_url + "/fix/sor-credentials", headers=headers)
        response.raise_for_status()

        credentials_data = response.json().get("data")
        if not credentials_data:
            raise ValueError("Failed to retrieve SOR credentials.")

        return credentials_data

    def initialize_sor_connector(self):
        """
        Initialize the SOR connector with fetched SOR credentials.
        """
        credentials = self.fetch_sor_credentials()
        self.sor_connector = SORConnector(
            aws_access_key_id=credentials["aws_access_key_id"],
            aws_secret_access_key=credentials["aws_secret_access_key"],
            region_name=credentials["sor_region"],
            endpoint=credentials["sagemaker_endpoint"],
        )

    def send_trade(
        self,
        payload: dict,
    ) -> dict:
        """_summary_
        Send a trade to the Trade API.
        Args:
            order_id (str): Order ID
            symbol (str): Trading symbol
            quantity (float): Quantity of shares
            side (str): "buy" or "sell"
            price (float): Price per share
            order_type (str): "limit" or "market"

        Raises:
            ValueError: If side or order_type is invalid

        Returns:
            dict: Response from the Trade API
        """
        if not self.sor_connector:
            self.initialize_sor_connector()
        if payload["side"].lower() not in ["buy", "sell"]:
            raise ValueError("Side must be 'buy' or 'sell'.")

        headers = {"x-api-key": self.api_key}
        try:
            response = requests.post(
                self.api_url + "/fix/order", headers=headers, json=payload
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as err:
            return {"error": str(err)}

    def schedule_trade(self, payload: dict) -> dict:
        """
        Schedules a trade order for future execution.

        Args:
            payload (dict): Trade order details.

        Returns:
            dict: Confirmation that the order is scheduled or an error message.
        """
        required_fields = ["symbol", "quantity", "side", "time_in_minutes"]
        
        # Check for missing fields
        missing_fields = [field for field in required_fields if field not in payload]
        if missing_fields:
            return {"error": f"Missing required fields: {', '.join(missing_fields)}"}

        # Validate side value
        if payload["side"].lower() not in ["buy", "sell"]:
            return {"error": "Side must be 'buy' or 'sell'."}

        # Validate quantity and price
        if not isinstance(payload["quantity"], (int, float)) or payload["quantity"] <= 0:
            return {"error": "Quantity must be a positive number."}
        # if not isinstance(payload["price"], (int, float)) or payload["price"] <= 0:
        #     return {"error": "Price must be a positive number."}

        # Validate time_in_minutes
        if not isinstance(payload["time_in_minutes"], int) or payload["time_in_minutes"] <= 0:
            return {"error": "time_in_minutes must be a positive integer."}

        # Generate a random order ID
        order_id = str(uuid.uuid4())
        payload["order_id"] = order_id
        self.scheduled_orders[order_id] = payload

        return {"status": "Order Submitted", "order_id": order_id}
    
    def update_trade(self, payload: dict) -> dict:
        """
        Updates an existing scheduled order.

        Args:
            payload (dict): Updated trade order details (must include "order_id").

        Returns:
            dict: Confirmation of the updated order or an error if order ID is not found.
        """
        # Check if order_id is present
        order_id = payload.get("order_id")
        if not order_id:
            return {"error": "Missing required field: order_id"}

        # Check if order_id exists in scheduled orders
        # if order_id not in self.scheduled_orders:
        #     return {"error": f"Order ID {order_id} not found."}

        # # Update the existing order with new values
        # self.scheduled_orders[order_id] = payload

        return {"status": "Order Updated", "order_id": order_id}
    
    def cancel_trade(self, order_id: str) -> dict:
        """
        Cancels a scheduled trade order.

        Args:
            order_id (str): Order ID to cancel.

        Returns:
            dict: Confirmation that the order is canceled or an error message.
        """

        return {"status": "Order Canceled", "order_id": order_id}


if __name__ == "__main__":
    client = TradeClient("0d22d704ac61d80f35dc109b47393cec")

    res = client.schedule_trade({
    "symbol": "AAPL",
    "quantity": 100,
    "side": "buy",
    "time_in_minutes": 30
    })

    print(res)
    res = client.update_trade({
    "order_id": "12345",
    "symbol": "AAPL",
    "quantity": 100,
    "side": "buy",
    "time_in_minutes": 30
    })

    print(res)
    res = client.cancel_trade("12345")
    print(res)

        # res = client.send_trade(
    #     order_id="12345",
    #     symbol="AAPL",
    #     quantity=100,
    #     side="buy",
    #     price=150.50,
    #     order_type="limit",
    # )
    # res = client.send_trade({
    #         "order_id": "12345",
    #         "symbol": "AAPL",
    #         "quantity": 100,
    #         "side": "buy",
    #         "price": 150.50,
    #         "order_type": "limit",
    #     })

    # print(res)
