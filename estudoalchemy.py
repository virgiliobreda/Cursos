from sqlalchemy import (
    Column, 
    String, 
    Integer, 
    Numeric, 
    ForeignKey, 
    create_engine, 
    inspect, 
    select,
)

from sqlalchemy.orm import (
    Session,
    declarative_base,
    relationship,
)


Base = declarative_base()

class Cliente(Base):
    __tablename__ = 'cliente'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    cpf = Column(String(9), nullable=False)
    endereco = Column(String, nullable=False)

    conta = relationship(
        'Conta', back_populates='cliente' 
    )

    def __repr__(self):
        return f'Cliente(id= {self.id}, name= {self.name}, cpf= {self.cpf}, endereço= {self.endereco})'


class Conta(Base):
    __tablename__ = 'conta'
    id = Column(Integer, primary_key=True)
    tipo = Column(String)
    agencia = Column(String(4))
    num = Column(Integer, autoincrement=True)
    id_cliente = Column(Integer, ForeignKey('cliente.id'), nullable=False)
    saldo = Column(Numeric)

    cliente = relationship(
        'Cliente', back_populates='conta'
    )

    def __repr__(self):
        return f'Conta(id={self.id}, tipo={self.tipo}, agencia={self.agencia}, num={self.num}, saldo={self.saldo})'
    

# Criação banco de dados 
engine = create_engine("sqlite://")

Base.metadata.create_all(engine)

inspect_engine = inspect(engine)


# Dados
with Session(engine) as session:
    paula = Cliente(
        name='paula',
        cpf='111111111',
        endereco='rua... número... bairro... cidade... estado...',
        conta= [Conta(
        tipo='credito',
        agencia='0001',
        saldo=10,
    )])
    
    joao = Cliente(
        name='joao',
        cpf='222222222',
        endereco='rua... número... bairro... cidade... estado...',
        conta= [Conta(
        tipo='poupança',
        agencia='0001',
        saldo= 1000
        )]
    )

    # Enviando os objetos para o Banco de dados
    session.add_all([paula, joao])
    session.commit()

# Recuperando dados do usuario através do nome
query_search_name = select(Cliente).where(Cliente.name.in_(['joao',]))
print('\nRecuperando dados através do nome')
for cliente in session.scalars(query_search_name):
    print(cliente)

# Recuperando dados do usuario através do cpf

query_search_cpf = select(Cliente).where(Cliente.cpf.in_(['111111111']))
print('\nRecuperando dados do usuario através do cpf 111111111')
for cpf in session.scalars(query_search_cpf):
    print(cpf)

# Recuperando saldo

query_saldo = select(Cliente.name, Conta.saldo).join(Conta).filter(Conta.id_cliente == Cliente.id)
print('\nRecuperando Saldo')
for nome, saldo in session.execute(query_saldo):
    print(f'nome: {nome}, saldo: {saldo:.2f}')

