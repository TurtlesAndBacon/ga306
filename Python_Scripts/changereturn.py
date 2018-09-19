print('How much change do you need?')
run_tot = int(input())
num_quarters = run_tot // 25
run_tot = run_tot - (num_quarters * 25)
num_dimes = run_tot // 10
run_tot = run_tot - (num_dimes * 10)
num_nickles = run_tot // 5
run_tot = run_tot - (num_nickles * 5)
num_pennies = run_tot // 1
run_tot = run_tot - (num_pennies * 1)
print('Quarters ' + str(num_quarters),
    'Dimes ' + str(num_dimes),
    'Nickles ' + str(num_nickles),
    'Pennies' + str(num_pennies)
    )
