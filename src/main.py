import requests
import random
import threading
import time

url = "https://platform-creativespace.com/tpao-land-twlfth/api.php"
charset = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z"
]

def randstr():
    string = []
    for i in range(20):
        string.append(random.choice(charset))
    return "".join(string)
    
def randphone():
    phone = []
    for i in range(10):
        phone.append(str(random.randint(0, 9)))
    return "".join(phone)
    
def randemail():
    return "%s%s%s%s" % (randstr(), "@", randstr(), ".com")
    
class main:
    total_req = 0
    def start_request_thread():
        self = main
        while True:
            self.total_req += 1
            status = requests.post(url=url, data={
                'forename': randstr(),
                'surname': randstr(),
                'email': randemail(),
                'phone': randphone(),
                'successUrl': 'https://platform-creativespace.com/tpao-land-twlfth/index.php',
                'clickid': 'f1637xsb7y9b99',
                'phonecc': '90',
                'country': 'tr'
            }).status_code
            print(f"posting request #{self.total_req} [status]: {status}")
        
    def start(thread_count):
        total_req = 0
        threads = []
        for i in range(thread_count):
            threads.append(threading.Thread(target=main.start_request_thread, daemon=True))
            
        for i in range(thread_count):
            threads[i].start()
            
        for i in range(thread_count):
            threads[i].join()
        
main.start(15)
