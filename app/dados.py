import mysql.connector as mc

logins = []

def enviandoProBanco():

    conexao = mc.connect(
    host="localhost",
    user="thiago",
    password="123",
    database="nfse",
    autocommit="True"
    )


    if conexao.is_connected():

        

        def tabelaExiste():
            tabelasLista = []
            cursor = conexao.cursor()

            cursor.execute("SHOW TABLES")
            tabelas = cursor.fetchall()

            for tabela in tabelas:
                tabela = str(tabela)
                tabela = tabela.replace("(", "")
                tabela = tabela.replace(")", "")
                tabela = tabela.replace(",", "")
                tabela = tabela.replace("'", "")
                tabelasLista.append(tabela)
            
            if "login" in tabelasLista:
                return True
        
        existe = tabelaExiste()

        def criandoTabela():
            if existe == True:
                cursor2 = conexao.cursor()
                cursor2.execute("Select email, password from login")
                dados = cursor2.fetchall()
                for d in dados:
                    logins.append(d)
            else:
                table = """"""
                
                
                cursor3 = conexao.cursor()
                cursor3.execute("CREATE TABLE login (id INT AUTO_INCREMENT PRIMARY KEY, email VARCHAR(100), password VARCHAR(100));")

                cursor4 = conexao.cursor()
                cursor4.execute("INSERT INTO login (email, password) VALUES ('adminSuporte@gmail.com', 'sup0rte');")

        criandoTabela()

enviandoProBanco()