from abc import ABC, abstractmethod

class Notificador(ABC):
    @abstractmethod
    def notificar(self, mensagem):
        pass


class NotificadorEmail(Notificador):
    def notificar(self, mensagem):
        print(f"Enviando email: {mensagem}")
    
class NotificadorSMS(Notificador):
    def notificar(self, mensagem):
        print(f"Enviando SMS: {mensagem}")

class NotificadorApp(Notificador):
    def notificar(self, mensagem):
        print(f"Enviando notificação no app: {mensagem}")


class CentralNotificacoes:
    def __init__(self, lista_de_notificadores):
        self.notificadores = lista_de_notificadores

    def adicionar_notificador(self, notificador):
        self.notificadores.append(notificador)

    def enviar_para_todos(self, mensagem):
        for notificador in self.notificadores:
            notificador.notificar(mensagem)