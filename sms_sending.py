from frappe.core.doctype.sms_settings.sms_settings import send_sms
import frappe

def otp_sending(mobile_no, otp):
    """
    Sends an OTP to the specified mobile number using the SMS gateway configured in ERPNext.

    :param mobile_no: Mobile number of the recipient (without country code)
    :param otp: One Time Password (OTP) to be sent
    :return: Response from the SMS sending function
    """
    # Add country code to the mobile number (Assuming country code is '91' for India)
    mobile = "91" + str(mobile_no)
    receiver_list = [mobile]  # List of recipients
    
    # Compose the OTP message
    msg = f"{otp} is your One Time Password (OTP) for login ."  
    
    # Fetch sender name from the site configuration (if configured)
    site_config = frappe.get_site_config()
    sender_name = site_config.get("sender_name", "Default Sender")  # Fallback to 'Default Sender' if not found
    
    # Send the SMS and return the response
    return send_sms(
        receiver_list=receiver_list,  # List of recipient mobile numbers
        msg=msg,                      # SMS content
        sender_name=sender_name,      # Sender name (optional)
        success_msg=True              # Enable success message logging
    )
