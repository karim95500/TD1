def sum_resistances(resistances):
    return sum(resistances)

def reciprocal_sum(resistances):
    return sum(1 / r for r in resistances if r != 0)

def calculate_series_resistance(resistances):
    return sum_resistances(resistances)

def calculate_parallel_resistance(resistances):
    reciprocal = reciprocal_sum(resistances)
    return 1 / reciprocal if reciprocal != 0 else 0
    
def main():
    resistances_series = [10, 20, 30]
    resistances_parallel = [10, 20, 30]

    series_result = calculate_series_resistance(resistances_series)
    parallel_result = calculate_parallel_resistance(resistances_parallel)

    print(f"Résistance équivalente en série : {series_result} Ω")
    print(f"Résistance équivalente en parallèle : {parallel_result:.2f} Ω")

if __name__ == "__main__":
    main()
