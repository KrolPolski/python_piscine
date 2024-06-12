#!/usr/bin/env python

from load_csv import load
import matplotlib.pyplot as plt


def main():
    data = load("life_expectancy_years.csv")
    finland = data.query('country =="Finland"')
    years = finland.columns[1:]
    values = finland.values[0][1:]
    years = [int(year) for year in years]
    values = [float(value) for value in values]
    plt.plot(years, values)
    plt.xlabel('Year')
    plt.ylabel('Life Expectancy')
    plt.title('Finland Life Expectancy Projections')
    plt.show()


if __name__ == '__main__':
    main()
