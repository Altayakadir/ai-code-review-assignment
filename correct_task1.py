# Write your corrected implementation for Task 1 here.
# Do not modify `task1.py`.
def calculate_aov_optimized(orders):
    if not orders:  # no orders, simply return zero.
        return 0.0

    valid_amounts = [
        order['amount']                                     # keep the amount
        for order in orders                                 # for each order
        if order.get('status') != 'cancelled'               # that is not cancelled
        and isinstance(order.get('amount'), (int, float))   # and has a valid (numerical) type.
    ]

    if not valid_amounts:  # avoid division by zero.
        return 0.0

    return sum(valid_amounts) / len(valid_amounts)  # average.