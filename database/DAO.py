from database.DB_connect import DBConnect

class DAO:
    @staticmethod
    def read_all_luoghi():
        conn = DBConnect.get_connection()
        try:
            cursor = conn.cursor(dictionary=True)
            try:
                cursor.execute("SELECT id, nome, tipo, quota_m FROM luogo ORDER BY id")
                result = []
                for row in cursor:
                    result.append(row)
                return result
            finally:
                cursor.close()
        finally:
            conn.close()

