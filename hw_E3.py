boston = datasets.load_boston()
boston_df = pd.DataFrame(boston['data'], columns=boston['feature_names'])
boston_df['PRICE'] = boston.target

def scatter(ax, x_data, y_data, x_label="", y_label="", color=""):
  ax.scatter(x_data, y_data, s=20, color=color)
  ax.set_xlabel(x_label)
  ax.set_ylabel(y_label)
  ax.grid()
fig, ax = plt.subplots(1,2)
scatter(ax[0], boston_df["PRICE"], boston_df["NOX"], x_label="Price", y_label="Nitric oxides concentration (parts per 10 million)", color="blue")
scatter(ax[1], boston_df["PRICE"], boston_df["PTRATIO"], x_label="Price", y_label="Pupil-teacher ratio", color="red")
fig.suptitle("You think this good neighbourhood?",fontsize=18)
