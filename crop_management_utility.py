def calculate_utility(soil_moisture, temperature, crop_health, market_demand):
    utility = (soil_moisture * 0.3) + (temperature * 0.2) + (crop_health * 0.4) + (market_demand * 0.1)
    return utility

def utility_action(utility):
    if utility > 80:
        return "Harvest the crop soon."
    elif utility > 50:
        return "Monitor and maintain the crop."
    else:
        return "Improve soil and crop conditions."


soil_moisture = 75
temperature = 60
crop_health = 85
market_demand = 70

utility_score = calculate_utility(soil_moisture, temperature, crop_health, market_demand)
action = utility_action(utility_score)

print("Utility Score:", utility_score)
print("Recommended Action:", action)
