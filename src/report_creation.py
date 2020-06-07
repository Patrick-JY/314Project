import pandas as pd
import matplotlib.pyplot as plt


def report_generation(df):
    # Create new data from input argument
    df = pd.DataFrame()

    # Create new headers for analysis of data
    df.columns = ['Correctness(%)', 'Positive/Negative', 'Number of Reviews', 'Score Ratio']

    # Test print
    print(df.head(10))


def column_graph_word_length(df):
    graph_df = prepare_word_length(df)

    graph_df.rename(columns={"cat1": "0-50", "cat2": "50-100", "cat3": "100-200", "cat4": "200-300", "cat5": ">300"}, inplace=True)
    print(graph_df)
    graph_df.plot(x="Mr#", y=["0-50", "50-100", "100-200", "200-300", ">300"], kind="bar")

    plt.show()


def prepare_word_length(df):
    output_df = pd.DataFrame()
    calculate_df = pd.DataFrame()
    x = 0
    # this monster operation sorts everything into a new dataframe and sorts each comp value into its category
    for index, row in df.iterrows():
        calculate_df.at[x, 'Mr#'] = "Mr0"
        calculate_df.at[x + 1, "Mr#"] = "Mr1cap"
        calculate_df.at[x + 2, "Mr#"] = "Mr2"
        calculate_df.at[x + 3, "Mr#"] = "Mr3"
        calculate_df.at[x + 4, "Mr#"] = "Mr4"
        calculate_df.at[x + 5, "Mr#"] = "Mr1uncap"
        calculate_df.at[x, "comp"] = row["Mr0"].get("compound")
        calculate_df.at[x + 1, "comp"] = row["Mr1"].get('capitalised').get('compound')
        calculate_df.at[x + 2, "comp"] = row["Mr2"].get("compound")
        calculate_df.at[x + 3, "comp"] = row["Mr3"].get("compound")
        calculate_df.at[x + 4, "comp"] = row["Mr4"].get("compound")
        calculate_df.at[x + 5, "comp"] = row["Mr1"].get('uncapitalised').get("compound")
        if len(row['ReviewText'].split()) < 50:
            calculate_df.at[x, "cat"] = "cat1"
            calculate_df.at[x+1, "cat"] = "cat1"
            calculate_df.at[x+2, "cat"] = "cat1"
            calculate_df.at[x+3, "cat"] = "cat1"
            calculate_df.at[x+4, "cat"] = "cat1"
            calculate_df.at[x+5, "cat"] = "cat1"

        elif len(row['ReviewText'].split()) < 100:
            calculate_df.at[x, "cat"] = "cat2"
            calculate_df.at[x + 1, "cat"] = "cat2"
            calculate_df.at[x + 2, "cat"] = "cat2"
            calculate_df.at[x + 3, "cat"] = "cat2"
            calculate_df.at[x + 4, "cat"] = "cat2"
            calculate_df.at[x + 5, "cat"] = "cat2"

        elif len(row['ReviewText'].split()) < 200:
            calculate_df.at[x, "cat"] = "cat3"
            calculate_df.at[x + 1, "cat"] = "cat3"
            calculate_df.at[x + 2, "cat"] = "cat3"
            calculate_df.at[x + 3, "cat"] = "cat3"
            calculate_df.at[x + 4, "cat"] = "cat3"
            calculate_df.at[x + 5, "cat"] = "cat3"

        elif len(row['ReviewText'].split()) < 300:
            calculate_df.at[x, "cat"] = "cat4"
            calculate_df.at[x + 1, "cat"] = "cat4"
            calculate_df.at[x + 2, "cat"] = "cat4"
            calculate_df.at[x + 3, "cat"] = "cat4"
            calculate_df.at[x + 4, "cat"] = "cat4"
            calculate_df.at[x + 5, "cat"] = "cat4"

        elif len(row['ReviewText'].split()) >= 300:
            calculate_df.at[x, "cat"] = "cat5"
            calculate_df.at[x + 1, "cat"] = "cat5"
            calculate_df.at[x + 2, "cat"] = "cat5"
            calculate_df.at[x + 3, "cat"] = "cat5"
            calculate_df.at[x + 4, "cat"] = "cat5"
            calculate_df.at[x + 5, "cat"] = "cat5"
        x = x + 6

    output_df.at[0, "Mr#"] = "Mr0"
    output_df.at[1, "Mr#"] = "Mr1uncap"
    output_df.at[2, "Mr#"] = "Mr1cap"
    output_df.at[3, "Mr#"] = "Mr2"
    output_df.at[4, "Mr#"] = "Mr3"
    output_df.at[5, "Mr#"] = "Mr4"

    output_df.insert(1, "cat1", [0.0, 0.0, 0.0, 0.0, 0.0, 0.0], True)
    output_df.insert(2, "cat2", [0.0, 0.0, 0.0, 0.0, 0.0, 0.0], True)
    output_df.insert(3, "cat3", [0.0, 0.0, 0.0, 0.0, 0.0, 0.0], True)
    output_df.insert(4, "cat4", [0.0, 0.0, 0.0, 0.0, 0.0, 0.0], True)
    output_df.insert(5, "cat5", [0.0, 0.0, 0.0, 0.0, 0.0, 0.0], True)

    rowcount = [0, 0, 0, 0, 0]

    for index, row in calculate_df.iterrows():
        y = row["Mr#"][-1]

        if y == "p":
            y = row["Mr#"][-5]

            if y == "u":
                y = "1"
            else:
                y = "2"
        elif int(y) > 0:
            y = int(y)+1

        # counts the total comp value per catergory
        output_df.at[int(y), row["cat"]] += row["comp"]
        rowcount[int(row["cat"][-1])-1] += 1

    # Gets the average rowcount is amount of times cat occurs in the calcuate df and its divided by 6 because that is
    # how many times that occurs
    output_df["cat1"] = output_df["cat1"].div(rowcount[0] / 6)
    output_df["cat2"] = output_df["cat2"].div(rowcount[1] / 6)
    output_df["cat3"] = output_df["cat3"].div(rowcount[2] / 6)
    output_df["cat4"] = output_df["cat4"].div(rowcount[3] / 6)
    output_df["cat5"] = output_df["cat5"].div(rowcount[4] / 6)



    return output_df

