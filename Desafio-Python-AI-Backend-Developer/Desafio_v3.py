from abc import ABC, abstractmethod
from datetime import datetime

# Classe Cliente
class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        """
        Realiza uma transação em uma conta.
        """
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        """
        Adiciona uma conta à lista de contas do cliente.
        """
        self.contas.append(conta)

# Classe PessoaFisica herdando de Cliente
class PessoaFisica(Cliente):
    def __init__(self, endereco, nome, data_nascimento, cpf):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

# Classe Conta
class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        """
        Método de classe para criar uma nova conta.
        """
        return cls(numero, cliente)
        
    @property
    def saldo(self):
        return self._saldo
        
    @property
    def numero(self):
        return self._numero
        
    @property
    def agencia(self):
        return self._agencia
        
    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico
        
    def sacar(self, valor):
        """
        Realiza um saque na conta.
        """
        if valor > self._saldo:
            print("Saldo insuficiente!")
            return False
        elif valor > 0:
            self._saldo -= valor
            print(f"Saque de: R${valor:.2f} realizado!")
            return True
        else:
            print("Valor inválido informado!")
            return False
    
    def depositar(self, valor):
        """
        Realiza um depósito na conta.
        """
        if valor > 0:
            self._saldo += valor
            print(f"Depósito de: R${valor:.2f} realizado!")
            return True
        else:
            print("Valor inválido informado!")
            return False

# Classe ContaCorrente herdando de Conta
class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        """
        Realiza um saque na conta corrente, considerando limite de saques e valor.
        """
        numero_saque = len([transacao for transacao in self.historico.transacoes if transacao["tipo"] == "Saque"])

        if valor > self.limite:
            print("O valor do saque excede o limite.")
            return False
        elif numero_saque >= self.limite_saques:
            print("Número máximo de saque excedido.")
            return False
        else:
            return super().sacar(valor)
            
    def __str__(self):
        return f"Agência: {self.agencia}\nC/C: {self.numero}\nTitular: {self.cliente.nome}"

# Classe Historico
class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes
    
    def adicionar_transacao(self, transacao):
        """
        Adiciona uma transação ao histórico.
        """
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            }
        )

    def listar_transacoes(self):
        """
        Lista todas as transações no histórico.
        """
        for transacao in self._transacoes:
            print(f"{transacao['tipo']} de R${transacao['valor']:.2f} em {transacao['data']}")

# Classe abstrata Transacao
class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass

# Classe Saque herdando de Transacao
class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        """
        Registra um saque na conta.
        """
        if conta.sacar(self.valor):
            conta.historico.adicionar_transacao(self)

# Classe Deposito herdando de Transacao
class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        """
        Registra um depósito na conta.
        """
        if conta.depositar(self.valor):
            conta.historico.adicionar_transacao(self)


# Testando a implementação

# Criando um cliente Pessoa Física
cliente = PessoaFisica("Rua das Pedras, 4578", "João", "01/12/1995", "458.269.5487-38")

# Criando uma Conta Corrente para o cliente
conta_corrente = ContaCorrente(59827, cliente)

# Adicionando a conta ao cliente
cliente.adicionar_conta(conta_corrente)

# Realizando um depósito
deposito = Deposito(2000)
cliente.realizar_transacao(conta_corrente, deposito)

# Realizando um saque
saque = Saque(350)
cliente.realizar_transacao(conta_corrente, saque)

# Tentando realizar um saque maior que o saldo disponível
saque = Saque(750)
cliente.realizar_transacao(conta_corrente, saque)

# Exibindo o saldo atual e o histórico de transações
print(f"Saldo atual: R${conta_corrente.saldo:.2f}")
conta_corrente.historico.listar_transacoes()
