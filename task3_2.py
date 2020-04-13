while True:
    print('To convert to Fahrenheit, enter F or C to convert to Celsius...')
    line=input('>')
    if line[0] == 'F':
        print('Enter the Celsius value to be converted to Fahrenheit...')
        val=input('>')
        res = (int(val) * 1.8) + 32
        print(res)
    elif line[0] == 'C':
        print('Enter the Fahrenheit value to be converted to Celsius...')
        val=input('')
        res = (int(val) - 32) / 1.8
        print(res)
    elif line[0] != 'C' and line[0] != 'F':
        print('Invalid entry')
        break
print('Done')
