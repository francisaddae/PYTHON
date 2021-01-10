'''quarterback_stats = {
    'Aaron Rodgers': {'COMP': 371, 'YDS': 4925, 'TD': 39, 'INT': 8},
    'Peyton Manning': {'COMP': 400, 'YDS': 4659, 'TD': 37, 'INT': 11},
    'Greg McElroy': {'COMP': 19, 'YDS': 214, 'TD': 1, 'INT': 1},
    'Matt Leinart': {'COMP': 16, 'YDS': 115, 'TD': 0, 'INT': 1}
}

print('2012 quarterback statistics:')

print('  Passes completed:')
for qb in quarterback_stats:
    comp = quarterback_stats[qb]['COMP']
    print('    %s: %d' % (qb, comp))  # Replace conversion specifiers
    # Hint: Use the conversion flag '-' to left-justify names

print('  Passing yards:')
for qb in quarterback_stats:
    yds = quarterback_stats[qb]['YDS']
    print('    %s: %d' %(qb, yds))

print('  Touchdown / interception ratio:')
for qb in quarterback_stats:
    td = quarterback_stats[qb]['TD']
    Int = quarterback_stats[qb]['INT']
    a = td/Int
    print('    %s:  %.02f' %(qb,a))'''

#NEXT EXAMPLE
'''

num_resistors = 5
resistors = []
voltage_drop = []

print( '%d resistors are in series.' % num_resistors)
print('This program calculates the'),
print('voltage drop across each resistor.')

input_voltage = float(input('Input voltage applied to circuit: '))
print (input_voltage)

print('Input ohms of %d resistors' % num_resistors)
for i in range(num_resistors):
    res = float(input('%d)' % (i + 1)))
    print(res)
    resistors.append(res)

#  Calculate current
current = input_voltage / sum(resistors)

# Calculate voltage drop over each resistor
print('Voltage drop per resistor is')
for i in range(len(resistors)):
  voltage_per = float(current * resistors[i])
  print('%d) %0.1f V' %(i+1,voltage_per))



# Print the voltage drop per resistor
# ...
'''


#NEXT EXAMPLE
'''

m1_rows = 4
m1_cols = 2
m2_rows = m1_cols  # Must have same value
m2_cols = 3

m1 = [
    [3, 4],
    [2, 3],
    [1, 2],
    [0, 2]
]

m2 = [
    [5, 4, 4],
    [0, 2, 3]
]

m3 = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

# m1 * m2 = m3
for i in range(m1_rows):  # for each row of m1
    for j in range(m2_cols):  # for each column of m2
        # Compute dot product
        dot_product = 0
        for k in range(m2_rows): #  for each row of m2
            dot_product += m1[i][k] * m2[k][j]

        m3[i][j] = dot_product

for i in range(m1_rows):
    for j in range(m2_cols):
        print('%2d' % m3[i][j], end=' ')
    print()  # Print single newline
'''
