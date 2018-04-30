def is_leap(n):
    if n % 400 == 0:
        return 'Yes, ' + str(n) + ' was a leap year!'

    elif n % 100 == 0:
        return 'No, ' + str(n) + ' was not a leap year!'

    elif n % 4 == 0:
        return 'Yes, ' + str(n) + ' was a leap year!'

    else:
        return 'No, ' + str(n) + ' was not a leap year!'


result = is_leap(2001)

print(result)
