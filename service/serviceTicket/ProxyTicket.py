from .TicketServices import TicketServices

class ProxyTicket(TicketServices): # Common interface
    """
    Maintain a reference that lets the proxy access the real subject.
    Provide an interface identical to Subject's.
    """
    
    def __init__(self, real_subject):
        self._real_subject = real_subject

    def create_ticket(self, ticket, pic):
        return self._real_subject.create_ticket(ticket, pic)
  
    def read_ticket(self):
        return self._real_subject.read_ticket()
   
    def read_all_tickets(self):
        return self._real_subject.read_all_tickets()
    
    def read_profile_pic(self, id_user: str):
        return self._real_subject.read_profile_pic(id_user)
    
    def update_ticket_state(self):
        pass
    
    def delete_ticket(self, id_ticket):
        return self._real_subject.delete_ticket(id_ticket)

    def get_tickets(self):
        return self._real_subject.get_tickets()