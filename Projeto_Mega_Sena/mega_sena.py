import sqlite3

# Função para criar tabela
def criar_tabela():
    conexao  = sqlite3.connect('jogos.db')
    cursor = conexao.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS jogos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        numero1 INTEGER,
        numero2 INTEGER,
        numero3 INTEGER,
        numero4 INTEGER,
        numero5 INTEGER,
        numero6 INTEGER
    )
''')
    
    conexao.commit()
    conexao.close()

# Função para adicionar novo jogo
def adicionar_jogo(numeros):
    # Validação e conversão da entrada
    try:
        numeros = tuple(map(int, numeros.split(',')))
    except ValueError:
        print("Erro: Certifique-se de inserir números separados por vírgula.")
        return

    # Verifica se a tupla tem exatamente 6 elementos
    if len(numeros) != 6:
        print("Erro: Certifique-se de inserir exatamente 6 números.")
        return

    conexao = sqlite3.connect('jogos.db')
    cursor = conexao.cursor()
    cursor.execute('''
        INSERT INTO jogos (numero1, numero2, numero3, numero4, numero5, numero6)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', numeros)
    
    conexao.commit()
    conexao.close()

# Função para obter dados do contato
def obter_jogos():
    conexao = sqlite3.connect('jogos.db')
    cursor = conexao.cursor()

    cursor.execute('''SELECT * FROM jogos''')

    jogos = cursor.fetchall()
    conexao.close()

    return jogos

# Função para atualizar Jogos
def atualizar_jogo(jogo_id, novo_jogo):
    # Validação e conversão da entrada
    try:
        novo_jogo = tuple(map(int, novo_jogo.split(',')))
    except ValueError:
        print("Erro: Certifique-se de inserir números separados por vírgula.")
        return

    # Verifica se a tupla tem exatamente 6 elementos
    if len(novo_jogo) != 6:
        print("Erro: Certifique-se de inserir exatamente 6 números.")
        return

    conexao = sqlite3.connect('jogos.db')
    cursor = conexao.cursor()

    cursor.execute('''
        UPDATE jogos 
        SET numero1 = ?, numero2 = ?, numero3 = ?, numero4 = ?, numero5 = ?, numero6 = ? 
        WHERE id = ?
    ''', (*novo_jogo, jogo_id))

    conexao.commit()
    conexao.close()

# Função para excluir Jogo
def excluir_jogo(jogo_id):
    conexao = sqlite3.connect('jogos.db')
    cursor = conexao.cursor()

    cursor.execute('DELETE FROM jogos WHERE id = ?', (jogo_id,))
    conexao.commit()
    conexao.close()



# Função principal
def main():
    criar_tabela()

    while True:
        print("\n Menu")
        print("1. Adicionar Jogos ")
        print("2. Listar Jogos")
        print("3. Atualizar Jogos")
        print("4. Excluir Jogos")
        print("5. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            numeros = input("Digite os numeros do jogo(EX: 01, 02, 03, 04, 05, 06): ")
            adicionar_jogo(numeros)
            print("jogo adicionado com sucesso!")
        
        elif escolha == "2":
            jogos = obter_jogos()
            print("\n Lista de contatos:")
            for jogo in jogos:
                print(f"{jogo[0]}. Numeros do jogo: {jogo[1]}, {jogo[2]}, {jogo[3]}, {jogo[4]}, {jogo[5]}, {jogo[6]}")

        elif escolha == "3":
            jogo_id = input("Digite o id do jogo que deseja atualizar: ")
            novo_jogo = input("Digite o novo jogo: ")
            
            atualizar_jogo(jogo_id, novo_jogo)

            print("Jogo atualizado com sucesso!")

        elif escolha == "4":
            jogo_id = input("Digite o id do jogo que deseja excluir: ")
            excluir_jogo(jogo_id)
            print("O jogo foi excluído com sucesso!")
            
        elif escolha == "5": 
            print("Saindo do programa")
            break

if __name__ == "__main__":
    main()