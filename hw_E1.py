poisson=np.random.poisson(1,1000)
def histogram(ax, data, bins, x_label = "", y_label = "", title = ""):
    ax.hist(data, bins = bins)
    ax.set_ylabel(y_label)
    ax.set_xlabel(x_label)
    ax.set_title(title)
    
fig, ax = plt.subplots()
fig.set_size_inches (10,5)
histogram (ax, poisson, 20, x_label="Value", y_label="Count", title="Poisson distribution")
