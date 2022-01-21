from vnt_protocol import VntProtocol
if __name__ == '__main__':
    print("\n\n\n#####__________________________________________________#####\n")
    vnt_protocol = VntProtocol()
    
    vnt_protocol.hydrate_with_hexa('766e7467756963423999')
    vnt_protocol.decode()
    print(vnt_protocol.binario)
    print(vnt_protocol.hexa)
    print(vnt_protocol)
