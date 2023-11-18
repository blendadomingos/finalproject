import sqlite3


class Data_base:

    def __init__(self, name='system.db') -> None:
        self.name = name

    def connect(self):
        self.connection = sqlite3.connect(self.name)

    def close_connection(self):
        try:
            self.connection.close()
        except:
            pass

    def create_table_company(self):
        cursor = self.connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS companies(
            CNPJ TEXT,
            NAME TEXT,
            ADDRESS TEXT,
            NUMBER TEXT,
            COMPLEMENT TEXT,
            NEIGHBORHOOD TEXT,
            CITY TEXT,
            STATE TEXT,
            ZIP_CODE TEXT, 
            PHONE TEXT,
            EMAIL TEXT,
            PRIMARY KEY(CNPJ)
            );



           
        
        
        """)

    def register_company(self, fullDataSet):

        
        campos_tabela = ('CNPJ', 'NAME', 'ADDRESS', 'NUMBER', 'COMPLEMENT', 'NEIGHBORHOOD', 'CITY',
                         'STATE', 'ZIP_CODE', 'PHONE', 'EMAIL')

        qntd = ("?,?,?,?,?,?,?,?,?,?,?")
        cursor = self.connection.cursor()

        try:
            cursor.execute(f"""INSERT INTO companies {campos_tabela}
            VALUES({qntd})""", fullDataSet)
            self.connection.commit()
            return ("OK")

        except:
            return "Erro"

    def select_all_companies(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM companies ORDER BY NOME")
            empresas = cursor.fetchall()
            return empresas
        except:
            pass

    def delete_companies(self, id):

        try:
            cursor = self.connection.cursor()
            cursor.execute(f"DELETE FROM companies WHERE CNPJ = '{id}' ")

            self.connection.commit()

            return "Company registration successfully deleted!"

        except:
            return "Error deleting record!"

    def update_company(self, fullDataSet):

        cursor = self.connection.cursor()
        cursor.execute(f""" UPDATE companies set


            CNPJ = '{fullDataSet[0]}',
            NAME = '{fullDataSet[1]}',
            ADDRESS = '{fullDataSet[2]}',
            NUMBER = '{fullDataSet[3]}',
            COMPLEMENT = '{fullDataSet[4]}',
            NEIGHBORHOOD = '{fullDataSet[5]}',
            CITY = '{fullDataSet[6]}',
            STATE = '{fullDataSet[7]}',
            ZIP_CODE = '{fullDataSet[8]}',
            PHONE = '{fullDataSet[9]}',
            EMAIL = '{fullDataSet[10]}'
            WHERE CNPJ = '{fullDataSet[0]}'""")

           
        self.connection.commit()
