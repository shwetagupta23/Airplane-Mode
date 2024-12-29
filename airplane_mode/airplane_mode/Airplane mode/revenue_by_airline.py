# Copyright (c) 2024, VIP and contributors
# For license information, please see license.txt

import frappe
from frappe import _

def execute(filters=None):
    revenue_data = frappe.db.sql("""
        SELECT
            a.name AS airline,
            IFNULL(SUM(at.flight_price), 0) AS revenue
        FROM
            `tabAirline` AS a
        LEFT JOIN
            `tabAirplane Ticket` AS at ON at.flight = a.name
        GROUP BY
            a.name
    """, as_dict=True)

    total_revenue = 0
    columns = [
        {
            "fieldname": "airline",
            "label": _("Airline"),
            "fieldtype": "Link",
            "options": "Airline",
            "width": 200
        },
        {
            "fieldname": "revenue",
            "label": _("Revenue"),
            "fieldtype": "Currency",
            "width": 150
        }
    ]

    formatted_data = []
    chart_data = {
        "labels": [],
        "datasets": [{
            "name": _("Revenue by Airline"),
            "values": []
        }]
    }
    
    # Process revenue data
    for item in revenue_data:
        formatted_data.append(item)
        total_revenue += item.revenue

        chart_data["labels"].append(item.airline)
        chart_data["datasets"][0]["values"].append(item.revenue)

    # Add total revenue to the formatted data and chart
    formatted_data.append({
        "airline": "Total",
        "revenue": total_revenue
    })

    chart_data["labels"].append("Total")
    chart_data["datasets"][0]["values"].append(total_revenue)

    # Chart options
    chart_options = {
        "title": _("Revenue Distribution by Airline"),
        "type": "donut",
        "data": chart_data,
        "colors": ["#FF6384", "#36A2EB", "#FFCE56", "#4BC0C0", "#9966FF"], 
        "donut": {
            "title": _("Total Revenue: {0}".format(total_revenue)),
            "label": _("Revenue")
        }
    }

    return columns, formatted_data, chart_options
