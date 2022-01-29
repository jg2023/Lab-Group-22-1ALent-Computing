import matplotlib.pyplot as plt

def plot_water_levels(station,dates,levels):
    """This procedure plots water level against time for a certain station"""
    plt.plot(dates,levels , label = 'Water Level Against Time')
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)
    plt.legend()
    plt.show
