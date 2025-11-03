// Copyright (c) 2025, Asher and contributors
// For license information, please see license.txt

frappe.ui.form.on("Server side scripting", {

    // enable: function(frm){
    //     frm.call({
    //         doc: frm.doc,
    //         method: 'frm_call',
    //         args: {
    //             msg: "Hello"
    //         },
    //         freeze: true,
    //         freeze_message: __('Calling frm_call Method'),
    //         callback: function(r) {
    //            // frappe.msgprint(r.message)
    //         }
    //     })
    // }

    // enable: function(frm){
    //         frappe.call({
    //             method: 'demo_app.programming_module.doctype.client_side_scripting.client_side_scripting.frappe_call',
    //             args: {
    //                 msg: "Hello"
    //             },
    //             freeze: true,
    //             freeze_message: __('Calling frappe_call Method'),
    //             callback: function(r) {
    //                //frappe.msgprint(r.message)
    //             }
    //         })
    //     }

    validate(frm) {
        const cdt = "Family Members"; // child DocType
        //const grid = frm.fields_dict.family_members.grid;
    
        // Row 1 → change person_name
        //if (grid.grid_rows.length >= 1) {
          //const cdn1 = grid.grid_rows[0].docname;      // cdn for row 1
        frappe.model.set_value(cdt, 'SER-0023-1', "person_name", "Ali Updated");
        //}
    
        // Row 2 → change age
        //if (grid.grid_rows.length >= 2) {
          //const cdn2 = grid.grid_rows[1].docname;      // cdn for row 2
        frappe.model.set_value(cdt, 'SER-0023-1', "age", 30);
        //}
    
        frm.refresh_field("family_members");
      }



 });
