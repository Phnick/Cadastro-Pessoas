import mysql.connector
from mysql.connector import errorcode
from flask_bcrypt import generate_password_hash

print("Conectando...")
print("Conectando...")
try:
    conn = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='Ph1140'
    )
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('Existe algo errado no nome de usuário ou senha')
    else:
        print(err)

cursor = conn.cursor()

cursor.execute("DROP DATABASE IF EXISTS `cadastros`;")

cursor.execute("CREATE DATABASE `cadastros`;")

cursor.execute("USE `cadastros`;")

# criando tabelas
TABLES = {}
TABLES['pessoas'] = ('''
      CREATE TABLE `pessoas` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `nome` varchar(50) NOT NULL,
      `idade` int NOT NULL,
      `sexo` varchar(20) NOT NULL,
      PRIMARY KEY (`id`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['Usuarios'] = ('''
      CREATE TABLE `usuarios` (
      `nome` varchar(20) NOT NULL,
      `senha` varchar(100) NOT NULL,
      PRIMARY KEY (`nome`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

for tabela_nome in TABLES:
    tabela_sql = TABLES[tabela_nome]
    try:
        print('Criando tabela {}:'.format(tabela_nome), end=' ')
        cursor.execute(tabela_sql)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print('Já existe')
        else:
            print(err.msg)
    else:
        print('OK')

# inserindo usuarios
usuario_sql = 'INSERT INTO usuarios (nome, senha) VALUES (%s, %s)'
# ,generate_password_hash("Ph1140").decode('utf-8') serve para criar um hash de segurança
usuarios = [
    ("Pedro Nick",generate_password_hash("Ph1140").decode('utf-8')),
    ("Gabriela Loures", generate_password_hash("gabi123").decode('utf-8'))

]
cursor.executemany(usuario_sql, usuarios)

cursor.execute('select * from cadastros.usuarios')
print(' -------------  Usuários:  -------------')
for user in cursor.fetchall():
    print(user[1])

# inserindo jogos
pessoas_cadastradas_sql = 'INSERT INTO pessoas (nome, idade, sexo) VALUES (%s, %s, %s)'
pessoas = [
    ('Pedro', 24, 'Masculino'),
    ('Gabi', 22, 'Feminino')

]
cursor.executemany(pessoas_cadastradas_sql, pessoas)

cursor.execute('select * from cadastros.pessoas')
print(' -------------  Pessoas:  -------------')
for pessoa in cursor.fetchall():
    print(pessoa[1])

# commitando se não nada tem efeito
conn.commit()

cursor.close()
conn.close()
