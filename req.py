import requests
import threading

url = ""

data = {
    "cc_number": "4111111111111111",
    "cc_exp": "12/2020",
    "cc_cvv": "123",
    "cc_name": "John Doe",
}


def do_request():
    while True:
        reponse = requests.post(url, data=data).text


threads = []

for i in range(50):
    t = threading.Thread(target=do_request)
    t.daemon = True
    threads.append(t)

for i in range(50):
    threads[i].start()

for i in range(50):
    threads[i].join()
