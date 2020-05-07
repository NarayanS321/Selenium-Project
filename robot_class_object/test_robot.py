"""
from robot_class_object.med_robot import MedSrvRbt
from robot_class_object.air_robot import AirServRob
"""
from robot_class_object.robot_for_medair import AirServRob, MedSrvRbt

robo_hina = MedSrvRbt("Hina", "Hundai", "MD001", "silver", "carbon-fiber", "english", "2.0")
robo_hina.greet_user()
robo_hina.book_doctor_appiontment()

print()
air_bot_01 = AirServRob("Airbot", "Hundai", "AB525", "silver", "carbon-fiber", "english", "2.0", "AirMexico")
air_bot_01.greet_user()
air_bot_01.whats_your_version()
air_bot_01.book_air_ticket()







"""
msr.book_doctor_appiontment()


asr = AirServRob
asr.book_air_ticket()

"""


