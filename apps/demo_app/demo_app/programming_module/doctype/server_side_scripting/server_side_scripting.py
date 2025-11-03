# Copyright (c) 2025, Asher and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document


class Serversidescripting(Document):
	pass

############## Server Side Events #########################	
	# def validate(self):

	# 	frappe.msgprint("Hello Frappe from 'validate' event")

	# def before_save(self):

	# 	frappe.throw("Hello Frappe from 'before_save' event")

	# def before_insert(self):

	# 	frappe.throw("Hello Frappe from 'before_insert event")

	# def after_insert(self):

	# 	frappe.throw("Hello Frappe from 'validate' event")
	
	# def on_update(self):

	# 	frappe.msgprint("Hello Frappe from 'validate' event")

	# def before_submit(self):

	# 	frappe.msgprint("Hello Frappe from 'validate' event")

	# def on_submit(self):

	# 	frappe.msgprint("Hello Frappe from 'validate' event")

	# def on_cancel(self):

	# 	frappe.msgprint("Hello Frappe from 'validate' event")

	# def on_trash(self):

	# 	frappe.msgprint("Hello Frappe from 'validate' event")
	
	# def after_delete(self):

	# 	frappe.msgprint("Hello Frappe from 'validate' event")

####################### get_value #################################

# frappe.db.get_value(doctype, name, fieldname) or frappe.db.get_value(doctype, filters, fieldname)

	# def validate (self):
	# 	self.get_value()
	
	# def get_value(self):

	# 	first_name, age = frappe.db.get_value('Client side scripting','PR-0011', ['first_name' ,'age'])
	# 	frappe.msgprint(_("The Parent first name is {0} and age is {1}").format(first_name,age))

####################### Set_value ###################################

# frappe.db.set_value(doctype , name, fieldname, value)
	# def validate (self):
	# 	self.set_value()
	
	# def set_value(self):

	# 	frappe.db.set_value('Client side scripting','PR-0011', 'first_name', 'Ahmed')

	# 	first_name, age = frappe.db.get_value('Client side scripting','PR-0011', ['first_name' ,'age'])
	# 	frappe.msgprint(_("The Parent first name is {0} and age is {1}").format(first_name,age))

################ Documents exists or not #######################

#frappe.db.exists(doctype , name)
	# def validate(self):
	# 	if frappe.db.exists('Client side scripting', 'PR-0013'):
	# 		frappe.msgprint("The document exists in DB")
	# 	else:
	# 		frappe.msgprint("The document doesnot exists in DB")	

#frappe.db.count(doctype, filters)
	# def validate(self):
	# 	doc_count = frappe.db.count('Client side scripting', {'enable':1})
	# 	frappe.msgprint(("The enable documnet count is {0}").format(doc_count))

################# Run SQL queries #####################

#frappe.db.sql(query, filters, as_dict)

	# def validate(self):
	# 	self.sql()

	# def sql(self):
	# 	data = frappe.db.sql("""
	# 							SELECT
	# 								first_name , age
	# 							FROM
	# 								`tabClient side scripting`
	# 							WHERE 
	# 								enable = 1
	# 						""", as_dict=1)
	
	# 	for d in data:
	# 		frappe.msgprint("The parent first name is {0} and age is {1}".format(d.first_name,d.age))

################## Value Fetching ##########################


	# def validate(self):
	# 	frappe.msgprint(("The full name is '{0}").format(self.first_name+" "+self.middle_name+" "+self.last_name))

	# def validate(self):
	# 	for row in self.get("family_members"):
	# 		frappe.msgprint(("{0} The family member name is {1} the relation is {2}").format(row.idx,row.person_name,row.relation))


####################### Get document (returns a document object of the record identified by doctype and name)############

#frappe.get_doc(doctype, name)

	# def validate(self):

	# 	self.get_document()

	# def get_document(self):
	# 	doc = frappe.get_doc("Client side scripting", self.client_side_doc)
	# 	frappe.msgprint(_("The first name is {0} and age is {1}").format(doc.first_name,doc.age))

	# 	for row in doc.get("family_members"):
	# 		frappe.msgprint(("{0} The family member name is {1} the relation is {2}").format(row.idx,row.person_name,row.relation))

######################## Create a new document #############################

#frappe.new_doc(doctype)

	# def validate(self):
	# 	self.new_document()

	# def new_document(self):

	# 	doc = frappe.new_doc("Client side scripting")
	# 	doc.first_name = "John"
	# 	doc.last_name = "Doe"
	# 	doc.age = 39
	# 	#doc.insert()
	# 	doc.append ("family_members",{"person_name":"Jain",
	# 								  "relation": "sister",
	# 								  "age":25})
	# 	doc.insert()
					
######################## frappe.delete_doc(doctype,name)############

	# def validate(self):
	# 	frappe.delete_doc("Client side scripting", "PR-0015")

################## Doc Methods

# doc.insert()

# some escape hatches that can be used to skip certain checks

# doc.insert(
# 	ignore_permissions = True , # ignore write permissions during insert
# 	ignore_links = True, 	# ignore Link Validation in the document
# 	ignore_if_duplicate = True, # donot insert if DuplicateEtryError is thrown
# 	ignore_mandatory = True # insert even if mandatory fields are not set 
# )

######## doc.save()

# doc.save(
# 	ignore_permissions = True, #ignore write permissions during insert
# 	ignore_version = True 	   # donot create a version record
# )
 

####### doc.delete()

	# def validate(self):

	# 	self.delete_document()

	# def delete_document(self):
	# 	doc = frappe.get_doc("Client side scripting", "PR-0014")
	#   doc.delete()

########## doc.db_set()

	# def validate(self):
	# 	self.set_document()
	
	# def set_document(self):
	# 	doc = frappe.get_doc("Client side scripting", "PR-0014")
	# 	doc.db_set("age",45)

############## Database APi #################################

#frappe.db.get_list(doctype, filters, or_filters, fields, order_by, group_by, start, page_length)

	# def validate(self):
	# 	self.get_list()

	# def get_list(self):
	# 	doc = frappe.db.get_list('Client side scripting',
	# 							filters = {
	# 								'enable':1
	# 							},
	# 							fields =['first_name','age']
	# 							) 
	# 	for d in doc:
	# 		frappe.msgprint("The parent first name is {0} and age is {1}".format(d.first_name,d.age))

	# @frappe.whitelist()
	# def frm_call(self,msg):
	# 	import time
	# 	time.sleep(5)

	# 	#frappe.msgprint(msg)
	# 	self.mob_no = 15428452




		#return "HI this message from frm_call"

