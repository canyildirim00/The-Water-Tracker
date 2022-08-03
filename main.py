import random
import time
from plyer import notification

message = ("Drinking Water Helps to Maintain the Balance of Body Fluids.",
           "Drinking Water Helps to Maximize Physical Performance",
           "Drinking Water Significantly Affects Energy Levels and Brain Function",
           "Drinking Water May Help Prevent and Treat Headaches",
           "Drinking Water May Help Relieve Constipation",
           "Drinking Water May Help Treat Kidney Stones",
           "Drinking Water Can Aid Weight Loss",
           "Drinking Water Delivers Oxygen Throughout the Body",
           "Drinking Water Boosts Skin Health and Beauty",
           )

while True:
    notification.notify(
            title = "Time to Drink Water Now!",
            message = random.choice(message),
            timeout= 10
            )
    time.sleep(60*60)



