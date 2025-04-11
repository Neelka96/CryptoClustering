import pandas as pd
import hvplot.pandas
from sklearn.cluster import KMeans
from collections.abc import Sequence

def make_scaled_df(df: pd.DataFrame, cols: Sequence, indx: Sequence) -> pd.DataFrame:
    # Create a new DataFrame with the PCA data.
    new_df = pd.DataFrame(df, columns = cols)

    # Copy the crypto names from the original scaled DataFrame
    new_df['coin_id'] = indx

    # Set the coin_id column as index
    new_df.set_index('coin_id', drop = True, inplace = True)

    # Display the scaled PCA DataFrame
    return new_df


def elbow_curve(end_range: int, df: pd.DataFrame):
    # Create a list with the number of k-values from 1 to 11
    k = list(range(1, end_range))

    # Create an empty list to store the inertia values
    inertia = []

    # Create a for loop to compute the inertia with each possible value of k
    # Inside the loop:
    # 1. Create a KMeans model using the loop counter for the n_clusters
    # 2. Fit the model to the data using the dataframe
    # 3. Append the model.inertia_ to the inertia list
    for i in k:
        k_model = KMeans(n_clusters = i, random_state = 1)
        k_model.fit(df)
        inertia.append(k_model.inertia_)

    # Create a DataFrame with the data to plot the Elbow curve
    elbow_df = pd.DataFrame({'k': k, 'inertia': inertia})

    # Plot a line chart with all the inertia values computed with
    # the different values of k to visually identify the optimal value for k.
    return elbow_df.hvplot.line(
        x = 'k',
        y = 'inertia',
        title = 'Elbow Curve',
        xticks = k
    )


def modeling(clusters: int, df: pd.DataFrame):
    # Initialize the K-Means model using the best value for k
    model = KMeans(n_clusters = clusters, random_state = 1)

    # Fit and predict the KMeans model using the dataframe
    clusters = model.fit_predict(df)

    # Print the resulting array of cluster values.
    print(f'Clusters: \n{clusters}')

    # Create a copy of the scaled DataFrame
    prediction_df = df.copy()

    # Add a new column to the copy of the scaled DataFrame with the predicted clusters
    prediction_df['CryptoCluster'] = clusters

    # Create a scatter plot using hvPlot by setting
    # `x="price_change_percentage_24h"` and `y="price_change_percentage_7d"`.
    # Color the graph points with the labels found using K-Means and
    # add the crypto name in the `hover_cols` parameter to identify
    # the cryptocurrency represented by each data point.
    plot = prediction_df.hvplot.scatter(
        x = prediction_df.columns[0],
        y = prediction_df.columns[1],
        by = 'CryptoCluster',
        title = 'Scaled CryptoClusters',
        hover_cols = ['coin_id']
    )
    return prediction_df, plot