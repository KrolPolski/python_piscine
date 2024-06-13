#!/usr/bin/env python

from load_csv import load
import matplotlib.pyplot as plt


def human_to_int(human: list) -> float:
    if human[-1] == 'k':
        result = float(human[:-1]) * 1000
    elif human[-1] == 'M':
        result = float(human[:-1]) * 1000000
    else:
        result = float(human)
    return result


def main():
    data = load("population_total.csv")
    fi_sw = data.query('country =="Finland" | country=="Sweden"')
    print(fi_sw)
    years = fi_sw.columns[1:]
    trimmed = fi_sw.drop(columns=fi_sw.columns[0], axis=1, inplace=False)
    values = trimmed.values
    years = [int(year) for year in years]
    values[0] = [human_to_int(num) for num in values[0]]
    values[1] = [human_to_int(num) for num in values[1]]
    print(values)
    ax = plt.subplot()
    ax.plot(years, values[0], label="Finland")
    ax.plot(years, values[1], label="Sweden")
    ax.set_yticklabels(['0', '2M', '4M', '6M', '8M', '10M', '12M'])
    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.title('Finland and Sweden Population Projections')
    plt.legend(["Finland", "Sweden"])
    plt.show()


if __name__ == '__main__':
    main()
