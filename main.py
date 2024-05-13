import tkinter as tk
from cadastro import CadastroClientes
from pesquisa_cliente import PesquisaCliente
from mostrar_clientes import MostrarClientes
from orcamento import Orcamento
from ver_orcamento import VerOrcamento  # Importe a classe VerOrcamento

class MainApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("F & S CAR")

        # Definindo os widgets da janela principal
        self.titulo_label = tk.Label(self.root, text="F & S CAR Mecânica automotiva", font=("Helvetica", 16))
        self.titulo_label.pack(pady=10)

        self.cadastro_button = tk.Button(self.root, text="Cadastro de Clientes", command=self.abrir_cadastro_clientes)
        self.cadastro_button.pack(pady=5)

        self.pesquisa_button = tk.Button(self.root, text="Pesquisar Cliente", command=self.abrir_pesquisa_cliente)
        self.pesquisa_button.pack(pady=5)

        self.mostrar_button = tk.Button(self.root, text="Mostrar Clientes", command=self.abrir_mostrar_clientes)
        self.mostrar_button.pack(pady=5)
        
        self.orcamento_button = tk.Button(self.root, text="Fazer Orçamento", command=self.abrir_orcamento)  # Adicione este botão
        self.orcamento_button.pack(pady=5)
        
        self.ver_orcamento_button = tk.Button(self.root, text="Ver Orçamentos", command=self.abrir_ver_orcamento)  # Adicione este botão
        self.ver_orcamento_button.pack(pady=5)

    def abrir_cadastro_clientes(self):
        cadastro_clientes = CadastroClientes()

    def abrir_pesquisa_cliente(self):
        pesquisa_cliente = PesquisaCliente()

    def abrir_mostrar_clientes(self):
        mostrar_clientes = MostrarClientes()
    
    def abrir_orcamento(self):  # Método para abrir a interface de realizar orçamento
        orcamento = Orcamento()
        
    def abrir_ver_orcamento(self):  # Método para abrir a interface de ver orçamentos
        ver_orcamento = VerOrcamento()
        
if __name__ == "__main__":
    app = MainApp()
    app.root.mainloop()
