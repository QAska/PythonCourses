def city_country(city, country):
    result = city + ', ' + country
    return result.title()


while True:
    print("Enter 'q' to quit.")
    city = input('Enter city: ')

    if city == 'q':
        break

    country = input('Enter country: ')
    if country == 'q':
        break

    print(city_country(city, country), '\n')


