// Copyright (c) 2025, Asher and contributors
// For license information, please see license.txt

 frappe.ui.form.on("Client side scripting", {
	// refresh(frm) {
    //     //frappe.msgprint("Hello Asher")
    //     frappe.throw("T´his is Error!")
	// }
    ////////////////////////// frm.set_val /////////////////////
    // validate: function(frm){
    //     frm.set_value ('full_name', frm.doc.first_name + " " + frm.doc.middle_name + " " + frm.doc.last_name )
    // ///////////////////////// add_child /////////////////////////////////  
    //     let row = frm.add_child('family_members',{
    //         person_name: 'Aneeb',
    //         relation: 'FAther',
    //         age:46,
    //     })
    // }

    // validate(frm) {
    //     // limit to the specific document
    //     if (frm.doc.name !== 'PR-0020') return;

    //     const rows = frm.doc.family_members || [];

    //     // first row age
    //     if (rows[0]) {
    //     rows[0].age = 52;
    //     }

    //     // third row name
    //     if (rows[2]) {
    //     rows[2].person_name = 'Ahmed';
    //     }

    //     // write back using frm.set_value (no rebuild)
    //     frm.set_value('family_members', rows);

    //     frm.refresh_field('family_members');
    // }
    after_save(frm) {
        // limit to the specific document
        if (frm.doc.name !== 'PR-0023') return;

        const rows = frm.doc.family_members || [];

        // first row age
        if (rows[0]) {
        rows[0].age = 25;
        }

        // third row name
        if (rows[2]) {
        rows[2].person_name = 'Areeb';
        }

        // write back using frm.set_value (no rebuild)
        frm.set_value('family_members', rows);

        frm.refresh_field('family_members');
    }
    ////////////////    set_df_property ///////////////////
    // enable: function (frm) {
    //         // frm.set_df_property('first_name','reqd',1)
    //         // // frm.refresh_field('first_name');

    //         // frm.set_df_property('middle_name','read_only',1)
    //         // frm.refresh_field('middle_nvalidate: function(frm){
    //     frm.set_value ('full_name', frm.doc.first_name + " " + frm.doc.middle_name + " " + frm.doc.last_name )
    // ///////////////////////// add_child /////////////////////////////////  
    //     let row = frm.add_child('family_members',{
    //         person_name: 'Aneeb',
    //         relation: 'FAther',
    //         age:46,
    //     })ame');

    //         frm.toggle_reqd('age',true)

    // }
////////////////// add_custom_button    //////////////////
    // refresh: function (frm) {

    //     // frm.add_custom_button ('Click me!',() =>{
    //     //     frappe.msgprint('YOu clicked me why!!');
    //     // })

    //     frm.add_custom_button ('Click me 1!',() =>{
    //         frappe.msgprint ('YOu clicked 1!!');
    //     },'click me!')

    //     frm.add_custom_button ('Click me 2!',() =>{
    //         frappe.msgprint ('YOu clicked 2!!');
    //     },'click me!')

    // }

  ////////////////////////////// VAlue Fetching /////////////////////////////////////
  
        // after_save:function(frm){
        //     frappe.msgprint (__("The full name is  '{0}'", [frm.doc.first_name + " " + frm.doc.middle_name + " " + frm.doc.last_name]))

        //     for( let row of frm.doc.family_members){
        //         frappe.msgprint(__("{0}. The family member name is {1} and relation is {2} ",[row.idx,row.person_name,row.relation]))
        //     }
        // }
////////////////////// set_intro (sets introduction custom as you want)/////////////////

//    refresh: function(frm){
//         //frm.set_intro('Now you can make custom intros and this page is for cusom side scrpting doctype')

// ////////////////  see only the intro first time /////////////////////
//         if (frm.is_new()){
//             frm.set_intro('Now you can make custom intros and this page is for cusom side scrpting doctype')
//         }

    //}

    /////////////////////////// ALL Events could use for checking or forming logics ///////////////////////

//     refresh: function (frm){
//         frappe.msgprint("Hello ASher from 'refresh event'")
//     },

//     onload: function (frm){
//         frappe.msgprint("Hello ASher from 'onload event'")
//     },

//     validate: function (frm){
//         frappe.msgprint("Hello ASher from 'validate event'")
//     },

//     before_save: function (frm){
//         frappe.msgprint("Hello ASher from 'refresh event'")
//     },
    
//     after_save: function (frm){
//         frappe.msgprint("Hello ASher from 'refresh event'")
//     },

//     enable: function (frm){
//         frappe.msgprint("Hello ASher from 'refresh event'")
//     },

//     age: function (frm){
//         frappe.msgprint("Hello ASher from 'refresh event'")
//     },

//     family_members_on_form_rendered: function (frm){
//         frappe.msgprint("Hello ASher from 'refresh event'")
//     },

//     before_submit: function (frm){
//         frappe.throw("Hello ASher from 'refresh event'")
//     },

//     on_submit: function (frm){
//         frappe.msgprint("Hello ASher from 'refresh event'")
//     },

//     age: function (frm){
//         frappe.msgprint("Hello ASher from 'refresh event'")
//     },

//     age: function (frm){
//         frappe.msgprint("Hello ASher from 'refresh event'")
//     },

//  });

 /////////////////////////////// CHILD TABLE SCRIPTS (Makes you to use child tables)//////////////////////////

//  frappe.ui.form.on('Family Members',{


//     // person_name: function(frm) {
//     //     frappe.msgprint('Hello Asher from Child doctype (person_name) event')
//     // }

//     age: function(frm) {
//         frappe.msgprint('Hello Asher from Child doctype (age) event')
//     }
 
  });
