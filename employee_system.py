class Employee:
    def work(self):
        raise NotImplementedError

    def take_break(self):
        raise NotImplementedError

    def attend_meeting(self):
        raise NotImplementedError

    """Vamos a dividir la clase Employee en varias clases más pequeñas y específicas"""

class Worker:
    def work(self):
        raise NotImplementedError

class Rest:
    def take_break(self):
        raise NotImplementedError

class MeetingAttender:
    def attend_meeting(self):
        raise NotImplementedError

    """Implementaciones para un desarrollador de software y un trabajador de mantenimiento"""

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