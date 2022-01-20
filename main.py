from vnt_protocol import VntProtocol
if __name__ == '__main__':
    vnt_protocol = VntProtocol()
    
    # vnt_protocol.hydrate_with_hexa('766E747065616C348787')
    # vnt_protocol.decode()
    # print(vnt_protocol)
    
    # vnt_protocol.hydrate_with_hexa('766e7466617261d17456')
    # vnt_protocol.decode()
    # print(vnt_protocol)
    
    
    body = {
        'id' : 'VNTELCA',
        'conta' : 'FTI',
        'idade' : 21,
        'estado' : 'MG',
        'curso' : 'CIENCIA DA COMPUTACAO',
        'linguagem' : 'PHP',
    }
    
    vnt_protocol.hydrate(body)
    # print(vnt_protocol)

    vnt_protocol.encode()
    print(vnt_protocol.binario)
    print(vnt_protocol.hexa)

    vnt_protocol.hydrate_with_hexa(vnt_protocol.hexa)
    vnt_protocol.decode()
    print(vnt_protocol)

    # v = Ventureiro('VNTELCA', 'FTI', 21, 'MG', 'CIENCIA DA COMPUTACAO', 'PHP')
    # print(v.conta)
