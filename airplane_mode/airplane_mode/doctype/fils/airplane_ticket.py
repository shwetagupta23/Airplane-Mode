# Copyright (c) 2024, VIP and contributors
# For license information, please see license.txt

import frappe
import random
from frappe.model.document import Document


class AirplaneTicket(Document):
     def validate(self):
         if not self.price:
             frappe.throw("Please provide a rate")
         total_amount = 0
         for item in self.items:
             total_amount += item.amount

             
         self.total_amount = total_amount + self.price
         
 

     def before_submit(self):
        if self.status != "Boarded":
            frappe.throw("Ticket cannot be submitted unless the status is 'Boarded'.")
            
            
    # def validate(self):
    # # Auto-assign a seat if it's not already set
    #     if not self.seat:
    #         available_seats = self.get_available_seats(self.airplane_flight)  # Function to fetch available seats
    #     if available_seats:
    #         self.seat = available_seats[0]  # Assign the first available seat
    #     else:
    #         frappe.throw("No seats available")

     def before_insert(self):
        random_number = random.randint(1,99)
        random_letter = random.choice("ABCDE")
        self.seat = f"{random_number} {random_letter}"
