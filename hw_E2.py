pareto=np.random.pareto(5,1000)
def histogram(ax, data, bins, x_label="", y_label="", title=""):
  ax.hist(data, bins=bins)
  ax.set_xlabel(x_label)
  ax.set_ylabel(y_label)
  ax.set_title(title)
  
fig, ax = plt.subplots()
histogram(ax, pareto, 100, x_label="Value", y_label="Count", title="Pareto Distribution")
