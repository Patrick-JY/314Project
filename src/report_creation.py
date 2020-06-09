import pandas as pd
import matplotlib.pyplot as plt
from src.analyse_results import calculate_test1, calculate_test5, calculate_test4, calculate_test3, calculate_test2
from tqdm import tqdm
from src.utils import join_base_path
from tabulate import tabulate

def report_generation(df):
    print("Tests Running \n Test 1: Accuracy of the Un-Modified DataSet")
    test1_result = calculate_test1(df)
    test_pass = [False, False, False, False, False]
    print("Overall Accuracy: " + str(round(test1_result['overall_accuracy'], 2)) + "%")
    print("Positive Accuracy: " + str(round(test1_result['positive_accuracy'], 2)) + "%")
    print("Negative Accuracy: " + str(round(test1_result['negative_accuracy'], 2)) + "%")
    print("Neutral Accuracy: " + str(round(test1_result['neutral_accuracy'], 2)) + "%")

    if test1_result['overall_accuracy'] < 50:
        print("Test 1 Failed\n")
    else:
        print("Test 1 Passed\n")
        test_pass[0] = True

    print("Test 2: ")
    test2_result = calculate_test2(df)
    print("Comparing the capitalised dataset and the un-capitalised dataset: ")
    print("They are " + str(round(test2_result, 2)) + "% the same")

    if test2_result < 90:
        print("Test 2 Failed\n")
    else:
        print("Test 2 Passed\n")
        test_pass[1] = True

    print("Test 3: ")
    test3_result = calculate_test3(df)
    print("Comparing Mr2 to the original Dataset")
    print("Mr2 is " + str(round(test3_result, 2)) + "% similar to Mr0")
    if test3_result < 90:
        print("Test 3 Failed\n")
    else:
        print("Test 3 Passed\n")
        test_pass[2] = True

    print("Test 4: ")
    test4_result = calculate_test4(df)
    print("Comparing Mr3 to the original Dataset")
    print("Mr3 is " + str(round(test4_result, 2)) + "% similar to Mr0")
    if test4_result < 90:
        print("Test 4 Failed\n")
    else:
        print("Test 4 Passed\n")
        test_pass[3] = True

    print("Test 5: ")
    test5_result = calculate_test5(df)
    print("Comparing Mr4 within a threshold of the original Dataset")
    print("Mr4 is " + str(round(test5_result, 2)) + "% within a threshold similar to Mr0")
    if test5_result < 75:
        print("Test 5 failed\n")
    else:
        print("Test 5 passed\n")
        test_pass[4] = True

    print("Outputting Graphs:")
    print("Column Graph grouped by Word length")
    column_graph_word_length(df)

    print("Outputting Summary: \n")
    summary_table(test_pass)
    plt.show()

def column_graph_word_length(df):
    graph_df = prepare_word_length(df)

    graph_df.rename(columns={"cat1": "0-50", "cat2": "50-100", "cat3": "100-200", "cat4": "200-300", "cat5": ">300"}, inplace=True)

    ax = graph_df.plot(x="Mr#", y=["0-50", "50-100", "100-200", "200-300", ">300"], kind="bar")
    ax.set_xlabel("Metamorphic Relation")
    ax.set_ylabel("Average Compound Value")
    ax.legend(title = "Word Length")
    plt.savefig(join_base_path("output/column_graph.png"))
    plt.draw()


def prepare_word_length(df):
    output_df = pd.DataFrame()
    calculate_df = pd.DataFrame()
    x = 0
    # this monster operation sorts everything into a new dataframe and sorts each comp value into its category
    for index, row in tqdm(df.iterrows(),total=len(df.index), unit="rows"):
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

    for index, row in tqdm(calculate_df.iterrows(),total=len(calculate_df.index), unit="rows"):
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


def summary_table(test_pass):
    df = pd.DataFrame()
    fig, ax = plt.subplots()

    # hide axes
    fig.patch.set_visible(False)
    ax.axis('off')
    ax.axis('tight')

    df.insert(0, "Test Numbers", [1, 2, 3, 4, 5])
    df.insert(1, "Passed", test_pass)
    ax.table(cellText=df.values, colLabels=df.columns, loc='center')
    fig.tight_layout()
    plt.savefig(join_base_path("output/summary_table.png"))
    print(tabulate(df, tablefmt="github", showindex=False, headers=["Test Numbers", "Passed"]))
    print()
    plt.draw()

