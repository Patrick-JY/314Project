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
    df["ReviewTextLength"] = df["ReviewText"].apply(lambda row: len(row.split()))
    bins = pd.cut(df["ReviewTextLength"], [0, 50, 100, 200, 300, float("inf")])
    grouped_df = df.groupby(bins)
    columns = [str(name).replace("300", ">300").replace(".0", "").replace(", ", "-").replace("-inf", "").replace("(",
                                                                                                                 "").replace(
        "[", "").replace("]", "").replace(")", "").replace(")", "").replace(" ", "").replace("->", "-") for name, group
               in grouped_df]
    output_df = pd.DataFrame(columns=columns, index=["Mr0", "Mr1_cap", "Mr1_uncap", "Mr2", "Mr3", "Mr4"])
    for name, group in grouped_df:
        new_df = pd.DataFrame()
        new_df["Mr0_Compound"] = group["Mr0"].apply(lambda x: x["compound"])
        new_df["Mr1_cap_Compound"] = group["Mr1"].apply(lambda x: x.get('capitalised')["compound"])
        new_df["Mr1_uncap_Compound"] = group["Mr1"].apply(lambda x: x.get('uncapitalised')["compound"])
        new_df["Mr2_Compound"] = group["Mr2"].apply(lambda x: x["compound"])
        new_df["Mr3_Compound"] = group["Mr3"].apply(lambda x: x["compound"])
        new_df["Mr4_Compound"] = group["Mr4"].apply(lambda x: x["compound"])
        mean_df = new_df.agg(["mean"])
        for col in mean_df.columns:
            output_df.loc[col.replace("_Compound", ""), str(name).replace("300", ">300").replace(".0", "").replace(", ",
                                                                                                                   "-").replace(
                "-inf", "").replace("(", "").replace("[", "").replace("]", "").replace(")", "").replace(")",
                                                                                                        "").replace(" ",
                                                                                                                    "").replace(
                "->", "-")] = mean_df[col].iloc[0]
    output_df["Mr#"] = output_df.index
    ax = output_df.plot(x="Mr#", y=columns, kind="bar")
    ax.set_xlabel("Metamorphic Relation")
    ax.set_ylabel("Average Compound Value")
    ax.legend(title="Word Length")
    plt.savefig(join_base_path("column_graph.png"))
    plt.draw()


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
    plt.savefig(join_base_path("summary_table.png"))
    print(tabulate(df, tablefmt="github", showindex=False, headers=["Test Numbers", "Passed"]))
    print()
    plt.draw()

