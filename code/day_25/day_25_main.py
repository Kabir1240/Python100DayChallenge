import csv
import pandas
weather_data_path = "weather_data.csv"


def read_csv_file_hard_method():
    """
    reading data from a csv files, using the inbuilt functions
    :return: weather_data, stripped and organized
    """
    with open(weather_data_path, mode='r') as file:
        weather_data = file.readlines()

    stripped_data = []
    for line in weather_data:
        stripped_data.append(line.strip("\n").split(","))

    return stripped_data


def read_csv_file_easy_method():
    """
    reading data from csv using the csv module
    :return: weather_data, stripped and organized
    """
    with open(weather_data_path, mode='r') as file:
        weather_data = csv.reader(file)
        stripped_data = []
        for line in weather_data:
            stripped_data.append(line)
    return stripped_data


def extract_temperatures_as_int():
    """
    reading data from csv file, using csv file to extract a specific module. This is too much work for a single column.
    :return: temperatures, from weather_data file
    """
    with open(weather_data_path, mode='r') as file:
        weather_data = csv.reader(file)
        temperatures = []
        for line in weather_data:
            if line[1].lower() != "temp":
                temperatures.append(int(line[1]))
    return temperatures


def reading_csv_with_pandas():
    """
    easiest method to read data. Check pandas documentation.
    :return:
    """
    data = pandas.read_csv(weather_data_path)
    # this prints the data in a very organized and readable manner
    print(data)
    print()
    # this can be used to extract a single column, much much easier
    temp_data = data["temp"]
    print(temp_data)
    print()
    # we can convert dataframe (tables) to dictionaries
    print(data.to_dict())
    print()
    # we can convert Series data (columns) to lists
    print(temp_data.to_list())
    print()
    # another way to get a column
    print(data.temp)
    print()
    # extracting a column
    print(data[data.day == "Monday"])
    print()


def working_on_data_with_pandas():
    """
    exercise to see how easy it is to work on csv files using pandas
    :return:
    """
    data = pandas.read_csv(weather_data_path)
    temp_data = data["temp"].to_list()
    average_temp = sum(temp_data)/len(temp_data)
    print(average_temp)
    print()
    # even easier method
    print(data["temp"].mean())
    print()
    # finding the max
    print(data["temp"].max())
    print()
    # find row which had max temp
    print(data[data.temp == data.temp.max()])
    print()
    # find temperature on monday (in Fahrenheit)
    monday = data[data.day == "Monday"]
    print((monday.temp[0] * 9/5) + 32 )


def creating_data_with_pandas():
    """
    generating new DataFrames with pandas. Also, making new csv files.
    :return:
    """
    data = {
        "students": ["Amy", "James", "Angela"],
        "scores": [10, 15, 20],
    }
    print(pandas.DataFrame(data))
    print()
    # you can even create a new csv file
    path = "new_file.csv"
    dataframe = pandas.DataFrame(data)
    dataframe.to_csv(path)


def extracting_squirrel_data():
    input_path = "2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv"
    output_path = "number_of_squirrels.csv"
    data = pandas.read_csv(input_path)
    group = data.groupby("Primary Fur Color")

    counts = []
    fur_color = []
    for i in group:
        fur_color.append(i[0])
        counts.append(len(data[data["Primary Fur Color"] == i[0]]))
    new_dict = {"Fur Color": fur_color,
                "Count": counts,
            }
    new_data = pandas.DataFrame(new_dict)
    new_data.to_csv(output_path)


# data_1 = read_csv_file_hard_method()
# data_2 = read_csv_file_easy_method()
# data_3 = extract_temperatures_as_int()
# for i in data_3:
#     print(i)


# reading_csv_with_pandas()
# working_on_data_with_pandas()
# creating_data_with_pandas()


extracting_squirrel_data()