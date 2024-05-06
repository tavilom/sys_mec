import tkinter as tk
from tkinter import messagebox
from mecanica import Mecanica

class Orcamento:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Gerar Orçamento")

        # Definindo os widgets da janela
        self.titulo_label = tk.Label(self.root, text="Gerar Orçamento", font=("Helvetica", 16))
        self.titulo_label.grid(row=0, column=0, columnspan=2, pady=10)

        self.item_label = tk.Label(self.root, text="Item:")
        self.item_label.grid(row=1, column=0, padx=10, pady=5)
        self.item_entry = tk.Entry(self.root)
        self.item_entry.grid(row=1, column=1, padx=10, pady=5)

        self.placa_label = tk.Label(self.root, text="Placa do carro:")
        self.placa_label.grid(row=2, column=0, padx=10, pady=5)
        self.placa_entry = tk.Entry(self.root)
        self.placa_entry.grid(row=2, column=1, padx=10, pady=5)

        self.mao_obra_label = tk.Label(self.root, text="Mão de obra (R$):")
        self.mao_obra_label.grid(row=3, column=0, padx=10, pady=5)
        self.mao_obra_entry = tk.Entry(self.root)
        self.mao_obra_entry.grid(row=3, column=1, padx=10, pady=5)

        self.valor_item_label = tk.Label(self.root, text="Valor do item (R$):")
        self.valor_item_label.grid(row=4, column=0, padx=10, pady=5)
        self.valor_item_entry = tk.Entry(self.root)
        self.valor_item_entry.grid(row=4, column=1, padx=10, pady=5)

        self.calcular_button = tk.Button(self.root, text="Calcular Valor Total", command=self.calcular_valor_total)
        self.calcular_button.grid(row=5, column=0, columnspan=2, pady=10)

        self.valor_total_label = tk.Label(self.root, text="Valor Total (R$):")
        self.valor_total_label.grid(row=6, column=0, padx=10, pady=5)
        self.valor_total_entry = tk.Entry(self.root, state="readonly")
        self.valor_total_entry.grid(row=6, column=1, padx=10, pady=5)

        self.gerar_button = tk.Button(self.root, text="Gerar Orçamento", command=self.gerar_orcamento)
        self.gerar_button.grid(row=7, column=0, columnspan=2, pady=10)

        self.root.mainloop()

    def calcular_valor_total(self):
        try:
            mao_obra = float(self.mao_obra_entry.get())
            valor_item = float(self.valor_item_entry.get())
            valor_total = mao_obra + valor_item
            self.valor_total_entry.config(state="normal")
            self.valor_total_entry.delete(0, tk.END)
            self.valor_total_entry.insert(0, f"{valor_total:.2f}")
            self.valor_total_entry.config(state="readonly")
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores válidos para a mão de obra e o valor do item.")

    def gerar_orcamento(self):
        item = self.item_entry.get()
        placa_carro = self.placa_entry.get()
        mao_obra = self.mao_obra_entry.get()
        valor_item = self.valor_item_entry.get()

        try:
            mao_obra = float(mao_obra)
            valor_item = float(valor_item)
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores válidos para a mão de obra e o valor do item.")
            return

        mecanica = Mecanica()  # Cria uma instância de Mecanica
        mecanica.gerar_orcamento(item, placa_carro, mao_obra, valor_item)
        #messagebox.showinfo("Sucesso", "Orçamento gerado com sucesso!")

# Execução da interface
if __name__ == "__main__":
    Orcamento()
