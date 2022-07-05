import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("what city are you interested in").lower()
    while True:
        if city == 'chicago':
            city = 'chicago'
            break
        elif city == 'new york city':
            city = 'new york city'
            break
        elif city == 'washington':
            city = 'washington'
            break
        else:
            city = input("please input a valid city").lower()


    # TO DO: get user input for month (all, january, february, ... , june)
    month =""
    month_list = ['all' , 'january', 'february','march','april', 'may', 'june']
    month_input = input("please input the desired month").lower()
    while True:
        if month_input in month_list:
            month = month_input
            break
        else:
            month_input = input("please give a valid month").lower()
    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day =""
    day_list = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday','saturday', 'sunday']
    day_input = input("please input the desired day of the week").lower()
    while True:
        if day_input in day_list:
            day = day_input
            break
        else:
            day_input = input('please input a valid day').lower()

    print('-'*40)
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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['all','january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) 
    
        # filter by month to create the new dataframe
        df = df[df['month']==month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    month_list =["all","January","February", "March", "April", "May","June","July"]
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("the most common month is:",month_list[df['month'].mode()[0]])

    # TO DO: display the most common day of week
    print("the most common day of the week:", df['day_of_week'].mode()[0])


    # TO DO: display the most common start hour
    print("the most common start hour is:", pd.to_datetime(df['Start Time']).dt.hour.mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("The most frequently used start station is:", df['Start Station'].mode()[0])
  
    # TO DO: display most commonly used end station
    print("The most frequently used end station is:", df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    print("the most frequent combination of start station and end station:", (df['Start Station'] + ' and ' + df['End Station']).mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("the total travel time in seconds is:" ,df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print("The mean travel time in seconds is:", df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print(df['User Type'].value_counts())

    # TO DO: Display counts of gender
    try:
        print(df['Gender'].value_counts())
    except:
        print("The Gender data you are looking for is not available")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        print("The earliest year of birth is:", df['Birth Year'].min())
        print("The most recent year of birth is:", df['Birth Year'].max())
        print("The most common year of Birth is:", df['Birth Year'].mode()[0])
    except:
        print("The birth data you are looking for is not available")
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def show_information(df):
    a=0
    b=5
    prompt = input("would you like to see the first few rows of the data [yes/no]").lower()
    while True:
        if prompt == 'yes': 
            print(df.iloc[a:b,:])
            prompt = input("would you like to see the first few rows of the data [yes/no]").lower()
            a = a+5
            b=b+5
        elif prompt == 'no':
            break
        else:
            prompt = input("please input a valid option").lower()
    

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        cf= df.copy()
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        
        user_stats(df)
        show_information(cf)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
