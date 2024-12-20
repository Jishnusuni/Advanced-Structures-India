
import frappe
import requests

@frappe.whitelist()
def telegram_notification():
    # Telegram Bot Token (Replace 'dummy_token' with your actual token)
    TOKEN = "dummy_token"
    
    # Telegram Chat ID of the recipient (Replace 'dummy_chat_id' with actual chat ID)
    chat_id = "dummy_chat_id"
    
    # Notification content
    notification_format = "This is a message for testing purposes."
    name = "test_user_name"  # Replace with the user's name dynamically if required
    
    # Formatting the message to be sent
    message = (
        f"Dear {name},\n"
        f"{notification_format}\n\n"
        f"-\n"
        f"Regards,"
    )
    
    # Telegram API URL to send the message
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
    
    # Sending the message via Telegram API
    response = requests.get(url).json()
    
    # Optionally, log the response for debugging or tracking purposes
    frappe.log_error(response, "Telegram Notification Response")
