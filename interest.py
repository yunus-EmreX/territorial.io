import matplotlib.pyplot as plt
import numpy as np

def calculate_interest_rate(x):
    if x <= 0:
        return 1
    
    interest_rate = 1 + (4 * x) ** 0.5
    
    if x >= 100 and interest_rate > 200:
        interest_rate = max(200 - ((x - 100) * (interest_rate - 1)) / (200 - interest_rate), 0)
    
    return round(interest_rate,2)

# Veri noktalarını oluşturma
x_values = np.arange(0,201,10)
y_values = [calculate_interest_rate(x) for x in x_values]

# Grafik çizdirme
plt.plot(x_values, y_values)
plt.xlabel("Bölge Sayısı")
plt.ylabel("Faiz Oranı")
plt.title("Territorial.io Faiz Oranı")
plt.grid(True)
plt.show()