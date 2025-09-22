from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

api = FastAPI()

class Ticket(BaseModel):
    id: int
    flight_name: str
    flight_date: str  # Example: "2025-10-15"
    flight_time: str  # Example: "14:30"
    destination: str

tickets: List[Ticket] = []

@api.get("/")
def index():
    return {"Message": "Welcome to the Ticket Booking System"}


@api.get("/ticket")
def get_tickets():
    return tickets


@api.post("/ticket")
def add_ticket(ticket: Ticket):
    tickets.append(ticket)
    return ticket


@api.put("/ticket/{ticket_id}")
def update_ticket(ticket_id: int, updated_ticket: Ticket):
    for index, ticket in enumerate(tickets):
        if ticket.id == ticket_id:
            tickets[index] = updated_ticket
            return updated_ticket
    return {"error": "Ticket Not Found"}



@api.delete("/ticket/{ticket_id}")
def delete_ticket(ticket_id: int):
    for index, ticket in enumerate(tickets):
        if ticket.id == ticket_id:
            deleted_ticket = tickets.pop(index)
            return deleted_ticket

    return {"error": "Ticket not found, deletion failed"}