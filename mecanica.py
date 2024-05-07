import tkinter as tk
from tkinter import messagebox
import mysql.connector

class Mecanica:
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="123",
            database="bancoteste"
        )
        self.cursor = self.conexao.cursor()

        # Verificar se o banco de dados existe e criar se não existir
        self.cursor.execute("CREATE DATABASE IF NOT EXISTS bancoteste")
        self.cursor.execute("USE bancoteste")
        self.conexao.commit()

        # Criar a tabela de clientes se não existir
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS clientes (
                                id INT AUTO_INCREMENT PRIMARY KEY,
                                nome VARCHAR(255),
                                modelo_carro VARCHAR(255),
                                placa_carro VARCHAR(255)
                              )""")
        self.conexao.commit()

        # Criar a tabela de orçamentos se não existir
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS orcamentos (
                                id INT AUTO_INCREMENT PRIMARY KEY,
                                item VARCHAR(255),
                                placa_carro VARCHAR(255),
                                mao_obra DECIMAL(10, 2),
                                valor DECIMAL(10, 2)
                              )""")
        self.conexao.commit()

    def cadastrar_cliente(self, nome, modelo_carro, placa_carro):
        sql = "INSERT INTO clientes (nome, modelo_carro, placa_carro) VALUES (%s, %s, %s)"
        valores = (nome, modelo_carro, placa_carro)
        self.cursor.execute(sql, valores)
        self.conexao.commit()
        messagebox.showinfo("Sucesso", f'Cliente {nome} cadastrado com sucesso!')

    def pesquisar_cliente_por_placa(self, placa_carro):
        sql = "SELECT nome, modelo_carro FROM clientes WHERE placa_carro = %s"
        self.cursor.execute(sql, (placa_carro,))
        resultado = self.cursor.fetchone()
        if resultado:
            messagebox.showinfo("Resultado da Pesquisa", f"Nome: {resultado[0]}\nModelo do carro: {resultado[1]}")
        else:
            messagebox.showinfo("Resultado da Pesquisa", "Cliente não encontrado com esta placa de carro.")
            
    def listar_clientes(self):
        self.cursor.execute("SELECT nome, modelo_carro, placa_carro FROM clientes")
        clientes = self.cursor.fetchall()
        return clientes


    def gerar_orcamento(self, item, placa_carro, mao_obra, valor):
        # Verificar se a placa do carro existe na tabela de clientes
        query = "SELECT * FROM clientes WHERE placa_carro = %s"
        self.cursor.execute(query, (placa_carro,))
        cliente = self.cursor.fetchone()

        if cliente:
            # Inserir o orçamento na tabela de orçamentos
            query = "INSERT INTO orcamentos (item, placa_carro, mao_obra, valor) VALUES (%s, %s, %s, %s)"
            valores = (item, placa_carro, mao_obra, valor)
            self.cursor.execute(query, valores)
            self.conexao.commit()
            messagebox.showinfo("Sucesso", "Orçamento gerado com sucesso!")
        else:
            messagebox.showerror("Erro", "Placa do carro não encontrada.")
            

    def ver_orcamento(self):
        # Obter os orçamentos do banco de dados
        self.cursor.execute("SELECT * FROM orcamentos")
        return self.cursor.fetchall()
    
    def obter_orcamento(self, placa_carro):
        # Consulta o banco de dados para obter o orçamento com base na placa do carro
        sql = "SELECT * FROM orcamentos WHERE placa_carro = %s"
        self.cursor.execute(sql, (placa_carro,))
        orcamento = self.cursor.fetchone()
        if orcamento:
            return {
                'item': orcamento[1],
                'placa_carro': orcamento[2],
                'mao_obra': orcamento[3],
                'valor_total': orcamento[4]
            }
        else:
            return None
        
        
    def apagar_orcamento(self, id_orcamento):
        # Exclui o orçamento com base no ID fornecido
        sql = "DELETE FROM orcamentos WHERE id = %s"
        self.cursor.execute(sql, (id_orcamento,))
        self.conexao.commit()

    def editar_orcamento(self, id_orcamento, item, placa_carro, mao_obra, valor):
        # Atualiza os detalhes do orçamento com base no ID fornecido
        sql = "UPDATE orcamentos SET item = %s, placa_carro = %s, mao_obra = %s, valor = %s WHERE id = %s"
        valores = (item, placa_carro, mao_obra, valor, id_orcamento)
        self.cursor.execute(sql, valores)
        self.conexao.commit()


    def fechar_conexao(self):
        self.conexao.close()