import time
import random
import pandas as pd
import matplotlib.pyplot as plt

print("Patient Temperature Monitoring System\n")

# Empty lists to store data
times = []
temps = []
statuses = []

try:
    for i in range(10):  # take 10 readings for demo
        temp = round(random.uniform(95, 104), 1)
        now = time.strftime("%H:%M:%S")

        if temp < 97:
            status = "Low"
        elif temp > 99:
            status = "Fever"
        else:
            status = "Normal"

        print(f"{now} | Temperature: {temp}°F | Status: {status}")

        # store data
        times.append(now)
        temps.append(temp)
        statuses.append(status)

        time.sleep(2)

except KeyboardInterrupt:
    print("\nMonitoring stopped by user.\n")

# Save to CSV
data = pd.DataFrame({"Time": times, "Temperature": temps, "Status": statuses})
data.to_csv("temperature_log.csv", index=False)
print("\nAll readings saved to temperature_log.csv")

# Plot temperature graph
plt.plot(times, temps, marker='o')
plt.title("Patient Temperature Trend")
plt.xlabel("Time")
plt.ylabel("Temperature (°F)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
