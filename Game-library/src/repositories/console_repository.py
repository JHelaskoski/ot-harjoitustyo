class ConsoleRepository:
    def __init__(self, connection):
        self._connection = connection

    def add_console(self, name):
        # Lisätään uusi konsoliperhe
        cursor = self._connection.cursor()
        cursor.execute(
            "insert into consoles (name) values (?)",
            (name,)
        )
        self._connection.commit()

    def get_all_consoles(self):
        cursor = self._connection.cursor()
        cursor.execute("select id, name from consoles")
        return cursor.fetchall()

    def get_console_by_id(self, console_id):
        cursor = self._connection.cursor()
        cursor.execute("SELECT id, name FROM consoles WHERE id = ?", (console_id,))
        return cursor.fetchone()

    def get_console_by_name(self, name):
        cursor = self._connection.cursor()
        cursor.execute("SELECT id, name FROM consoles WHERE name = ?", (name,))
        return cursor.fetchone()
