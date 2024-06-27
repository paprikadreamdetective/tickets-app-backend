import abc

class TicketServices(abc.ABC): # Common interface
    @abc.abstractmethod
    def create_ticket(self):
        pass
    @abc.abstractmethod
    def read_ticket(self):
        pass
    @abc.abstractmethod
    def read_all_tickets(self):
        pass
    @abc.abstractmethod
    def update_ticket_state(self):
        pass
    @abc.abstractmethod
    def delete_ticket(self):
        pass
    @abc.abstractmethod
    def get_tickets(self):
        pass