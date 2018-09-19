print('How much change does the customer need?')
run_tot = float(input())
run_tot = (run_tot * 100)
num_twent = run_tot // 2000
run_tot = run_tot - (num_twent * 2000)
num_ten = run_tot // 1000
run_tot = run_tot - (num_ten * 1000)
num_five = run_tot // 500
run_tot = run_tot - (num_five * 500)
num_dol = run_tot // 100
run_tot = run_tot - (num_dol * 100)
num_quarters = run_tot // 25
run_tot = run_tot - (num_quarters * 25)
num_dimes = run_tot // 10
run_tot = run_tot - (num_dimes * 10)
num_nickles = run_tot // 5
run_tot = run_tot - (num_nickles * 5)
num_pennies = run_tot // 1
run_tot = run_tot - (num_pennies * 1)
print('BE SURE TO WAD UP AND PLACE ON COUNTER IN FRONT OF CUSTOMER\'S OUTSTRETCHED HAND!')
print('Twenties ' + str(num_twent),
    '\nTens ' + str(num_ten),
    '\nFives ' + str(num_five),
    '\nDollars ' + str(num_dol),
    '\nQuarters ' + str(num_quarters),
    '\nDimes ' + str(num_dimes),
    '\nNickles ' + str(num_nickles),
    '\nPennies ' + str(num_pennies)
    )
