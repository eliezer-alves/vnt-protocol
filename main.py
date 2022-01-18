from vnt_protocol import VntProtocol
if __name__ == '__main__':
    vnt_protocol = VntProtocol()
    body = {
        'id' : 'VNTELCA',
        'conta' : 'FTI',
        'idade' : 21,
        'estado' : 'MG',
        'curso' : 'CIENCIA DA COMPUTACAO',
        'linguagem' : 'PHP',
    }
    
    vnt_protocol.fill(body)

    print(vnt_protocol.idade)
    # v = Ventureiro('VNTELCA', 'FTI', 21, 'MG', 'CIENCIA DA COMPUTACAO', 'PHP')
    # print(v.conta)
