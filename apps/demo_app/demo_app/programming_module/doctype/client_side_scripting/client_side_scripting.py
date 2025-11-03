# Copyright (c) 2025, Asher and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Clientsidescripting(Document):
	pass


@frappe.whitelist()
def frappe_call (msg):

	import time
	time.sleep(5)
	frappe.msgprint(msg)

	#return 'HI this message is from frappe_call'