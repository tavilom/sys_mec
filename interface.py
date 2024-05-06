import tkinter as tk
from tkinter import messagebox
from mecanica import Mecanica

class CadastroClientes:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Cadastro de Clientes")

        # Definindo os widgets da janela
        self.titulo_label = tk.Label(self.root, text="Cadastro de Clientes", font=("Helvetica", 16))
        self.titulo_label.grid(row=0, column=0, columnspan=2, pady=10)

        self.nome_label = tk.Label(self.root, text="Nome:")
        self.nome_label.grid(row=1, column=0, padx=10, pady=5)
        self.nome_entry = tk.Entry(self.root)
        self.nome_entry.grid(row=1, column=1, padx=10, pady=5)

        self.modelo_label = tk.Label(self.root, text="Modelo do carro:")
        self.modelo_label.grid(row=2, column=0, padx=10, pady=5)
        self.modelo_entry = tk.Entry(self.root)
        self.modelo_entry.grid(row=2, column=1, padx=10, pady=5)

        self.placa_label = tk.Label(self.root, text="Placa do carro:")
        self.placa_label.grid(row=3, column=0, padx=10, pady=5)
        self.placa_entry = tk.Entry(self.root)
        self.placa_entry.grid(row=3, column=1, padx=10, pady=5)

        self.cadastrar_button = tk.Button(self.root, text="Cadastrar Cliente", command=self.cadastrar_cliente)
        self.cadastrar_button.grid(row=4, column=0, columnspan=2, pady=10)

        self.root.mainloop()

    def cadastrar_cliente(self):
        nome = self.nome_entry.get()
        modelo_carro = self.modelo_entry.get()
        placa_carro = self.placa_entry.get()
        mecanica = Mecanica()  # Cria uma instância de Mecanica
        mecanica.cadastrar_cliente(nome, modelo_carro, placa_carro)
        messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso!")

# Execução da interface
if __name__ == "__main__":
    CadastroClientes()
