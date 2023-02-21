import requests
from lxml import html


def convertToNumber(string):
    string = string[:-2]
    ind = len(string) + 1
    for element in string:
        if element == ',':
            ind = string.index(element)
    return float(string[:ind] + string[ind + 1:])


def costOfLivingForCountry(countryName):
    if countryName == 'Czech':
        countryName = 'Czech+Republic'
    if countryName == 'United Kingdom':
        countryName = 'United+Kingdom'
    if countryName == 'United States of America':
        countryName = 'United+States'
    dictionary = {'mealInexpensiveRestaurant': 0,
                  'mealFor2PeopleMidRestaurant': 0, 'mcMealAtMcDonalds': 0, 'domesticBeerRestaurant': 0,
                  'importedBeerRestaurant': 0, 'cappuccino': 0, 'pepsi': 0, 'water': 0,
                  'milk': 0, 'loafOfFreshWhiteBread': 0, 'rice': 0, 'eggs': 0,
                  'localCheese': 0, 'chickenFillets': 0, 'beefRound': 0,
                  'apples': 0, 'banana': 0, 'oranges': 0, 'tomato': 0,
                  'potato': 0, 'onion': 0, 'lettuce': 0, 'waterBigBottle': 0,
                  'bottleOfWine': 0, 'domesticBeer': 0, 'importedBeer': 0, 'cigarettesPack': 0,
                  'oneWayTicketLocal': 0, 'monthlyPass': 0, 'taxiStart': 0,
                  'taxi1km': 0, 'taxi1hourWaiting': 0, 'gasoline': 0, 'volkswagenGolf': 0,
                  'toyotaCorollaSedan': 0, 'basic': 0, 'mobileTariffLocal': 0, 'internet': 0,
                  'fitnessClub': 0, 'tennisCourt': 0, 'cinema': 0, 'preschool': 0,
                  'internationalPrimarySchool': 0, 'jeans': 0, 'dress': 0, 'pairOfNikeRunningShoes': 0,
                  'pairOfMenLeatherBusinessShoes': 0, 'apartment1RoomInCityCentre': 0,
                  'apartment1RoomOutsideOfCentre': 0, 'apartment3RoomsInCityCentre': 0,
                  'apartment3RoomsOutsideOfCentre': 0, 'pricePerSquareMeterToBuyApartmentInCityCentre': 0,
                  'pricePerSquareMeterToBuyApartmentOutsideOfCentre': 0,
                  'averageMonthlyNetSalary': 0}
    params = {'displayCurrency': 'USD'}
    url = 'https://www.numbeo.com/cost-of-living/country_result.jsp?country={}'.format(countryName)
    r = requests.get(url, params=params)
    tree = html.fromstring(r.text)
    table = '//table[@class = "data_wide_table new_bar_table"]'
    descrs = tree.xpath('{}/tr/td/text()'.format(table))
    p = tree.xpath('{}/tr/td/span/text()'.format(table))
    prices = []
    for descr in descrs:
        if descr != ' ' and descr != '\n' and descr != 'Mortgage Interest Rate in Percentages (%), Yearly, for 20 Years Fixed-Rate ':
            prices.append(convertToNumber(p[descrs.index(descr)]))
    index = 0
    for element in dictionary:
        dictionary[element] = prices[index]
        index += 1
    lst = [{}, {}, {}, {}, {}, {}, {}, {}, {}, {}]
    index = 0
    for element in dictionary:
        if index < 8:
            lst[0][element] = dictionary[element]
        elif 7 < index < 27:
            lst[1][element] = dictionary[element]
        elif 26 < index < 35:
            lst[2][element] = dictionary[element]
        elif 34 < index < 38:
            lst[3][element] = dictionary[element]
        elif 37 < index < 41:
            lst[4][element] = dictionary[element]
        elif 40 < index < 43:
            lst[5][element] = dictionary[element]
        elif 42 < index < 47:
            lst[6][element] = dictionary[element]
        elif 46 < index < 51:
            lst[7][element] = dictionary[element]
        elif 50 < index < 53:
            lst[8][element] = dictionary[element]
        elif index == 53:
            lst[9][element] = dictionary[element]
        index += 1
    return lst


def crimeThingForCountry(countryName):
    if countryName == 'Czech':
        countryName = 'Czech+Republic'
    if countryName == 'United Kingdom':
        countryName = 'United+Kingdom'
    if countryName == 'United States of America':
        countryName = 'United+States'
    dictionary = {}
    url = 'https://www.numbeo.com/crime/country_result.jsp?country={}'.format(countryName)
    r = requests.get(url)
    tree = html.fromstring(r.text)
    keys = tree.xpath('//tr/td[@class = "columnWithName"]/text()')
    lst = []
    for key in keys:
        letter = key[0]
        key = str(key.title())
        element = (letter.lower() + key[1:]).replace(' ', '')
        lst.append(element)
    lst[8] = 'worriesBeingSubjectToAPhysicalAttack'
    values = tree.xpath('//tr/td[@class = "indexValueTd"]/text()')
    for index in range(len(keys)):
        dictionary[lst[index]] = int(float(values[index]))
    return dictionary


def climatForCountry(countryName):
    if countryName == 'Czech':
        countryName = 'Czech+Republic'
    if countryName == 'United Kingdom':
        countryName = 'United+Kingdom'
    if countryName == 'United States of America':
        countryName = 'United+States'
    dictionary = {}
    url = 'https://www.numbeo.com/pollution/country_result.jsp?country={}'.format(countryName)
    r = requests.get(url)
    tree = html.fromstring(r.text)
    keys = tree.xpath('//tr/td[@class = "columnWithName"]/text()')
    lst = []
    for key in keys:
        letter = key[0]
        key = str(key.title())
        element = (letter.lower() + key[1:]).replace(' ', '')
        lst.append(element)
    values = tree.xpath('//tr/td[@class = "indexValueTd"]/text()')
    for index in range(len(keys)):
        dictionary[lst[index]] = int(float(values[index]))
    return dictionary


def healthForCountry(countryName):
    if countryName == 'Czech':
        countryName = 'Czech+Republic'
    if countryName == 'United Kingdom':
        countryName = 'United+Kingdom'
    if countryName == 'United States of America':
        countryName = 'United+States'
    dictionary = {}
    url = 'https://www.numbeo.com/health-care/country_result.jsp?country={}'.format(countryName)
    r = requests.get(url)
    tree = html.fromstring(r.text)
    keys = tree.xpath('//tr/td[@class = "columnWithName"]/text()')
    lst = []
    for key in keys:
        letter = key[0]
        key = str(key.title())
        element = (letter.lower() + key[1:]).replace(' ', '')
        lst.append(element)
    lst[5] = 'satisfactionWithResponsivenessInMedicalInstitutions'
    values = tree.xpath('//tr/td[@class = "indexValueTd"]/text()')
    for index in range(len(keys)):
        dictionary[lst[index]] = int(float(values[index]))
    return dictionary