from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base
import datetime

class Transacao(Base):
    __tablename__ = 'transacoes'

    id = Column(Integer, primary_key=True, index=True)
    descricao = Column(String)
    tipo = Column(String) # 'receita' ou 'despesa'
    valor = Column(Float)
    data = Column(DateTime, default=datetime.datetime.now)

# Você pode adicionar mais classes aqui, como Membro, Orcamento, etc.
# Exemplo:
# class Membro(Base):
#     __tablename__ = 'membros'
#     id = Column(Integer, primary_key=True, index=True)
#     nome = Column(String)
#     cargo = Column(String)