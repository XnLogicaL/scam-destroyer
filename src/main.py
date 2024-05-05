import requests
import random
import threading

url = "https://platform-creativespace.com/tpao-land-twlfth/api.php"
charset = "abcdefghijklmonpqrstuvwxyzABCDEFGHIJKLMONPQRSTUVWXYZ"


class Main:
    def __init__(self, thread_count):
        self.total_req = 0
        self.threads = []
        for i in range(thread_count):
            new_thread = threading.Thread(target=self.create_thread, daemon=True)
            new_thread.run()
            self.threads.append(new_thread)

        for i in range(thread_count):
            self.threads[i].join()

    def rand_str(self):
        string = []
        for i in range(20):
            string.append(charset[random.randint(0, len(charset))])
        return "".join(string)

    def rand_phone(self):
        phone = []
        for i in range(10):
            phone.append(str(random.randint(0, 9)))
        return "".join(phone)

    def rand_email(self):
        return "%s@%s.com" % (self.rand_str(), self.rand_str())

    def create_thread(self):
        while True:
            self.total_req += 1
            status = requests.post(url=url, data={
                'forename': self.rand_str(),
                'surname': self.rand_str(),
                'email': self.rand_email(),
                'phone': self.rand_phone(),
                'successUrl': 'https://platform-creativespace.com/tpao-land-twlfth/index.php',
                'clickid': 'f1637xsb7y9b99',
                'phonecc': '90',
                'country': 'tr'
            }).status_code
            print(f"posting request #{self.total_req} [status]: {status}")


if __name__ == "__main__":
    Main(50)
