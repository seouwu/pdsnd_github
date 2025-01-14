# -*- coding: utf-8 -*-
"""bikeshare.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LWKySQhumC9RgTWekbA3JEKiRmyCG0qH
"""
"""if you have question about this code, please email me
    my email is "gkrtks030611@gmail.com"
"""

import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv','newyorkcity': 'new_york_city.csv','washington': 'washington.csv' }

def get_filters():
    """This Function is ask for client to analyze city, month and day
         (str) city : city name to analyze
         (str) month : month name to filter, if you don't want that, write 'all'
         (str) day : day name to filter, if you don'y want that, write 'all'
    """

    city_data={'chicago','newyorkcity','washington'}
    month_data={'all','january','februray','march','april','may','june','july','october','september','november','december'}
    day_data={'all','1','2','3','4','5','6','7'}
    print('Welcome! Let\'s explore some US bikeshare data!')

    print("Would you like to see data for Chicago, New York City, or Washington?")
    city=input()
    city=city.lower()
    city=city.replace(' ','')
    while(city not in city_data):
        print('That is incorrect data, Choose again please !')
        city=input()
        city=city.lower()

    print("Which month? January, Februray, March, April, May or June?, you can also write 'all'")
    month=input()
    month=month.lower()
    while(month not in month_data):
        print('That is incorrect month, Choose again please !')
        month=input()
        month=month.lower()

    print("Which day? Please type your response as an integer(e.g., 1=Sunday), you can also write 'all'")
    day=input()
    day=day.lower()
    while(day not in day_data):
        print('That is incorrect day, Choose again please !')
        day=input()
        day=day.lower()

    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """load city, month, day data """
    df=pd.read_csv(CITY_DATA[city])

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['Start Time']=pd.to_datetime(df['Start Time'])
    month=df['Start Time'].dt.month
    DoW=df['Start Time'].dt.day
    hour=df['Start Time'].dt.hour
    print("The most common month : ",month.mode()[0])
    print("The most common day of week : ", DoW.mode()[0])
    print("The most common Start Time : ", hour.mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    #S=df['Start Station'].str.split('&')
    #E=df['End Station'].str.split('&')
    CommonStartStation=df['Start Station'].value_counts()[:1].astype('str')
    CommonEndStation=df['End Station'].value_counts()[:1].astype('str')
    CommonCombination= 'Start Station :'+CommonStartStation +' / End Station : '+ CommonEndStation
    print("The most common Start Station is : ",CommonStartStation)
    print("The most common End Station is :",CommonEndStation)
    print("The most combination of Start station and End Station travels is :", CommonCombination)
    # 가장 일반적으로 사용되는 시작 측점 표시
    # 가장 일반적으로 사용되는 종점역을 표시합니다
    # 시작 역과 종료 역 여행의 가장 빈번한 조합을 표시합니다

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    #전체 여행 시간을 표시합니다.
    #평균 이동 시간을 표시합니다
    total=df['Trip Duration'].sum()
    average=total/df['Trip Duration'].shape[0]
    print("The total travel time is.",total)
    print("The average travel time is.",average)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    #사용자 유형 표시
    #성별 수 표시
    #가장 빠른, 가장 최근 및 가장 일반적인 출생 연도 표시
    if('Birth Year' not in df):
        print("There is no Birth day data ! ")
    else:
        earliest=int(df['Birth Year'].min())
        recent=int(df['Birth Year'].max())
        common=int(df['Birth Year'].mean())
        print("The earliest year of Birth :  ",earliest)
        print("The most recent year of Birth : ", recent)
        print("The most common year of Birth : ", common)
    if ('Gender' not in df):
        print("There is no Gender data!")
    else:
        total_gender=df['Gender'].count()
        Female=len(df.loc[df['Gender']=='Female'])
        Male=len(df.loc[df['Gender']=='Male'])
        print("Total gender :",total_gender,"Female:", Female ," Male: total:", Male)


    UserTypes=df['User Type'].value_counts()
    print("User Types  : ", UserTypes )
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def individual_data(df):
    """print Imdivisual data if user wans to see
    yes = print 5 indivisual data
    no= stop print indivisual data"""
    i=0
    while(True):
        print("Would you like to view individual Trip data? Yes or No")
        answer=input()
        if(answer.lower()=="yes"):
            print(df.iloc[0+i])
            print(df.iloc[1+i])
            print(df.iloc[2+i])
            print(df.iloc[3+i])
            print(df.iloc[4+i])
            i+=5
        elif answer.lower()=="no":
            break
        else:
            print("wrong amswer")
def main():
    while True:
        city, month, day = get_filters()
        df=load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        individual_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()