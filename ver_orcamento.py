import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog
from mecanica import Mecanica
from tkinter import messagebox
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

class VerOrcamento:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Visualizar Orçamentos")

        # Criar uma instância de Mecanica para acessar os orçamentos
        self.mecanica = Mecanica()

        # Criar uma treeview para exibir os orçamentos
        self.tree = ttk.Treeview(self.root, columns=("Item", "Placa do Carro", "Mão de Obra", "Valor Total", "Data"), show="headings")
        self.tree.heading("#1", text="Item")
        self.tree.heading("#2", text="Placa do Carro")
        self.tree.heading("#3", text="Mão de Obra")
        self.tree.heading("#4", text="Valor Total")
        self.tree.heading("#5", text="Dia")
        self.tree.grid(row=0, column=0, padx=10, pady=10)

        # Preencher a treeview com os orçamentos
        self.carregar_orcamentos()

        # Botão para gerar o PDF
        self.pdf_button = tk.Button(self.root, text="Gerar PDF", command=self.gerar_pdf)
        self.pdf_button.grid(row=1, column=0, pady=5)
        
        # Botão para atualizar informações
        self.atualizar_info_button = tk.Button(self.root, text="Atualizar Informações", command=self.atualizar_pagina)
        self.atualizar_info_button.grid(row=2, column=0, pady=5)

        # Botão para apagar orçamento por placa do carro
        self.apagar_orcamento_button = tk.Button(self.root, text="Apagar Orçamento por Placa", command=self.apagar_orcamento_por_placa)
        self.apagar_orcamento_button.grid(row=3, column=0, pady=5)

        self.root.mainloop()

    def carregar_orcamentos(self):
        # Limpar a treeview antes de carregar os orçamentos
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Obter os orçamentos do banco de dados
        orcamentos = self.mecanica.ver_orcamento()

        # Preencher a treeview com os orçamentos
        for orcamento in orcamentos:
            self.tree.insert("", "end", values=(orcamento[1], orcamento[2], orcamento[3], orcamento[4], orcamento[5]))

    def gerar_pdf(self):
        # Obter o item selecionado na treeview
        item_selecionado = self.tree.selection()
        if item_selecionado:
            # Obter os dados do orçamento
            placa_carro = self.tree.item(item_selecionado)['values'][1]
            orcamento = self.mecanica.obter_orcamento(placa_carro)
            if orcamento:
                # Nome do arquivo PDF
                nome_arquivo = f"orcamento_{placa_carro}.pdf"

                # Gerar PDF
                c = canvas.Canvas(nome_arquivo, pagesize=letter)
                c.drawString(100, 750, f"Placa do Carro: {placa_carro}")
                c.drawString(100, 730, f"Item: {orcamento['item']}")
                c.drawString(100, 710, f"Mão de Obra: {orcamento['mao_obra']}")
                c.drawString(100, 690, f"Valor Total: {orcamento['valor_total']}")
                c.drawString(100, 670, f"Dia: {orcamento['data']}")
                c.save()

                messagebox.showinfo("Sucesso", f"PDF gerado com sucesso: {nome_arquivo}")
            else:
                messagebox.showerror("Erro", "Orçamento não encontrado.")
        else:
            messagebox.showwarning("Aviso", "Nenhum orçamento selecionado.")

    def atualizar_pagina(self):
        # Recarregar os orçamentos na treeview
        self.carregar_orcamentos()

    def apagar_orcamento_por_placa(self):
        # Abrir uma caixa de diálogo para obter a placa do carro a ser apagada
        placa_carro = simpledialog.askstring("Apagar Orçamento por Placa", "Digite a placa do carro:")
        if placa_carro:
            # Chamar a função para apagar o orçamento por placa do carro
            self.mecanica.apagar_orcamento_por_placa(placa_carro)
            # Atualizar a treeview após a exclusão
            self.carregar_orcamentos()

# Execução da interface
if __name__ == "__main__":
    VerOrcamento()
