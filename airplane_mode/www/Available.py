import frappe

def get_context(context):
    context.airports = frappe.get_all('Airport', fields=['name'])

    selected_airport = frappe.form_dict.get('airport', '')
    context.selected_airport = selected_airport

    filters = get_filters(selected_airport)

    context.shops = frappe.get_all(
        'Shop',
        filters=filters,
        fields=['shop_name', 'area']
    )

    return context

def get_filters(selected_airport):
    filters = {'status': 'Available'}

    if selected_airport:
        filters['airport'] = selected_airport
    else:
        airports = frappe.get_all('Airport', fields=['name'])
        if airports:
            filters['airport'] = ['in', [airport['name'] for airport in airports]]

    return filters
