import pandas as pd
import matplotlib.pyplot as plt


def plot_iris_data(file_path):
    """Creates 3 plots of the iris data and saves them as pngs
    :param file_path: string

    :return: 3 png files
    """
    # ensure file path is a string
    if not isinstance(file_path, str):
        raise TypeError("file_path must be of type string")

    # read data in
    iris = pd.read_csv(file_path, header=None)
    iris.columns = [
        "sepal_width",
        "sepal_length",
        "petal_width",
        "petal_length",
        "species",
    ]

    # create box plot iris measurements
    measurement_names = ["sepal_length", "sepal_width", "petal_width", "petal_length"]
    plt.boxplot(iris[measurement_names], labels=measurement_names)
    plt.ylabel("cm")
    plt.savefig("iris_boxplot.png")
    plt.close()

    # create scatter plot of iris petal width by petal length
    for species_name in set(iris["species"]):
        iris_subset = iris[iris["species"] == species_name]
        plt.scatter(
            iris_subset["petal_width"],
            iris_subset["petal_length"],
            label=species_name,
            s=5,
        )
    plt.legend()
    plt.xlabel("Petal Width (cm)")
    plt.ylabel("Petal Length (cm)")
    plt.savefig("petal_width_v_length_scatter.png")
    plt.close()

    # recreate the two plots as subplots to merge them as one
    # create subplots
    fig, axes = plt.subplots(1, 2)
    fig.set_size_inches(10, 10)

    # create box plot iris measurements
    measurement_names = ["sepal_length", "sepal_width", "petal_width", "petal_length"]
    axes[0].boxplot(iris[measurement_names], labels=measurement_names)
    axes[0].set_ylabel("cm")

    # create scatter plot of iris petal width by petal length
    for species_name in set(iris["species"]):
        iris_subset = iris[iris["species"] == species_name]
        axes[1].scatter(
            iris_subset["petal_width"],
            iris_subset["petal_length"],
            label=species_name,
            s=5,
        )
    axes[1].legend()
    axes[1].set_xlabel("Petal Width (cm)")
    axes[1].set_ylabel("Petal Length (cm)")

    # remove top and right boarders
    # for each column
    for i in range(2):
        # choose to hide of show certain borders or "spines"
        axes[i].spines["top"].set_visible(False)
        axes[i].spines["right"].set_visible(False)
        axes[i].spines["bottom"].set_visible(True)
        axes[i].spines["left"].set_visible(True)

    # save multipanel figure
    fig.savefig("multi_panel_figure.png")

    return None
