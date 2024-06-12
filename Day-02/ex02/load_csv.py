#!/usr/bin/env python
import pandas as pd


def load(path: str) -> pd.DataFrame:
    try:
        result = pd.read_csv(path)
    except FileNotFoundError:
        print(f"Error: {path} does not exist")
        return None
    except PermissionError:
        print(f"Error: You do not have permission to read {path}")
        return None
    except pd.errors.EmptyDataError:
        print(f"Error: {path} was unable to be loaded: \
            No columns to parse from file")
        return None
    print(f"Loading dataset of dimensions {result.shape}")
    return result


def main():
    load("life_expectancy_years.csv")
    load("Nope.csv")
    load("dummy.csv")


if __name__ == '__main__':
    main()
