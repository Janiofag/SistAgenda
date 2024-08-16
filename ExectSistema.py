import PySimpleGUI as sg
#Classe cliente e consulta
class Cliente:
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email

class Consulta:
    def __init__(self, cliente, data, hora, servico):
        self.cliente = cliente
        self.data = data
        self.hora = hora
        self.servico = servico

#Funções para gerenciar a agenda
consultas = []

def agendar_consulta(cliente, data, hora, servico):
    consulta = Consulta(cliente, data, hora, servico)
    consultas.append(consulta)

def listar_consultas():
    return consultas
import PySimpleGUI as sg
class Cliente:
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email

class Consulta:
    def __init__(self, cliente, data, hora, servico):
        self.cliente = cliente
        self.data = data
        self.hora = hora
        self.servico = servico


consultas = []

def agendar_consulta(cliente, data, hora, servico):
    consulta = Consulta(cliente, data, hora, servico)
    consultas.append(consulta)

def listar_consultas():
    return consultas

#Implementação da interface gráfica com PySimpleGUIs
import PySimpleGUI as sg

def main():
    sg.change_look_and_feel('DarkBrown19')
    layout = [

        [sg.Text("Sistema de Agendamento de Clínica Estética")],
        [sg.Button("Agendar Consulta"), sg.Button("Visualizar Consultas")],
        [sg.Button("Sair")]
    ]

    window = sg.Window("Clínica Estética Lovely", layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Sair":
            break
        elif event == "Agendar Consulta":
            agendar_consulta_tela()
        elif event == "Visualizar Consultas":
            visualizar_consultas_tela()

    window.close()

def agendar_consulta_tela():
    layout = [
        [sg.Text("Nome do Cliente"), sg.InputText(key="nome")],
        [sg.Text("Telefone"), sg.InputText(key="telefone")],
        [sg.Text("Email"), sg.InputText(key="email")],
        [sg.Text("Data (DD/MM/AAAA)"), sg.InputText(key="data")],
        [sg.Text("Hora (HH:MM)"), sg.InputText(key="hora")],
        [sg.Text("Serviço"), sg.InputText(key="servico")],
        [sg.Button("Agendar"), sg.Button("Voltar")]
    ]

    window = sg.Window("Agendar Consulta", layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Voltar":
            break
        elif event == "Agendar":
            cliente = Cliente(values['nome'], values['telefone'], values['email'])
            agendar_consulta(cliente, values['data'], values['hora'], values['servico'])
            sg.popup("Consulta agendada com sucesso!")
            break

    window.close()

def visualizar_consultas_tela():
    layout = [
        [sg.Text("Consultas Agendadas")],
        [sg.Listbox(values=[f"{c.data} {c.hora} - {c.cliente.nome} ({c.servico})" for c in listar_consultas()], size=(40, 10))],
        [sg.Button("Voltar")]
    ]

    window = sg.Window("Visualizar Consultas", layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Voltar":
            break

    window.close()

if __name__ == "__main__":
    main()
    
    #Banco de dados, (opcional)
    import sqlite3

def criar_tabela():
    conn = sqlite3.connect('clinica.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS consultas
                      (id INTEGER PRIMARY KEY, nome TEXT, telefone TEXT, email TEXT, data TEXT, hora TEXT, servico TEXT)''')
    conn.commit()
    conn.close()

def salvar_consulta(cliente, data, hora, servico):
    conn = sqlite3.connect('clinica.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO consultas (nome, telefone, email, data, hora, servico) VALUES (?, ?, ?, ?, ?, ?)",
                   (cliente.nome, cliente.telefone, cliente.email, data, hora, servico))
    conn.commit()
    conn.close()

def listar_consultas():
    conn = sqlite3.connect('clinica.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM consultas")
    consultas = cursor.fetchall()
    conn.close()
    return consultas