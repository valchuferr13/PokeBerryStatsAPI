import matplotlib.pyplot as plt


def create_histogram(berry_data):
    growth_times = list(berry_data.values())
    plt.figure(figsize=(10, 6))
    plt.hist(growth_times, bins=range(min(growth_times),
             max(growth_times) + 1, 1), alpha=0.7, color='seagreen')

    plt.title('Frequency of Growth Times for Berries', fontsize=14)
    plt.xlabel('Growth Time', fontsize=12)
    plt.ylabel('Frequency', fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    plt.savefig('static/berry_growth_histogram.png', transparent=True)
