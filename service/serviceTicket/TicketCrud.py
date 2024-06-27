from TicketServices import TicketServices

import pymysql

class TicketCrud(TicketServices):
    def __init__(self, db_name: str) -> None:
        self._db_name = db_name
        self._connection_db = None
    
    def init_connection_db(self) -> None:
        self._connection_db = pymysql.connect(host='localhost', port=3306, user='root', passwd='', database=self._db_name, cursorclass=pymysql.cursors.DictCursor)

    def close_connection_db(self) -> None:
        self._connection_db.commit()
        self._connection_db.close()

    def create_ticket(self, ticket: dict):
        try:
            self.init_connection_db()
            cursor = self._connection_db.cursor()
            query_insert = """
                        INSERT INTO ticket(
                        asunto_ticket, 
                        descripcion_ticket,
                        fecha_creacion_ticket, 
                        categoria_ticket, 
                        captura_pantalla_ticket,
                        id_usuario, 
                        id_estado
                        ) VALUES (%s, %s, %s, %s, %s, %s, %s)
                """
            cursor.execute(query_insert, (
                    ticket['asunto_ticket'],
                    ticket['descripcion_ticket'],
                    ticket['fecha_creacion_ticket'],
                    ticket['categoria_ticket'],
                    ticket['captura_pantalla_ticket'],
                    ticket['id_usuario'],
                    ticket['id_estado']
                ))
            cursor.close()
            self.close_connection_db()
            print('Ticket generado', ticket)
        except Exception as e:
            self.close_connection_db()   
            print('Error al crear ticket', e)
            return 'Error al crear ticket', 500
    
    def read_all_tickets(self):
        try:    
            self.init_connection_db()
            cursor = self._connection_db.cursor()
            query_select = "SELECT * FROM ticket"
            cursor.execute(query_select)
            ticket = cursor.fetchall()
            cursor.close()
            self.close_connection_db()
            return 200, ticket
        except Exception as e:
            self.close_connection_db()
            print('Error al leer tickets', e)
            return 'Error al leer tickets', 500
        
    def read_ticket(self, id_ticket: int):
        try:
            self.init_connection_db()
            cursor = self._connection_db.cursor()
            query_select = "SELECT * FROM ticket WHERE id_ticket = %s"
            cursor.execute(query_select, (id_ticket,))
            ticket = cursor.fetchone()
            cursor.close()
            self.close_connection_db()
            return 200, ticket
        except Exception as e:
            self.close_connection_db()
            return 500, str(e)
        
    def update_ticket_state(self, id_estado: int, nuevo_estado: int):
        try:
            self.init_connection_db()
            cursor = self._connection_db.cursor()
            query_update = "UPDATE ticket SET id_estado = %s WHERE id_estado = %s"
            cursor.execute(query_update, (nuevo_estado, id_estado))
            self._connection_db.commit()
            cursor.close()
            self.close_connection_db()
            print('Se ha actualizado el estado de revisión del ticket.')    
            return 200, 'Se ha actualizado el estado de revisión del ticket.'
        except Exception as e:
            self.close_connection_db()
            return 'Error al actualizar estado.', 500

    def delete_ticket(self, id_ticket: int):
        try:
            self.init_connection_db()
            cursor = self._connection_db.cursor()
            query_delete = "DELETE FROM ticket WHERE id_ticket = %s;"
            ticket = cursor.execute(query_delete, (id_ticket,))
            self.close_connection_db()
            return 200, 'Registro eliminado.'
        except Exception as e:
            self.close_connection_db()   
            return 500, str(e)

    def date_order(self):
        try:
            self.init_connection_db()
            cursor = self._connection_db.cursor()
            query_select = "SELECT * FROM ticket ORDER BY fecha_creacion_ticket DESC"
            cursor.execute(query_select)
            ticket = cursor.fetchall()
            cursor.close()
            return 200, ticket
        except Exception as e:
            self.close_connection_db()
            print('No fue posible ordenar los tickets.', e)
            return 'No fue posible ordenar los tickets.', 500
        
    def merge_tables(self):
        try:
            self.init_connection_db()
            cursor = self._connection_db.cursor()
            query_merge = '''
                        SELECT usuario.nombre_usuario, usuario.apellido_paterno, usuario.apellido_materno, 
                        ticket.*, area.nombre_area, equipo.marca_equipo, equipo.modelo_equipo, 
                        equipo.num_serie_equipo FROM ticket JOIN usuario ON usuario.id_usuario = ticket.id_usuario 
                        JOIN area ON usuario.id_area = area.id_area JOIN equipo ON usuario.id_equipo = equipo.id_equipo"
            '''
            cursor.execute()
            ticket = cursor.fetchall()
            cursor.close()
        except Exception as e:
            self.close_connection_db()
            print('Error al realizar la consulta.', e)
            return 'Error al realizar la consulta.', 500
        
    def get_tickets(self):
        try:
            self.init_connection_db()
            cursor = self._connection_db.cursor()
            query_request = '''
                          SELECT ticket.asunto_ticket, ticket.descripcion_ticket, usuario.nombre_usuario, 
                          usuario.apellido_paterno, usuario.apellido_materno, area.nombre_area FROM ticket JOIN usuario 
                          ON ticket.id_usuario = usuario.id_usuario JOIN area ON usuario.id_area = area.id_area
            '''
            cursor.execute(query_request)
            self.close_connection_db()
            tickets = cursor.fetchall()
            return 200, tickets 
        except Exception as e:
            self.close_connection_db()
            print('Error al realizar la consulta.', e)
            return 500, 'Error al realizar la consulta.'