import frappe

def send_custom_email_with_template(recipient, subject, body_content, attachments=None):
    """
    Sends a custom email using a predefined HTML template.
    
    :param recipient: Email address of the recipient (string or list of strings)
    :param subject: Subject of the email
    :param body_content: Content to replace the placeholder in the email template
    :param attachments: Optional list of file attachments (default: None)
    :return: Success message on email delivery
    """
    try:
        # Path to the HTML template (update 'custom_app' with the correct app name)
        template_path = frappe.get_app_path('custom_app', 'templates', 'email_template.html')
        
        # Load the HTML template content
        with open(template_path, "r") as file:
            html_template = file.read()
        
        # Replace placeholder {{ body }} in the template with dynamic content
        html_content = html_template.replace("{{ body }}", body_content)
        
        # Send the email using Frappe's sendmail function
        frappe.sendmail(
            recipients=recipient,         # Recipient(s) of the email
            subject=subject,              # Subject of the email
            message=html_content,         # HTML content of the email
            delayed=False,                # Sends the email immediately (set True to queue)
            attachments=attachments,      # Attachments, if any
            now=True                      # Sends the email without waiting for email queue
        )
        
        # Return success message
        return 'Email sent successfully!'
    
    except Exception as e:
        # Log error for debugging purposes and raise an exception
        frappe.log_error(f"Error sending email: {str(e)}", "Email Sending Error")
        raise frappe.ValidationError(f"Failed to send email: {str(e)}")
