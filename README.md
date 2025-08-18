# Sistema de Pedidos com Design Patterns e Princípios SOLID

Este projeto demonstra a implementação de um sistema de pedidos em Python aplicando diversos **Design Patterns** e os princípios **SOLID** de programação orientada a objetos.

* Testes unitários sendo criados

## � Índice

- [Visão Geral](#visão-geral)
- [Design Patterns Implementados](#design-patterns-implementados)
- [Princípios SOLID Aplicados](#princípios-solid-aplicados)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Como Executar](#como-executar)
- [Exemplos de Uso](#exemplos-de-uso)

## 🎯 Visão Geral

O sistema simula um processo de pedidos de delivery/coleta com funcionalidades de:
- Criação de pedidos (delivery ou coleta)
- Processamento de pagamentos (cartão ou PIX)
- Sistema de notificações (email e SMS)
- Acompanhamento de status do pedido

## 🔧 Design Patterns Implementados

### 1. **Strategy Pattern**
**Localização:** `src/payment/`

O Strategy Pattern é usado para implementar diferentes métodos de pagamento, permitindo que o algoritmo de pagamento seja selecionado em tempo de execução.

```python
# Interface Strategy
class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount: float):
        pass

# Concrete Strategies
class PaymentCard(Payment):
    def process_payment(self, amount):
        print(f"Processing card payment of R$: {amount:.2f}.")

class PaymentPIX(Payment):
    def process_payment(self, amount):
        print(f"Processing PIX payment of R$: {amount:.2f}.")
```

### 2. **Factory Pattern**
**Localização:** `src/payment/payment_factory.py`

O Factory Pattern é usado para criar instâncias de diferentes tipos de pagamento sem expor a lógica de criação ao cliente.

```python
class PaymentFactory:
    @staticmethod
    def create_payment(type):
        if type == "pix":
            return PaymentPIX()
        elif type == "cartao":
            return PaymentCard()
        else:
            raise ValueError(f"tipo de pagamento '{type}' não suportado")
```

### 3. **Observer Pattern**
**Localização:** `src/observer/` e `src/order/order.py`

O Observer Pattern é implementado para notificar automaticamente quando o status do pedido muda.

```python
class Order(ABC):
    def __init__(self, client_name, items):
        self.observers = []
    
    @status.setter
    def status(self, new_status):
        self._status = new_status
        self.notify_observers()
    
    def notify_observers(self):
        for observer in self.observers:
            observer.update_status(self)

class ObserverStatus:
    def update_status(self, order):
        message = f"Order updated, status: {order.status}"
        self.notifications.send_notifications(order.client_name, message)
```

### 4. **Facade Pattern**
**Localização:** `src/notification/notification_facade.py`

O Facade Pattern simplifica a interface para o subsistema de notificações, permitindo enviar múltiplas notificações com uma única chamada.

```python
class NotificationFacade:
    def __init__(self):
        self.notifications = [NotificationSMS(), NotificationEmail()]

    def send_notifications(self, client_name, message):
        for notification in self.notifications:
            notification.send_notification(client_name, message)
```

### 5. **Template Method Pattern**
**Localização:** `src/order/order.py`

Embora implícito, o Template Method é usado na classe abstrata `Order` que define a estrutura básica, enquanto as subclasses implementam detalhes específicos.

```python
class Order(ABC):
    @abstractmethod
    def calculate_total(self):
        pass

class OrderDelivery(Order):
    def calculate_total(self):
        total = sum(item.price for item in self.items) + self.tax_delivery
        return total
```

## 🎯 Princípios SOLID Aplicados

### **S - Single Responsibility Principle (SRP)**
Cada classe tem uma única responsabilidade:
- `Client`: Gerencia dados do cliente
- `Item`: Representa um item do pedido
- `PaymentCard/PaymentPIX`: Processam pagamentos específicos
- `NotificationEmail/NotificationSMS`: Enviam notificações específicas

### **O - Open/Closed Principle (OCP)**
O sistema está aberto para extensão e fechado para modificação:
- Novos tipos de pagamento podem ser adicionados implementando a interface `Payment`
- Novos tipos de pedido podem ser criados herdando de `Order`
- Novos tipos de notificação podem ser implementados via interface `Notification`

### **L - Liskov Substitution Principle (LSP)**
As subclasses podem substituir suas classes base sem quebrar a funcionalidade:
- `OrderDelivery` e `OrderCollected` podem ser usados onde `Order` é esperado
- `PaymentCard` e `PaymentPIX` podem substituir `Payment`

### **I - Interface Segregation Principle (ISP)**
As interfaces são específicas e focadas:
- `Payment`: Interface específica para pagamentos
- `Notification`: Interface específica para notificações
- `Order`: Classe abstrata com métodos específicos para pedidos

### **D - Dependency Inversion Principle (DIP)**
O código depende de abstrações, não de implementações concretas:
- `PaymentFactory` retorna uma abstração `Payment`
- `NotificationFacade` trabalha com a interface `Notification`
- `ObserverStatus` recebe notificações via injeção de dependência

## 📁 Estrutura do Projeto

```
src/
├── client.py                      # Classe Cliente
├── item.py                        # Classe Item
├── main.py                        # Arquivo principal
├── notification/
│   ├── notification.py            # Interface Notification
│   ├── notification_email.py      # Implementação Email
│   ├── notification_sms.py        # Implementação SMS
│   └── notification_facade.py     # Facade Pattern
├── observer/
│   └── observer_status.py         # Observer Pattern
├── order/
│   ├── order.py                   # Classe abstrata Order
│   ├── order_delivery.py          # Pedido com delivery
│   └── order_collected.py         # Pedido para coleta
└── payment/
    ├── payment.py                 # Interface Payment
    ├── payment_card.py            # Pagamento com cartão
    ├── payment_pix.py             # Pagamento PIX
    └── payment_factory.py         # Factory Pattern
```

## 🚀 Como Executar

1. **Clone o repositório:**
```bash
git clone https://github.com/Leonardojdss/solid-python.git
cd solid-python
```

2. **Ative o ambiente virtual:**
```bash
source env/bin/activate
```

3. **Execute o projeto:**
```bash
python3 src/main.py
```

Este projeto demonstra como aplicar boas práticas de programação orientada a objetos, resultando em um código mais limpo, organizando e fácil de manter.