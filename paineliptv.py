# Script para gerar lista M3U com autenticação para um site

import random
import string

class Canal:
    def __init__(self, nome, url):
        self.nome = nome
        self.url = url

class Usuario:
    def __init__(self, usuario, senha):
        self.usuario = usuario
        self.senha = senha

class PainelIPTV:
    def __init__(self):
        self.canais = []
        self.usuarios = []

    def adicionar_canal(self, nome, url):
        novo_canal = Canal(nome, url)
        self.canais.append(novo_canal)
        print(f"Canal '{nome}' adicionado com sucesso!")

    def remover_canal(self, nome):
        self.canais = [canal for canal in self.canais if canal.nome != nome]
        print(f"Canal '{nome}' removido com sucesso!")

    def listar_canais(self):
        print("Lista de Canais:")
        for canal in self.canais:
            print(f"{canal.nome} - {canal.url}")

    def criar_usuario(self):
        usuario = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        senha = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        novo_usuario = Usuario(usuario, senha)
        self.usuarios.append(novo_usuario)
        print(f"Usuário '{usuario}' criado com sucesso!")
        return usuario, senha

    def gerar_lista_m3u(self):
        lista_m3u = '#EXTM3U\n'
        for canal in self.canais:
            lista_m3u += f'#EXTINF:-1,{canal.nome}\n{canal.url}\n'
        return lista_m3u

# Exemplo de uso
painel = PainelIPTV()
painel.adicionar_canal("Canal 1", "http://url.do.canal1/stream")
painel.adicionar_canal("Canal 2", "http://url.do.canal2/stream")
usuario, senha = painel.criar_usuario()
print(f"Usuário: {usuario}, Senha: {senha}")
print(painel.gerar_lista_m3u())
  
