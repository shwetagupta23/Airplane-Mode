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
        
    #  def validate_ticket_creation(ticket):
    #    flight_ticket = frappe.get_doc("Airplane Ticket", ticket)
    
    #    airplane = frappe.get_doc("Airplane", flight_ticket.airplane)
    
    #    ticket_count = frappe.db.count("Airplane Ticket", {"flight": flight_ticket.flight})
    #    if ticket_count >= airplane.capacity:
    #         frappe.throw(_("Cannot create ticket. The number of tickets exceeds the airplane's capacity."))
        

    #  def before_save(self):
    #     airplane = frappe.get_doc('Airplane', self.airplane)
    #     current_tickets = frappe.db.count('Airplane Ticket', {'airplane': self.airplane})
        
    #     if current_tickets >= airplane.capacity:
    #         frappe.throw(f'The airplane has reached its capacity of {airplane.capacity} seats.')


     def check_airplane_capacity(self):
        flight = frappe.get_doc('Airplane Flight', self.flight)
        print(flight, "flight")

        airplane_capacity = frappe.db.get_value('Airplane', flight.airplane, 'capacity')
        print(flight.airplane, "airplane")
        print(airplane_capacity, "airplane capacity")

        current_tickets = frappe.db.count('Airplane Ticket', {'flight': self.flight})
        print(current_tickets, "current ticket")

        if current_tickets >= airplane_capacity:
            frappe.throw(_("Cannot create more tickets. The airplane has only {0} seats, and they are all booked.").format(airplane_capacity))

     def on_save(self):
        self.check_airplane_capacity()
        


