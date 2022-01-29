import matplotlib.pyplot as plt

def plot_water_levels(station,dates,levels):
    """This procedure plots water level against time for a certain station"""
    plt.plot(dates,levels , label = 'Water Level Against Time')
    plt.axhline(station.typical_range[0],color = 'g',label = 'Low typical range boundary')
    plt.axhline(station.typical_range[1],color = 'r',label = 'High typical range boundary')
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=11)
    plt.title(station.name)
    plt.legend()
    plt.show()
