frappe.pages['programming-page'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Demo Page ',
		single_column: true
	});


	page.set_title('My Page')

	page.set_indicator('Done','red')

	let $btn = page.set_primary_action ('New', () => frappe.msgprint("CLicked New"))

	let $btnOne = page.set_secondary_action ('Refresh', () => frappe.msgprint("CLicked Refresh"))

	page.add_menu_item('Send Email', () => frappe.msgprint('Clicked Send EMail'))

	page.add_action_item ('Delete', () => frappe.msgprint('CLicked Delete'))

	let field =  page.add_field({
		label : 'Status',
		fieldtype: 'Select',
		fieldname:'status',
		options: [
			'OPen',
			'Closed',
			'cANCELLED'
		],
		change(){
			frappe.msgprint(field.get_value());
		}
	});

}