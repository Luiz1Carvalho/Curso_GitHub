import sys

from PySide6.QtWidgets import QApplication, QGridLayout, QPushButton, QWidget, QMainWindow, QLineEdit

app = QApplication(sys.argv)
window = QMainWindow()
central_widget = QWidget()
window.setCentralWidget(central_widget)
window.setWindowTitle('CALCULADORA')

resposta1 = []
resposta2 = []
def fazer_botao(texto):
    btn = QPushButton(texto)
    btn.setStyleSheet('font-size: 40px;')
    return btn

def adicionar_lista(texto):

    if texto == '=':
        return

    resposta1.append(texto)
    numero = ''.join(str(x) for x in resposta1)
    resposta2.clear()
    resposta2.append(numero)
    campo_resultado.setText(str(numero))

    if len(resposta2) == 1:
        teste = resposta2[0]
        caractere = 0

        for item in teste:
            if caractere == 1 and any(op in item for op in '+-/*'):
                nova = []
                for c in teste:
                    nova.append(c)

                asd = nova[0:len(nova) - 1]
                numero = ''.join(str(x) for x in asd)
                resposta2.clear()
                resposta1.clear()
                resposta2.append(numero)

                return igual(simbolo = str(texto))

            if any(op in item for op in '+-/*'):
                caractere = caractere + 1


def igual(simbolo=''):
    resultado = eval(resposta2[0])
    campo_resultado.setText(str(resultado))
    resposta2.clear()
    resposta1.clear()        
    resposta1.append(resultado)
    if simbolo:
        resposta1.append(simbolo)

def limpa():
    resposta1.clear()
    resposta2.clear()
    campo_resultado.setText(str(0))


layout = QGridLayout()
central_widget.setLayout(layout)

botao1 = fazer_botao('1')
botao2 = fazer_botao('2')
botao3 = fazer_botao('3')
botao4 = fazer_botao('4')
botao5 = fazer_botao('5')
botao6 = fazer_botao('6')
botao7 = fazer_botao('7')
botao8 = fazer_botao('8')
botao9 = fazer_botao('9')
botao0 = fazer_botao('0')


botao_div = fazer_botao('÷')
botao_mult = fazer_botao('*')
botao_soma = fazer_botao('+')
botao_subt = fazer_botao('-')
botao_igual = fazer_botao('=')
botao_virgula = fazer_botao('.')
botao_limpar = fazer_botao('C')

campo_resultado = QLineEdit()
campo_resultado.setReadOnly(True)  # Deixa o campo só para leitura (o usuário não digita)
campo_resultado.setStyleSheet('font-size: 40px;')  # Define uma altura para o campo
campo_resultado.setText("")

layout.addWidget(botao7, 3, 1, 1, 1)
layout.addWidget(botao8, 3, 2, 1, 1)
layout.addWidget(botao9, 3, 3, 1, 1)
layout.addWidget(botao4, 4, 1, 1, 1)
layout.addWidget(botao5, 4, 2, 1, 1)
layout.addWidget(botao6, 4, 3, 1, 1)
layout.addWidget(botao1, 5, 1, 1, 1)
layout.addWidget(botao2, 5, 2, 1, 1)
layout.addWidget(botao3, 5, 3, 1, 1)
layout.addWidget(botao0, 6, 2, 1, 1)
layout.addWidget(botao_virgula, 6, 3, 1, 1)
layout.addWidget(botao_limpar, 6, 1, 1, 1)

layout.addWidget(botao_div, 2, 4, 1, 1)
layout.addWidget(botao_mult, 3, 4, 1, 1)
layout.addWidget(botao_subt, 4, 4, 1, 1)
layout.addWidget(botao_soma, 5, 4, 1, 1)
layout.addWidget(botao_igual, 6, 4, 1, 1)
layout.addWidget(campo_resultado, 1, 1, 1, 5)

botao1.clicked.connect(lambda: adicionar_lista(1))
botao2.clicked.connect(lambda: adicionar_lista(2))
botao3.clicked.connect(lambda: adicionar_lista(3))
botao4.clicked.connect(lambda: adicionar_lista(4))
botao5.clicked.connect(lambda: adicionar_lista(5))
botao6.clicked.connect(lambda: adicionar_lista(6))
botao7.clicked.connect(lambda: adicionar_lista(7))
botao8.clicked.connect(lambda: adicionar_lista(8))
botao9.clicked.connect(lambda: adicionar_lista(9))
botao0.clicked.connect(lambda: adicionar_lista(0))

botao_div.clicked.connect(lambda: adicionar_lista('/'))
botao_mult.clicked.connect(lambda: adicionar_lista('*'))
botao_subt.clicked.connect(lambda: adicionar_lista('-'))
botao_soma.clicked.connect(lambda: adicionar_lista('+'))
botao_igual.clicked.connect(lambda: adicionar_lista('='))
botao_igual.clicked.connect(igual)
botao_virgula.clicked.connect(lambda: adicionar_lista('.'))
botao_limpar.clicked.connect(limpa)

window.show()
app.exec()