# Import Modules
import os
import csv

# Define variables
months = 0
netProfit = 0
profitChanges = []
lastMonthsProfit = None
greatestIncrease = 0
greatestDecrease = 0

# Import CSV
budgetPath = os.path.join('Resources', 'budget_data.csv')

# Read CSV
with open(budgetPath) as budget:

    # Parse CSV
    reader = csv.reader(budget, delimiter=",")

    # Skip header
    next(reader, None)

    # Loop through rows of CSV
    for row in reader:

        # Increment months
        months += 1

        # Convert profit to an integer
        profit = int(row[1])

        # Add this month's profit to the total
        netProfit += profit

        # Calculate change in profit, but not in week 1
        if (lastMonthsProfit != None):
            change = profit - lastMonthsProfit
            profitChanges.append(change)

            # Compare to current greatest increase and decrease
            if change > greatestIncrease:
                greatestIncrease = change
                greatestIncreaseMonth = row[0]
            elif change < greatestDecrease:
                greatestDecrease = change
                greatestDecreaseMonth = row[0]

        # Prepare lastMonthsProfit for the next row
        lastMonthsProfit = profit

    # Calculate average change
    avgChange = sum(profitChanges)/len(profitChanges)

    # Print data
    analysis = f"""
    Financial Analysis
    ----------------------------
    Total Months: {months}
    Total: ${netProfit}
    Average Change: ${avgChange:.2f}
    Greatest Increase in Profits: {greatestIncreaseMonth} $({greatestIncrease})
    Greatest Decrease in Profits: {greatestDecreaseMonth} $({greatestDecrease})
    """
    
    print(analysis)

    output = open("Analysis/results.txt", "w")
    output.write(analysis)
    output.close()
