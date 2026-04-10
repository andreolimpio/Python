# Classe Livro representa um livro da biblioteca
class Livro:
    def __init__(self, titulo, autor):
        # Atributos básicos do livro
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True  # Indica se o livro está disponível

    def emprestar(self):
        # Método para emprestar o livro
        if self.disponivel:
            self.disponivel = False
            return True
        return False

    def devolver(self):
        # Método para devolver o livro
        self.disponivel = True


# Classe Usuario representa uma pessoa que pode pegar livros
class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self.livros_emprestados = []  # Lista de livros que o usuário pegou

    def pegar_livro(self, livro):
        # Tenta pegar um livro emprestado
        if livro.emprestar():
            self.livros_emprestados.append(livro)
            print(f"{self.nome} pegou o livro '{livro.titulo}'")
        else:
            print(f"O livro '{livro.titulo}' não está disponível")

    def devolver_livro(self, livro):
        # Devolve um livro
        if livro in self.livros_emprestados:
            livro.devolver()
            self.livros_emprestados.remove(livro)
            print(f"{self.nome} devolveu o livro '{livro.titulo}'")
        else:
            print(f"{self.nome} não possui esse livro")


# Classe Biblioteca gerencia livros e usuários
class Biblioteca:
    def __init__(self):
        self.livros = []
        self.usuarios = []

    def adicionar_livro(self, livro):
        # Adiciona um livro ao acervo
        self.livros.append(livro)

    def cadastrar_usuario(self, usuario):
        # Adiciona um usuário ao sistema
        self.usuarios.append(usuario)

    def listar_livros(self):
        # Mostra todos os livros com status
        print("\n📚 Lista de livros:")
        for livro in self.livros:
            status = "Disponível" if livro.disponivel else "Emprestado"
            print(f"- {livro.titulo} ({livro.autor}) - {status}")


# =========================
# 🚀 Uso do sistema
# =========================

# Criando a biblioteca
biblioteca = Biblioteca()

# Criando livros
livro1 = Livro("1984", "George Orwell")
livro2 = Livro("Dom Casmurro", "Machado de Assis")

# Adicionando livros à biblioteca
biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)

# Criando usuário
usuario1 = Usuario("André")

# Cadastrando usuário
biblioteca.cadastrar_usuario(usuario1)

# Listando livros disponíveis
biblioteca.listar_livros()

# Usuário pega um livro
usuario1.pegar_livro(livro1)

# Listando novamente para ver mudança
biblioteca.listar_livros()

# Usuário devolve o livro
usuario1.devolver_livro(livro1)

# Estado final
biblioteca.listar_livros()