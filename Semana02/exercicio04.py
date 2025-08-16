class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def tamanho_livro(self):
        if self.paginas <= 100:
            return "um livro Curto"
        else:
            return "um livro Longo"

livro1 = Livro("O Puntel", "Fernando", 88)
livro2 = Livro("AMF", "Antonio Meneghetti", 256)

print(f"{livro1.titulo} ({livro1.paginas} páginas) é {livro1.tamanho_livro()}")
print(f"{livro2.titulo} ({livro2.paginas} páginas) é {livro2.tamanho_livro()}")
