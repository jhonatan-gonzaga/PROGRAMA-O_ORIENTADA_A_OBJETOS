from notificador import Notificador, NotificadorEmail, NotificadorSMS, CentralNotificacoes, NotificadorApp

def main():
    # Criando instâncias dos notificadores
    notificador_email = NotificadorEmail()
    notificador_sms = NotificadorSMS()
    notificador_app = NotificadorApp()

    # Criando a central de notificações
    central = CentralNotificacoes([notificador_email, notificador_sms, notificador_app])

    # Enviando notificação para todos
    central.enviar_para_todos("Esta é uma mensagem de teste.")

if __name__ == "__main__":
    main()