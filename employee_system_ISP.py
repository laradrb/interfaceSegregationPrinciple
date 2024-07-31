class Worker:
    def work(self):
        raise NotImplementedError

class Rest:
    def take_break(self):
        raise NotImplementedError

class MeetingAttender:
    def attend_meeting(self):
        raise NotImplementedError

class Developer(Worker, MeetingAttender):
    def work(self):
        print("Developer is writing code.")

    def attend_meeting(self):
        print("Developer is attending a meeting.")

class MaintenanceWorker(Worker, Rest):
    def work(self):
        print("Maintenance worker is fixing things.")

    def take_break(self):
        print("Maintenance worker is taking a break.")

def main():
    developer = Developer()
    developer.work()
    developer.attend_meeting()

    maintenance_worker = MaintenanceWorker()
    maintenance_worker.work()
    maintenance_worker.take_break()

if __name__ == "__main__":
    main()