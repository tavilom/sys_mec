import tkinter as tk
from tkinter import ttk
from mecanica import Mecanica

class MostrarClientes:
    def __init__(self):
        self.mecanica = Mecanica()

        self.root = tk.Tk()
        self.root.title("Lista de Clientes")

        self.tree = ttk.Treeview(self.root)
        self.tree["columns"] = ("Modelo do Carro", "Placa do Carro")
        self.tree.heading("#0", text="Nome")
        self.tree.column("#0", width=200)
        self.tree.heading("Modelo do Carro", text="Modelo do Carro")
        self.tree.column("Modelo do Carro", width=200)
        self.tree.heading("Placa do Carro", text="Placa do Carro")
        self.tree.column("Placa do Carro", width=150)
        self.tree.pack(expand=True, fill="both")

        self.carregar_clientes()

        self.root.mainloop()

    def carregar_clientes(self):
        # Limpar a treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Consultar o banco de dados e exibir os clientes na treeview
        clientes = self.mecanica.listar_clientes()
        for cliente in clientes:
            self.tree.insert("", "end", text=cliente[0], values=(cliente[1], cliente[2]))

if __name__ == "__main__":
    MostrarClientes()
