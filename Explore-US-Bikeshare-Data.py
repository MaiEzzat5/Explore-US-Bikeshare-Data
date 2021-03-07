import time
import pandas as pd
import numpy as np

CITY_DATA = { "Chicago": "D:/Python/chicago.csv",
              "New York City": "D:/Python/new_york_city.csv",
              "Washington": "D:/Python/washington.csv" }

cities = ["Chicago", "New York City", "Washington"]
months = ["January", "February", "March", "April", "May", "June", "All"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    """Loop for asking the user the name of the city, and if he wants to filter the data by month or day or by both(month then day)"""
    while True :
        try :
            city = input("\nWould you like to see data for Chicago, New York City, or Washington?\n").title()
            if city in cities :
                break           
        except KeyboardInterrupt :
            print("\nNO Input Taken!")
        else :   
            print("\nInvalid Input!\nPlease try one of the following cities\nChicago, New York City and Washington.\n")
    
    while True :
        try :
            month = input("\nWhich month - January, February, March, April, May, June? or All if you want to see all the data\n").title()
            if month in months :
                break
        except KeyboardInterrupt :
            print("\nNO Input Taken!\n")
        else :   
            print("\nInvalid Input!\nPlease try one of the following monthes\nJanuary, February, March, April, May, June or All\n")    
    
    while True :
        try :
            day = input("\nWhich day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday? or All if you want to see all the data\n").title()
            if day in days :
                break
        except KeyboardInterrupt :
            print("\nNO Input Taken!\n")
        else :   
            print("\nInvalid Input!\nPlease try one of the following days\nMonday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or All\n")       
                                                             
    print("-"*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    """Load data file into a dataframe"""
    df = pd.read_csv(CITY_DATA[city])
   
    """Convert the Start Time column to datetime"""
    df["Start Time"] = pd.to_datetime(df["Start Time"])

    """Extract month and day of week from Start Time to create new columns"""
    df["Month"] = df["Start Time"].dt.month
    df["Day of Week"] = df["Start Time"].dt.weekday_name
    
    """Filter by month"""
    if month != "All":        
        months = ["January", "February", "March", "April", "May", "June"]
        month = months.index(month) + 1
        df = df[df["Month"] == month]      
        
    """Filter by the day of the week"""
    if day != "All":       
        df = df[df["Day of Week"] == day.title()]
  
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    """Display the most common month"""
    most_common_month = df["Month"].mode()[0]
    print("Most Common Month: {}".format(most_common_month))

    """Display the most common day of week"""
    most_common_day = df["Day of Week"].mode()[0]
    print("Most Common Day: {}".format(most_common_day))
    
    """Display the most common start hour"""
    df["Hour"] = df["Start Time"].dt.hour
    most_common_hour = df["Hour"].mode()[0]
    print("Most Common Hour: {}".format(most_common_hour))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-"*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print("\nCalculating The Most Popular Stations and Trip...\n")
    start_time = time.time()

    """Display most commonly used start station"""
    most_common_start_station = df["Start Station"].mode()[0]
    print("Most Common Start Station: {}".format(most_common_start_station))
    
    """Display most commonly used end station"""
    most_common_end_station = df["End Station"].mode()[0]
    print("Most Common End Station: {}".format(most_common_end_station))

    """Display most frequent combination of start station and end station trip"""
    df["Start Station and End Station"] = df["Start Station"] + "," + df["End Station"]
    most_common_start_end_station = df["Start Station and End Station"].mode()[0]
    print("Most Common Start & End Station: {}".format(most_common_start_end_station))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-"*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print("\nCalculating Trip Duration...\n")
    start_time = time.time()

    """Display total travel time"""
    total_travel_time = df["Trip Duration"].sum()
    print("Total Travel Time: {}".format(total_travel_time))

    """Display mean travel time"""
    mean_travel_time = df["Trip Duration"].mean()
    print("Mean Travel Time: {}".format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print("\nCalculating The Most Popular Stations and Trip...\n")
    start_time = time.time()

    """Display most commonly used start station"""
    most_common_start_station = df["Start Station"].mode()[0]
    print("Most Common Start Station: {}".format(most_common_start_station))
    
    """Display most commonly used end station"""
    most_common_end_station = df["End Station"].mode()[0]
    print("Most Common End Station: {}".format(most_common_end_station))

    """Display most frequent combination of start station and end station trip"""
    df["Start Station and End Station"] = df["Start Station"] + "," + df["End Station"]
    most_common_start_end_station = df["Start Station and End Station"].mode()[0]
    print("Most Common Start & End Station: {}".format(most_common_start_end_station))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-"*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print("\nCalculating Trip Duration...\n")
    start_time = time.time()

    """Display total travel time"""
    total_travel_time = df["Trip Duration"].sum()
    print("Total Travel Time: {}".format(total_travel_time))

    """Display mean travel time"""
    mean_travel_time = df["Trip Duration"].mean()
    print("Mean Travel Time: {}".format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print("\nCalculating User Stats...\n")
    start_time = time.time()

    """Display counts of user types"""
    counts_of_user_types = df["User Type"].value_counts()
    print("Counts of User Types: {}".format(counts_of_user_types))

    """Display counts of gender"""      
    for city in cities :
        if city == "Chicago" or city == "New York City" :
            counts_of_gender = df["Gender"].value_counts()
            print("Counts of Gender: {}".format(counts_of_gender))
    
    """Display earliest, most recent, and most common year of birth""" 
    for city in cities :
        if city == "Chicago" or city == "New York City" :
            earliest_year = df["Birth Year"].min()
            print("Earliest Year: {}".format(earliest_year))
            most_recent_year = df["Birth Year"].max()
            print("Most Recent Year: {}".format(most_recent_year))
            most_common_year = df["Birth Year"].mode()[0]
            print("Most Common Year: {}".format(most_common_year))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-"*40)

def display_raw_data(df):
    """Displays raw data for the user."""
    
    """Loop to Ask the user if he wants to see raw data, and display about 5 rows each time he/ she answers yes"""
    n = 0
    display_raw_data = input("\nDo you want to check the raw data available? Please type yes or no.\n")
    for city in cities :
        if display_raw_data == "yes"  :   
           for n in range (0,2000,5):
             n+=5
             df = pd.read_csv(CITY_DATA[city]).head(n)
             print(df)
             try :
                display_more_data = input("\nDo you want to check more raw data? Please type yes or no.\n")
                if display_more_data  == "yes" : 
                    print(df)
                if display_more_data  == "no" :   
                     break               
             except KeyboardInterrupt :
                print("\nNO Input Taken!\n")             
        if display_raw_data == "no" :
            break
        print("\nThank You\n")
    
    return df    
        
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)
       
        restart = input("\nWould you like to restart? Enter yes or no.\n")
        if restart.lower() != "yes":
            break


if __name__ == "__main__":
	main()

