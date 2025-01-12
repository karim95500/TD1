def calculate_series_resistance(resistances):
    total = 0
    for r in resistances:
        total += r
    return total

def calculate_parallel_resistance(resistances):
    total = 0
    for r in resistances:
        if r != 0:
            total += 1 / r
    if total != 0:
        return 1 / total
    return 0

resistances_series = [10, 20, 30]
resistances_parallel = [10, 20, 30]

series_result = calculate_series_resistance(resistances_series)
parallel_result = calculate_parallel_resistance(resistances_parallel)

print(f"Résistance équivalente en série : {series_result} Ω")
print(f"Résistance équivalente en parallèle : {parallel_result:.2f} Ω")

