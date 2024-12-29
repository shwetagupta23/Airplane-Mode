// Copyright (c) 2024, VIP and contributors
// For license information, please see license.txt

frappe.ui.form.on('Airplane Ticket', {
    refresh: function(frm) {
        frm.add_custom_button(__('Assign Seat'), function() {
            frappe.prompt({
                label: __('Seat Number'),
                fieldname: 'seat_number',
                fieldtype: 'Data',
                reqd: true
            }, function(data) {
                frm.set_value('seat', data.seat_number);
            });
        });
    }
});
