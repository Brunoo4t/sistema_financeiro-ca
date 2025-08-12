from .database import init_db, SessionLocal
from .models import Transacao
from sqlalchemy import extract
import datetime

def registrar_transacao(descricao, tipo, valor, data):
    """
    Função para registrar uma nova transação no banco de dados.
    """
    db = SessionLocal()
    try:
        nova_transacao = Transacao(descricao=descricao, tipo=tipo, valor=valor, data=data)
        db.add(nova_transacao)
        db.commit()
        print("Transação registrada com sucesso!")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        db.rollback()
    finally:
        db.close()

def ver_saldo_por_ano(ano):
    """
    Função para gerar o relatório de saldo de um ano específico.
    """
    db = SessionLocal()
    try:
        # Filtra as transações para o ano especificado usando extract() do SQLAlchemy
        transacoes_do_ano = db.query(Transacao).filter(extract('year', Transacao.data) == ano).all()

        if not transacoes_do_ano:
            print(f"\nNão há transações registradas para o ano de {ano}.")
            return

        receitas = sum(t.valor for t in transacoes_do_ano if t.tipo == 'receita')
        despesas = sum(t.valor for t in transacoes_do_ano if t.tipo == 'despesa')
        saldo = receitas - despesas
        
        print(f"\n--- Relatório Financeiro do Ano {ano} ---")
        print(f"Total de Receitas: R$ {receitas:.2f}")
        print(f"Total de Despesas: R$ {despesas:.2f}")
        print(f"Saldo Atual: R$ {saldo:.2f}")
        print("--------------------------------------\n")
    finally:
        db.close()

if __name__ == "__main__":
    init_db()  # Garante que as tabelas existem antes de qualquer operação
    
    while True:
        print("\nMenu:")
        print("1. Registrar Transação")
        print("2. Ver Saldo por Ano")
        print("3. Sair")
        
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            descricao = input("Descrição da transação: ")
            tipo = input("Tipo (receita/despesa): ")
            valor = float(input("Valor: "))
            
            # Nova lógica para capturar o mês e ano
            try:
                ano_input = int(input("Ano (ex: 2024): "))
                mes_input = int(input("Mês (1-12): "))
                
                data_transacao = datetime.datetime(ano_input, mes_input, 1)
                registrar_transacao(descricao, tipo, valor, data_transacao)
            except ValueError:
                print("Entrada inválida. Por favor, insira o mês e o ano corretamente.")
            except Exception as e:
                print(f"Ocorreu um erro ao registrar a transação: {e}")

        elif escolha == '2':
            try:
                ano_relatorio = int(input("Digite o ano para o relatório (ex: 2024): "))
                ver_saldo_por_ano(ano_relatorio)
            except ValueError:
                print("Ano inválido. Por favor, insira um número de 4 dígitos.")

        elif escolha == '3':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")