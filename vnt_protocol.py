from constants import ESTADOS, CONTAS, CURSOS, LINGUAGENS

class VntProtocol:

    id = ''
    conta = ''
    idade = 0
    estado = ''
    curso = ''
    linguagem = ''
    binario = ''
    hexa = ''
    
    def __str__(self):
        return f'\n## VntProtocol\n{{\n   id => {self.id},\n   conta => {self.conta},\n   idade => {self.idade},\n   estado => {self.estado},\n   curso => {self.curso},\n   linguagem => {self.linguagem}\n}}\n'

    def hydrate(self, attributes):
        self.id = attributes['id']
        self.conta = attributes['conta']
        self.idade = attributes['idade']
        self.estado = attributes['estado']
        self.curso = attributes['curso']
        self.linguagem = attributes['linguagem']
    
    def hydrate_with_hexa(self, hexa):
        self.hexa = hexa
        binario = self.hexa_to_bin(hexa)[::-1]
        
        self.binario    = binario[::-1]
        self.linguagem  = (binario[0:4])[::-1]
        self.curso      = (binario[4:8])[::-1]
        self.estado     = (binario[8:13])[::-1]
        self.idade      = (binario[13:20])[::-1]
        self.conta      = (binario[20:24])[::-1]
        self.id         = (binario[24::])[::-1]
    
    def encode(self):
        # print(self.key_for_value(ESTADOS, self.estado))

        linguagem  = str(format(self.key_for_value(LINGUAGENS, self.linguagem), "b")).rjust(4, '0')
        curso      = str(format(self.key_for_value(CURSOS, self.curso), "b")).rjust(4, '0')
        estado     = str(format(self.key_for_value(ESTADOS, self.estado), "b")).rjust(5, '0')
        conta      = str(format(self.key_for_value(CONTAS, self.conta), "b")).rjust(4, '0')
        idade      = str(format(self.idade, "b")).rjust(7, '0')
        id         = self.ascii_to_bin(self.id)
        
        self.binario = (id + conta + idade + estado + curso + linguagem)
        self.hexa = self.bin_to_hexa(self.binario)


    def decode(self):
        self.linguagem  = LINGUAGENS[self.bin_to_dec(self.linguagem)]
        self.curso      = CURSOS[self.bin_to_dec(self.curso)]
        self.estado     = ESTADOS[self.bin_to_dec(self.estado)]
        self.conta      = CONTAS[self.bin_to_dec(self.conta)]
        self.idade      = self.bin_to_dec(self.idade)
        self.id         = self.bin_to_ascii(self.id)

    def transmit(encoded_data):
        return

    def scan(self):
        encoded_data = "00000000000000000000000000000000000000000000000000000000000000000000000000000000"
        return encoded_data
    
    def bin_to_ascii(self, binario):
        ascii = ''
        for i in range(0, len(binario), 8):
            ascii += chr(self.bin_to_dec(binario[i:i+8]))
        
        return ascii
    
    def ascii_to_bin(self, ascii):
        binario = ''
        print(ascii)
        for i in ascii:
            binario += str(format(ord(i), "b")).rjust(8, '0')
        
        return binario
    
    def bin_to_hexa(self, binario, range_bits = 4):
        hexa = ''
        for i in range(0, len(binario), range_bits):
            dec = self.bin_to_dec(binario[i:i+range_bits])
            hexa += str(hex(dec)).replace("0x", "")

        return hexa
    
    def hexa_to_bin(self, hash):
        binario = ''
        for i in hash:
            decimal = int(i,16)
            binario += str(format(decimal, "b")).rjust(4, '0')
        
        return binario

    def bin_to_dec(self, binario):
        decimal = 0
        cont = 1
        for i in reversed(binario):
            decimal += int(i)*cont
            if((cont%2) == 0):                
                cont*=2
            else:
                cont+=1

        return decimal
    
    def key_for_value(self, dictionary, search_vaue):
        for key, value in dictionary.items():
            if search_vaue == value:
                return key
        
        return False

