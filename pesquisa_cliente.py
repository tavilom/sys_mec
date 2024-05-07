import tkinter as tk
from tkinter import messagebox
from mecanica import Mecanica

class PesquisaCliente:
    def __init__(self):
        self.root = tk.Toplevel()
        self.root.title("Pesquisar Cliente por Placa")

        # Definindo os widgets da janela
        self.titulo_label = tk.Label(self.root, text="Pesquisar Cliente por Placa", font=("Helvetica", 16))
        self.titulo_label.grid(row=0, column=0, columnspan=2, pady=10)

        self.placa_label = tk.Label(self.root, text="Placa do carro:")
        self.placa_label.grid(row=1, column=0, padx=10, pady=5)
        self.placa_entry = tk.Entry(self.root)
        self.placa_entry.grid(row=1, column=1, padx=10, pady=5)

        self.pesquisar_button = tk.Button(self.root, text="Pesquisar", command=self.pesquisar_cliente)
        self.pesquisar_button.grid(row=2, column=0, columnspan=2, pady=10)

    def pesquisar_cliente(self):
        placa_carro = self.placa_entry.get()
        mecanica = Mecanica()  # Cria uma instância de Mecanica
        resultado = mecanica.pesquisar_cliente_por_placa(placa_carro)

        if resultado:
            messagebox.showinfo("Resultado da Pesquisa", f"Nome: {resultado[0]}\nModelo do Carro: {resultado[1]}")
        # else:
        #     messagebox.showinfo("Resultado da Pesquisa", "Cliente não encontrado.")

if __name__ == "__main__":
    pesquisa_cliente = PesquisaCliente()
