from database_connection import get_database_connection

class ConsoleModelRepository:
    def __init__(self):
        self._connection = get_database_connection()

    def add_console_model(self, console_id, name):
        cursor = self._connection.cursor()
        cursor.execute(
            "insert into console_models (console_id, name) values (?, ?)",
            (console_id, name) 
        )
        self._connection.commit()
        
    def get_console_models_by_console_id(self, console_id):
        # Hakee kaikki konsolimallit tietyn konsolin id:n perusteella.
        cursor = self._connection.cursor()
        cursor.execute(
            "select * from console_models where console_id = ?",
            (console_id,)
        )
        return cursor.fetchall()
    
    def get_all_console_models(self):
        # Hakee kaikki konsolimallit.
        cursor = self._connection.cursor()
        cursor.execute("select * from console_models")
        rows = cursor.fetchall()
        return rows