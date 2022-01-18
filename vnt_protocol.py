from constants import ESTADOS, CONTAS, CURSOS, LINGUAGENS

class VntProtocol:

    id = ''
    conta = ''
    idade = 5
    estado = ''
    curso = ''
    linguagem = ''
    
    def fill(self, attributes):
        self.id = attributes['id']
        self.conta = attributes['conta']
        self.idade = attributes['idade']
        self.estado = attributes['estado']
        self.curso = attributes['curso']
        self.linguagem = attributes['linguagem']
