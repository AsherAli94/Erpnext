import frappe
import requests
import json

def send_whatsapp_message(to_number, template_name="hello_world", components=None):
    settings = frappe.get_site_config().get("whatsapp_settings", {})
    token = settings.get("access_token")
    phone_id = settings.get("phone_number_id")
    api_ver = settings.get("api_version", "v20.0")

    url = f"https://graph.facebook.com/{api_ver}/{phone_id}/messages"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    payload = {
        "messaging_product": "whatsapp",
        "to": to_number,
        "type": "template",
        "template": {
            "name": template_name,
            "language": {"code": "en_US"}
        }
    }
    if components:
        payload["template"]["components"] = components

    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        if response.status_code >= 300:
            frappe.log_error(f"WhatsApp Error: {response.text}", "WhatsApp API Error")
    except Exception:
        frappe.log_error(frappe.get_traceback(), "WhatsApp Integration Exception")

def on_submit_sales_invoice(doc, method=None):
    to_number = doc.custom_whatsapp_number or frappe.get_site_config().get("whatsapp_settings", {}).get("default_test_recipient")
    if not to_number:
        frappe.log_error("No WhatsApp recipient found", "WhatsApp Integration")
        return

    send_whatsapp_message(to_number)
