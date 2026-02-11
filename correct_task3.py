# Write your corrected implementation for Task 3 here.
# Do not modify `task3.py`.
import math

def average_valid_measurements(values):
    total = 0.0
    count = 0

    if values is None:
        return 0.0

    for v in values:
        if v is not None:
            try:
                val = float(v)

                # ignore not a number
                if math.isnan(val):
                    continue

                total += val
                count += 1
            except ValueError:
                continue

    if count == 0:
        return 0.0

    return total / count