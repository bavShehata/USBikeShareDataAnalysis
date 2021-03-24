import pandas as pd 
import time

# Set the precision of our dataframes to one decimal place.
pd.set_option('precision', 1)

# City names corresponding to files
df_dic = {'chicago': 'chicago.csv','washington': 'washington.csv','new york': 'new_york_city.csv'}

def mostFrequent(df):
    """Show the most frequent hour,day, or month for starting to rent a bike
        arguments:
        df -- the DataFrame 
    """
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    # find the most common hour (from 0 to 23)
    popHour = df['hour'].mode()[0]
    # extract day from the Start Time column to create an day column
    df['day'] = df['Start Time'].dt.day
    # find the most common day (from 1 to 31)
    popDay = df['day'].mode()[0]
    # extract month from the Start Time column to create an month column
    df['month'] = df['Start Time'].dt.month
    # find the most common month (from 1 to 12)
    popMonth = df['month'].mode()[0]
    return (popHour, popDay, popMonth)

def load_data(city, month = -1, day = -1):
    """ load and filter dataset function

    keyword arguments:
    city -- the city to analyze (chicago, washington, new york)
    month -- (1:12, default is -1)
    day -- (0:7, default is -1)
    """
    print("\n\nGetting your statistics...\n\n")
    beginning = time.time()
    # Load the dataset for the specified city. 
    df = pd.read_csv(df_dic[city])

    # Create month and day_of_week columns. 
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.strftime("%w").astype('int64')
    if (month >= 0) & (day >= 0):
        # Filter by both
        df = df.loc[(df['month'] == month) & (df['day_of_week'] == day)]
    elif month >= 0:
        # Filter by month.
        df = df.loc[df['month'] == month]
    elif day >= 0:
        # Filter by day of week
        df = df.loc[df['day_of_week'] == day]
    end = time.time()
    print("\n-----------------General Overview-----------------")

            
    userTypes = df['User Type'].value_counts().to_string()
    genderCount = df['Gender'].value_counts().to_string()
    durationMean = df['Trip Duration'].mean()
    durationMax = df['Trip Duration'].max()
    durationMin = df['Trip Duration'].min()
    popStart = df['Start Station'].mode()[0]
    popEnd = df['End Station'].mode()[0]
    popStartEnd = (df['Start Station'] + " AND " + df['End Station']).mode()[0]
    yearMean = int(df['Birth Year'].mean())
    yearMode = int(df['Birth Year'].mode())
    yearMax = int(df['Birth Year'].max())
    yearMin = int(df['Birth Year'].min())
    popDayName = df['day_of_week'].mode()[0]
    popHour,popDay,popMonth = mostFrequent(df)

    print("\n-----------------User Count-----------------")
    print("-Count of users depending on their type \n", userTypes)
    print("-Count of users depending on their gender \n", genderCount)

    print("\n-----------------Duration Statistics (in minutes)-----------------")
    print("-Max duration: ", int(durationMax/60))
    print("-Min duration: ", int(durationMin/60))
    print("-Mean duration: ", int(durationMean/60))
    
    print("\n-----------------Station Statistics-----------------")
    print("-Most popular start station: ", popStart)
    print("-Most popular end station: ", popEnd)
    print("-Most popular start-end station combination: ", popStartEnd)

    print("\n-----------------Year Statistics-----------------")
    print("-Youngest users are born in year: ", yearMax)
    print("-Oldest users are born in year: ", yearMin)
    print("-Average number of users are born in year: ", yearMean)
    print("-Most users are born in year: ", yearMode)

    print("\n-----------------Start Statistics-----------------")
    print('-Most Frequent Start Hour (from 0 to 23)\n', popHour)
    print('-Most Frequent Start Day (from 1 to 31)\n', popDay)
    print('-Most Frequent Start Day (from 0 to 6: Sun to Sat)\n', popDayName)
    print('-Most Frequent Start Month (from 1 to 12)\n', popMonth)


    print("\n\nThis operation took {} seconds\n".format(end-beginning))
    print("\n-----------------Raw data-----------------")
    more = 1
    start = 0
    maxCount =  df.count().iloc[0]
    while more == 1:
        print("\n{}\n".format(df.iloc[start:start+5]))
        start += 5
        if start + 5 > maxCount:
            print("You have reached the end of the data\n")
            break
        while True:
            more = int(input("There are {} more records, would you like to show 5 more ?\n0-1 for no-yes: ".format(maxCount-start)))
            if (more != 0) and (more != 1):
                print("\n-----Please make sure you enter either 0 or 1-----")
            else:
                break
        
    
    



print("-------------------------Welcome to bike share script-------------------------\n\n")
print("This interactive script will take take you through a process to view the data regarding Motivate bike share system in the first 6 months of 2017")
again = 1

while again == 1:
    while True:
        city = input("\n\nPlease choose a city out of chicago, washington, and new york: ").lower()
        if (city not in df_dic):
            print("\n-----Please make sure you typed the city name correctly-----")
        else:
            break
    while True:
        month = int(input("What month are you looking for?\n1-6 for Jan-Jun. for all months, choose -1: "))
        if  (month > 6) or ((month < 1) and (month != -1)):
            print("\n-----Please make sure you choose a month between 1 and 6, or -1-----")
        else:
            break
    while True:
        day = int(input("What day are you looking for?\n0-6 for Sun-Sat. for all days, choose -1: "))
        if  (day > 6) or ((day < 0) and (day != -1)):
            print("\n-----Please make sure you choose a day between 0 and 6 or -1-----")
        else:
            break
    load_data(city, month, day)
    while True:
        again = int(input("Would you like to choose different set of data?\n0-1 for no-yes: "))
        if (again != 0) and (again != 1):
            print("\n-----Please make sure you enter either 0 or 1-----")
        else:
            break
print("\n\nClosing script...\n")