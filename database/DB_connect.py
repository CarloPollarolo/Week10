import os
from pathlib import Path
import mysql.connector


class DBConnect:
    @staticmethod
    def get_connection():
        # Copiare connector.cnf.example in connector.cnf e configurare le credenziali.
        config = Path(__file__).with_name("db.cnf")
        if not config.exists():
            raise FileNotFoundError(f"Configurare {config}")
        return mysql.connector.connect(option_files=str(config),
                                       database="parco_sentieri")
