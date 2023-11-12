import pandas as pd

# change local path to work on
LOCAL_PATH = "C:\\Users\\bbmcm\\Downloads"
NUMERIC_ROWS = ["GPA", "InState", "OutOfState"]


# reads in the main dataframe for filename passed in
def read_main_data_frame(data_dir):
    df = pd.read_csv(LOCAL_PATH + data_dir)
    df = df.drop("Year", axis=1)
    return df


# extracts info from main frame
def extract_numeric_data(dataframe):
    df_numbers = dataframe[dataframe["Stat"].isin(NUMERIC_ROWS)]
    df_numbers.set_index(["Stat"], inplace=True)
    df_numbers.apply(pd.to_numeric)
    print(df_numbers)
    # --------------
    # THIS IS BROKEN
    # ______________
    # for row in NUMERIC_ROWS:
    #     df_numbers[row] = df_numbers[row].astype(int)
    # print(df_numbers.mean(axis=1))

    return df_numbers


if __name__ == '__main__':
    infile_name = "\\test_stats.csv"
    df_main = read_main_data_frame(infile_name)
    print(df_main)
    # df_main.set_index(["Stat"], inplace=True)
    df_numeric = extract_numeric_data(df_main)





