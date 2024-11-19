
        # Bug no meu pc
        conn = None
        cursor = None
        try:
            # Conectar ao banco de dados MySQL
            conn = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                password="admin",
                database="consultoriov1"
            )

            cursor = conn.cursor()
        
        except mysql.connector.Error as err:
            print(f"Erro: {err}")
        finally:
            if cursor:
                cursor.close()
            if conn:
                c