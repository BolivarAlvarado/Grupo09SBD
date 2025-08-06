import mysql.connector

class DBConnection:
    def __init__(self):
        self.host = "0.tcp.sa.ngrok.io"
        self.port = 18480
        self.user = "adminmuarte"
        self.password = "awp2210S@"
        self.database = "muarteDB" 

    def conectar(self):
        return mysql.connector.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            database=self.database
        )