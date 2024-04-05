import csv


filename = "budget_data.csv"

# Initialize variables
max_difference = 0
min_difference = float('inf')  # Set to infinity to ensure any real value is lower
total_profit = 0
sum_difference = 0
max_date = ""
min_date = ""
previous_profit = 0
number_lines = 0

with open(filename, 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip header

    for row in csv_reader:
        date = row[0]
        profit = int(row[1])
        
        # Accumulate total profit
        total_profit += profit

        # Calculate difference and update running sum of differences
        if number_lines > 0:
            difference = profit - previous_profit
            sum_difference += difference

            # Check and update max difference
            if difference > max_difference:
                max_difference = difference
                max_date = date
            
            # Check and update min difference
            if difference < min_difference:
                min_difference = difference
                min_date = date

        previous_profit = profit  # Update previous profit for next iteration
        number_lines += 1

# Compute average difference; avoid division by zero
average_difference = sum_difference / (number_lines - 1) if number_lines > 1 else 0


# Print the ANALYSIS RESULTS to the TERMINAL
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {number_lines}")
print(f"Total Profit: {total_profit}")
print(f"Average Change: {average_difference:.2f}")
print(f"Max Increase in Profits: {max_difference} on {max_date}")
print(f"Max Decrease in Profits: {min_difference} on {min_date}")

# Write the results to a text file
with open('financial_analysis.txt', 'w') as file:
    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write(f"Total Months: {number_lines}\n")
    file.write(f"Total Profit: ${total_profit}\n")
    file.write(f"Average Change: ${average_difference:.2f}\n")
    file.write(f"Max Increase in Profits: ${max_difference} on {max_date}\n")
    file.write(f"Max Decrease in Profits: ${min_difference} on {min_date}\n")
