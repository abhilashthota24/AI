import psutil

if hasattr(psutil, "sensors_temperatures"):
    temperatures = psutil.sensors_temperatures()
    if temperatures:
        for sensor, entries in temperatures.items():
            print(f"Sensor: {sensor}")
            for entry in entries:
                print(f"  {entry.label or 'Temperature'}: {entry.current}°C")
