import threading
import time

receptionest = threading.Semaphore(5)


def enter_examinationroom(n):
    print(f"Patient {n} is wating for his turn ")
    receptionest.acquire()
    print(f"Patient {n} is in examinationroom ")
    time.sleep(2)
    print(f"Patient {n} is out of examinationroom ")
    receptionest.release()


Patients = []
for i in range(10):
    Patient = threading.Thread(target=enter_examinationroom, args=(i,))
    Patients.append(Patient)
    Patient.start()
