// Copyright (c) 2024, VIP and contributors
// For license information, please see license.txt

frappe.ui.form.on('Airline', {
    refresh: function(frm) {
        // Check if the website field has a value
        if (frm.doc.website) {
            // Add a web link to the form, pointing to the airline's website
            frm.add_web_link(frm.doc.website, 'Official Website');
        }
    }
});

