# Importação do banco de dados
import MySQLdb

# Classe que inicializa a conexão e o cursor com o banco de dados
class BaseDao:
    def __init__(self):
        # conectando BD
        self.conn = MySQLdb.connect(
            host='mysql.topskills.study', database='topskills04', user='topskills04', passwd='Elenice2019')
        self.cursor = self.conn.cursor()
        
# Metodos que realizaram ações no banco

    def listar(self, sqll):
        self.cursor.execute(sqll)
        return self.cursor.fetchall()
        
    def buscar_por_id(self, sqll):
        self.cursor.execute(sqll)
        return self.cursor.fetchone()
    
    def inserir(self,sqll):
        self.cursor.execute(sqll)
        self.cursor.commit()
    
    def alterar(self, sqll):
        self.cursor.execute(sqll)
        self.cursor.commit()
        
    def deletar(self, sqll):
        self.cursor.execute(sqll)
        self.cursor.commit()
