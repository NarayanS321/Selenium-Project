class Robot:

    def __init__(self, name, make, model, color, body_type, langague, version):
        self.name = name
        self.make = make
        self.model = model
        self.color = color
        self.body_type = body_type
        self.language = langague
        self.version = version

    def greet_user(self):
        # user_inp = input("please input your name : ")
        print(f"Hi, I am a robot and my name is {self.name}. How can I help you?")
        # return user_inp

    def whats_your_version(self):
        print(f"Hi, my version is {self.version}.")


class AirServRob(Robot):

    def __init__(self, name, make, model, color, body_type, langague, version, airline_name):
        super().__init__(name, make, model, color, body_type, langague, version)
        self.airline_serving = airline_name

    def book_air_ticket(self):
        print(f"{self.name} robot booked your flight in {self.airline_serving} airline for tomorrow.")


class MedSrvRbt(Robot):

    def book_doctor_appiontment(self):
        print(f"Robot '{self.name}', booked your appointment with doctor Reddy for tomorrow.")
