import time
class petSensor:
    def pet_sensor(last_feed_time):
     current_time = time.time()
    
     if current_time - last_feed_time >= 6 * 3600:  
         return "provide food to the pet"
     else:
        return "no need to feed now"

last_feed_time = time.time() - 7 * 3600
last_feed_time_hours = (time.time()-last_feed_time) / 3600
print(f"when did the pet got food last time is:  {last_feed_time_hours:.2f} hours ago:")  
result = petSensor.pet_sensor(last_feed_time)
print("The sensor performs:", result)
