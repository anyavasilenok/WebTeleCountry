from neo4j import GraphDatabase
from course.main.database.parsing.parsingInfoForDataBase import crimeThingForCountry, climatForCountry, costOfLivingForCountry, healthForCountry
from course.config import LOCALHOST, LOGIN, PASSWORD


def formParams(dict):
    params = '{'
    for key, value in dict.items():
        params += '%s: %s, ' % (key, str(value))
    params = params[:-2] + '}'
    return params


class CountryCreator:

    def __init__(self):
        self.driver = GraphDatabase.driver(LOCALHOST, auth=(LOGIN, PASSWORD))

    def close(self):
        self.driver.close()

    def createBase(self, countryName, citiesDict, officialLanguage,
                   # currency
                   currencyName, currencyEqualsToDollar,
                   # military
                   milPolBlock, amountOfPeopleInArmy,
                   # healthcare
                   numberOfDoctorsPer100kPopulation, menAverageLifeExpectancy, womenAverageLifeExpectancy,
                   # climat
                   juneAverageTemperature, decemberAverageTemperature, averageHumidity,
                   averageDurationOfWinter, averageRainfallPerMonth, averageNumberOfFoggyDaysPerYear,
                   averageNumberOfRainyDaysPerYear, averageNumberOfClearDays,
                   # security
                   situationInTheCountry, freedomOfSpeech,
                   assessmentOfFamilyLife, attitudeTowardsLGBT,
                   # population
                   populationCount, procentOfMales, procentOfFemales, populationDensityPerSquareKilometer,
                   speedOfLife, workPlaces, nightLifeEntertainment,
                   # citizenship
                   citizenshipGlobalRank,
                   # communication
                   communicationOnEnglish,
                   # transport
                   averageTravelTimeToWork, developmentLevelOfPublicTransport,
                   # internet
                   speedOfInternetMbps, freeWifi,
                   # education
                   rankingOfNationalEducationSystem, universities, faculties, programs, costs, links, images,
                   requirements,
                   hostel, scolarship, sights, beaches, mountains, skiResorts, lakes, rivers, friendlyToForeigners
                   ):
        with self.driver.session() as session:
            base = session.execute_write(self._createBase, countryName, citiesDict, officialLanguage,
                                         # currency
                                         currencyName, currencyEqualsToDollar,
                                         # military
                                         milPolBlock, amountOfPeopleInArmy,
                                         # healthcare
                                         numberOfDoctorsPer100kPopulation, menAverageLifeExpectancy,
                                         womenAverageLifeExpectancy,
                                         # climat
                                         juneAverageTemperature, decemberAverageTemperature, averageHumidity,
                                         averageDurationOfWinter, averageRainfallPerMonth,
                                         averageNumberOfFoggyDaysPerYear,
                                         averageNumberOfRainyDaysPerYear, averageNumberOfClearDays,
                                         # security
                                         situationInTheCountry, freedomOfSpeech,
                                         assessmentOfFamilyLife, attitudeTowardsLGBT,
                                         # population
                                         populationCount, procentOfMales, procentOfFemales,
                                         populationDensityPerSquareKilometer,
                                         speedOfLife, workPlaces, nightLifeEntertainment,
                                         # citizenship
                                         citizenshipGlobalRank,
                                         # communication
                                         communicationOnEnglish,
                                         # transport
                                         averageTravelTimeToWork, developmentLevelOfPublicTransport,
                                         # internet
                                         speedOfInternetMbps, freeWifi,
                                         # education
                                         rankingOfNationalEducationSystem, universities, faculties, programs, costs,
                                         links, images,
                                         requirements,
                                         hostel, scolarship, sights, beaches, mountains, skiResorts, lakes, rivers,
                                         friendlyToForeigners
                                         )
            return base

    @staticmethod
    def _createBase(tx, countryName, citiesDict, officialLanguage,
                    # currency
                    currencyName, currencyEqualsToDollar,
                    # military
                    milPolBlock, amountOfPeopleInArmy,
                    # healthcare
                    numberOfDoctorsPer100kPopulation, menAverageLifeExpectancy, womenAverageLifeExpectancy,
                    # climat
                    juneAverageTemperature, decemberAverageTemperature, averageHumidity,
                    averageDurationOfWinter, averageRainfallPerMonth, averageNumberOfFoggyDaysPerYear,
                    averageNumberOfRainyDaysPerYear, averageNumberOfClearDays,
                    # security
                    situationInTheCountry, freedomOfSpeech,
                    assessmentOfFamilyLife, attitudeTowardsLGBT,
                    # population
                    populationCount, procentOfMales, procentOfFemales, populationDensityPerSquareKilometer,
                    speedOfLife, workPlaces, nightLifeEntertainment,
                    # citizenship
                    citizenshipGlobalRank,
                    # communication
                    communicationOnEnglish,
                    # transport
                    averageTravelTimeToWork, developmentLevelOfPublicTransport,
                    # internet
                    speedOfInternetMbps, freeWifi,
                    # education
                    rankingOfNationalEducationSystem, universities, faculties, programs, costs, links, images,
                    requirements,
                    hostel, scolarship, sights, beaches, mountains, skiResorts, lakes, rivers, friendlyToForeigners
                    ):
        # country
        resultStr = 'create (country:Country {name:"%s"})' % (str(countryName))
        # Crime
        crime = crimeThingForCountry(countryName)
        crimeParams = formParams(crime)
        resultStr += '\ncreate (crime:CrimeThing %s)\n' % crimeParams
        resultStr += 'create (country)-[:crime_indexes]->(crime)\n'
        # Climat
        climat = climatForCountry(countryName)
        climatParams = '{'
        for key, value in climat.items():
            climatParams += '%s: %s, ' % (key, str(value))
        climatParams += 'juneAverageTemperature: %s, ' % juneAverageTemperature
        climatParams += 'decemberAverageTemperature: %s, ' % decemberAverageTemperature
        climatParams += 'averageHumidity: %s, ' % averageHumidity
        climatParams += 'averageDurationOfWinter: %s, ' % averageDurationOfWinter
        climatParams += 'averageRainfallPerMonth: %s, ' % averageRainfallPerMonth
        climatParams += 'averageNumberOfFoggyDaysPerYear: %s, ' % averageNumberOfFoggyDaysPerYear
        climatParams += 'averageNumberOfRainyDaysPerYear: %s, ' % averageNumberOfRainyDaysPerYear
        climatParams += 'averageNumberOfClearDays: %s, ' % averageNumberOfClearDays
        climatParams = climatParams[:-2] + '}'
        resultStr += 'create (climat:Climat %s)\n' % climatParams
        resultStr += 'create (country)-[:climat]->(climat)\n'
        # economic situation
        resultStr += 'create (economicSituation:EconomicSituation)'
        economicList = costOfLivingForCountry(countryName)
        restaurantsParams = formParams(economicList[0])
        marketsParams = formParams(economicList[1])
        transportationParams = formParams(economicList[2])
        utilitiesParams = formParams(economicList[3])
        sportsParams = formParams(economicList[4])
        childcareParams = formParams(economicList[5])
        clothingParams = formParams(economicList[6])
        rentParams = formParams(economicList[7])
        buyParams = formParams(economicList[8])
        salariesParams = formParams(economicList[9])
        resultStr += '\ncreate (restaurantsPrices:RestaurantsPrices %s)' % restaurantsParams
        resultStr += '\ncreate (economicSituation)-[:prices_in_restaurants]->(restaurantsPrices)'
        resultStr += '\ncreate (marketsPrices:MarketsPrices %s)' % marketsParams
        resultStr += '\ncreate (economicSituation)-[:prices_in_markets]->(marketsPrices)'
        resultStr += '\ncreate (transportationPrices:TransportationPrices %s)' % transportationParams
        resultStr += '\ncreate (economicSituation)-[:transportation_prices]->(transportationPrices)'
        resultStr += '\ncreate (utilitiesPrices:UtilitiesPrices %s)' % utilitiesParams
        resultStr += '\ncreate (economicSituation)-[:utilities_prices]->(utilitiesPrices)'
        resultStr += '\ncreate (sportsPrices:SportsPrices %s)' % sportsParams
        resultStr += '\ncreate (economicSituation)-[:sports_prices]->(sportsPrices)'
        resultStr += '\ncreate (childcarePrices:ChildcarePrices %s)' % childcareParams
        resultStr += '\ncreate (economicSituation)-[:childcare_prices]->(childcarePrices)'
        resultStr += '\ncreate (clothingPrices:ClothingPrices %s)' % clothingParams
        resultStr += '\ncreate (economicSituation)-[:clothing_prices]->(clothingPrices)'
        resultStr += '\ncreate (rentPrices:RentPrices %s)' % rentParams
        resultStr += '\ncreate (economicSituation)-[:rent_prices]->(rentPrices)'
        resultStr += '\ncreate (buyPrices:BuyPrices %s)' % buyParams
        resultStr += '\ncreate (economicSituation)-[:buy_prices]->(buyPrices)'
        resultStr += '\ncreate (salaries:Salaries %s)' % salariesParams
        resultStr += '\ncreate (economicSituation)-[:salaries]->(salaries)'
        resultStr += '\ncreate (country)-[:economic_situation]->(economicSituation)'
        # healthcare
        healthDict = healthForCountry(countryName)
        healthParams = '{'
        for key, value in healthDict.items():
            healthParams += '%s: %s, ' % (key, str(value))
        healthParams += 'numberOfDoctorsPer100kPopulation: %s, ' % numberOfDoctorsPer100kPopulation
        healthParams += 'menAverageLifeExpectancy: %s, ' % menAverageLifeExpectancy
        healthParams += 'womenAverageLifeExpectancy: %s, ' % womenAverageLifeExpectancy
        healthParams = healthParams[:-2] + '}'
        resultStr += 'create (health:HealthCare %s)\n' % healthParams
        resultStr += 'create (country)-[:healthcare]->(health)'

        # cities
        index = 1
        for city in citiesDict:
            resultStr += '\ncreate (city%d:City {name:"%s", isBig:"%s", isResort:"%s"})' % (
                index, city, str(citiesDict[city][0]), str(citiesDict[city][1]))
            resultStr += '\ncreate (country)-[:has_city]->(city%d)' % index
            if index == 1:
                resultStr += '\ncreate (country)-[:capital]->(city%d)' % index
            if citiesDict[city][2] is not None:
                resultStr += '\nmerge (water%d:Water {name:"%s"})' % (index, str(citiesDict[city][2]))
                resultStr += '\nmerge (water%d)-[:washes]->(city%d)' % (index, index)
                resultStr += '\nmerge (water%d)-[:washes]->(country)' % (index)
            index += 1
        # education
        resultStr += '\ncreate (education:Education {rankingOfNationalEducationSystem:%d})' % rankingOfNationalEducationSystem
        resultStr += '\ncreate (country)-[:education]->(education)\n'

        index = 1
        if sights:
            for sight in sights.keys():
                resultStr += '\ncreate (sight%d:Sight {name:"%s", description:"%s", image:"%s"})' % (
                    index, sight, sights[sight][0], sights[sight][1])
                resultStr += '\ncreate (country)-[:sight]->(sight%d)' % (index)
                index += 1

        index = 1
        if beaches:
            for beach in beaches.keys():
                resultStr += '\ncreate (beach%d:Beach {name:"%s", description:"%s", image:"%s"})' % (
                    index, beach, beaches[beach][0], beaches[beach][1])
                resultStr += '\ncreate (country)-[:beach]->(beach%d)' % (index)
                index += 1

        index = 1
        if mountains:
            for mountain in mountains.keys():
                resultStr += '\ncreate (mountain%d:Mountain {name:"%s", description:"%s", image:"%s"})' % (
                    index, mountain, mountains[mountain][0], mountains[mountain][1])
                resultStr += '\ncreate (country)-[:mountain]->(mountain%d)' % (index)
                index += 1

        index = 1
        if lakes:
            for lake in lakes.keys():
                resultStr += '\ncreate (lake%d:Lake {name:"%s", description:"%s", image:"%s"})' % (
                    index, lake, lakes[lake][0], lakes[lake][1])
                resultStr += '\ncreate (country)-[:lake]->(lake%d)' % (index)
                index += 1

        index = 1
        if rivers:
            for river in rivers.keys():
                resultStr += '\ncreate (river%d:River {name:"%s", description:"%s", image:"%s"})' % (
                    index, river, rivers[river][0], rivers[river][1])
                resultStr += '\ncreate (country)-[:river]->(river%d)' % (index)
                index += 1

        index = 1
        if skiResorts:
            for skiResort in skiResorts.keys():
                resultStr += '\ncreate (skiResort%d:SkiResort {name:"%s", description:"%s", image:"%s"})' % (
                    index, skiResort, skiResorts[skiResort][0], skiResorts[skiResort][1])
                resultStr += '\ncreate (country)-[:skiResort]->(skiResort%d)' % (index)
                index += 1

        index = 1
        fac = 1
        univ_ind = 1
        prog = 1

        for city in citiesDict:
            if city in universities.keys():
                for univ in universities[city]:
                    try:
                        link = links[univ]
                        cost = costs[univ]
                        image = images[univ]
                        req = requirements[univ]
                        host = hostel[univ]
                        scolar = scolarship[univ]
                    except:
                        link = "a"
                        cost = 1000
                        image = 'clear'
                        req = 'No requirements'
                        host = 'No'
                        scolar = 'No'
                    resultStr += '\ncreate (univ%d:University {name:"%s",link:"%s",cost:%d,hostel:"%s",scolarship:"%s",image:"%s",requirements:"%s"})' % (
                        univ_ind, univ, link, cost, host, scolar, image, req)
                    for faculty in faculties[univ]:
                        resultStr += '\nmerge (faculty%d:Faculty {name:"%s"})' % (fac, faculty)
                        resultStr += '\nmerge (univ%d)-[:faculty]->(faculty%d)' % (univ_ind, fac)
                        fac += 1
                    try:
                        for program in programs[univ]:
                            resultStr += '\nmerge (program%d:Program {name:"%s"})' % (prog, program)
                            resultStr += '\nmerge (univ%d)-[:program]->(program%d)' % (univ_ind, prog)
                            prog += 1
                    except:
                        pass

                    # resultStr += '\ncreate (cost%d:Cost {value:%d})' % (c, cost)
                    # resultStr += '\ncreate (univ%d)-[:cost]->(cost%d)' % (ind, c)

                    resultStr += '\ncreate (city%d)-[:university]->(univ%d)' % (index, univ_ind)
                    resultStr += '\ncreate (country)-[:university]->(univ%d)' % univ_ind
                    univ_ind += 1
                index += 1

        # language
        resultStr += '\ncreate (language:Language {name:"%s"})' % (str(officialLanguage))
        resultStr += '\ncreate (country)-[:official_language]->(language)'
        # currency
        resultStr += '\ncreate (currency:Currency {name:"%s", oneDollarEquals:%s})' % (
            str(currencyName), currencyEqualsToDollar)
        resultStr += '\ncreate (country)-[:currency]->(currency)'
        # military political block
        resultStr += '\nmerge (militaryPoliticalBlock:MilitaryPoliticalBlock {name:"%s"})' % (str(milPolBlock))
        resultStr += '\ncreate (country)-[:belongs_to_military_political_block]->(militaryPoliticalBlock)'
        # military Power
        resultStr += '\ncreate (militaryPower:MilitaryPower {amountOfPeople:%d})' % amountOfPeopleInArmy
        resultStr += '\ncreate (country)-[:military_power]->(militaryPower)'
        # security
        resultStr += '\ncreate (security:Security {situationInTheCountry:%d, freedomOfSpeech:%d,' \
                     ' assessmentOfFamilyLife:%d, attitudeTowardsLGBT:%d})' % (situationInTheCountry, freedomOfSpeech,
                                                                               assessmentOfFamilyLife,
                                                                               attitudeTowardsLGBT)
        resultStr += '\ncreate (country)-[:security]->(security)'

        # population
        resultStr += '\ncreate (population:Population {count:%i, procentOfMales:%s, procentOfFemales:%s, populationDensityPerSquareKilometer:%d,' \
                     ' speedOfLife:%d, workPlaces:%d, nightLifeEntertainment:%d})' \
                     % (populationCount, procentOfMales, procentOfFemales, populationDensityPerSquareKilometer,
                        speedOfLife, workPlaces, nightLifeEntertainment)
        resultStr += '\ncreate (country)-[:population]->(population)'
        #
        # citizenship
        resultStr += '\ncreate (citizenship:Citizenship {globalRank:%d, friendlyToForeigners:%d})' % (
            citizenshipGlobalRank, friendlyToForeigners)
        resultStr += '\ncreate (country)-[:citizenship]->(citizenship)'
        # communication
        resultStr += '\ncreate (communication:Communication {communicationOnEnglish:%d})' % (communicationOnEnglish)
        resultStr += '\ncreate (country)-[:communication]->(communication)'
        # transport
        resultStr += '\ncreate (transport:Transport {averageTravelTimeToWork:%d, developmentLevelOfPublicTransport:%d})' \
                     % (averageTravelTimeToWork, developmentLevelOfPublicTransport)

        resultStr += '\ncreate (country)-[:transport]->(transport)'

        # internet
        resultStr += '\ncreate (internet:Internet {speedOfInternetMbps:%d, freeWifi:%d})' % (
            speedOfInternetMbps, freeWifi)
        resultStr += '\ncreate (country)-[:internet]->(internet)'
        print('+', countryName)
        result = tx.run(resultStr)

    def createManMadeDisaster(self, countryName, nameOfDisaster, typeOfMMD, aomuntOfDeadPeople,
                              aomuntOfInjuredPeople, territoryOfPollution):
        with self.driver.session() as session:
            manMadeDisaster = session.execute_write(self._createManMadeDisaster, countryName, nameOfDisaster, typeOfMMD,
                                                    aomuntOfDeadPeople, aomuntOfInjuredPeople, territoryOfPollution)
            return manMadeDisaster

    @staticmethod
    def _createManMadeDisaster(tx, countryName, nameOfDisaster, typeOfMMD, aomuntOfDeadPeople,
                               aomuntOfInjuredPeople, territoryOfPollution):
        resultStr = 'match (country:Country {name:"%s"}' % countryName
        resultStr += '\nmatch (country)->[:climat]->(climat)'
        resultStr += 'create (manMadeDisaster:ManMadeDisaster {name:"%s", typeOfMMD:"%s", aomuntOfDeadPeople:%d,' \
                     '                                         aomuntOfInjuredPeople:%d, territoryOfPollution:"%d km^2"})' % (
                         nameOfDisaster, typeOfMMD, aomuntOfDeadPeople,
                         aomuntOfInjuredPeople, territoryOfPollution)
        resultStr += 'create (climat)-[:man_made_disaster]->(manMadeDisaster)'

        result = tx.run(resultStr)

    def createOceans(self):
        with self.driver.session() as session:
            oceans = session.execute_write(self._createOceans)
            return oceans

    @staticmethod
    def _createOceans(tx):
        request = '''
        match (city1:City {name:"Quebec"})
        match (city2:City {name:"Vancouver"})
        create (ocean1:Ocean {name: "Pacific"})
        create (ocean2:Ocean {name: "Atlantic"})
        create (ocean2)-[:washes]->(city1)
        create (ocean1)-[:washes]->(city2)\n'''
        result = tx.run(request)

    def createBorders(self):
        with self.driver.session() as session:
            borders = session.execute_write(self._createBorders)
            return borders

    @staticmethod
    def _createBorders(tx):
        request = '''
        match (canada:Country {name:"Canada"})
        match (uae:Country {name:"United Arab Emirates"})
        match (usa:Country {name:"United States of America"})
        match (spain:Country {name:"Spain"})
        match (italy:Country {name:"Italy"})
        match (portugal:Country {name:"Portugal"})
        match (argentina:Country {name:"Argentina"})
        match (brazil:Country {name:"Brazil"})
        match (poland:Country {name:"Poland"})
        match (germany:Country {name:"Germany"})
        match (czech:Country {name:"Czech"})
        match (slovakia:Country {name:"Slovakia"})
        match (hungary:Country {name:"Hungary"})
        match (uk:Country {name:"United Kingdom"})
        match (finland:Country {name:"Finland"})
        match (sweden:Country {name:"Sweden"})
        match (norway:Country {name:"Norway"})
        match (france:Country {name:"France"})

        create (brazil)-[:borders_with]->(argentina)
        create (argentina)-[:borders_with]->(brazil)

        create (poland)-[:borders_with]->(czech)
        create (poland)-[:borders_with]->(germany)
        create (poland)-[:borders_with]->(slovakia)
        create (czech)-[:borders_with]->(poland)
        create (czech)-[:borders_with]->(germany)
        create (czech)-[:borders_with]->(slovakia)
        create (germany)-[:borders_with]->(poland)        
        create (germany)-[:borders_with]->(czech)
        create (germany)-[:borders_with]->(france)
        create (slovakia)-[:borders_with]->(poland)      
        create (slovakia)-[:borders_with]->(czech)
        create (slovakia)-[:borders_with]->(hungary) 
        create (hungary)-[:borders_with]->(slovakia)
        create (finland)-[:borders_with]->(sweden)
        create (finland)-[:borders_with]->(norway)
        create (sweden)-[:borders_with]->(finland)
        create (sweden)-[:borders_with]->(norway)
        create (norway)-[:borders_with]->(finland)
        create (norway)-[:borders_with]->(sweden)

        create (france)-[:borders_with]->(germany)
        create (canada)-[:borders_with]->(usa)
        create (usa)-[:borders_with]->(canada)

        create (spain)-[:borders_with]->(portugal)
        create (spain)-[:borders_with]->(france)
        create (france)-[:borders_with]->(spain)

        create (italy)-[:borders_with]->(france)
        create (france)-[:borders_with]->(italy)

        create (portugal)-[:borders_with]->(spain)
        \n'''
        result = tx.run(request)

    def clear_db(self):
        with self.driver.session() as session:
            clr = session.execute_write(self._clear_db)
            return clr

    @staticmethod
    def _clear_db(tx):
        request = "match (n) detach delete n"
        tx.run(request)


if __name__ == "__main__":
    cc = CountryCreator()

    cc.clear_db()

    #############################   CANADA   #############################

    # Country
    countryName = "Canada"
    officialLanguage = "English"

    # cities    name   isBig isResort washesBy
    cities = {'Ottawa': [True, True, None], 'Toronto': [True, False, None], 'Montreal': [True, True, None],
              'Quebec': [True, True, 'Atlantic ocean'], 'Vancouver': [True, True, 'Pacific ocean'],
              'Victoria': [False, True, 'Salish sea']}
    sights = {'Parliament building of Canada': [
        "The architectural complex, which hosts working meetings of the Canadian government, looks like a medieval castle from the outside. "
        "It is located in a convenient location for travelers - in the heart of Ottawa. "
        "The gray stone from which the building is built seems gloomy at first glance. "
        "However, the overall composition of the building is so precise and accurate that the complex inspires involuntary respect. "
        "It seems that the architects who built the complex in 1860 were fanatically devoted to the idea of symmetry in architecture."
        "The pointed towers are located strictly symmetrically with respect to the central column, on which the clock runs, visible from everywhere. "
        "The strength of the building is evidenced by the fact that the gray stone is also covered with copper plates. "
        "However, in 1916 the building did not survive the devastating fire. "
        "Reconstruction work was carried out in an organized manner, but they dragged on until 1922.",
        'https://cdn.britannica.com/29/179429-050-EDBCAE49/Parliament-Buildings-Ottawa.jpg'],
        'Oratory of St. Joseph': [
            "Among those sights that you must visit in Canada is the Oratory of St. Joseph. Construction work began in 1904. "
            "The initiative of the project belongs to André Bessette. "
            "The original version of the oratorio was a small chapel that nestled comfortably on the slopes of Mont Royal next to Notre Dame College. "
            "The church quickly became popular, the number of parishioners increased every year. "
            "Therefore, already in 1917, a church for 1000 people was built here."
            "The church keeps the memory of many miracles performed by Brother Andre Bessette. "
            "It is significant that Pope John Paul II recognized the miracles that are attributed to brother Andrew. "
            "The recognition took place in 1982, and already in 2010 the canonization of brother Andrei took place. "
            "He was canonized by Pope Benedict XVII.",
            'https://dynamic-media-cdn.tripadvisor.com/media/photo-o/18/2c/de/a9/photo0jpg.jpg?w=1200&h=1200&s=1'],
        'Niagara Falls': ["Niagara Falls is included in the list of natural attractions in Canada. "
                          "In addition, it is considered one of the wonders of the world. "
                          "The waterfall is located on the border of Canada and America. "
                          "With a terrifying roar, tons of water flows powerfully rush every second. "
                          "The waterfall is located in a dense cloud of spray, since the water pressure here is quite strong. "
                          'This is fully true, since a giant water stream falls from a 50-meter height. '
                          'Millions of travelers come here to see this unique natural phenomenon with their own eyes.',
                          'https://cdn.britannica.com/30/94430-050-D0FC51CD/Niagara-Falls.jpg']}
    beaches = {'Wasaga Beach': [
        "The longest freshwater beach in the world, attracting tourists with its 12 km of sandy coastline. "
        "The warm, shallow waters of the beach are ideal for swimming, while the soft white sand is ideal for picnicking, "
        "relaxing and watching the beautiful sunset. This urban beach, which is somewhat reminiscent of the famous beaches in Florida: "
        "Daytona Beach and Fort Lauderdale.",
        'https://a.travel-assets.com/findyours-php/viewfinder/images/res70/83000/83440-Wasaga-Beach-Provincial-Park.jpg'],
        "Brady’s Beach": [
            "Bradis Beach is located in a very secluded area on the Pacific Ocean. The only way to get here is by ferry, plane or timber barge. "
            "Yes, the path is not easy, but the rest here is worth such a voyage. Try to be there during the Music by The Sea festival. "
            "By August, the water here warms up to temperatures suitable for a refreshing swim. "
            "The advantages of this beach are that it is surrounded by the Pacific Rim National Park, the ocean, and the territory of the Indians. "
            "Excellent diving. Proximity to Barkley Sound islands inhabited by sea lions and bald eagles.",
            "https://i.pinimg.com/originals/7a/a9/8e/7aa98ea42f317f0d87f38eac822fe7ab.jpg"],
        'Ingonish Beach': [
            "Ingonish Beach is the only beach in the Cape Breton Highlands National Park, with a unique opportunity to swim in both fresh and sea water. "
            "This sandy beach is washed away in winter and washed back by waves every spring, and a natural barrier separates the lake from the waters of the Atlantic Ocean. "
            "In addition to swimming, here you will be offered to go on a boat trip to go fishing and, of course, watch the whales in their habitat.",
            'https://i0.wp.com/anotherwalkinthepark.com/wp-content/uploads/2015/01/briarisland_capebreton_canon-1503.jpg?ssl=1']}
    mountains = {
        'Robson': ['The highest point of the Rocky Mountains; it is also the highest point of the Canadian Rockies. '
                   'The mountain is located within the Robson Provincial Park in British Columbia.',
                   'https://s9.travelask.ru/system/images/files/001/326/820/wysiwyg_jpg/x1l4g1t1xa911.jpg?1560886998'],
        'Temple': ['Mountain in Banff National Park in the Canadian Rockies, the 7th highest peak in Alberta. '
                   'The Temple is located in the Bow River Valley between Paradise Creek and Moraine Creek and is the highest point in the Lake Louise region.',
                   'https://upload.wikimedia.org/wikipedia/commons/thumb/9/98/Mount_Temple.jpg/640px-Mount_Temple.jpg'],
        'Snow House': [
            'A mountain on the continental divide of the Columbia Icefield on the border of Banff and Jasper National Parks. '
            'Located in the Canadian Rockies on the border of British Columbia and Alberta. The height of the peak is 3456 m.',
            'https://img2.goodfon.com/wallpaper/nbig/8/55/winter-landscape-snow-zima-3936.jpg'],
        'Assiniboine': [
            'Pyramidal mountain located on the American Continental Divide on the border of the Canadian provinces of Alberta and British Columbia. '
            'The height is 3618 m above sea level.',
            'https://offtracktravel.ca/wp-content/uploads/2020/03/viewpoint-mount-assiniboine-sunburst-bc-1000x750.jpg']}
    skiResorts = {'Whistler Blackcomb': ['At the heart of Whistler and Blackcomb is the charming village of Whistler. '
                                         "You don't even have to ski to enjoy your trip to Whistler, but if you do, you'll find "
                                         'seemingly limitless terrain that can accommodate any level of skier, from first timers to extreme skiers. '
                                         "You'll find beautiful wide-open bowls at Mount Whistler and incredible groomed runs on both mountains. "
                                         "On Blackcomb, the Horstmann Glacier offers year-round skiing.",
                                         'https://skibookings.com/wp-content/uploads/201712_wb_paulmorrison_village_064.jpg'],
                  'Lake Louise': [
                      "Lake Louise, in the heart of the Rocky Mountains and less than an hour from the city of Banff, is one of Canada's most famous resorts. "
                      "From the slopes, majestic scenery stretches over the Luke Valley and the surrounding mountains and beyond to the palatial Fairmont Chateau Lake Louise. "
                      "This is a mountain for all skiers, from extreme skiers to families coming here to learn about the sport. "
                      "In a resort with 4,200 acres of rocky terrain, the resort offers a combination of wide-open bowls, steepness, flumes and plenty of groomed trails."
                      "The Lake Louise Ski Resort doesn't have an onsite location, but it does have fantastic daytime facilities at the base, as well as restaurants serving delicious food, "
                      "as well as other restaurants in the mountains. Skiers can take a dip in the nearby village of Lake Louise or the town of Banff.",
                      'https://skitheworld.com/wp-content/uploads/2018/12/LAke-louise-ski-village.jpg'],
                  'Revelstoke': [
                      "Located in the interior of British Columbia, about 2.5 hours from the city of Kelowna, Revelstoke is a bit harder to get to some resorts, but well worth it. "
                      "The mountain sees a large number of powder days; few crowds; and offers great terrain, from open bowls to tree trails and starter areas. "
                      "Add to that the affordable accommodation options in Revelstoke; ski slopes, ski slopes on the mountain; and fabulous mountain scenery and it's hard to beat this resort. "
                      "This is not the place for a glamorous five-star experience or shopping experience. It is a mountain of skiers and a great place for families.",
                      'https://dynamic-media-cdn.tripadvisor.com/media/photo-o/0e/34/81/6a/the-sutton-place-hotel.jpg?w=700&h=-1&s=1']}
    lakes = {'Louise': [
        "A natural wonder of Banff National Park. Lies surrounded by the Rocky Mountains and the bright greenery of the forest, at an altitude of 1646 meters. "
        "The unusual emerald color of the water is due to the presence of rock particles brought into the lake by glaciers. The area of the lake is 0.8 km2. "
        "On the shore there is a 5-star hotel, a number of campsites and tourist centers, nearby is the famous ski resort. "
        "Hiking and cycling routes are organized around the reservoir. Canoe excursions are available.",
        'https://dynamic-media-cdn.tripadvisor.com/media/photo-o/01/25/ce/47/moraine-lake.jpg?w=700&h=-1&s=1'],
        'Moraine': ["One of the most beautiful and photographed lakes in the world. Business card of Canada. "
                    "Its stunning landscapes can be found in many magazines and catalogs, on Canadian currency, Windows screensaver, etc. "
                    "It lies in the Valley of the Ten Peaks of the famous Banff Park, at an altitude of 1885 meters. "
                    "Origin - glacial. The area is 0.5 km2. Routes have been laid out for tourists, it is better to move along them with an experienced guide. "
                    "A hotel was built on the shore, there is a boat rental.",
                    'https://media-cdn.tripadvisor.com/media/photo-s/10/23/d3/72/moraine-lake.jpg'],
        'Superior': [
            'The largest in terms of area in the composition of the Great Five and among the fresh lakes of the world. '
            'Located in Canada and the USA. It occupies an area of 82.7 thousand km2. The shores are indented, there are large bays, islands. '
            'There are many parks on the lake, a marine reserve has been created. The water is cold, even in summer it does not exceed 4 ° C, in winter it does not freeze due to frequent storms. '
            'The lake is rich in fish. Navigable. The major port is Thunder Bay. The southern part of the reservoir is known as the graveyard of ships.',
            'https://webmandry.com/wp-content/uploads/2019/07/Samye-bolshie-ozera-kakoe-samoe-bolshoe-ozero-v-mire-2-Verhnee.jpg']}
    rivers = {'Yukon': ["One of the largest rivers of the North American continent originates in Lake Marsh. "
                        "Most of the Yukon is located in the United States, but the source is located in the Canadian province of the same name. "
                        'A tributary of the Yukon, the Klondike, is famous for the gold rush of the 20th century. '
                        'Almost the entire river is located in the subarctic climate zone, but in the Canadian part of the Yukon it is much warmer than in the north.'
                        'The total length of the river is 3190 km.',
                        'https://www.worldatlas.com/r/w768/upload/5f/53/53/shutterstock-7670922581.jpg'],
              'Colombia': ["The source of the river is Lake Columbia in the Rocky Mountains. "
                           "Due to its fast current and large elevation difference, Colombia is actively used to generate electricity. "
                           "In total, there are 14 hydroelectric power stations on it. The river is a spawning ground for many species of salmon. "
                           "Dams and hydroelectric power stations prevent the advancement of both adults and fry, but all power plants have fish passages, "
                           "and fry are in some cases transported to the ocean by the US Army. "
                           "The total length of the river is 2000 km.",
                           'https://www.americanrivers.org/wp-content/uploads/2016/03/Columbia-River-Credit-Alan-Majchrowicz-header.jpg'],
              'Churchill': [
                  "Thanks to an artificial canal built in the 20th century, most of the water from the Churchill River goes to Saskatchewan to increase hydroelectric power generation. "
                  "The river originates in the central part of the province of Saskatchewan and carries its waters east to Hudson Bay. "
                  "The rich flora and fauna of the river basin was the reason for its nomination for inclusion in the List of Protected Rivers of Canada.",
                  'https://media.socastsrm.com/wordpress/wp-content/blogs.dir/900/files/2022/05/churchill-falls-1969-heritage-nl.jpg']}
    universities = {'Ottawa': ['Carleton University', 'University of Ottawa'],
                    'Toronto': ['York University', 'University of Toronto'],
                    'Montreal': ['Montreal University', 'Polytechnique Montreal'],
                    'Quebec': ['Laval University', 'TELUQ University'],
                    'Vancouver': ['University of British Columbia', 'University Canada West']}
    faculties = {'Carleton University': ['Faculty of Arts', 'Faculty of Computer Engineering and Software',
                                         'Faculty of Education',
                                         'Faculty of Law', 'Faculty of Science', 'Faculty of Social Sciences'],
                 'University of Ottawa': ['Faculty of Arts', 'Faculty of Engineering', 'Faculty of Education',
                                          'Faculty of Science', 'Faculty of Medicine', 'Faculty of Law',
                                          'Faculty of Social Sciences'],
                 'York University': ['Faculty of Education', 'Faculty of Arts', 'Faculty of Medicine',
                                     'Faculty of Science'],
                 'University of Toronto': ['Faculty of Arts', 'Faculty of Science', 'Faculty of Medicine'],
                 'Montreal University': ['Faculty of Arts', 'Faculty of Science', 'Faculty of Law',
                                         'Faculty of Medicine',
                                         'Faculty of Education'],
                 'Polytechnique Montreal': ['Faculty of Computer Engineering and Software', 'Faculty of Science',
                                            'Faculty of Medicine'],
                 'Laval University': ['Faculty of Arts', 'Faculty of Law', 'Faculty of Education',
                                      'Faculty of Forestry', 'Faculty of Medicine'],
                 'TELUQ University': ['Faculty of Arts', 'Faculty of Science', 'Faculty of Medicine'],
                 'University of British Columbia': ['Faculty of Economics', 'Faculty of Forestry',
                                                    'Faculty of Education',
                                                    'Faculty of Science', 'Faculty of Medicine', 'Faculty of Law'],
                 'University Canada West': ['Faculty of Arts', 'Faculty of Computer Engineering and Software',
                                            'Faculty of Education',
                                            'Faculty of Law', 'Faculty of Science', 'Faculty of Social Sciences']}
    programs = {'Carleton University': ['Magistracy', 'Undergraduate'],
                'University of Ottawa': ['Magistracy', 'Undergraduate'],
                'York University': ['Magistracy', 'Undergraduate'],
                'University of Toronto': ['Foundation', 'Undergraduate', 'MBA'],
                'Montreal University': ['Magistracy', 'Undergraduate'],
                'Polytechnique Montreal': ['Magistracy', 'Undergraduate'],
                'Laval University': ['Magistracy', 'Undergraduate'],
                'TELUQ University': ['Magistracy', 'Undergraduate'],
                'University of British Columbia': ['Magistracy', 'Undergraduate', 'MBA'],
                'University Canada West': ['Magistracy', 'Undergraduate']}
    links = {'Carleton University': 'https://carleton.ca',
             'University of Ottawa': 'https://www.uottawa.ca/en',
             'York University': 'https://www.yorku.ca',
             'University of Toronto': 'https://www.utoronto.ca',
             'Montreal University': 'https://www.umontreal.ca/en',
             'Polytechnique Montreal': 'https://www.polymtl.ca',
             'Laval University': 'https://www.ulaval.ca/en',
             'TELUQ University': 'https://www.teluq.ca',
             'University of British Columbia': 'https://www.ubc.ca',
             'University Canada West': 'https://www.ucanwest.ca'}
    images = {'Carleton University': 'https://mtarch.com/wp-content/uploads/2012/06/River01-640x632.jpg',
              'University of Ottawa': 'https://www.timeshighereducation.com/sites/default/files/institution/header_image/times_higner_education_profile_header_1950x700_v1.jpg',
              'York University': 'https://www.timeshighereducation.com/sites/default/files/institution/header_image/vari-drone.jpeg',
              'University of Toronto': 'https://upload.wikimedia.org/wikipedia/commons/b/b4/Uoft_universitycollege.jpg',
              'Montreal University': 'https://www.timeshighereducation.com/sites/default/files/styles/the_breaking_news_image_style/public/university_of_montreal.jpg?itok=nvpq29hR',
              'Polytechnique Montreal': 'https://www.letudiant.fr/uploads/mediatheque/ETU_ETU/1/9/1723919-polytechnique-montreal-1-3-original.jpg',
              'Laval University': 'https://frenchitalian.washington.edu/sites/frenchitalian/files/styles/large/public/images/u_laval_quebec.png?itok=S64NOYC-',
              'TELUQ University': 'https://upload.wikimedia.org/wikipedia/commons/2/29/T%C3%89LUQ_panorama.jpg',
              'University of British Columbia': 'https://dynamic-media-cdn.tripadvisor.com/media/photo-o/10/1b/0f/b6/irving-k-barber-learning.jpg?w=1200&h=-1&s=1',
              'University Canada West': 'https://www.ucanwest.ca/wp-content/uploads/2022/04/UCW-Vancouver-House-Campus-3.jpg'}
    hostel = {'Carleton University': 'Yes',
              'University of Ottawa': 'Yes',
              'York University': 'Yes',
              'University of Toronto': 'Yes',
              'Montreal University': 'Yes',
              'Polytechnique Montreal': 'No',
              'Laval University': 'No',
              'TELUQ University': 'No',
              'University of British Columbia': 'Yes',
              'University Canada West': 'Yes'}
    scolarship = {'Carleton University': 'Yes',
                  'University of Ottawa': 'Yes',
                  'York University': 'Yes',
                  'University of Toronto': 'Yes',
                  'Montreal University': 'Yes',
                  'Polytechnique Montreal': 'No',
                  'Laval University': 'No',
                  'TELUQ University': 'No',
                  'University of British Columbia': 'Yes',
                  'University Canada West': 'Yes'}
    requirements = {'Carleton University': 'Four years of English. '
                                           'Three or more years of mathematics. '
                                           'Two or more years of science. '
                                           'Three or more years of social science.',
                    'University of Ottawa': 'An admissions application (you can apply online). '
                                            'A $75 application fee. '
                                            'All official undergraduate transcripts (3.0 GPA - minimum requirement)'
                                            'A Graduate School Admission Essay/Personal Statement - This is a two-page essay focused on professional career development.',
                    'York University': 'For Ontario high school students, the minimum admission requirement is the completion of the Ontario Secondary School Diploma (OSSD) or equivalent and six 4U/M courses, including ENG4U. '
                                       'Students may also be required to fulfill Faculty or program-specific prerequisites.'
                                       'Francophone applicants may present FRA4U.You must successfully complete the OSSD, including six 4U/M courses and all of the prerequisites for your programs, and maintain the average used for conditional admission.',
                    'University of Toronto': 'Entry requirements for international students are based on current high school grades. '
                                             'The average score sufficient for admission should be at least 75-80% of the maximum possible. '
                                             'The age limit is at least 17 years old. '
                                             'English at IELTS level minimum 6.5 or TOEFL iBT 100+',
                    'Montreal University': 'To secure admission at UdeM, international students are required to have a minimum GPA of 3.0 i.e 85% for UG programs, and a GPA of 3.3 i.e 88% for PG programs.y',
                    'Polytechnique Montreal': 'A certified or official French or English translation is required for any documentation not written in French or English. A copy of original documents as well as their official translations must be provided.'
                                              ' All documentation provided becomes property of Polytechnique Montréal and will not be returned to the applicant.',
                    'Laval University': 'You must hold the minimum diploma required for the level of studies you are pursuing and demonstrate an adequate level of French proficiency.',
                    'TELUQ University': 'When applying for admission to Tele-Universite TELUQ in Canada you should prepare all required documents. '
                                        'Request a list of necessary documents directly from a university, as it may vary for different countries. '
                                        'Using our live chat, you can also ask for sample documents.',
                    'University of British Columbia': 'Graduation from high school. '
                                                      'Minimum of 70% in Grade 11 or Grade 12 English (or their equivalents)'
                                                      'At least six academic/non-academic Grade 12 courses (recommended, but not required)',
                    'University Canada West': "Usually, the university accepts a bachelor's degree in BBA/BCom or its equivalent and a minimum of three years of documented professional or management experience with evidence of career progression. "
                                              "The English language requirement includes an overall IELTS score of 6.5 with at least 6.0 in Writing."}

    costs = {'Carleton University': 18911,
             'University of Ottawa': 19041,
             'York University': 20102,
             'University of Toronto': 34045,
             'Montreal University': 18400,
             'Polytechnique Montreal': 23000,
             'Laval University': 18151,
             'TELUQ University': 17256,
             'University of British Columbia': 38946,
             'University Canada West': 19624}
    # currency
    currencyName = 'CAD'
    currencyEqualsToDollar = 1.33

    # military
    milPolBlock = "NATO"
    amountOfPeopleInArmy = 92000

    # healthcare
    numberOfDoctorsPer100kPopulation = 241
    menAverageLifeExpectancy = 78.8
    womenAverageLifeExpectancy = 84.1

    # climat
    juneAverageTemperature = 20
    decemberAverageTemperature = 4.5
    averageHumidity = 73
    averageDurationOfWinter = 3.5
    averageRainfallPerMonth = 104
    averageNumberOfFoggyDaysPerYear = 47
    averageNumberOfRainyDaysPerYear = 63
    averageNumberOfClearDays = 119

    # Man-made disasters
    nameMMD = '0'
    typeOfMMD = '0'
    aomuntOfDeadPeople = 0
    aomuntOfInjuredPeople = 0
    territoryOfPollution = 0
    # manMadeDisaster = {'name': 'Авария на ЧАЭС', 'typeOfMMD': 'Авария на АЭС', 'aomuntOfDeadPeople': 37500,
    #                    'aomuntOfInjuredPeople': 5000000, 'territoryOfPollution': 145000}

    # security
    situationInTheCountry = 3  # [1, 3] 1-bad, 3-good
    freedomOfSpeech = 3  # [1, 3]
    assessmentOfFamilyLife = 3  # [1, 3]
    attitudeTowardsLGBT = 3  # [1, 3]

    # population
    populationCount = 38010000
    procentOfMales = 49.6
    procentOfFemales = 50.4
    populationDensityPerSquareKilometer = 4.2
    speedOfLife = 3  # [1, 3]
    workPlaces = 3  # [1, 3]
    nightLifeEntertainment = 3  # [1, 3]

    # citizenship
    citizenshipGlobalRank = 5
    friendlyToForeigners = 2

    # communication
    communicationOnEnglish = 3  # [1, 3]

    # transport
    averageTravelTimeToWork = 54
    developmentLevelOfPublicTransport = 3  # [1, 3]

    # internet
    speedOfInternetMbps = 52.4  # Мегабиты в секунду
    freeWifi = 2  # [1, 3]

    # education
    rankingOfNationalEducationSystem = 7

    cc.createBase(countryName, cities, officialLanguage,
                  # currency
                  currencyName, currencyEqualsToDollar,
                  # military
                  milPolBlock, amountOfPeopleInArmy,
                  # healthcare
                  numberOfDoctorsPer100kPopulation, menAverageLifeExpectancy, womenAverageLifeExpectancy,
                  # climat
                  juneAverageTemperature, decemberAverageTemperature, averageHumidity,
                  averageDurationOfWinter, averageRainfallPerMonth, averageNumberOfFoggyDaysPerYear,
                  averageNumberOfRainyDaysPerYear, averageNumberOfClearDays,
                  # security
                  situationInTheCountry, freedomOfSpeech,
                  assessmentOfFamilyLife, attitudeTowardsLGBT,
                  # population
                  populationCount, procentOfMales, procentOfFemales, populationDensityPerSquareKilometer,
                  speedOfLife, workPlaces, nightLifeEntertainment,
                  # citizenship
                  citizenshipGlobalRank,
                  # communication
                  communicationOnEnglish,
                  # transport
                  averageTravelTimeToWork, developmentLevelOfPublicTransport,
                  # internet
                  speedOfInternetMbps, freeWifi,
                  # education
                  rankingOfNationalEducationSystem, universities, faculties, programs, costs, links, images,
                  requirements,
                  hostel, scolarship, sights, beaches, mountains, skiResorts, lakes, rivers, friendlyToForeigners
                  )
    #############################   CANADA   #############################
    #############################   United Arab Emirates   #############################

    # Country
    countryName = "United Arab Emirates"
    officialLanguage = "Arabic"

    # cities    name   isBig  washesBy
    cities = {'Abu Dhabi': [True, True, 'Persian Gulf'], 'Dubai': [True, True, 'Persian Gulf'],
              'Sharjah': [True, True, 'Persian Gulf'],
              'Al Ain': [True, False, None], 'Ajman': [True, True, 'Persian Gulf'],
              'Fujairah': [False, True, 'Gulf of Oman']}

    # education
    universities = {'Dubai': ['Murdoch University Dubai'],
                    'Abu Dhabi': ['Abu Dhabi University', 'Khalifa University'],
                    'Sharjah': ['American University of Sharjah']}
    faculties = {'Abu Dhabi University': ['Faculty of Arts', 'Faculty of Economics', 'Faculty of Engineering',
                                          'Faculty of Medicine', 'Faculty of Law'],
                 'Khalifa University': ['Faculty of Arts', 'Faculty of Engineering', 'Faculty of Medicine'],
                 'Murdoch University Dubai': ['Faculty of Computer Engineering and Software', 'Faculty of Economics',
                                              'Faculty of Social Sciences'],
                 'American University of Sharjah': ['Faculty of Arts', 'Faculty of Computer Engineering and Software',
                                                    'Faculty of Engineering',
                                                    'Faculty of Medicine', 'Faculty of Science']}
    programs = {'Abu Dhabi University': ['Magistracy', 'Undergraduate'],
                'Khalifa University': ['Magistracy', 'Undergraduate'],
                'Murdoch University Dubai': ['Magistracy', 'Undergraduate'],
                'American University of Sharjah': ['Magistracy', 'Undergraduate']}
    links = {'Abu Dhabi University': 'https://www.adu.ac.ae',
             'Khalifa University': 'https://www.ku.ac.ae',
             'Murdoch University Dubai': 'https://www.murdochuniversitydubai.com',
             'American University of Sharjah': 'https://www.aus.edu'}
    images = {'Abu Dhabi University': 'https://assets.wam.ae/uploads/2020/06/2314327737839258810.jpg',
              'Khalifa University': 'https://www.ku.ac.ae/wp-content/uploads/2020/09/Khalifa-University-Campus-at-Night-1.jpg',
              'Murdoch University Dubai': 'https://smapse.ru/storage/2020/03/murdoch-university-dubai-smapse14.jpg',
              'American University of Sharjah': 'https://i.dawn.com/primary/2022/06/62971f912ce9d.png'}
    hostel = {'Abu Dhabi University': 'Yes',
              'Khalifa University': 'Yes',
              'Murdoch University Dubai': 'Yes',
              'American University of Sharjah': 'Yes'}
    scolarship = {'Abu Dhabi University': 'Yes',
                  'Khalifa University': 'Yes',
                  'Murdoch University Dubai': 'Yes',
                  'American University of Sharjah': 'Yes'}
    requirements = {
        'Abu Dhabi University': 'During the application process, the admissions committee will evaluate academic performance from the school or college. '
                                'To be admitted to the University of Abu Dhabi, you must also pass exams for the chosen faculty. '
                                'In the process of learning, students learn the program of one course in two semesters, on the basis of which the academic year is formed.',
        'Khalifa University': 'For admission, it is required to provide the admission committee with a document on basic education, on the basis of the average score of which a decision will be made on further passing the examination. '
                              'Each faculty appoints its own set of examinations. The success of passing these tests serves as a guarantee of enrollment in Khalifa University.',
        'Murdoch University Dubai': 'Certificate of general secondary education. '
                                    'TOEFL certificate confirming the required level of a foreign language (min. 550/CAT 213 or 4.0 TWE or Internet Based 79-80/w24). '
                                    'Two letters of recommendation from high school teachers. '
                                    'In addition, you need to pay: Registration , Margin, Package of visa documents, Medical insurance.',
        'American University of Sharjah': 'An official high school diploma certified by the appropriate authorities: an American high school diploma - a minimum of B or 80% of the final grade (12th grade)'
                                          ' or the average of the best two years in 10th, 11th and 12th grades; British high school diploma - 5 subjects IGCSE / GCSE (level O) and two subjects GCE (level AS / A);'
                                          ' IB diploma in six subjects (excluding Islamic education) - a minimum of 24 points; German Abitur - minimum score of 7 in the last year. '
                                          'Official progress reports for the last three years of high school, certified by the relevant authorities. '
                                          'Color scan of the passport. '
                                          'English proficiency test results: IELTS Academic - 6.5, TOEFL iBT - 80, TOEFL iTP - 550, Cambridge English - 176, EmSAT Achieve-English - 1550.'}
    costs = {'Abu Dhabi University': 11000,
             'Khalifa University': 7000,
             'Murdoch University Dubai': 42200,
             'American University of Sharjah': 22200}
    sights = {'Burj Khalifa': [
        "What is the first thing that comes to mind when talking about the sights of the UAE? Of course, the grandiose Burj Khalifa. "
        "According to the project, this building was originally planned to be the tallest in the world, "
        "its height was kept secret until the end so that it could be adjusted if the building was designed higher. "
        "The height of this truly huge skyscraper is 828 m (163 floors), which is 196 m higher than the Shanghai Tower, which is 632 m high."
        "Inside this huge building, in addition to the hotel, there are apartments, a huge number of shopping centers and offices. "
        "The highest observation deck is located at an altitude of 472 m. The air inside the Dubai Tower, in addition to cooling, is additionally flavored. "
        "Not far from the skyscraper are the highest singing fountains in the world, which are an unusually beautiful sight.",
        'https://luxeadventuretraveler.com/wp-content/uploads/2012/12/Luxe-Adventure-Traveler-Dubai-Burj-Khalifa-6.jpg'],
        'Palm Islands': ["The Palm Islands can rightly be considered the eighth wonder of the world. "
                         "Of all that has been built by man, only this artificial archipelago and the Great Wall of China are visible from space. "
                         "This place is a business center, today it is the center of tourism of the entire Persian Gulf."
                         "The archipelago is made up of three attractions of the UAE - islands that look like date palms. "
                         "This plant is especially revered in Islam. "
                         "The largest of the artificial islands is Palm Deira, the Palm Jebel Ali and Jumeirah are slightly more modest in size. "
                         "Following the terminology, it would be more correct to call the Palms peninsulas, since they are connected to the coastline by their trunks. "
                         "The crown of each island is a crescent - a symbol of the Islamic religion. "
                         "The islands are protected from the water by barrier reefs, on which quotes from the poems of Sheikh Dubai are carved.",
                         'https://cdn.hswstatic.com/gif/dubai-palm-island-1.jpg'],
        'Singing Fountains': ["Singing fountains in Dubai are a symbol of wealth and prosperity of the country. "
                              "The complex is located in the center of the pool area of 12 hectares. "
                              "The pool is decorated with mosaics and is located next to the Burj Khalifa, the tallest skyscraper. "
                              "The pond is illuminated by a huge number of spotlights. The height of the jet during the performance reaches 150 meters. "
                              "Such power is provided by water cannons, which make a sound similar to a shot."
                              " Guns, pumps and music are controlled by a program that was developed specifically when creating the fountain. "
                              "Powerful acoustic systems are located around the entire pool. "
                              "They accompany the water dance with various songs in Arabic and English. "
                              "In total, about 20 compositions are performed per day without repetitions. "
                              "Only at the very beginning of the performance a song in honor of the capital sounds.",
                              'https://www.taritravel.com/upload/medialibrary/21b/21bb5ac705f6abad5813f7991efdb091.jpg']}
    beaches = {'Cornish': [
        "Corniche Beach is located in the largest emirate and, at the same time, in the city of the same name, which is the capital of the UAE - in Abu Dhabi. "
        "Corniche Beach is called one of the symbols of Abu Dhabi - the infrastructure is well developed here, the surroundings are clean, there is a constant flow of tourists. "
        "There are no high waves here due to the nearby islands of Al Lulu and Al Marin. "
        "The promenade, about 5 km long, has everything you need to enjoy your vacation by the sea: "
        "here you can rent beach equipment, have fun on the rides, try international cuisine in coastal restaurants and cafes. "
        "Along the beach there are hotels that meet high standards and skyscrapers, which gives the beach a certain charm. "
        "There are three zones on the beach. There are paid and free. "
        "The beach and the sea are the same there, but there is still a difference: "
        "in paid areas you can rent sun loungers and towels, and there are also more local cafes and restaurants, beautiful small gardens with palm trees and flowers. "
        "The third zone is a special area for families - Family Beach Section. You have to pay to enter there, but this family corner is worth it.",
        'https://media.cntraveller.com/photos/611be91fa86777b29fbc4f00/16:9/w_2580,c_limit/beach-at-porthcurno-saint-levan-cornwall-conde-nast-traveller-18aug16-alamy.jpg'],
        "Saadiyat": [
            "Saadiyat Beach is located on the artificial island of the same name, 5 kilometers from the UAE capital Abu Dhabi. "
            "The beach area has a length of 9 km. There is white soft sand, nice waves."
            " The beach has a calm atmosphere and allows you to relax from the bustle of the city. "
            "The beach itself can be divided into a public beach, party and a beach from hotels. "
            "We note right away that the hotels on this beach are mostly luxury. "
            "All areas on Saadiyat Beach are paid: the cheapest vacation is on the public beach, the most expensive is the beach of the Hyatt Hotel. "
            "Saadiyat has a huge selection of entertainment: water rides, yachts, surfing. "
            "For those who relax in the club or hotel zone, there is an opportunity to visit swimming pools, spas, fitness centers, elite restaurants and bars.",
            'https://fs.tonkosti.ru/0g/91/0g91mdjb4lzww8s0gkggwgoo0.jpg'],
        'Jumeirah': [
            "Jumeirah Beach is the largest and most visited beach in Dubai, which includes several smaller beaches. "
            "It is named after the area that bears the same name and stretches for 20 km. "
            "The beaches succeed each other in a chain: first private, then public. "
            "The prices here are very different: you can relax on the free Jumeirah Open Beach, and on the beach at the Jumeirah Beach Hotel. "
            "The peculiarity of the beach is the view of the 7-star Burj Arab hotel. "
            "Everyone who stays at Jumeirah Beach does not miss the opportunity to take a picture against the backdrop of the sail hotel. "
            "By the way, because of the hotel, excursions from other Dubai beaches are organized to Jumeirah Beach. "
            "We will tell you about the most popular and best areas of this huge beach.",
            'https://www.timeoutdubai.com/cloud/timeoutdubai/2022/03/15/Dubais-best-beaches.jpg']}
    mountains = {'Jebel Hafeet': [
        "The mountain located mainly in the vicinity of Al Ain, which is located in the Emirate of Abu Dhabi in the UAE. "
        "Part of the mountain is surrounded by the border with Oman, and the peak is located entirely within the United Arab Emirates.",
        'https://dynamic-media-cdn.tripadvisor.com/media/photo-o/1b/b4/6a/9e/abu-dhabi-is-one-of-the.jpg?w=1200&h=-1&s=1'],
        'Jabal Yibir': ["This is one of the best; if not the best mountain drive in UAE. "
                        "Very steep climb and narrow hairpins. Dangerous but Adventurous. "
                        "Won’t recommend to drive along with family though. Once you reached top of the mountain you are blessed with astonishing sceneries. "
                        "Every angle will give you a perfect picture even for amateurs. "
                        "You can see Dubai skyline along with setting sun and the marvelous Burj Khalifa at one view point.",
                        'https://dynamic-media-cdn.tripadvisor.com/media/photo-o/0e/dd/d1/2f/stopover-area.jpg?w=1200&h=-1&s=1'],
        'Jabal Bil Ays': [
            'The mountain in the northwestern Hajar Range in the Musandam province of Oman, and also in Ras Al Khaimah, United Arab Emirates. '
            'The summit has a height of 1934 m.',
            'https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/View_from_Jebel_Jais_-_panoramio.jpg/1200px-View_from_Jebel_Jais_-_panoramio.jpg']}
    skiResorts = {'Ski Dubai': [
        "An amusement park and the first indoor ski resort in the Middle East and one of the largest in the world with an area of about 22.5 thousand m², "
        "covered with artificial snow all year round. Capacity - 1.5 thousand visitors. Located in the Mall of the Emirates.",
        'https://static.toiimg.com/photo/40367677.cms']}
    lakes = {}
    rivers = {}
    # currency
    currencyName = 'DH'
    currencyEqualsToDollar = 3.67

    # military
    milPolBlock = 'None'
    amountOfPeopleInArmy = 63000

    # healthcare
    numberOfDoctorsPer100kPopulation = 326
    menAverageLifeExpectancy = 78
    womenAverageLifeExpectancy = 80.7

    # climat
    juneAverageTemperature = 31.5
    decemberAverageTemperature = 20.5
    averageHumidity = 55
    averageDurationOfWinter = 0
    averageRainfallPerMonth = 7.4
    averageNumberOfFoggyDaysPerYear = 11
    averageNumberOfRainyDaysPerYear = 13
    averageNumberOfClearDays = 287

    # security
    situationInTheCountry = 3  # [1, 3] 1-bad, 3-good
    freedomOfSpeech = 1  # [1, 3]
    assessmentOfFamilyLife = 2  # [1, 3]
    attitudeTowardsLGBT = 1  # [1, 3]

    # population
    populationCount = 9991000
    procentOfMales = 69.5
    procentOfFemales = 30.5
    populationDensityPerSquareKilometer = 122.1
    speedOfLife = 3  # [1, 3]
    workPlaces = 3  # [1, 3]
    nightLifeEntertainment = 3  # [1, 3]

    # citizenship
    citizenshipGlobalRank = 15
    friendlyToForeigners = 2

    # communication
    communicationOnEnglish = 3  # [1, 3]

    # transport
    averageTravelTimeToWork = 36
    developmentLevelOfPublicTransport = 3  # [1, 3]

    # internet
    speedOfInternetMbps = 10.2  # Мегабиты в секунду
    freeWifi = 3  # [1, 3]

    # education
    rankingOfNationalEducationSystem = 51

    cc.createBase(countryName, cities, officialLanguage,
                  # currency
                  currencyName, currencyEqualsToDollar,
                  # military
                  milPolBlock, amountOfPeopleInArmy,
                  # healthcare
                  numberOfDoctorsPer100kPopulation, menAverageLifeExpectancy, womenAverageLifeExpectancy,
                  # climat
                  juneAverageTemperature, decemberAverageTemperature, averageHumidity,
                  averageDurationOfWinter, averageRainfallPerMonth, averageNumberOfFoggyDaysPerYear,
                  averageNumberOfRainyDaysPerYear, averageNumberOfClearDays,
                  # security
                  situationInTheCountry, freedomOfSpeech,
                  assessmentOfFamilyLife, attitudeTowardsLGBT,
                  # population
                  populationCount, procentOfMales, procentOfFemales, populationDensityPerSquareKilometer,
                  speedOfLife, workPlaces, nightLifeEntertainment,
                  # citizenship
                  citizenshipGlobalRank,
                  # communication
                  communicationOnEnglish,
                  # transport
                  averageTravelTimeToWork, developmentLevelOfPublicTransport,
                  # internet
                  speedOfInternetMbps, freeWifi,
                  # education
                  rankingOfNationalEducationSystem, universities, faculties, programs, costs, links, images,
                  requirements,
                  hostel, scolarship, sights, beaches, mountains, skiResorts, lakes, rivers, friendlyToForeigners
                  )

    # cc.createManMadeDisaster(countryName, nameMMD, typeOfMMD, aomuntOfDeadPeople,
    #                           aomuntOfInjuredPeople, territoryOfPollution)
    # cc.createOceans()
    #############################   United Arab Emirates   #############################
    #############################   USA   #############################

    # Country
    countryName = "United States of America"
    officialLanguage = "English"

    # cities    name   isBig  washesBy
    cities = {
        'New York': [True, True, 'Atlantic ocean'],
        'Los Angeles': [True, True, 'Pacific ocean'], 'Chicago': [True, True, None],
        'Houston': [True, False, 'Gulf of Mexico'],
        'Miami': [False, True, 'Atlantic ocean'], 'Hawaii': [False, True, 'Pacific ocean'],
        'Cambridge': [False, False, 'Atlantic ocean'],
        'Palo Alto': [False, False, None]}

    # education
    universities = {'Cambridge': ['Harvard University'],
                    'Palo Alto': ['Stanford University'],
                    'Chicago': ['University of Chicago'],
                    'New York': ['New York University']}
    faculties = {
        'Harvard University': ['Faculty of Arts', 'Faculty of Science', 'Faculty of Engineering',
                               'Faculty of Economics',
                               'Faculty of Social Sciences'],
        'Stanford University': ['Faculty of Economics', 'Faculty of Engineering',
                                'Faculty of Computer Engineering and Software',
                                'Faculty of Science', 'Faculty of Social Sciences', 'Faculty of Medicine',
                                'Faculty of Law'],
        'University of Chicago': ['Faculty of Law', 'Faculty of Social Sciences', 'Faculty of Medicine',
                                  'Faculty of Economics'],
        'New York University': ['Faculty of Arts', 'Faculty of Social Sciences', 'Faculty of Medicine',
                                'Faculty of Law']}
    programs = {'Stanford University': ['Magistracy', 'Undergraduate'],
                'New York University': ['Magistracy', 'Undergraduate', 'MBA'],
                'Harvard University': ['Magistracy', 'Undergraduate'],
                'University of Chicago': ['Magistracy', 'Undergraduate']}
    links = {'Harvard University': 'https://www.harvard.edu',
             'University of Chicago': 'https://www.uchicago.edu',
             'New York University': 'https://as.nyu.edu',
             'Stanford University': 'https://www.stanford.edu'}
    images = {'University of Chicago': 'https://www.pennclub.org/images/dynamic/getImage.gif?ID=100002765',
              'Harvard University': 'https://www.harvard.edu/wp-content/uploads/2021/02/091520_Stock_KS_025-1200x630.jpeg',
              'New York University': 'https://www.usnews.com/dims4/USNEWS/72c90e6/17177859217/resize/800x540%3E/quality/85/?url=https%3A%2F%2Fmedia.beam.usnews.com%2F9d%2Fd819230374ef6531890bb7eee1dac0%2FNYU_WSP_Header.jpg',
              'Stanford University': 'https://www.studylab.ru/upload/Institutions/image/big/28bdde35702ffcfbdcc4f9138a29be10.jpg'}
    # общага
    hostel = {'University of Chicago': 'Yes',
              'Harvard University': 'Yes',
              'New York University': 'Yes',
              'Stanford University': 'Yes'}
    # стипендия
    scolarship = {'University of Chicago': 'Yes',
                  'Harvard University': 'Yes',
                  'New York University': 'Yes',
                  'Stanford University': 'Yes'}
    # требования к поступлению
    requirements = {'University of Chicago': 'IELTS (7.0) or TOEFL (from 104), Application for admission, '
                                             'Officially certified and translated educational documents, Registration fee, '
                                             'Letters of recommendation from teachers, Financial documents, SAT and ACT exam results.',
                    'Harvard University': 'Passing the SAT or ACT exam. The choice is given to the applicant. '
                                          'The SAT is a standard exam that all applicants to higher education institutions in the United States take. '
                                          'Consists of 3 parts: mathematics, writing, text analysis. To know how to get into Harvard, you need to know how to take the American Admissions Exam.'
                                          'Apply. You can do this online, the cost of the application is $ 75. '
                                          'The certificate of school education needs to be translated. '
                                          'Passing TOEFL with a minimum of 90 points. '
                                          'The presence of 2 recommendations from teachers. Foreign applicants need a translation. '
                                          'The presence of a report from the school. Intermediate and annual required.',
                    'New York University': 'In this educational institution, education is given in 230 areas. '
                                           'This process is carried out on the basis of 14 14 colleges, schools and institutes. '
                                           'An applicant must leave an application for admission to NYU on the commonapp.org website, '
                                           'while making sure to pay a fee of $ 70, which, no matter the result, will not be returned. '
                                           'Foreigners need to add a certificate guaranteeing their ability to pay. '
                                           'If a student needs a scholarship, the relevant document should be submitted to the selection committee.',
                    'Stanford University': "Stanford University was founded by former California Governor Leland Stanford in 1891. "
                                           "More than 17,000 students study at Stanford, most of them undergraduates and graduate students."
                                           "The main campus was designed by architect and designer Frederick Law Olmstead, who also designed Central Park and Prospect Park in New York. "
                                           "Now the campus is one of the largest in the United States - there are even 24 bus routes on its territory."
                                           "Currently, 17 Nobel laureates, 4 Pulitzer Prize winners, 288 members of the American Academy of Arts and Sciences and 109 members of the National Academy of Engineering work and teach at the university. "
                                           "The university invests heavily in the development of research activities, and also motivates students to create start-ups, some of which are funded by the university and its trustees."
                                           "The 31st US President Herbert Hoover, the founders of high-tech companies: Sergey Brin (Google), "
                                           "William Hewlett and David Packard (Hewlett-Packard), Reed Hastings (Netflix), "
                                           "Mike Krieger (Instagram) studied at Stanford University at different times; and actress Sigourney Weaver."}
    costs = {'University of Chicago': 48759,
             'Harvard University': 28000,
             'New York University': 39000,
             'Stanford University': 54315}

    sights = {'The Statue of Liberty': [
        "For the first time in America, people tend to see all the sights of the United States. "
        "One of the most famous symbols of the country in the world - the Statue of Liberty - is located on a small island in the port of New York. "
        "The majestic sculpture of a woman with a torch in her hand, stretched into the sky, has become the personification of America's freedom. "
        "The crown on her head has seven rays, which means seven continents and seven oceans (according to Western geographical tradition). "
        "In her other hand she holds a slab engraved with the date of the Declaration of Independence. "
        "The monument was made by French masters by order of the US government and sent to the island in parts. "
        "Here, the Americans have already assembled it on a built plinth. "
        "The Statue of Liberty is not only a symbol, but also a functioning lighthouse in New York Harbor. "
        "The height of the statue from the beginning of the pedestal to the top of the torch is 93 meters. "
        "The figure is made of copper plates mounted on a steel frame.",
        'https://www.history.com/.image/ar_16:9%2Cc_fill%2Ccs_srgb%2Cfl_progressive%2Cq_auto:good%2Cw_1200/MTY1MTc1MTk3ODI0MDAxNjA5/topic-statue-of-liberty-gettyimages-960610006-promo.jpg'],
        'Central park': [
            "The sights of the United States are of great interest to tourists. New York's Central Park occupies a special place among them. "
            "It is an oasis of calm in the bustling business flow of Manhattan. The green zone is 4 km long and 800 meters wide. "
            "The opening of the park took place in 1859. Tens of thousands of workers ennobled the territory for another 20 years. "
            "About 5 million trees were planted, and the land was brought from ecologically clean areas. "
            "Now the park has a whole recreation infrastructure. "
            "These are various playgrounds, attractions, skating rinks and just lawns for a picnic.",
            'http://askandgo.ru/images/poi/2990.jpg'],
        'White House': ["US attractions are represented by a very extensive list. "
                        "But the most important of them in terms of the history of executive power is, of course, the White House. "
                        "It is a symbol of America's democracy. The residence of the rulers of the country is named after the color of the building itself. "
                        "This is one of the main attractions in the United States, and every year about one and a half million tourists"
                        " flock to the capital to see the grandeur and beauty of the world-famous building. "
                        "The President's House is also a museum of both history and art history. "
                        "The interior of the building contains old canvases, antique furniture and household items. "
                        "Of particular interest among tourists is the gallery of paintings, which depict all the presidents of the country and their wives. "
                        "Tours are free, but you need to sign up six months in advance. "
                        "Despite the accessibility, there are employees of the US Secret Service in the building itself and along its perimeter.",
                        'https://www.rd.com/wp-content/uploads/2017/12/this-is-why-the-white-house-is-white-119809810-Orhan-Cam-ft.jpg'],
        'Hollywood and Avenue of Stars': [
            "When asked by a tourist what to see in the USA, the answer comes with lightning speed - of course, Hollywood. "
            "Everyone wants to visit the Dream Factory and see with their own eyes the places where legends live and are created. "
            "Most of the film studios are located on the West Side. "
            "In Hollywood, location shooting and film editing are carried out. "
            "It also hosts the Oscars, America's highest award in the film industry. Since 2005, "
            "Hollywood has been recognized as an independent territorial unit. "
            "You can not pass by the famous landmark of the United States - Star Avenue. "
            "It is the symbol of California and the most visited place in America. "
            "The Alley is located in the courtyard of the Grauman Theater and is a complex of concrete slabs with copper stars. "
            "It is on these stars that the names of celebrities are imprinted. There are about 2600 such plates. "
            "The first star appeared back in 1958.",
            'https://thumbs.dreamstime.com/b/famous-hollywood-boulevard-avenue-stars-los-angelos-california-usa-september-147460759.jpg']}
    beaches = {'Siesta Beach': ["The beach located in the Gulf of Mexico on the coast of Florida. "
                                "Siesta Beach has received numerous awards, including being named America's Best Beach in 2011. "
                                " are lifeguards, showers and toilets, snack bars, souvenir shops, picnic tables, gazebos, sun loungers, equipped playgrounds, "
                                "tennis courts and a large parking lot for cars (it is better to arrive early on weekends so that there are no problems with free places). "
                                "The beach stretches along the coast for several kilometers, so there is always free space on it. "
                                "On the beach there is a shower with fresh water, as well as toilets and changing rooms. "
                                "The width of the beach reaches 100 meters, a smooth entrance to the sea, "
                                "the absence of big waves and a gentle shore make the beach a great place to relax with children.",
                                'https://www.siestakeyluxuryrentalproperties.com/wp-content/uploads/2020/07/shutterstock_319854593.jpg'],
               "Poipu Beach Park": [
                   "Popular with visitors and locals alike, this crescent-shaped beach offers crystal-clear waters and occasional Hawaiian monk seal appearances. "
                   "(If you do spot a monk seal, please be mindful by staying at least 100 feet away and no flash photography as they are currently on the endangered species list.)"
                   " With lifeguards, picnic facilities, showers and a natural wading pool for young swimmers, it’s also a great destination for a family beach day. "
                   "There’s a bodyboarding site directly in front of the park for older children and novice adults, a surfing site for experienced surfers and a good reef for snorkeling. "
                   "From December through April, you can sometimes spot humpback whales in the distance.",
                   'https://poipubeach.org/wp-content/uploads/2014/05/poipu-beach-aerial.jpg'],
               'Moonstone Beach': [
                   "Famous for its dramatic coastline and breathtaking views, the Moonstone Beach Boardwalk is where your Cambria seaside escape begins. "
                   "Whether you want to sink your toes into the sand, catch glimpses of marine life swimming by, explore living tide pools, "
                   "or head out to sea for surfing, boating, and other aquatic adventures, you will find there is something for everyone to enjoy on Moonstone Beach. "
                   "Take a relaxing one-mile stroll along the Moonstone Beach Boardwalk. "
                   "Enjoy playful sea otters, watch whales and dolphins in season, "
                   "and spy the wildlife on-shore while taking in the stunning ocean views.",
                   'https://www.hikespeak.com/img/Central-Coast/SLO/Cambria/Moonstone_Beach_Boardwalk_IMG_9185.jpg']}
    mountains = {'Appalachians': [
        "Mountain system in the east of the country, running through Massachusetts, New York, Ohio, Virginia, "
        "Kentucky, Georgia, Alabama and numerous other states. Coal and other minerals are mined here. "
        "The average height of the mountains in the system is no more than a kilometer above sea level. "
        "The highest eastern point in the United States is Mount Mitchell in North Carolina. "
        "It rises more than 2 thousand meters.",
        'https://peakvisor.com/img/news/Appalachian-Mountains.jpg'],
        'Pacific mountains': ["These are mountain ranges off the coast of the United States. "
                              "The system begins in the north, where Mount Olympus rises 2.4 thousand meters in Washington. "
                              "The western slopes of these mountains descend into the ocean. "
                              "Then the Cascade Mountains rise to the south, forming a volcanic chain in California and Oregon. "
                              "The last major eruption here was in the 80s. "
                              "20th century The maximum height of the ridge in this area is 1,200 m.",
                              'https://i.pinimg.com/736x/ef/be/93/efbe932a83360e8fc3854b8ddc30b891--mountain-range-south-island.jpg'],
        'Rocky Mountains': ['In the Cordillera system, the ridge stretches for 4.5 thousand km. '
                            'In the south, the mountains begin in New Mexico, gradually rising and widening towards Utah. '
                            'Most of the major Rocky Mountains are located in Colorado. '
                            'Here, the highest point of the region is Mount Elbert with a height of 4.5 thousand meters above the sea. '
                            'Toward the northwest, the mountains decrease and narrow. '
                            'The Rocky Mountains are rich in minerals, so gold, silver, copper, and lead are mined there. '
                            'A national park has also been formed on the territory, protecting the thermal springs and geysers of the ridges. '
                            'The Rocky Mountains separate the Pacific and Atlantic oceans.',
                            'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Moraine_Lake_17092005.jpg/1200px-Moraine_Lake_17092005.jpg']}
    skiResorts = {'Aspen': ["Aspen is one of the largest resorts in the United States. "
                            "It has a reputation as a prestigious and expensive resort. "
                            "This is partly true, but Aspen is accessible to those on a tight budget, and snow is almost always guaranteed here. "
                            "Aspen combines four isolated ski areas - Aspen Mountain (Aspen Mountain), Aspen Highlands (Aspen Highlands), Buttermilk (Buttermilk) and Snowmass (Snowmass). "
                            "All together they offer 200 km of slopes for all tastes, both for beginners and experienced skiers, with a developed lift system. "
                            "The highest peaks in the area are Maroon Bells (4247m) and Pyramid Peak (4205m). "
                            "Aspen is a Victorian-style resort town nestled in the picturesque Roaring Fork Valley, with a plethora of restaurants, "
                            "shops and plenty of activities besides skiing.",
                            'https://ski.ru/kohana/upload/user_images/3_1359622357.jpg'],
                  'Heavenly': ["Heavenly Resort is located on the Nevada/California border. "
                               "At the foot of the mountain lies the largest mountain lake in the Americas, Lake Tahoe. "
                               "Here you will have a unique opportunity to combine a ski holiday with a visit to the casino. "
                               " Resort combines the beauty of nature, great skiing on the wooded slopes and unparalleled nightlife. "
                               "Located on the border of Nevada, Heavenly has gaming centers and casinos where you can spend time in the evening. "
                               "There is a wide choice of bars, restaurants, night clubs and discos for young people.",
                               'https://travelask.ru/uploads/hint_place/000/070/715/image/129ebb8e0c8f5e6800fa5305b55af7d7.jpg'],
                  'Keystone': [
                      "Keystone is one of the largest ski resorts in Colorado where you can ski all day long with family and friends. "
                      "You can go down on an inflatable ring from the Adventure Point hill, go ice skating on the picturesque Keystone Lake"
                      " and visit the snow fortress at the top of Mount Dercum. The whole family will love it, and it's all in one place. "
                      "After descending the slopes, you can go snowshoeing, cross-country skiing or ice skating, or simply relax in the spa.",
                      'http://triplook.me/media/resorts/photo/5/e/u27.jpg']}
    lakes = {'Okeechobee': [
        "Okeechobee is a freshwater lake in Florida. It occupies the Glades, Okeechobee, Martin, Palm Beach, and Hendry counties. "
        "By area, it is the largest lake in the southern United States and the second largest freshwater lake in area, located entirely in the country. "
        "Several small rivers flow into the lake, the largest being the Kissimmee. "
        "Several small channels of the Everglades biosystem flow from Okeechobee, to which the lake belongs. "
        "Also on the lake there are several small islands, the largest of which is Creamer, inhabited. "
        "The city of Cluiston is located on the south coast.",
        'https://i0.wp.com/courrierdesameriques.com/wp-content/uploads/2018/03/Clewiston-Lake-Okeechobee-Floride-0555.jpg?resize=708%2C531&ssl=1'],
        'Ontario': [
            "Ontario is a lake in the United States and Canada, the lowest and smallest in area in the Great Lakes system. "
            "It is the fifth largest lake in the United States by area. "
            "The name of the lake comes from the language of the Huron Indian tribe and means Lake of shining waters. "
            "Later, the province of Ontario became known as the same. On old maps you can see different names of the lake. On the map from 1662-1663. "
            "The lake was called Ondiara.",
            'https://touristam.com/wp-content/uploads/2020/12/ozero-ontario-1.jpg'],
        'Michigan': ['Michigan is a freshwater lake in the United States, one of the North American Great Lakes. '
                     'The only one of the Great Lakes that is entirely within the United States, the largest of those located entirely in the United States. '
                     'Located south of Lake Superior, connected to Lake Huron by the Strait of Mackinac, with the Mississippi River system - the Chicago-Lockport Canal. '
                     'From the point of view of hydrography, Michigan and Huron form a single system, but geographically they are considered to be separate lakes.',
                     'https://fanfacts.ru/picture/fakty-ozero-michigan-960x540.jpg']}
    rivers = {'Missouri': ["It flows through 10 states. This is the longest river in the USA. "
                           "Its source is in the Rocky Mountains at an altitude of 2750 meters above sea level. "
                           "More than 10 Indian tribes lived on its banks. "
                           "The Missouri became an important transportation route for westward settlers in the 19th century. "
                           "Many dams and dams began to be built on it. Beavers, raccoons, muskrats and otters live near the river. "
                           "The extraction of their fur attracted colonizers and indigenous people. "
                           "The length of the river is 3767 km.",
                           'https://pibig.info/uploads/posts/2021-05/thumbs/1622059734_4-pibig_info-p-missuri-reka-priroda-krasivo-foto-5.jpg'],
              'Mississippi': ["The river is one of the largest in the world. Flows in a southerly direction. "
                              "The source takes in the state of Minnesota, and ends in the Gulf of Mexico. "
                              "The course of the Mississippi is very winding. For several states, the river is a natural border. "
                              "The river is fed by rain and melt water. The river often causes floods. "
                              "The largest occurred in 1927, it was called the great flood.",
                              'https://s9.travelask.ru/system/images/files/001/457/202/wysiwyg_jpg/mississippi-river.jpg?1613421527'],
              'Yukon': ["Yukon translates as Big River. This name was given to her by the Gwich'in tribe. "
                        "It flows through Alaska and Canada, then flows into the Bering Sea. "
                        " the Gold Rush, thousands of prospectors came to the Yukon River and its tributary, the Klondike. "
                        "The famous writer Jack London was also on this river. The climate on the banks of the river is harsh, "
                        "in winter the temperature drops to minus fifty degrees, and in summer it rarely reaches plus twelve. "
                        "The length of the river is 3190 km.",
                        'https://about-planet.ru/images/severnaya_amerika/priroda/yukon/yukon2.jpg']}
    # currency
    currencyName = 'USD'
    currencyEqualsToDollar = 1

    # military
    milPolBlock = 'NATO'
    amountOfPeopleInArmy = 1395350

    # healthcare
    numberOfDoctorsPer100kPopulation = 294
    menAverageLifeExpectancy = 73.2
    womenAverageLifeExpectancy = 79.1

    # climat
    juneAverageTemperature = 25
    decemberAverageTemperature = 9
    averageHumidity = 63
    averageDurationOfWinter = 3.5
    averageRainfallPerMonth = 27.6
    averageNumberOfFoggyDaysPerYear = 42
    averageNumberOfRainyDaysPerYear = 108
    averageNumberOfClearDays = 189

    # security
    situationInTheCountry = 2  # [1, 3] 1-bad, 3-good
    freedomOfSpeech = 3  # [1, 3]
    assessmentOfFamilyLife = 3  # [1, 3]
    attitudeTowardsLGBT = 3  # [1, 3]

    # population
    populationCount = 331900000
    procentOfMales = 49.4
    procentOfFemales = 50.6
    populationDensityPerSquareKilometer = 34.8
    speedOfLife = 3  # [1, 3]
    workPlaces = 3  # [1, 3]
    nightLifeEntertainment = 3  # [1, 3]

    # citizenship
    citizenshipGlobalRank = 3
    friendlyToForeigners = 3

    # communication
    communicationOnEnglish = 3  # [1, 3]

    # transport
    averageTravelTimeToWork = 32.91
    developmentLevelOfPublicTransport = 3  # [1, 3]

    # internet
    speedOfInternetMbps = 31  # Мегабиты в секунду
    freeWifi = 3  # [1, 3]

    # education
    rankingOfNationalEducationSystem = 1

    cc.createBase(countryName, cities, officialLanguage,
                  # currency
                  currencyName, currencyEqualsToDollar,
                  # military
                  milPolBlock, amountOfPeopleInArmy,
                  # healthcare
                  numberOfDoctorsPer100kPopulation, menAverageLifeExpectancy, womenAverageLifeExpectancy,
                  # climat
                  juneAverageTemperature, decemberAverageTemperature, averageHumidity,
                  averageDurationOfWinter, averageRainfallPerMonth, averageNumberOfFoggyDaysPerYear,
                  averageNumberOfRainyDaysPerYear, averageNumberOfClearDays,
                  # security
                  situationInTheCountry, freedomOfSpeech,
                  assessmentOfFamilyLife, attitudeTowardsLGBT,
                  # population
                  populationCount, procentOfMales, procentOfFemales, populationDensityPerSquareKilometer,
                  speedOfLife, workPlaces, nightLifeEntertainment,
                  # citizenship
                  citizenshipGlobalRank,
                  # communication
                  communicationOnEnglish,
                  # transport
                  averageTravelTimeToWork, developmentLevelOfPublicTransport,
                  # internet
                  speedOfInternetMbps, freeWifi,
                  # education
                  rankingOfNationalEducationSystem, universities, faculties, programs, costs, links, images,
                  requirements,
                  hostel, scolarship, sights, beaches, mountains, skiResorts, lakes, rivers, friendlyToForeigners
                  )

    # cc.createManMadeDisaster(countryName, nameMMD, typeOfMMD, aomuntOfDeadPeople,
    #                           aomuntOfInjuredPeople, territoryOfPollution)
    # cc.createOceans()
    #############################   USA   #############################

    #############################   Italy   #############################

    # Country
    countryName = "Italy"
    officialLanguage = "Italian"

    # cities    name   isBig  washesBy
    cities = {
        'Rome': [True, False, None], 'Milan': [True, False, None], 'Naples': [True, True, 'Tyrrhenian Sea'],
        'Turin': [True, False, None], 'Palermo': [True, True, 'Tyrrhenian Sea'],
        'Venice': [False, True, 'Adriatic Sea'],
        'Sicily': [False, True, 'Mediterranean Sea'], 'Rimini': [False, True, 'Adriatic Sea'],
        'Bologna': [False, False, None]}

    # education
    universities = {'Milan': ['Politecnico di Milano', 'University of Milan'],
                    'Rome': ['Sapienza University'],
                    'Turin': ['Politecnico di Torino']}
    faculties = {
        'Politecnico di Milano': ['Faculty of Arts', 'Faculty of Medicine', 'Faculty of Engineering',
                                  'Faculty of Computer Engineering and Software', 'Faculty of Science'],
        'University of Milan': ['Faculty of Medicine', 'Faculty of Law', 'Faculty of Science',
                                'Faculty of Social Sciences',
                                'Faculty of Computer Engineering and Software'],
        'Sapienza University': ['Faculty of Economics', 'Faculty of Arts', 'Faculty of Law', 'Faculty of Engineering',
                                'Faculty of Medicine',
                                'Faculty of Social Sciences', 'Faculty of Architecture', 'Faculty of Science'],
        'Politecnico di Torino': ['Faculty of Engineering', 'Faculty of Computer Engineering and Software',
                                  'Faculty of Medicine', 'Faculty of Arts']}
    programs = {
        'Politecnico di Milano': ['Magistracy', 'Undergraduate'],
        'University of Milan': ['Magistracy', 'Undergraduate'],
        'Sapienza University': ['Magistracy', 'Undergraduate'],
        'Politecnico di Torino': ['Magistracy', 'Undergraduate']}
    links = {'Politecnico di Milano': 'https://www.polimi.it',
             'University of Milan': 'https://misom.unimi.it',
             'Sapienza University': 'https://www.uniroma1.it',
             'Politecnico di Torino': 'https://www.polito.it'}
    images = {
        'Politecnico di Milano': 'https://italyadaegitim.com/wp-content/uploads/2020/11/politecnico-di-milano.jpg',
        'University of Milan': 'https://diginlaw.files.wordpress.com/2021/04/02.-faculty-photo.jpg?w=1200',
        'Sapienza University': 'https://smapse.ru/storage/2018/09/sapienza-universita-roma.jpg',
        'Politecnico di Torino': 'https://fartakapply.com/wp-content/uploads/2020/09/6-POLITO.jpg'}
    # общага
    hostel = {'Politecnico di Milano': 'Yes',
              'University of Milan': 'Yes',
              'Sapienza University': 'No',
              'Politecnico di Torino': 'No'}
    # стипендия
    scolarship = {'Politecnico di Milano': 'Yes',
                  'University of Milan': 'Yes',
                  'Sapienza University': 'Yes',
                  'Politecnico di Torino': 'Yes'}
    # требования к поступлению
    requirements = {'Politecnico di Milano': 'For admission, applicants must provide: '
                                             'Certified translation of the certificate of secondary education, '
                                             'TOEFL iBT 80 (minimum)/Academic IELTS 6.0 (minimum), '
                                             'Entrance exam results, Registration fee payment certificate = $160.',
                    'University of Milan': 'The requirements for admission to the University of Milan are standard, as in many other universities in Europe: '
                                           'previous grades and entrance exams, certificate / diploma + for enrolling in some specialties, '
                                           'you may need a motivation letter and recommendations.',
                    'Sapienza University': '12 years completed education. '
                                           'All documents must be translated, apostilled and legalized with a Dichiarazione di valore in loco consular certificate. '
                                           'For studying in Italian: level B2 and above. '
                                           'For study in English: certificate IELTS, TOEFL, Cambridge B2, TOEIC (exact requirements depend on the program). '
                                           'If the applicant does not have a certificate at the time of application, he can take the Italian exam at the university '
                                           '(usually held in September, but the exact dates need to be clarified). '
                                           'Applicants for medical courses take the IMAT test, for closed and open access programs, a TOLC type exam may be required.',
                    'Politecnico di Torino': 'To enter the university, citizens of other states need to study at least one '
                                             'year at any university so that their documents meet the requirements of the admission committee.'}
    costs = {'Politecnico di Milano': 3900,
             'University of Milan': 2500,
             'Sapienza University': 2280,
             'Politecnico di Torino': 3600}

    sights = {'Pantheon': ["A real achievement of the building technologies of antiquity, "
                           "a magnificent temple, which became a model of ancient architecture and gave rise to many imitators. "
                           "The Pantheon, fortunately, is perfectly preserved, so everyone can visit it. "
                           "This is best done at noon, when a real pillar of light breaks through the hole in the roof.",
                           'https://top10.travel/wp-content/uploads/2014/10/panteon.jpg'],
              'Coliseum': [
                  "This is a visiting card of Rome, a building that is familiar even to those who have never left their hometown. "
                  "Today, the Colosseum, of course, bears the marks of time and needs to be reconstructed. "
                  "And still, a visit to this historical monument is included in the mandatory program of "
                  "all tourists and leaves an indelible impression.",
                  'https://top10.travel/wp-content/uploads/2014/10/kolizey.jpg'],
              'San Gimignano': ["City in Tuscany, near Florence. "
                                "San Gimignano is known for the fact that it managed to preserve its medieval appearance and from afar it "
                                "seems that horse-drawn carts still move along its streets, and knights with swords walk sedately. "
                                "Be sure to see the 14 ancient towers and the local history museum.",
                                'https://top10.travel/wp-content/uploads/2014/10/san-gimignano.jpg']}
    beaches = {'Red bay': ["Looking for a quiet beach to get away from everyone and have some peace and quiet? "
                           "Head to Favignana, a tiny island off the coast of Sicily. "
                           "Only a few thousand people live here and there are four dozen hotels on the entire island. "
                           "Getting here is not easy - only by ferry from Sicily, but that's why there are few people here. "
                           "The only thing that can overshadow your vacation is your phone, so don't forget to turn it off on the ship.",
                           'https://dynamic-media-cdn.tripadvisor.com/media/photo-o/13/a7/bf/3a/red-beach.jpg?w=1200&h=-1&s=1'],
               "Marina Picola": [
                   "The island of Capri has been an elite resort for a very long time: Caesar Augustus had a “cottage” here. "
                   "And since the days of the Roman Empire, for some reason (or perhaps just following the fashion), celebrities have flocked here. "
                   "Russian celebrities are no exception, almost every outstanding person in our recent history has visited Capri: "
                   "from Tchaikovsky and Bunin to Gorky and Lenin. "
                   "The beach at Marina Picola Bay is overshadowed by Capri's other famous beaches and attractions, such as the famous Blue Grotto. "
                   "But this is for the best, because today Capri is still an elite resort, and finding a secluded place here is not so easy.",
                   'https://tournavigator.pro/%D1%84%D0%BE%D1%82%D0%BE/other_1022_1003_1657754408.jpg'],
               'Rabbit beach': ["Rabbit Beach has been repeatedly recognized as the best beach in the world. "
                                "No wonder, because this is one of those places where you want to stay forever. "
                                "The beach is located in a protected area, and it is not easy to get to it. "
                                "First you need to come to the island of Lampedusa, which in itself is not a trivial task. "
                                "Then you need to go by bus or car, and then walk for 20 minutes. "
                                "And these 20 minutes, perhaps, will leave you even more impressions than the beach itself: "
                                "the views from the mountain path are simply amazing.",
                                'https://ostrova24.ru/wp-content/uploads/2017/05/ostrov-Lampeduza-v-Italii.jpg']}
    mountains = {
        'Mont Blanc': ["Mont Blanc is a peak in the massif of the same name, rising above Lake Leman in the Alps. "
                       "This is the highest point of the Alps, reaching a height of 4810 m above sea level. "
                       "The highest mountain in the European Union and Europe, excluding the Caucasus Mountains as part of Europe. "
                       "Located on the border of Italy and France.",
                       'https://funart.pro/uploads/posts/2019-11/1573381953_monblan-gora-francija-3.jpg'],
        'Marmolada': ["Marmolada is a mountain in northeastern Italy, the highest mountain in the Dolomites. "
                      "This is part of the ridge that stretches from west to east. "
                      "In the west, the mountain breaks into steep cliffs, forming a stone wall several kilometers long. "
                      "To the north is the relatively gentle Marmolada Glacier.",
                      'https://st2.depositphotos.com/1355276/5612/i/950/depositphotos_56122677-stock-photo-marmolada-ski-resort-in-italy.jpg'],
        'Dolomites': [
            'The Dolomites are a mountain range in the Eastern Alps, part of the system of the Southern Limestone Alps. '
            'The massif is located in the northeastern part of Italy in the provinces of Belluno, Bolzano, Pordenone, Trento and Udine. '
            'The massif is bounded by river valleys: Isarco, Pusteria, Piave, Brenta and Adige.',
            'https://otdyhateli.com/wp-content/uploads/2017/03/The-Dolomites-1050x700.jpg']}
    skiResorts = {'Breuil-Cervinia': [
        "The Breuil-Cervinia ski resort is located in the Valle d'Aosta region, at the foot of the Matterhorn rocky ridge (2050 above sea level). "
        "It is considered one of the best in the north of the country. "
        "From here, via a single ski area, you can reach the Swiss side of the Matterhorn on the slopes of Zermatt. "
        "The entire winter season, even not at a very high altitude, there will be plenty of snow here, and this is almost 6 months a year. "
        "In total, Cervinia covers more than 100 km of ski slopes of varying difficulty. "
        "In summer, the cross-country ski run turns into a golf course. "
        "Also in the summer, hiking is very developed and climbing to the top of the Matterhorn is popular.",
        'https://planetofhotels.com/guide/sites/default/files/styles/paragraph__live_banner__lb_image__1880bp/public/live_banner/Cervinia-1.jpg'],
        'Val Gardena': [
            "Val Gardena is one of the best ski resorts in Italy, divided into the three municipalities of Ortisei, Santa Cristina in Val Gardena and Selva di Val Gardena (Trentino-Alto Adige region). "
            "Val Gardena is located in the heart of the Dolomites and offers some challenging pistes surrounded by beautiful pine forests. "
            "The valley is very popular among tourists, partly because of the fact that the stages of the Ski World Cup take place here. "
            "In total, there are 175 km of ski slopes, 115 km of cross-country trails and 83 ski lifts.",
            'https://www.dolomiticlass.it/storage/localities/67/conversions/Selva_Gardena_inverno-tablet.jpg'],
        "Cortina d'Ampezzo": [
            "Cortina d'Ampezzo is located in the Veneto region, and is called the Pearl of the Dolomites, for the presence of slopes for every taste. "
            "In total, they make up 115 km of ski slopes with different levels of difficulty. "
            "Cortina d'Ampezzo is considered one of the most equipped ski resorts in Italy and is the ideal place for a family holiday. "
            "One of the strengths of this resort is the presence of numerous hotels and inns that can satisfy the needs of even the most demanding tourists. "
            "The main attraction of Cortina d'Ampezzo is, of course, the historic center of the city, where the main sports, antique and souvenir shops are located.",
            'https://live.staticflickr.com/65535/49089210372_6f075ba8d5_o.jpg']}
    lakes = {'Lago Maggiore': [
        "On the border of Lombardy, Piedmont and Switzerland, Lake Maggiore is located, an endless expanse of water that reflects the surrounding landscapes: "
        "fragrant pine groves, centuries-old forests and majestic mountains. "
        "In the middle of the emerald green vegetation and the blinding blue of the sky, numerous castles, "
        "palaces and Italian gardens rise, related to the two noble families that influenced the history of this place - the Visconti and the Borromeo. "
        "You can start your journey through these picturesque beauties from Stresa on the Piedmontese coast, "
        "opposite the Borromean Islands, real open-air museums: Bella Island with the Borromeo Palace, "
        "Madre Island with its stunning vegetation and the Fishermen's Island, on which, as the name suggests, there is a characteristic settlement. "
        "Verbania is another lively Piedmont town with a number of beautiful villas such as Villa Giulia, San Remigio and Taranto, "
        "where you can see 20,000 species of plants.",
        'https://www.travelbook.de/data/uploads/2022/04/gettyimages-642500890.jpg'],
        'Lago di Bracciano': [
            "Lake Bracciano, also called Lake Sabatino, is of volcanic origin, only one river flows into it - Arrone, "
            "originating on the southeast coast and carrying its waters to the Tyrrhenian Sea. "
            "The coast of Italy's lake is conducive to long walks. "
            "There are various establishments along the way. "
            "Including restaurants whose cuisine specializes in dishes with lake fish. "
            "The beach is wide with a large sandy area.",
            'https://www.lazionascosto.it/wp-content/uploads/2019/05/lago-di-bracciano.jpg'],
        'Lago di Garda': ['Lake Garda, or Benaco, is the largest lake in Italy. '
                          'In the south it is surrounded by moraine hills formed by the last glacier, and in the north by higher mountain '
                          'ranges that help maintain a mild Mediterranean climate. '
                          'The radiance of nature, the mildness of the climate, the rich vegetation (mainly olive trees, palms, cypresses, lemons, oleanders and oranges)'
                          ' and the majestic scenery, together with cultural and historical values, make Lake Garda the most attractive among Italian lakes.',
                          'https://www.valeggio.com/wp-content/uploads/2021/03/lago-di-garda-lanfredi-valeggio-5.jpg']}
    rivers = {'Po': ["In Italy, the Po River is the longest, most abundant and has the largest basin. "
                     "Along it there are several cities of interest for their historical monuments, and its mouth itself is a landmark.",
                     'https://planetofhotels.com/guide/sites/default/files/styles/paragraph__text_with_image___twi_image/public/2020-05/po-river-1.jpg']}
    # currency
    currencyName = 'ITL'
    currencyEqualsToDollar = 1835.88

    # military
    milPolBlock = "NATO"
    amountOfPeopleInArmy = 161550

    # healthcare
    numberOfDoctorsPer100kPopulation = 395
    menAverageLifeExpectancy = 78.8
    womenAverageLifeExpectancy = 84.1

    # climat
    juneAverageTemperature = 27
    decemberAverageTemperature = 12
    averageHumidity = 69
    averageDurationOfWinter = 1.5
    averageRainfallPerMonth = 78.8
    averageNumberOfFoggyDaysPerYear = 42
    averageNumberOfRainyDaysPerYear = 80
    averageNumberOfClearDays = 117

    # security
    situationInTheCountry = 2  # [1, 3] 1-bad, 3-good
    freedomOfSpeech = 3  # [1, 3]
    assessmentOfFamilyLife = 2  # [1, 3]
    attitudeTowardsLGBT = 1  # [1, 3]

    # population
    populationCount = 59070000
    procentOfMales = 49
    procentOfFemales = 51
    populationDensityPerSquareKilometer = 33.6
    speedOfLife = 2  # [1, 3]
    workPlaces = 2  # [1, 3]
    nightLifeEntertainment = 3  # [1, 3]

    # citizenship
    citizenshipGlobalRank = 2
    friendlyToForeigners = 3

    # communication
    communicationOnEnglish = 1  # [1, 3]

    # transport
    averageTravelTimeToWork = 33.56
    developmentLevelOfPublicTransport = 2  # [1, 3]

    # internet
    speedOfInternetMbps = 13  # Мегабиты в секунду
    freeWifi = 1  # [1, 3]

    # education
    rankingOfNationalEducationSystem = 30

    cc.createBase(countryName, cities, officialLanguage,
                  # currency
                  currencyName, currencyEqualsToDollar,
                  # military
                  milPolBlock, amountOfPeopleInArmy,
                  # healthcare
                  numberOfDoctorsPer100kPopulation, menAverageLifeExpectancy, womenAverageLifeExpectancy,
                  # climat
                  juneAverageTemperature, decemberAverageTemperature, averageHumidity,
                  averageDurationOfWinter, averageRainfallPerMonth, averageNumberOfFoggyDaysPerYear,
                  averageNumberOfRainyDaysPerYear, averageNumberOfClearDays,
                  # security
                  situationInTheCountry, freedomOfSpeech,
                  assessmentOfFamilyLife, attitudeTowardsLGBT,
                  # population
                  populationCount, procentOfMales, procentOfFemales, populationDensityPerSquareKilometer,
                  speedOfLife, workPlaces, nightLifeEntertainment,
                  # citizenship
                  citizenshipGlobalRank,
                  # communication
                  communicationOnEnglish,
                  # transport
                  averageTravelTimeToWork, developmentLevelOfPublicTransport,
                  # internet
                  speedOfInternetMbps, freeWifi,
                  # education
                  rankingOfNationalEducationSystem, universities, faculties, programs, costs, links, images,
                  requirements,
                  hostel, scolarship, sights, beaches, mountains, skiResorts, lakes, rivers, friendlyToForeigners
                  )

    # cc.createManMadeDisaster(countryName, nameMMD, typeOfMMD, aomuntOfDeadPeople,
    #                           aomuntOfInjuredPeople, territoryOfPollution)
    # cc.createOceans()
    #############################   Italy   #############################

    #############################   Spain   #############################

    # Country
    countryName = "Spain"
    officialLanguage = "Spanish"

    # cities    name   isBig  washesBy
    cities = {
        'Madrid': [True, False, None], 'Barcelona': [True, True, 'Balearic sea'],
        'Valencia': [True, True, 'Balearic sea'],
        'Seville': [True, False, None], 'Zaragoza': [True, False, None], 'Ibiza': [True, True, 'Balearic sea'],
        'Majorca': [True, True, 'Balearic sea'], 'San Sebastian': [False, True, 'Atlantic ocean']}

    # education
    universities = {'Barcelona': ['University of Barcelona', 'EU Business School'],
                    'Madrid': ['Saint Louis University'],
                    'Seville': ['University of Seville']}
    faculties = {
        'University of Barcelona': ['Faculty of Medicine', 'Faculty of Law', 'Faculty of Science',
                                    'Faculty of Economics', 'Faculty of Social Sciences'],
        'EU Business School': ['Faculty of Economics', 'Faculty of Arts', 'Faculty of Social Sciences',
                               'Faculty of Education'],
        'Saint Louis University': ['Faculty of Arts', 'Faculty of Social Sciences', 'Faculty of Medicine',
                                   'Faculty of Education'],
        'University of Seville': ['Faculty of Economics', 'Faculty of Social Sciences', 'Faculty of Law',
                                  'Faculty of Computer Engineering and Software']}
    programs = {
        'University of Barcelona': ['Magistracy', 'Undergraduate', 'Doctoral'],
        'EU Business School': ['Magistracy', 'Undergraduate', 'MBA', 'Foundation'],
        'Saint Louis University': ['Magistracy', 'Undergraduate'],
        'University of Seville': ['Magistracy', 'Undergraduate']}
    links = {'University of Barcelona': 'https://www.ub.edu',
             'EU Business School': 'https://www.euruni.edu',
             'Saint Louis University': 'https://www.uhsp.edu',
             'University of Seville': 'https://ics-seville.org'}
    images = {
        'University of Barcelona': 'https://www.usnews.com/object/image/00000152-46f4-d86f-a7f6-cfff51660000/160115-universityofbarcelona-submitted.jpg?update-time=1452889458023&size=responsiveFlow970',
        'EU Business School': 'https://www.studylab.ru/upload/Institutions/image/big/cc262389c39ef03abce744a2f1991757.jpg',
        'Saint Louis University': 'https://nogoonjade.mn/wp-content/uploads/2019/02/Saint-Louis-University.jpg',
        'University of Seville': 'https://ics-seville.org/wp-content/uploads/2017/01/notas-de-corte-universidad-de-sevilla-2016.jpg'}
    # общага
    hostel = {'University of Barcelona': 'Yes',
              'EU Business School': 'Yes',
              'Saint Louis University': 'Yes',
              'University of Seville': 'Yes'}
    # стипендия
    scolarship = {'University of Barcelona': 'Yes',
                  'EU Business School': 'Yes',
                  'Saint Louis University': 'Yes',
                  'University of Seville': 'Yes'}
    # требования к поступлению
    requirements = {
        'University of Barcelona': 'There are no restrictions on the basis of religious views, as well as on the basis of gender for admission to the university. '
                                   'Enrollment is made on the basis of the provided data on the academic achievements of the applicant.'
                                   ' One of the conditions put forward by the university is knowledge of the Spanish language, which is assessed by a special test. '
                                   'The list of documents required for admission is posted on the university website. '
                                   'For foreign applicants - all documents included in the application package must have a notarized translation into Spanish. '
                                   'Usually about 80% of applicants are enrolled, but depending on the prestige of the faculty, this figure may vary. '
                                   'The cost of studying at the University of Barcelona is relatively low. '
                                   "Obtaining a bachelor's degree will cost USD 1,000 per year, and an annual master's degree will cost USD 3,000. "
                                   "There is also a scholarship program based on the competition.",
        'EU Business School': 'Age: 17+, Duration: 6-7 semesters (3 - 3.5 years), ECTS: 240, '
                              'Beginning of studies: August, October, February and June, '
                              'Language requirements: TOEFL iBT 80+, IELTS Academic 6.0+, CAE B2 (169+), '
                              'Academic requirements: completed secondary or secondary special education with good academic performance',
        'Saint Louis University': '1. Age: from 17 years old; '
                                  '2. High school diploma (good and excellent grades and high GPA);'
                                  '3. Proficiency in English: IELTS 6.5/TOEFL 80/Pearson Versant 69 or equivalent (certificate is valid for two years after the exam date); '
                                  '4. Portfolio; '
                                  '5. GPA-3.0; '
                                  '6. High performance and knowledge in core disciplines.',
        'University of Seville': 'The admission procedure provides for the provision of a document confirming academic performance at the previous place of study. '
                                 'Then comes the exam. According to the general results, enrollment takes place. '
                                 'Everything related to admission, deadlines for submitting documents and the cost of individual programs is described on the official '
                                 'website of the University of Seville.'}
    costs = {'University of Barcelona': 3000,
             'EU Business School': 4900,
             'Saint Louis University': 10880,
             'University of Seville': 1000}

    sights = {'National Prado Museum': ["The museum is located on the Boulevard of Arts - a popular tourist route. "
                                        "Its most valuable collection includes more than 8.5 thousand paintings and about 700 sculptures. "
                                        "Art connoisseurs from different eras will find something to see in Spain, in particular, in the Prado Museum. "
                                        "It welcomes visitors with paintings by the great Spanish masters, including paintings by Goya and Velasquez. "
                                        "The Italian art school is represented here by the works of Tintoretto, Botticelli, Titian, Raphael, Veronese, Fra Angelico, Mantegna. "
                                        "And within the framework of Flemish painting, the museum exhibits paintings by Vander Weyden, Pieter Brueghel the Elder, Hieronymus Bosch, Jacob Jordaens, Peter Paul Rubens.",
                                        'https://www.tripzaza.com/ru/destinations/wp-content/uploads/2017/04/Spain-1-The-Prado-Museum-e1491982394705.jpg'],
              'Sagrada Familia': ["The place of this attraction in Spain is included in the lists of UNESCO sites. "
                                  "Sagrada Familia or Sagrada Familia, as it is also called, gives tourists different feelings. "
                                  "The first associations evoke an old church building, but the unusual structure suggests that it was created by an alien mind. "
                                  "The creator of the project of the original temple is Antoni Gaudí. Don't know what to see in Spain that will be remembered forever? "
                                  "Visit the Sagrada Familia. As conceived by Gaudi, the temple was destined for the role of the Bible, embodied in architecture. "
                                  "The magnificent facades were supposed to symbolize the main stages of the life of Christ: the Birth, the Torments of Christ, the Resurrection. "
                                  "The amazing acoustics in the temple is due to the perfect bell system, and the columns, approaching the vaults, form a fantastic likeness of intertwining tree branches.",
                                  'https://media.decorateme.com/images/aa/48/d5/vitaia-forma-bashen-gaudi-obiasniaetsia-tem-chto.webp'],
              'Ordesa y Monte Perdido National Park': [
                  "The famous sights of Spain are also in its most remote corners. "
                  "One of the first national parks - Ordesa y Monte Perdido Reserve - is still considered the most beautiful in the country. "
                  "The main attraction of the park is the Ordesa Canyon. "
                  "It impresses with huge rocks hanging from both sides of the mountain path. "
                  "The river of the same name runs along the bottom of the canyon. "
                  "Its waters are replenished by streams flowing down the slopes. "
                  "The lower part of the park is represented by a dense forest, where you can meet many representatives of the forest fauna. "
                  "There are many waterfalls that cascade one after another. "
                  "Among them, the most powerful, perhaps, is the Cola de Caballo waterfall, from which the Ordesa River begins. "
                  "Cows graze on the spacious meadows of the park, dense poplar and beech forests are located at the foot of the mountains.",
                  'https://www.tripzaza.com/ru/destinations/wp-content/uploads/2017/04/Spain-9-Ordesa-y-Monte-Perdido-National-Park-e1491984613524.jpg']}
    beaches = {'Rodas, Sie Islands': [
        "Rodas Beach (Playa de Rodas) topped the ranking of the best beaches in the world in 2007, according to the British newspaper The Guardian. "
        "And this is no coincidence. "
        "The Cies archipelago is made up of three large islands - Monteagudo, Faro, San Martino. Since 2002 they have been part of the National Park of the Atlantic Islands of Galicia. "
        "Protected by the state. Here are the most beautiful beaches in Spain. "
        "It is no coincidence that they are called paradises - there is impeccable white sand and huge areas of untouched nature. "
        "Add to this the abundance of rare birds in the vicinity and dolphins in the ocean waters.",
        'https://planetofhotels.com/guide/sites/default/files/styles/paragraph__text_with_image___twi_image/public/2020-08/Praia-de-Rodas-beach.jpg'],
        "Burriana": ["Burriana (Playa Burriana) is one of the best beaches in Spain. "
                     "It is located in the city of Nerja (province of Malaga) along the Paseo Marítimo Antonio Mercero promenade. "
                     "The coastline is 800 meters long and 40 meters wide. "
                     "Playa Burriana is marked with the Blue Flag, famous for its clean sand, luxurious palm trees and many entertainments. "
                     "There are playgrounds, clubs, bars and restaurants.",
                     'https://planetofhotels.com/guide/sites/default/files/styles/paragraph__text_with_image___twi_image/public/2020-08/Playa-Burriana-at-Nerja.jpg'],
        'Playa de Palma, Mallorca': [
            "It is difficult to find a person who has not heard about this resort on the Mediterranean coast. "
            "Its beauty is painted by artists and sung by poets. "
            "Playa de Palma beach has been awarded the Blue Flag and proudly bears this award, delighting with white sand and developed infrastructure. "
            "It is perfect for a family vacation, as the entrance to the sea is quite gentle here, and the bottom is sandy and soft, like a velvet cover. "
            "On the beach there are playgrounds for playing volleyball, basketball, rental of bicycles and equipment for water activities, it is possible to rent sun loungers. "
            "Within walking distance there are at least a dozen bars with refreshing drinks.",
            'https://planetofhotels.com/guide/sites/default/files/styles/paragraph__text_with_image___twi_image/public/2020-06/palma-de-mallorca-4.jpg']}
    mountains = {'Mulasen': ["Mulasen is a mountain in southern Spain, the highest peak of the Iberian Peninsula. "
                             "It is located in the Sierra Nevada, one of the spurs of the Cordillera Penibetica. "
                             "On the northern slope of the mountain lies a small avalanche glacier, from which the river Khenil originates.",
                             'https://i.pinimg.com/736x/29/82/0e/29820ee0e5527c20b6d4d20b3c0b3c6f--natural-park-sierra-nevada.jpg'],
                 'Aneto': [
                     "Aneto Peak is the highest mountain in the Pyrenees, located in the province of Huesca, Spain. "
                     "The third highest mountain in Spain. "
                     "The mountain is also known by the French name Pic de Neto, but this name is rarely used, since the mountain is entirely in Spanish territory.",
                     'https://peakfinder.ru/image/original/304_pik_aneto.jpg'],
                 'Veleta': ['Veleta is a mountain peak in southern Spain, in the province of Granada in Andalusia. '
                            'It is part of the Sierra Nevada mountain range. One of the highest points in the entire Iberian Peninsula.',
                            'https://ic.pics.livejournal.com/vpervye1/34433614/1067216/1067216_original.jpg']}
    skiResorts = {
        'Sierra Nevada': ["Sierra Nevada is the most popular resort in Spain, the highest geographical location. "
                          "It is located in the southwest, near Granada. The elite of society comes here: actors, famous people, politicians. "
                          "87 kilometers of slopes of different levels are equipped here, there are cross-country flat trails. "
                          "More than 400 cannons provide ideal coverage of the slopes. "
                          "Fashionable hotels, ski schools, all kinds of après-ski establishments are open for guests.",
                          'https://espanarusa.com/files/autoupload/3/21/70/3ealic0o48095.jpg'],
        'Baqueira-Beret': [
            "Baqueira Beret is the largest resort in the Pyrenees on the eastern side of the Aran Valley (Catalonia). "
            "Here, among the magnificent landscapes, very reminiscent of the Alpine landscapes, the snow remains for a long time - until March. "
            "110 km of diverse routes have been laid; stable snow cover is provided by 500 guns. "
            "The resort is considered universal, democratic: skiers of all levels and ages come here. "
            "The skiing season is from December to April.",
            'https://i.f1g.fr/media/figaro/orig/2018/01/17/XVM346ad012-fac7-11e7-9962-196e3970bf6d.jpg'],
        'Port del Comte': ["Port del Comte is a relatively new resort, it has existed since the 70s. "
                           "XX century, located in the Eastern Pyrenees. "
                           "The length of its tracks is approximately 40 km; Ten lifts have been installed. "
                           "The local slopes have a low, simple relief; the local ski school employs dozens of instructors. "
                           "Ski season from late November to late March",
                           'https://upload.wikimedia.org/wikipedia/commons/b/b6/Port_del_Comte-Estivella.JPG']}
    lakes = {'Lago de Sanabria': ["Lake Sanabria in Zamora is one of the largest in Spain and Europe. "
                                  "Its width is 1.5 kilometers, length - 3 kilometers, and depth - about 50 meters. "
                                  "Since there are many different types of water activities on the lake, you can meet hundreds of people enjoying water recreation here.",
                                  'https://upload.wikimedia.org/wikipedia/commons/8/80/Lago_de_Sanabria%2C_provincia_de_Zamora%2C_Espa%C3%B1a.jpg'],
             'Lagos de Covadonga': [
                 "Lagos de Covadonga are three glacial lakes in the Picos de Europa National Park in Spain. "
                 "Enol, La Ercina and El Brisial lakes have water only in the warm months of the year after the ice has melted. "
                 "This area is one of the most visited places of natural beauty in Spain, especially during the summer.",
                 'https://www.65ymas.com/uploads/s1/14/25/49/santuario-lagos-covadonga-asturias-2.jpeg'],
             'Lago de Sant Maurici': ['This stunning lake in Spain is located in the Pyrenees on the Catalan side. '
                                      'It is located in Espot in Lleida at an altitude of 1,910 meters. '
                                      'The lake is part of the Aiguestortes Natural Park, which is the only one in the Catalonia region. '
                                      'Lake Maurici is 1,100 meters long and 200 meters wide.',
                                      'https://1.bp.blogspot.com/-A55cdO4aPRQ/XoIqhXZ2VSI/AAAAAAAALCw/8E0xeUVUs6AOOq9f-w58onJX9KVJlLrfgCLcBGAsYHQ/s1600/estany-gerber-aiguestortes-2.jpg']}
    rivers = {'Mundo': [
        "Located in the province of Albacete, next to the city of Riopar, it is the source of the world river, "
        "in particular in the Natural Park of Calares del Mundo y de la Sima, to which many people go to admire the beautiful waterfall and cave. "
        "The area known as Los Chorros, where the Mundo river originates, where springs and beautiful waterfalls are located, "
        "is accessible by a route of about 6.5 kilometers, which takes no more than two hours. "
        "The mountainous region surrounding the area offers visitors waterfalls between caves and tunnels. "
        "Along the trail you can hear how the riverbed descends abundantly parallel to the trail, "
        "leaving behind many lakes with crystal clear water, where trout lives.",
        'https://upload.wikimedia.org/wikipedia/commons/7/78/Nacimiento_del_R%C3%ADo_Mundo.jpg'],
        'Tagus': [
            "The longest river in Spain originates in the Universal Mountains, west of the province of Teruel on the border with Cuenca, "
            "and flows off the coast of Portugal in the Atlantic Ocean. "
            "A monument with the symbols of the provinces of Teruel (bull with a star), Guadalajara (knight) and Cuenca (bowl) marks the beginning of its canal, "
            "which can be reached by car, and from this point you can start the route on foot. "
            "It passes through a pine forest until it reaches Casas de Fuente Garcia. "
            "The first stream of water from the Tagus falls there. "
            "It is located near the beautiful town of Albarracín, the ideal place to end your holiday in Teruel.",
            'https://terra-z.com/wp-content/uploads/2014/03/523.jpg']}
    # currency
    currencyName = 'EUR'
    currencyEqualsToDollar = 0.95

    # military
    milPolBlock = "NATO"
    amountOfPeopleInArmy = 122850

    # healthcare
    numberOfDoctorsPer100kPopulation = 382
    menAverageLifeExpectancy = 78.2
    womenAverageLifeExpectancy = 84.4

    # climat
    juneAverageTemperature = 25
    decemberAverageTemperature = 14
    averageHumidity = 71
    averageDurationOfWinter = 3.5
    averageRainfallPerMonth = 54
    averageNumberOfFoggyDaysPerYear = 26
    averageNumberOfRainyDaysPerYear = 63
    averageNumberOfClearDays = 97

    # security
    situationInTheCountry = 3  # [1, 3] 1-bad, 3-good
    freedomOfSpeech = 3  # [1, 3]
    assessmentOfFamilyLife = 2  # [1, 3]
    attitudeTowardsLGBT = 3  # [1, 3]

    # population
    populationCount = 47330000
    procentOfMales = 49.4
    procentOfFemales = 50.6
    populationDensityPerSquareKilometer = 92.1
    speedOfLife = 3  # [1, 3]
    workPlaces = 3  # [1, 3]
    nightLifeEntertainment = 3  # [1, 3]

    # citizenship
    citizenshipGlobalRank = 2
    friendlyToForeigners = 2

    # communication
    communicationOnEnglish = 2  # [1, 3]

    # transport
    averageTravelTimeToWork = 29.06
    developmentLevelOfPublicTransport = 3  # [1, 3]

    # internet
    speedOfInternetMbps = 21  # Мегабиты в секунду
    freeWifi = 2  # [1, 3]

    # education
    rankingOfNationalEducationSystem = 23

    cc.createBase(countryName, cities, officialLanguage,
                  # currency
                  currencyName, currencyEqualsToDollar,
                  # military
                  milPolBlock, amountOfPeopleInArmy,
                  # healthcare
                  numberOfDoctorsPer100kPopulation, menAverageLifeExpectancy, womenAverageLifeExpectancy,
                  # climat
                  juneAverageTemperature, decemberAverageTemperature, averageHumidity,
                  averageDurationOfWinter, averageRainfallPerMonth, averageNumberOfFoggyDaysPerYear,
                  averageNumberOfRainyDaysPerYear, averageNumberOfClearDays,
                  # security
                  situationInTheCountry, freedomOfSpeech,
                  assessmentOfFamilyLife, attitudeTowardsLGBT,
                  # population
                  populationCount, procentOfMales, procentOfFemales, populationDensityPerSquareKilometer,
                  speedOfLife, workPlaces, nightLifeEntertainment,
                  # citizenship
                  citizenshipGlobalRank,
                  # communication
                  communicationOnEnglish,
                  # transport
                  averageTravelTimeToWork, developmentLevelOfPublicTransport,
                  # internet
                  speedOfInternetMbps, freeWifi,
                  # education
                  rankingOfNationalEducationSystem, universities, faculties, programs, costs, links, images,
                  requirements,
                  hostel, scolarship, sights, beaches, mountains, skiResorts, lakes, rivers, friendlyToForeigners
                  )

    # cc.createManMadeDisaster(countryName, nameMMD, typeOfMMD, aomuntOfDeadPeople,
    #                           aomuntOfInjuredPeople, territoryOfPollution)
    # cc.createOceans()
    #############################   Spain   #############################

    #############################   Portugal   #############################

    # Country
    countryName = "Portugal"
    officialLanguage = "Portuguese"

    # cities    name   isBig  washesBy
    cities = {
        'Lisbon': [True, True, 'Atlantic ocean'],
        'Portu': [True, True, 'Atlantic ocean'],
        'Amadora': [True, True, 'Atlantic ocean'],
        'Braga': [True, False, None],
        'Setubal': [True, True, 'Atlantic ocean'],
        'Faro': [True, True, 'Atlantic ocean']}

    # education
    universities = {'Lisbon': ['Polytechnic Institute', 'University of Lisbon'],
                    'Portu': ['Universidade do Porto'],
                    'Faro': ['Universidade do Algarve']}
    faculties = {
        'Polytechnic Institute': ['Faculty of Education', 'Faculty of Engineering', 'Faculty of Medicine',
                                  'Faculty of Economics'],
        'University of Lisbon': ['Faculty of Architecture', 'Faculty of Arts', 'Faculty of Law', 'Faculty of Science',
                                 'Faculty of Education', 'Faculty of Medicine'],
        'Universidade do Porto': ['Faculty of Architecture', 'Faculty of Arts', 'Faculty of Law',
                                  'Faculty of Economics',
                                  'Faculty of Engineering', 'Faculty of Medicine'],
        'Universidade do Algarve': ['Faculty of Economics', 'Faculty of Medicine', 'Faculty of Law',
                                    'Faculty of Engineering']}
    programs = {
        'Polytechnic Institute': ['Magistracy', 'Undergraduate'],
        'University of Lisbon': ['Magistracy', 'Undergraduate', 'Doctoral'],
        'Universidade do Porto': ['Magistracy', 'Undergraduate', 'Doctoral'],
        'Universidade do Algarve': ['Magistracy', 'Undergraduate']}
    links = {'Polytechnic Institute': 'https://www.ipl.pt',
             'University of Lisbon': 'https://www.ulisboa.pt',
             'Universidade do Porto': 'https://www.up.pt/',
             'Universidade do Algarve': 'https://www.ualg.pt/'}
    images = {
        'Polytechnic Institute': 'https://smapse.com/storage/2019/08/z1-21.jpg',
        'University of Lisbon': 'https://smapse.com/storage/2020/12/universidade-de-lisboa-smapse7.jpg',
        'Universidade do Porto': 'https://www.estudarfora.org.br/wp-content/uploads/2020/04/unipo.jpg',
        'Universidade do Algarve': 'https://www.clbrief.com/wp-content/uploads/2020/11/algarve-uni-2-1000x642.jpg'}
    # общага
    hostel = {'Polytechnic Institute': 'Yes',
              'University of Lisbon': 'Yes',
              'Universidade do Porto': 'Yes',
              'Universidade do Algarve': 'Yes'}
    # стипендия
    scolarship = {'Polytechnic Institute': 'Yes',
                  'University of Lisbon': 'Yes',
                  'Universidade do Porto': 'Yes',
                  'Universidade do Algarve': 'Yes'}
    # требования к поступлению
    requirements = {
        'Polytechnic Institute': 'A certain number of students can enter the university every year. '
                                 'A special selection committee makes its decision on the recruitment of first-year students, based on data on past academic performance. '
                                 'The results of the entrance exams are also taken into account. By and large, not only residents of Portugal, but also the entire globe, apply for places in the university.',
        'University of Lisbon': 'The deadline for submitting documents is from June 20 to July 20.',
        'Universidade do Porto': 'High school diploma (12 years), certificates of additional programs (International Foundation), documents confirming the completion of 1-2 courses. '
                                 'Proficiency in Portuguese - B2 according to CEFRL. '
                                 'Compliance with the prerequisites (physical, functional or professional conditions) established for the study cycle they intend to take.',
        'Universidade do Algarve': 'Enrollment to study at the university is based on the previously provided results of the exams passed. '
                                   'Each academic year is traditionally divided into semesters.'}
    costs = {'Polytechnic Institute': 3200,
             'University of Lisbon': 1900,
             'Universidade do Porto': 3500,
             'Universidade do Algarve': 3460}

    sights = {'Obidos Castle': [
        "A true favorite among the medieval castles of Portugal can be considered the castle of Obidos, located on a hill, "
        "offering a wonderful view of the surroundings of the city of the same name: vineyards, windmills, bright terracotta roofs of the surrounding houses. "
        "The castle itself attracts many tourists with its battlements, preserved from the Middle Ages to the present day in surprisingly good condition. "
        "In the form in which we see the castle now, it was built in the 13th century, and before that, in the era of the Roman Empire, "
        "there were public baths and a square, which played the role of the center of the political life of the settlement. "
        "After the fall of the Roman Empire, with the coming to power of the Visigoths, a fortress was built on this site, around which a settlement was formed - the future city of Obidos. "
        "In the 8th century, the fortress passed into the possession of the Muslims, and only in the 13th century did the Portuguese king Afonso recapture this building. "
        "Today, this landmark of Portugal has retained its appearance, which is why it attracts many tourists - you can walk around the castle grounds, "
        "study its architecture - arched passages, medieval bas-reliefs, as well as view magnificent views of the surroundings from a height.",
        'https://dynamic-media-cdn.tripadvisor.com/media/photo-o/0d/6e/7b/06/castelo-de-obidos.jpg?w=1200&h=-1&s=1'],
        'Pena Palace': [
            "Sintra is a suburb of the Portuguese capital, the most important in terms of attractions in Portugal. "
            "Not far from Sintra, in the mountains, there is an unusual castle-palace of Pena. "
            "Its uniqueness lies in the fact that initially an empty monastery was taken as its basis, which was erected here back in the distant 12th century in honor of the Mother of God. "
            "Over time, the temple fell into disrepair. "
            "The inconspicuous and abandoned chapel, lost in the mountains, was remembered only in the 16th century, when King Manuel I, "
            "being very religious, turned his gaze to this temple and to the rather vast empty lands around it. "
            "From that moment, the reconstruction of the sanctuary began - it was rebuilt from stone and stood for about 2 more centuries, "
            "until a powerful earthquake known throughout Europe happened, which turned the monastery into ruins. "
            "And only in 1838, King Fernando II buys the land along with the ruins of the temple and the picturesque adjacent territories on the mountain. "
            "He orders to rebuild a palace on these lands, which later became the summer residence of the royal family. "
            "Romantic Fernando made a significant contribution to the design of the castle and its surrounding areas. "
            "As a result, a beautiful and majestic building has grown on these lands with an exotic exterior, representing a mixture of several styles, "
            "bright facades and an amazing park, with its winding paths, cozy gazebos and rich colors of outlandish plants.",
            'https://www.tripzaza.com/ru/destinations/wp-content/uploads/2017/06/Portugal-3-The-Pena-Palace-e1497061654426.jpg'],
        'Alto Douro': [
            "The Alto Douro region has long been known for producing wine of exceptional taste and quality for over 2,000 years. "
            "Local climatic conditions have such weather features that allow you to collect generous harvests of grapes of various varieties. "
            "The area is distinguished by a rather steep soil relief, from different sides it is protected from winds and moisture by the mountains of Montemuro and Maran, "
            "which creates a dry and hot climate here, which is most favorable for the ripening of grapes and for obtaining fragrant fortified wines. "
            "The wine produced here takes first place in international competitions, and this once again confirms the quality of local products. "
            "Traveling through the wine attractions of Portugal, in one of the local farms you can have a tasting of drinks, buy delicious wine or port wine. "
            "If you wish, you can take part in the harvest and the subsequent wine festival, feel the taste of life in this beautiful and fertile land.",
            'https://www.tripzaza.com/ru/destinations/wp-content/uploads/2017/06/Portugal-5-Alto-Douro-e1497062089463.jpg']}
    beaches = {'Praia da Marina beach': ["The beach is distinguished not only by its exquisite beauty, "
                                         "but also by the steepness of the coastline, therefore, to get to the water, you have to go down a long and steep staircase, but it's worth it. "
                                         "Below you will see the coast from a new angle - many islands-rocks, which have bizarre shapes due to prolonged exposure to water and wind, "
                                         "in an ensemble with the sea create an amazingly beautiful landscape. "
                                         "On the beach, you can not only swim or soak up the sun - outdoor enthusiasts can explore the local bays, caves and grottoes. "
                                         "Despite the wild scenery, the beach itself is landscaped - there is parking, a restaurant, rental of swimming equipment, lifeguards work. "
                                         "There is also the opportunity to snorkel and explore the rich underwater world - it may not be as rich as in the Red Sea, but all kinds of shrimp, "
                                         "colorful fish and starfish are present here in abundance.",
                                         'https://www.tripzaza.com/ru/destinations/wp-content/uploads/2017/06/Portugal-11-Praia-da-Marinha-e1497064402881.jpg'],
               "Praia de Sao Rafael": ["San Rafael is beautiful, like all the beaches in the south of Portugal. "
                                       "It is surrounded by several limestone cliffs with unique water caves. "
                                       "Here, the purest water and soft sand, however, during low tide and strong surf, "
                                       "it is very difficult to enter the water - immediately behind the sandy strip, the bottom is lined with stones. "
                                       "You need to go down the stairs to the beach, although the descent is not big. "
                                       "The infrastructure of de Sao Rafael is quite well developed: there are many public showers, there are shops, there is an excellent restaurant serving fresh seafood. "
                                       "There is a large free car park nearby. But there are no places to rent sunbeds.",
                                       'https://kuku.travel/wp-content/uploads/2018/04/%D0%9F%D0%BB%D1%8F%D0%B6-Praia-de-Sao-Rafael.jpg'],
               'Praia da Coelha': [
                   "5 km east of Albufeira there is a small Coelha beach with a sand strip of 70-80 m long, completely protected from the winds by high cliffs. "
                   "Like many beaches around Albufeira, it has been awarded the Blue Flag. "
                   "Clean and gentle entry into the water makes this beach attractive for a relaxing holiday with kids, and many adults will enjoy snorkeling among the coastal cliffs. "
                   "In summer, the water warms up to an average of + 20-23 ºC.",
                   'https://kuku.travel/wp-content/uploads/2018/04/%D0%A4%D0%BE%D1%82%D0%BE-%D0%BF%D0%BB%D1%8F%D0%B6%D0%B0-Praia-da-Coelha.jpg']}
    mountains = {'Pico': [
        "Pico is a dormant active stratovolcano located on the Mid-Atlantic Ridge and is the highest point of the ridge, Pico Island and Portugal.",
        'https://upload.wikimedia.org/wikipedia/commons/f/fd/Picocanal.jpg'],
        'Pico do Arieiro': ["Pico do Arieiro is the third highest mountain on the island of Madeira, "
                            "the main island of the archipelago of the same name in the Atlantic Ocean, after Pico Ruivo and Pico das Torres. "
                            "It is a good vantage point for viewing the surrounding landscapes, "
                            "as well as one of the options for the starting point of the PR1 Vereda do Areeiro hiking route.",
                            'https://upload.tury.club/data/41f045bafea2d2b40352c725132f5394/9A3PBhFx/GwcyrlD8.jpg'],
        'Pico Ruivo': [
            'Pico Ruivo is the highest mountain in Madeira, the main island of the Madeira archipelago in the Atlantic Ocean. '
            'The height of the mountain is 1862 meters. It is also the third highest peak in Portugal.',
            'https://fs.tonkosti.ru/9g/z6/9gz6f3rpujoksckogkgks4wsc.jpg']}
    skiResorts = {}
    lakes = {'Lagoa do Fogo': [
        "This lake is situated on Sao Miguel island, Azores. It is the second largest lake on the island. In 1974 it was declared a natural reserve. "
        "It covers an area of 13.6 km², located at an altitude of 947 m above sea level, "
        "located on the cauldron of an extinct volcano, which formed about 15,000 years ago",
        'https://s9.travelask.ru/uploads/hint_place/000/115/653/image/aa2b00ee315d4f6aed788503f3c9c91f.jpg'],
        'Pateira de Fermentelos': [
            "This is the largest natural lake in the entire Iberian Peninsula, which is known as a habitat for a variety of flora and fauna. "
            "It is fed by two rivers, the Settima and the Agueda, which converge at the lake. "
            "Pateira de Fermentelos offers its guests excellent fishing, canoeing, boating and sailing. "
            "In the nearest city, Aveiro, tourists will find many options for accommodation.",
            'https://womanadvice.ru/sites/default/files/49/2018-03-03_1703/pateyra_de_fermentelos.jpg'],
        'Lake Obidos': [
            'In this unique location, located in the Obidos and Caldas da Reina regions of Portugal, the lake is bordered by a sea lagoon. '
            'As well as relaxing on stunning beaches, you can enjoy shellfishing, boating, sailing, windsurfing and canoeing. '
            'In the nearby town of Obidos, tourists will find several small guesthouses and hotels, authentic Portuguese cuisine and an impressive medieval fortress.',
            'https://womanadvice.ru/sites/default/files/49/2018-03-03_1703/ozero_obidush.jpg']}
    rivers = {'Minho': ["Length - 340 km, basin area - 22.5 thousand km². "
                        "The sources of Minho are in the Cantabrian Mountains in the Meira region of the province of Lugo, then the river flows through the hilly terrain of the autonomous community of Galicia. "
                        "After the confluence of the main tributary, the Sil River, the valley becomes wider. "
                        "The last 80 km before it flows into the Atlantic Ocean, Minho is the border between Spain and Portugal.",
                        'https://img.freepik.com/premium-photo/panoramic-view-of-cerveira-and-the-river-minho-on-the-border-between-portugal-and-spain_462054-914.jpg'],
              'Tacho': [
                  "Tajo flows in Spain through the autonomous communities of Aragon, Castile-La Mancha, Madrid and Extremadura, "
                  "then a small section of the river runs along the border of Spain and Portugal. "
                  "A river flows through the territory of Portugal under the name Tagus. "
                  "To the southeast of Lisbon, the river is crossed by the Vasco da Gama Bridge, 17.2 km long. "
                  "The river flows into the bay of Mar da Paglia, which is sometimes considered its estuary. "
                  "The double name of the river, as a rule, is reflected on geographical maps. "
                  "On the territory of Spain, the river is called Tajo, and in Portugal the name changes to Tejo: "
                  "there is an analogy for the change of names in the Western Dvina in the territories of Russia and Belarus, "
                  "which in the territory of Latvia changes its name to the Daugava, as well as the Neman in Belarus, "
                  "which is in the territory of Lithuania called Nemunas.",
                  'https://thumbs.dreamstime.com/b/%D1%80%D0%B5%D0%BA%D0%B0-%D1%82%D0%B0%D1%85%D0%BE-35824273.jpg']}
    # currency
    currencyName = 'EUR'
    currencyEqualsToDollar = 0.95

    # military
    milPolBlock = "NATO"
    amountOfPeopleInArmy = 27250

    # healthcare
    numberOfDoctorsPer100kPopulation = 443
    menAverageLifeExpectancy = 75.3
    womenAverageLifeExpectancy = 82

    # climat
    juneAverageTemperature = 22
    decemberAverageTemperature = 16
    averageHumidity = 71
    averageDurationOfWinter = 3
    averageRainfallPerMonth = 68
    averageNumberOfFoggyDaysPerYear = 26
    averageNumberOfRainyDaysPerYear = 112
    averageNumberOfClearDays = 184

    # security
    situationInTheCountry = 3  # [1, 3] 1-bad, 3-good
    freedomOfSpeech = 3  # [1, 3]
    assessmentOfFamilyLife = 2  # [1, 3]
    attitudeTowardsLGBT = 3  # [1, 3]

    # population
    populationCount = 47330000
    procentOfMales = 49.4
    procentOfFemales = 50.6
    populationDensityPerSquareKilometer = 109.9
    speedOfLife = 3  # [1, 3]
    workPlaces = 3  # [1, 3]
    nightLifeEntertainment = 3  # [1, 3]

    # citizenship
    citizenshipGlobalRank = 3
    friendlyToForeigners = 1

    # communication
    communicationOnEnglish = 3  # [1, 3]

    # transport
    averageTravelTimeToWork = 29.56
    developmentLevelOfPublicTransport = 3  # [1, 3]

    # internet
    speedOfInternetMbps = 28  # Мегабиты в секунду
    freeWifi = 2  # [1, 3]

    # education
    rankingOfNationalEducationSystem = 25

    cc.createBase(countryName, cities, officialLanguage,
                  # currency
                  currencyName, currencyEqualsToDollar,
                  # military
                  milPolBlock, amountOfPeopleInArmy,
                  # healthcare
                  numberOfDoctorsPer100kPopulation, menAverageLifeExpectancy, womenAverageLifeExpectancy,
                  # climat
                  juneAverageTemperature, decemberAverageTemperature, averageHumidity,
                  averageDurationOfWinter, averageRainfallPerMonth, averageNumberOfFoggyDaysPerYear,
                  averageNumberOfRainyDaysPerYear, averageNumberOfClearDays,
                  # security
                  situationInTheCountry, freedomOfSpeech,
                  assessmentOfFamilyLife, attitudeTowardsLGBT,
                  # population
                  populationCount, procentOfMales, procentOfFemales, populationDensityPerSquareKilometer,
                  speedOfLife, workPlaces, nightLifeEntertainment,
                  # citizenship
                  citizenshipGlobalRank,
                  # communication
                  communicationOnEnglish,
                  # transport
                  averageTravelTimeToWork, developmentLevelOfPublicTransport,
                  # internet
                  speedOfInternetMbps, freeWifi,
                  # education
                  rankingOfNationalEducationSystem, universities, faculties, programs, costs, links, images,
                  requirements,
                  hostel, scolarship, sights, beaches, mountains, skiResorts, lakes, rivers, friendlyToForeigners
                  )

    # cc.createManMadeDisaster(countryName, nameMMD, typeOfMMD, aomuntOfDeadPeople,
    #                           aomuntOfInjuredPeople, territoryOfPollution)
    # cc.createOceans()
    #############################   Portugal   #############################
    #############################   Argentina   #############################

    # Country
    countryName = "Argentina"
    officialLanguage = "Spanish"

    # cities    name   isBig  washesBy
    cities = {
        'Buenos Aires': [True, True, 'Atlantic ocean'],
        'Cordova': [True, False, None],
        'Rosario': [True, False, None],
        'Mendoza': [True, False, None],
        'La Plata': [True, True, 'Atlantic ocean'],
        'Mar del Plata': [False, True, 'Atlantic ocean'],
        'Pinamar': [False, True, 'Atlantic ocean'],
        'Miramar': [False, True, 'Atlantic ocean']}

    # education
    universities = {'Buenos Aires': ['University of Buenos Aires', 'Universidad de Palermo Argentina'],
                    'La Plata': ['National University of La Plata'],
                    'Rosario': ['Universidad Nacional de Rosario']}
    faculties = {
        'University of Buenos Aires': ['Faculty of Economics', 'Faculty of Architecture', 'Faculty of Arts',
                                       'Faculty of Social Sciences',
                                       'Faculty of Law', 'Faculty of Engineering', 'Faculty of Medicine',
                                       'Faculty of Science'],
        'Universidad de Palermo Argentina': ['Faculty of Economics', 'Faculty of Architecture', 'Faculty of Education',
                                             'Faculty of Social Sciences'],
        'National University of La Plata': ['Faculty of Arts', 'Faculty of Computer Engineering and Software',
                                            'Faculty of Education',
                                            'Faculty of Science', 'Faculty of Social Sciences',
                                            'Faculty of Engineering',
                                            'Faculty of Medicine', 'Faculty of Law', 'Faculty of Forestry',
                                            'Faculty of Economics',
                                            'Faculty of Architecture', 'Faculty of Forestry'],
        'Universidad Nacional de Rosario': ['Faculty of Law', 'Faculty of Medicine', 'Faculty of Science',
                                            'Faculty of Economics',
                                            'Faculty of Architecture']}
    programs = {
        'University of Buenos Aires': ['Magistracy', 'Undergraduate'],
        'Universidad de Palermo Argentina': ['Magistracy', 'Undergraduate', 'MBA'],
        'National University of La Plata': ['Magistracy', 'Undergraduate'],
        'Universidad Nacional de Rosario': ['Magistracy', 'Undergraduate']}
    links = {'University of Buenos Aires': 'https://www.uba.ar',
             'Universidad de Palermo Argentina': 'https://www.palermo.edu',
             'National University of La Plata': 'https://www.unipage.net',
             'Universidad Nacional de Rosario': 'https://unr.edu.ar/'}
    images = {
        'University of Buenos Aires': 'https://i0.wp.com/www.argencon.org/wp-content/uploads/2022/04/argencon_uba_110422.jpg?fit=1920%2C1080&ssl=1',
        'Universidad de Palermo Argentina': 'https://fastly.4sqi.net/img/general/600x600/27422897_cc6kJ6R3ALL5CLDnno1c1nHarbnni-qT_PTb19iPnXg.jpg',
        'National University of La Plata': 'https://forum.awd.ru/files/06/54/65838_68aa88ccc36031103bcacf0d49fd69be.jpg',
        'Universidad Nacional de Rosario': 'https://conlagentenoticias.com/wp-content/uploads/2020/06/facultad-de-medicina-rosario.jpg'}
    # общага
    hostel = {'University of Buenos Aires': 'Yes',
              'Universidad de Palermo Argentina': 'Yes',
              'National University of La Plata': 'Yes',
              'Universidad Nacional de Rosario': 'Yes'}
    # стипендия
    scolarship = {'University of Buenos Aires': 'Yes',
                  'Universidad de Palermo Argentina': 'Yes',
                  'National University of La Plata': 'Yes',
                  'Universidad Nacional de Rosario': 'Yes'}
    # требования к поступлению
    requirements = {
        'University of Buenos Aires': 'Unlike most universities, the academic year here is divided into quarters. '
                                      'Annual education at the university costs only 1000 USD. Undergraduates of any direction for an annual stay in these walls must pay the same amount. '
                                      'Most of the students use the opportunity to receive distance education. '
                                      'All questions related to admission and payment procedure can be clarified on the official website of the university.',
        'Universidad de Palermo Argentina': "To get an undergraduate education, you will need to pay an amount of about 5000 USD, and for a master's degree - about 7000 USD. "
                                            "To enter the University of Palermo in Argentina, you must pass the entrance exams. As in many higher education institutions, the academic year here consists of semesters. "
                                            "Universidad de Palermo Argentina is a relatively small institution. "
                                            "The university accommodates about 10,000 thousand students (both local residents and guests from other states). "
                                            "There are also about 1000 teaching staff here, including tinned professors, candidates and doctors of science.",
        'National University of La Plata': 'To become a student, you need to submit an application and an application package, as well as pass exams. '
                                           'The selection committee takes into account only the academic achievements of the applicant, without discriminating him on gender, religious or political grounds. '
                                           'Tuition at the university is paid. For citizens of Argentina and foreigners, the tuition fee is 1000 USD / year. '
                                           'This amount is the same for undergraduate and graduate students. '
                                           'The cost of living during the period of study will cost the student in the amount of 450 to 880 USD per month.',
        'Universidad Nacional de Rosario': 'Since 2013, to confirm the school certificate, it is necessary to pass specialized exams. '
                                           'As for the certificate itself and its appendix, this issue should be clarified in advance with the selection committee of the selected university. '
                                           'Perhaps an apostilled document with a legal Spanish translation made in Argentina will suffice. '
                                           'Among other required documents: two photocopies of the international passport and photos for the student card. '
                                           'The full list of documents for admission should be found on the website of the selected university - requirements may vary'}
    costs = {'University of Buenos Aires': 1000,
             'Universidad de Palermo Argentina': 5000,
             'National University of La Plata': 1000,
             'Universidad Nacional de Rosario': 1000}

    sights = {'Iguazu Falls': ["The real pearl of the country are the Iguazu Falls. "
                               "This is a real miracle of nature, consisting of a whole complex of waterfalls, the number of which reaches 275. "
                               "They are located in the form of a crescent. One of the seven wonders of the world appeared as a result of a volcanic eruption. "
                               "Interestingly, in translation, the name of the waterfall means big water. "
                               "The treasure was discovered in 1541 by the Spaniard Cabeza de Vaca while traveling through the South American jungle. "
                               "There are many legends associated with this place. One of them says that once God fell in love with an aboriginal beauty named Naipu, but these feelings were not mutual. "
                               "Naipu loved another man, with whom she decided to sail away in a canoe. God got angry and cut the river, creating a waterfall so that the lovers would die.",
                               'https://www.tripzaza.com/ru/destinations/wp-content/uploads/2017/08/Iguazu_Falls_with_Rainbow-e1503547292769.jpg'],
              'Nahuel Huapi National Park': [
                  "Once in Argentina, it is impossible not to visit the amazing Nahuel Huapi National Park. "
                  "This attraction is located in the very south of the country. The park got its name because of Lake Nahuel Huapi. "
                  "The main territory of the park is seven hundred and eighty-five hectares. The main goal is the conservation of rare plants and animals. "
                  "There are many representatives of the animal world, as well as powerful and majestic forests. Individual trees are about five hundred years old. "
                  "One of the places that deserve attention in the park is the extinct volcano Tronador. Its height is about 3478 meters above sea level. "
                  "You can see on the Internet the sights of Argentina with photos and descriptions.",
                  'https://www.tripzaza.com/ru/destinations/wp-content/uploads/2017/08/Cerro_Tronador-e1503550048710.jpg'],
              'Talampaya Park': ["In the province of La Rioja, we offer tourists to visit the unique Talampaya Park. "
                                 "It became national only in 1997, and in 2000 it ended up on the World Heritage List. "
                                 "Due to the large number of rivers, many species of animals live here. "
                                 "Archaeological excavations are constantly conducted in the park. "
                                 "For example, a lot of evidence was found that dinosaurs lived here for a very long time. "
                                 "The nature of the park is unique. Here you can find unique sculptures made of stone and sand. "
                                 "The famous composition is The Lost City. The remains of a turtle that lived on the planet about two hundred and ten million years ago were found in the park.",
                                 'https://www.tripzaza.com/ru/destinations/wp-content/uploads/2017/08/Natsionalnyiy_park_Talampayya-e1503552911253.jpg']}
    beaches = {'Miramar': [
        "Miramar (Miramar) translated from Spanish translates as Look at the sea, in some sources you can find Overlooking the sea."
        " The Argentinean resort is located on the Atlantic coast in the quiet town of Miramar, 40 km from Mar Del Plata. "
        "The beach itself is located in the picturesque lagoon of La Bellenera, a quiet and peaceful place, which is often chosen by families with children.",
        'https://1001beach.ru/img/posts/1032/750/las_grutas_beach-1.webp?t=1580381569'],
        "Las Grutas": [
            "Las Grutas is located 15 km from the city of San Antonio Oeste on the coast of the Atlantic Ocean. "
            "Translated from Spanish, the name of the beach means caves and grottoes, which surround the beach area, turning it into a picturesque place. "
            "Locals call Las Grutas a piece of paradise in Patagonian land.",
            'https://1001beach.ru/img/posts/1034/750/villa_gesell_beach-1.webp?t=1580381584'],
        'Pinamar': [
            "Pinamar is a small resort town, in which a huge number of tourists from the country's capital arrive in the warm season. "
            "It is located on the Atlantic coast about three hundred kilometers from Buenos Aires and about one hundred kilometers north of another popular resort in the country - Mar del Plata.",
            'https://1001beach.ru/img/posts/1030/750/carilo_beach-1.webp?t=1580381558']}
    mountains = {'Aconcagua': ["The peak of this mountain reaches 6962 meters, it is also called the Stone Guard. "
                               "Aconcagua is the main attraction in Argentina, because it is the highest mountain and an extinct volcano in all of South America. "
                               "The summit is covered with permanent snow. The mountain is located in the center of the Andes. "
                               "Another unique place here that nature has created is the Inca Bridge. "
                               "Aconcagua attracts climbers with its grandeur.",
                               'https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Aconcagua2016.jpg/640px-Aconcagua2016.jpg'],
                 'Fitzroy': ["There is a peak on the border between Chile and Argentina in Patagonia. "
                             "The height of the peak is 3405 m. Often there is another name “Cerro Chalten”, which means “smoking mountain”. "
                             "Clouds enveloping the top create a picture as if it is in the power of smoke. "
                             "Jagged cliffs, as well as adverse weather conditions, get in the way of climbers,"
                             " so conquering the summit is a rather difficult task.",
                             'https://media-cdn.tripadvisor.com/media/photo-s/0f/31/cc/8b/photo0jpg.jpg'],
                 'Serranha del Aguarage': [
                     'Colored mountains striking with their uniqueness and beauty stretch for 154 km in the province of Jujuy. '
                     'Locals call this mountain range Hornokal. The zigzag shape of the mountains has about 11 shades, if you carefully consider them. '
                     'Such a natural miracle is due to various deposits of natural rocks that lie on top of each other in layers, creating a magnificent landscape.',
                     'https://live.staticflickr.com/65535/49094173797_5eab0bd8eb_b.jpg']}
    skiResorts = {
        'La Jolla': ["The resort is located in Chubut, near Esquel, where one of the best snows in Argentina falls. "
                     "La Jolla receives 900 cm of dry powder annually. "
                     "Snowfall is usually expected in the fall - early, possibly mid-October. "
                     "This is because the ski resort is oriented to the south. "
                     "La Jolla is a small ski resort with little infrastructure. "
                     "However, excellent snow cover compensates for this. "
                     "Dry loose off-piste snow is what gives skiers the thrill of their lives. "
                     "This resort offers unrivaled off-piste opportunities like no other. "
                     "There are natural half-pipes, wide-open bowls, flutes, long groomed runs, everything an avid skier wants to see on a ski run. "
                     "The forbidden territory of this resort is indescribable, with long miles of couloirs, wide bowls.",
                     'https://skipedia.ru/wp-content/uploads/2017/11/3af8f8ee0380868ef2717ecef34ad6e5.jpg'],
        'Cerro Chapelco': [
            "Recently, Chapelco has spent resources improving its lifts, adding high-speed quads and gondolas to their base. "
            "This gives skiers the opportunity to have a complete skiing experience in the snowy mountains of Argentina. "
            "What distinguishes the landscape of this resort from other resorts is the hanging moss-covered trees. "
            "Tourists will not find similar trees with grated powder anywhere else but this place. "
            "As for the terrain, whether you are a beginner or an experienced skier, the ski area suits skiers of all levels.",
            'https://bungary.ru/wp-content/uploads/2020/10/14.jpg'],
        'Las Leñas': [
            "Known for its steep slopes, stunning off-piste runs, Las Leñas welcomes many visitors of all abilities. "
            "Although tourists, skiers, riders need to make a lot of efforts to get to the resort. "
            "However, the location and scenic beauty make the trip even more worthwhile. "
            "The epic terrain makes Las Leñas skiing a real treat. "
            "The snow cover changes every year, but the quality is usually top notch, even during July. "
            "Las Leñas offers one of the longest, most exciting runs in the world. "
            "This makes it even more fun for intermediate to advanced hikers as they can experience a real skiing adventure "
            "in the middle of summer when summer is at its peak in the US.",
            'https://dynamic-media-cdn.tripadvisor.com/media/photo-o/13/c9/fd/7f/desde-la-pista-departamentos.jpg?w=600&h=400&s=1']}
    lakes = {'Nahuel Huapi': [
        "Lake Nahuel Huapi is not only famous for its beauty and grandeur, but many mysterious stories are associated with it. "
        "It is believed that a monster lives at the very bottom of the lake, which sometimes appears from under the water. "
        "Crowds of tourists travel to Argentina to see the mysterious beast. "
        "Scientists have repeatedly come to discover the monster, but all to no avail. "
        "Locals offer tourists all kinds of souvenirs in the form of a mysterious beast. "
        "Trips around the park by car are offered, the length of the path is two hundred and eighty kilometers.",
        'https://www.tripzaza.com/ru/destinations/wp-content/uploads/2017/08/Ozero_Nahue%60l_Huapi-e1503549110284.jpge'],
        'Buenos Aires': [
            "The border lake in the Andes between Chile and Argentina receives glacial nourishment of the highlands. "
            "Area - 1850 km². The maximum depth of the reservoir is 580 meters. T"
            "he rivers flowing from Buenos Aires carry their waters to the Pacifiс Ocean. "
            "In the west of the reservoir there are many fjords, the rest of the lake parts are located on the plain. "
            "There are wonderful marble grottoes on the Chilean side of the freshwater lake.",
            'https://must-see.top/wp-content/uploads/2019/09/buenos-ai-res-700x465.jpeg'],
        'Lago Argentino': [
            'The freshwater reservoir is located in the province of Santa Cruz. The area is 1415 km². '
            'The maximum depth of the reservoir is 500 meters. The lake is part of the Los Glaciares National Park. '
            'The type of nutrition of the reservoir is considered glacial. Lago Argentino is a great place for fishing. '
            'The lake fauna consists of a huge number of fish species. Not far from this place is a large Argentine airport and the city of El Calafate.',
            'https://must-see.top/wp-content/uploads/2019/09/lago-arhentino-700x463.jpg']}
    rivers = {'Paraná': [
        "Parana - a river in South America, the second longest after the famous Amazon, takes 8th place in the list of the largest water systems on the planet. "
        "It flows in the southeastern part of the continent, linking three countries: it partially serves as the natural state border of Brazil, Argentina and Paraguay. "
        "The name of the river in the language of the Indian tribe Tupi means Big as the sea or Similar to the sea.",
        'https://www.syl.ru/misc/i/ai/293549/1617532.jpg']}
    # currency
    currencyName = 'ARS'
    currencyEqualsToDollar = 169.93

    # military
    milPolBlock = 'TIAR'
    amountOfPeopleInArmy = 214000

    # healthcare
    numberOfDoctorsPer100kPopulation = 326
    menAverageLifeExpectancy = 68.4
    womenAverageLifeExpectancy = 73.8

    # climat
    juneAverageTemperature = 15
    decemberAverageTemperature = 25
    averageHumidity = 69
    averageDurationOfWinter = 5
    averageRainfallPerMonth = 98
    averageNumberOfFoggyDaysPerYear = 26
    averageNumberOfRainyDaysPerYear = 102
    averageNumberOfClearDays = 105

    # security
    situationInTheCountry = 3  # [1, 3] 1-bad, 3-good
    freedomOfSpeech = 3  # [1, 3]
    assessmentOfFamilyLife = 2  # [1, 3]
    attitudeTowardsLGBT = 3  # [1, 3]

    # population
    populationCount = 45810000
    procentOfMales = 48.9
    procentOfFemales = 51.1
    populationDensityPerSquareKilometer = 16.5
    speedOfLife = 3  # [1, 3]
    workPlaces = 3  # [1, 3]
    nightLifeEntertainment = 3  # [1, 3]

    # citizenship
    citizenshipGlobalRank = 11
    friendlyToForeigners = 3

    # communication
    communicationOnEnglish = 1  # [1, 3]

    # transport
    averageTravelTimeToWork = 43.86
    developmentLevelOfPublicTransport = 2  # [1, 3]

    # internet
    speedOfInternetMbps = 4  # Мегабиты в секунду
    freeWifi = 2  # [1, 3]

    # education
    rankingOfNationalEducationSystem = 40

    cc.createBase(countryName, cities, officialLanguage,
                  # currency
                  currencyName, currencyEqualsToDollar,
                  # military
                  milPolBlock, amountOfPeopleInArmy,
                  # healthcare
                  numberOfDoctorsPer100kPopulation, menAverageLifeExpectancy, womenAverageLifeExpectancy,
                  # climat
                  juneAverageTemperature, decemberAverageTemperature, averageHumidity,
                  averageDurationOfWinter, averageRainfallPerMonth, averageNumberOfFoggyDaysPerYear,
                  averageNumberOfRainyDaysPerYear, averageNumberOfClearDays,
                  # security
                  situationInTheCountry, freedomOfSpeech,
                  assessmentOfFamilyLife, attitudeTowardsLGBT,
                  # population
                  populationCount, procentOfMales, procentOfFemales, populationDensityPerSquareKilometer,
                  speedOfLife, workPlaces, nightLifeEntertainment,
                  # citizenship
                  citizenshipGlobalRank,
                  # communication
                  communicationOnEnglish,
                  # transport
                  averageTravelTimeToWork, developmentLevelOfPublicTransport,
                  # internet
                  speedOfInternetMbps, freeWifi,
                  # education
                  rankingOfNationalEducationSystem, universities, faculties, programs, costs, links, images,
                  requirements,
                  hostel, scolarship, sights, beaches, mountains, skiResorts, lakes, rivers, friendlyToForeigners
                  )

    # cc.createManMadeDisaster(countryName, nameMMD, typeOfMMD, aomuntOfDeadPeople,
    #                           aomuntOfInjuredPeople, territoryOfPollution)
    # cc.createOceans()
    #############################   Argentina   #############################
    #############################   POLAND   #############################

    # Country
    countryName = "Poland"
    officialLanguage = "Polish"

    # cities    name    isBig WashesBy
    cities = {'Warsaw': [True, True, None], 'Krakow': [True, False, None], 'Lodz': [True, False, None],
              'Wroclaw': [True, True, None], 'Bialystok': [True, False, None], 'Sopot': [False, True, 'Baltic Sea'],
              'Gdynia': [False, True, 'Baltic Sea'], 'Gdansk': [False, True, 'Baltic Sea']}

    # education
    universities = {
        'Warsaw': ['University of Economics and Human Sciences', 'University of Engineering and Health'],
        # https://univerpl.com.ua/ru/universiteti-varshavi/
        'Krakow': ['Jagiellonian University', 'Krakow Academy named after A.F. Modzhevsky'],
        # https://univerpl.com.ua/ru/universiteti-krakova/
        'Lodz': ['Łódź University of Technology', 'University of Lodz'],
        'Wroclaw': ['Wrocław University of Science and Technology', 'University of Wrocław'],
        'Bialystok': ['Bialystok Technical University', 'University of Bialystok']}

    faculties = {'University of Economics and Human Sciences': ['Faculty of Economics',
                                                                'Faculty of Social Sciences',
                                                                'Faculty of Computer Engineering and Software',
                                                                'Faculty of Law', 'Faculty of Medicine'],
                 'University of Engineering and Health': ['Faculty of Social Sciences',
                                                          'Faculty of Architecture',
                                                          'Faculty of Engineering', 'Faculty of Science'],
                 'Jagiellonian University': ['Faculty of Law', 'Faculty of Medicine',
                                             'Faculty of Social Sciences', 'Faculty of Science'],
                 'Krakow Academy named after A.F. Modzhevsky': ['Faculty of Arts',
                                                                'Faculty of Engineering',
                                                                'Faculty of Computer Engineering and Software'],
                 'Łódź University of Technology': [
                     'Faculty of Engineering',
                     'Faculty of Science',
                     'Faculty of Architecture',
                     'Faculty of Economics'],
                 'University of Lodz': ['Faculty of Science', 'Faculty of Social Sciences',
                                        'Faculty of Computer Engineering and Software', 'Faculty of Economics'],
                 'Wrocław University of Science and Technology': ['Faculty of Architecture', 'Faculty of Science',
                                                                  'Faculty of Engineering',
                                                                  'Faculty of Economics'],
                 'University of Wrocław': ['Faculty of Science',
                                           'Faculty of Computer Engineering and Software',
                                           'Faculty of Social Sciences'],
                 'Bialystok Technical University': ['Faculty of Architecture',
                                                    'Faculty of Computer Engineering and Software',
                                                    'Faculty of Engineering',
                                                    'Faculty of Economics'],
                 'University of Bialystok': ['Faculty of Social Sciences',
                                             'Faculty of Computer Engineering and Software', 'Faculty of Economics']}

    programs = {'University of Economics and Human Sciences': ['Magistracy', 'Undergraduate', 'MBA'],
                'University of Engineering and Health': ['Magistracy'],
                'Jagiellonian University': ['Magistracy', 'Undergraduate', 'MBA'],
                'Krakow Academy named after A.F. Modzhevsky': ['Foundation', 'Undergraduate', 'MBA'],
                'Łódź University of Technology': ['Magistracy', 'Undergraduate'],
                'University of Lodz': ['Magistracy', 'Undergraduate'],
                'Wrocław University of Science and Technology': ['Magistracy', 'Undergraduate', 'MBA'],
                'University of Wrocław': ['Magistracy', 'Undergraduate'],
                'Bialystok Technical University': ['Magistracy', 'Undergraduate', 'MBA'],
                'University of Bialystok': ['Magistracy', 'Undergraduate']}
    links = {'University of Economics and Human Sciences': 'https://vizja.pl/en/',
             'University of Engineering and Health': 'https://entrant.eu/en/university/universytet-kosmetologiyi-ta-doglyadu-za-zdorov-yam/',
             'Jagiellonian University': 'https://en.uj.edu.pl/en_GB/start',
             'Krakow Academy named after A.F. Modzhevsky': 'https://en.ka.edu.pl/',
             'Łódź University of Technology': 'https://p.lodz.pl/',
             'University of Lodz': 'https://www.uni.lodz.pl/en',
             'Wrocław University of Science and Technology': 'https://pwr.edu.pl/en/',
             'University of Wrocław': 'https://uwr.edu.pl/',
             'Bialystok Technical University': 'https://pb.edu.pl/',
             'University of Bialystok': 'https://uwb.edu.pl/home'}
    images = {
        'University of Economics and Human Sciences': 'https://vizja.pl/en/wp-content/uploads/sites/2/2021/02/aeh-widok.jpg',
        'University of Engineering and Health': 'https://entrant.eu/wp-content/uploads/2017/12/Wyz-sza-Szko-a-Inz-ynierii-i-Zdrowia.jpg',
        'Jagiellonian University': 'https://kafkadesk.org/wp-content/uploads/2021/05/Jagiellonian-University.png',
        'Krakow Academy named after A.F. Modzhevsky': 'https://en.ka.edu.pl/wp-content/uploads/afmku3.jpg',
        'Łódź University of Technology': 'https://study.gov.pl/sites/default/files/styles/wiz/public/foto_ucz_wiz/86/dfz_1448_70.jpg?itok=T4Q_vkzp',
        'University of Lodz': 'https://study.gov.pl/sites/default/files/styles/wiz/public/foto_ucz_wiz/90/wfl.jpg?itok=haO8CSqe',
        'Wrocław University of Science and Technology': 'https://s3.ap-south-1.amazonaws.com/gotouniv/cover_photo/1119/cover_photo_1500X500.jpg',
        'University of Wrocław': 'https://study.gov.pl/sites/default/files/styles/wiz/public/foto_ucz_wiz/1/_mg_3243_copy_77.jpg?itok=EcTdGl1R',
        'Bialystok Technical University': 'https://smapse.ru/storage/2019/08/z1-3.jpg',
        'University of Bialystok': 'https://study.gov.pl/sites/default/files/styles/wiz/public/foto_ucz_wiz/1/1_235.jpg?itok=Rv93iCE-'}
    # общага
    hostel = {'University of Economics and Human Sciences': 'Yes',
              'University of Engineering and Health': 'Yes',
              'Jagiellonian University': 'Yes',
              'Krakow Academy named after A.F. Modzhevsky': 'No',
              'Łódź University of Technology': 'Yes',
              'University of Lodz': 'No',
              'Wrocław University of Science and Technology': 'No',
              'University of Wrocław': 'No',
              'Bialystok Technical University': 'Yes',
              'University of Bialystok': 'Yes'}
    # стипендия
    scolarship = {'University of Economics and Human Sciences': 'Yes',
                  'University of Engineering and Health': 'Yes',
                  'Jagiellonian University': 'Yes',
                  'Krakow Academy named after A.F. Modzhevsky': 'Yes',
                  'Łódź University of Technology': 'Yes',
                  'University of Lodz': 'Yes',
                  'Wrocław University of Science and Technology': 'Yes',
                  'University of Wrocław': 'Yes',
                  'Bialystok Technical University': 'Yes',
                  'University of Bialystok': 'Yes'
                  }
    # требования к поступлению
    requirements = {'University of Economics and Human Sciences': 'photo. '
                                                                  'passport. '
                                                                  'high school diploma and attachment to high school diploma with subjects and grades. '
                                                                  'bachelor diploma and transcript of studies (for Masters studies). '
                                                                  'certificate of language proficiency (if available)',
                    'University of Engineering and Health': 'minimum GPA of 2 in order to stand a good chance to get admission',
                    'Jagiellonian University': 'complete TOEFL exam with a minimum score of 87. c) TOEFL/IELTS scores if the applicants native language is not English.',
                    'Krakow Academy named after A.F. Modzhevsky': 'Request a list of necessary documents directly from a university, as it may vary for different countries.',
                    'Łódź University of Technology': 'Legalised original (or duplicate) of relevant education certificate(s). Documentary evidence of learning. Polish translation of the certificate (diploma). Passport.',
                    'University of Lodz': 'A high school diploma, a transcript of records showing the subjects/grades and a certificate of proficiency in English (unless the secondary education was taught in English)',
                    'Wrocław University of Science and Technology': 'Passport for inspection,'
                                                                    'your application form printed out from the application system and signed;'
                                                                    'transfer details of payment for your fees (application, tuition, student ID);'
                                                                    'your language certificate or another document serving as such'
                                                                    'for undergraduate programs: your secondary school diploma with a list of grades, for postgraduate programs: your Bachelor’s diploma with a full academic transcript. These documents should be legalized/apostilled and presented together with a certified translation into Polish or English made by a sworn translator.',
                    'University of Wrocław': 'High School graduation certificate or equivalent with decision about nostrification (learn more about nostrification procedure on our website)'
                                             'High School transcript of grades.'
                                             'Certificate confirming access to higher education in your country.',
                    'Bialystok Technical University': 'Secondary school certificate (12 years of education) being the equivalent of Polish secondary school certificate. English language international B2 certificate (upper intermediate) such as FCE, IELTS (min. 6 points),',
                    'University of Bialystok': 'Positive grades in two out of four subjects - Chemistry, Biology, Physics or Mathematics - must be shown on the certificate. or have passed the Matura Exam (High School Final Exam) in two out of four subjects: Chemistry, Biology, Physics or Mathematics.'}

    costs = {'University of Economics and Human Sciences': 2600,
             'University of Engineering and Health': 4300,
             'Jagiellonian University': 3500,
             'Krakow Academy named after A.F. Modzhevsky': 3200,
             'Łódź University of Technology': 2700,
             'University of Lodz': 2400,
             'Wrocław University of Science and Technology': 4100,
             'University of Wrocław': 3000,
             'Bialystok Technical University': 2400,
             'University of Bialystok': 13500}

    # resort
    sights = {'Warsaw Old Town': [
        "Traveling around the country is worth starting with an acquaintance with the historical district of its official capital. It is represented by a market square with a large number of shops, cafes and restaurants for every taste and color. A positive feature of this landmark of Poland is the richness of the area with monuments of medieval architecture. It is interesting to know that the Old Town was founded back in the 13th century, initially it was surrounded by an earthen rampart, later it was replaced with brick walls. Don't forget to bring your camera to take many beautiful photos.",
        'https://www.tripzaza.com/ru/destinations/wp-content/uploads/2018/02/1-The_Warsaw_Old_Town-e1518313891144.jpg'],
        'Marienburg Castle': [
            "Among the main attractions of the country is the 'nest' of German knights. The brick bulk of this castle rises on the banks of the Nogat River, which flows 80 km from the border with the Kaliningrad region of the Russian Federation. Its history began 700 years ago, when the residence of the Teutons was officially transferred from Venice to Marienburg. The fortress was repeatedly completed and decorated. In 1945, the castle was heavily damaged, but after the end of World War II, it was literally rebuilt. Now a museum functions within the walls of the building, there are interesting weapons collections, amber jewelry, and armor.",
            'https://www.tripzaza.com/ru/destinations/wp-content/uploads/2018/02/2-Malbork_Castle-e1518314093567.jpg'],
        'Tatras': [
            "This is the name of the Carpathian mountain system, the highest point of which reaches 2499 m. This place attracts tourists not only with heights in the range of 1800-2500 m, but also with glacial cirques, mountain lakes in large numbers, and deep valleys. The rating of this attraction in Poland is rated as high, all because there is still a ski resort here, known as Zakopane. From the capital, you can get here by train. The Tatras are also known for caves, of which there are really many.",
            'https://www.tripzaza.com/ru/destinations/wp-content/uploads/2018/02/3-Tatry-e1518314227738.jpg']}
    beaches = {'Debki': [
        "Hidden behind the coastal forest, far from the main routes, has long attracted lovers of wild beaches and windsurfers. There are no large crowds of people here and you can enjoy plenty of clean beaches and excellent sand. And the “correct” wind creates all the conditions for practicing water sports.",
        'https://polomedia.ru/sites/default/files/news/05-14/plaza2.jpg'],
        "Krynica Morska": [
            "The Baltic Spit is a corner of the Baltic coast that has not yet been fully discovered by tourists. But here, vacationers have at their disposal two water spaces at once: the Vistula (Kaliningrad) Bay and the main part of the Baltic Sea. And you can walk from one coast to another in just a few minutes. In addition, it is in these places that the sun shines brightest on the entire Polish Baltic coast. And the most unforgettable impression is made by the wide sandy beach, which has repeatedly received the Blue Flag certificate.",
            'https://polomedia.ru/sites/default/files/news/05-14/plaza3.jpg'],
        'Sopot': [
            "Sopot beaches have both admirers and opponents. However, the fact that this is a resort with a truly European atmosphere is indisputable. And soft sand is just one of those details that impress tourists. It is here that the stars of the Gdynia Opener Festival rest - the fun these days does not stop until the morning. The longest wooden pier in Europe attracts tourists. And to this we should add stylish architecture, excellent restaurants and the proximity of the sights of Gdansk.",
            'https://polomedia.ru/sites/default/files/news/05-14/plaza4.jpg']}
    mountains = {'Świętokrzyskie mountains': [
        "The Świętokrzyskie Mountains (Góry Świętokrzyskie) is a low mountain range in south-central Poland. The highest point is Mount Lysitsa (614 meters above sea level). Despite their modest size, these mountains are popular with tourists. There are two main reasons for this.\n"
        "First, the Świętokrzyskie Mountains are the oldest in Poland. They formed 500 million years ago! Looking at such antiquity, you begin to perceive everything completely differently ... Secondly, in the Swietokrzyski National Park you can admire stunning views. For example, amazing rocky slopes hidden between dense forests, or beautiful spacious valleys (the width of the Vilkovskaya Valley reaches four kilometers).",
        'https://api.culture.pl/sites/default/files/styles/1920_auto/public/2019-07/goloborze_en.jpg?itok=iBCQnZAq'],
        'Tatras': [
            "The Tatras are the highest mountain range in Poland. It is located in the very south of the country, on the border with Slovakia. The highest point in the Polish Tatras is Mount Rysy (2499 meters above sea level), although there are higher peaks in Slovakia. The Tatras are the only high mountain range in Poland, which is why they are very popular among tourists.\n "
            "Giewont without a cross and other unusual pictures of the Tatras a hundred years ago\n"
            "We will not find such a mountain world frozen in the frame before the tourist era either in hundreds of albums available on the market, or in guidebooks around Zakopane and the surrounding area.",
            'https://api.culture.pl/sites/default/files/styles/1920_auto/public/2019-07/morskie_oko_en.jpg?itok=ccIU-EIZ'],
        'Peniny': [
            "The Pieniny mountain range is located an hour northeast of the Tatras. The highest point is Three Crowns (Trzy Korony), 982 meters above sea level.\n"
            "Pieniny is most often associated with rafting on the Dunajec River, winding through the mountain gorge. For eight kilometers you can admire the picturesque views of the rocky cliffs. The Peniny are also famous for their pine trees growing on the steep mountain slopes. The most famous of them is the pine tree on Mount Sokolitsa",
            'https://api.culture.pl/sites/default/files/styles/1920_auto/public/2019-07/sosna_na_skolicy_w_pieninach_en.jpg?itok=bnAE2HK2']}
    skiResorts = {'Zakopane': [
        "The most famous and prestigious ski resort in Poland is Zakopane. Thanks to a very developed infrastructure, it gained great popularity, which ensured its fame as the “winter capital” of the country. It is located in a picturesque basin at the foot of the Tatras, 116 km from Krakow. On the territory of the resort there are 6 main ski areas in the altitude range of 860-2000 m, which are assigned different levels of difficulty. This opens up almost unlimited possibilities for skiing and luge. The lifts work from morning until late at night for quite a long time. The ski season starts here in early December and lasts almost until mid-April. In total, there are more than 60 lifts in Zakopane and its environs, and the total length of the slopes exceeds 65 km.",
        'https://shoppingpl.com/uploads/images/Vidpochynok%20v%20Polshi/Narty%20w%20Polsce/Narty%20w%20Zakopanem.jpg'],
        'Kasprowy-Verkh': [
            "Among skiers, the most popular place in the Zakopane region is the Kasprowy Wierch base on the mountain of the same name in the Tatra National Park, which is located almost on the Polish-Slovak border about 10 km south of the famous town. Sometimes it is also called the 'sacred mountain of Polish skiing'. Height - 1987 meters above sea level. Many believe that more than one generation of skiers grew up on this mountain. And this is not surprising. The infrastructure is constantly being developed here and the service for ski lovers is being improved. One of the features of this mountain is the presence of only natural snow cover, which forces skiers to take into account the vagaries of the weather. However, the pleasure of skiing on moderately compacted and moderately loose snow can only be appreciated by real skiers.",
            'https://shoppingpl.com/uploads/images/Vidpochynok%20v%20Polshi/Narty%20w%20Polsce/Narty%20w%20Kasprowy-Wierch.jpg'],
        'Skiing extravaganza in Bialka Tatrzanska': [
            "Every year, the popularity of the Białka Tatrzańska ski resort in the Lesser Poland Voivodeship is growing at an incredible pace. From Krakow, it is better to get to it along the Zakopianka highway - in good weather, you will quickly overcome less than a hundred kilometers. If you depart from Zakopane, then this resort can be reached in half an hour by car.",
            'https://shoppingpl.com/uploads/images/Vidpochynok%20v%20Polshi/Narty%20w%20Polsce/Narty%20w%20Bialka%20Tatrzanska.jpg']}
    lakes = {'Elk': [
        "Lake Elk, formed by the melting of a glacier and surrounded by dense forest, is a secret that Poles would rather not share with anyone. The reservoir is located in the Masurian Lake District region and is transformed with the advent of each season. In the summer, outdoor enthusiasts flock to the town of Elk, famous for its terracotta-roofed houses, and flock to the grassy shores of the lake to watch kayaks surrounded by emerald pines. When autumn arrives, a light fog appears over Lake Elk, water lilies bloom in the water, and the foliage on the trees turns a warm dark brown color.",
        'https://bstatic.com/data/xphoto/1182x887/540/54070855.jpg?size=S'],
        'Lake Chos': [
            "Lake Chos, located in the heart of the Masurian Lake District, is the largest of the three lakes that surround the town of Mrągowo. In the summer, vacationers lazily sunbathe on the boardwalks along the banks. Due to the large water surface area, sailing is also popular. Arriving at the lake in winter, you will get a completely different, but no less amazing experience. In the cold season, snow-covered trees lean over lonely reeds, reflecting the modest elegance of winter.",
            'https://bstatic.com/data/xphoto/1182x887/540/54070840.jpg?size=S'],
        'Augustow lakes': [
            "The Augustow Lakes, surrounding the spa town of Augustow, are a constellation of sapphire pools. Lakes Necko, Rospuda and Saino, Beloe Augustovskoe Lake and Lake Studzenichno are just a few options to choose from, while the Augustow Canal is great for kayaking. It stretches across the entire Augustovskaya Pushcha to Belarus. The ancient trees in this forest provide a protective canopy, and the only sound you will hear is the splashing of water from your oars. Lovers of romantic views should head to the secluded Saino Lake and admire the sunrise.",
            'https://bstatic.com/data/xphoto/1182x887/540/54070836.jpg?size=S']}
    rivers = {'river_name1': ["dicsr", '_river'],
              'river_name2': ["discr", '_river'],
              'river_name3': ["discr", '_river']}

    # currency
    currencyName = 'PLN'
    currencyEqualsToDollar = 4.52

    # military
    milPolBlock = "NATO"
    amountOfPeopleInArmy = 125500

    # healthcare
    numberOfDoctorsPer100kPopulation = 227
    menAverageLifeExpectancy = 74  # years
    womenAverageLifeExpectancy = 82  # years

    # climat
    juneAverageTemperature = 21.9  # °C
    decemberAverageTemperature = 0  # °C
    averageHumidity = 71.25  # %
    averageDurationOfWinter = 3  # month
    averageRainfallPerMonth = 50  # mm (?)
    averageNumberOfFoggyDaysPerYear = 156  # days
    averageNumberOfRainyDaysPerYear = 136  # days
    averageNumberOfClearDays = 73  # days

    # security
    situationInTheCountry = 3  # [1, 3] 1-bad, 3-good
    freedomOfSpeech = 3  # [1, 3]
    assessmentOfFamilyLife = 2  # [1, 3]
    attitudeTowardsLGBT = 1  # [1, 3]

    # population
    populationCount = 37780000
    procentOfMales = 48.2
    procentOfFemales = 51.8
    populationDensityPerSquareKilometer = 121.2
    speedOfLife = 2  # [1, 3]
    workPlaces = 3  # [1, 3]
    nightLifeEntertainment = 2  # [1, 3]

    # citizenship
    citizenshipGlobalRank = 3
    friendlyToForeigners = 1

    # communication
    communicationOnEnglish = 3  # [1, 3]

    # transport
    averageTravelTimeToWork = 45
    developmentLevelOfPublicTransport = 3  # [1, 3]

    # internet
    speedOfInternetMbps = 85  # Мегабиты в секунду
    freeWifi = 2  # [1, 3]

    # education
    rankingOfNationalEducationSystem = 32

    cc.createBase(countryName, cities, officialLanguage,
                  # currency
                  currencyName, currencyEqualsToDollar,
                  # military
                  milPolBlock, amountOfPeopleInArmy,
                  # healthcare
                  numberOfDoctorsPer100kPopulation, menAverageLifeExpectancy, womenAverageLifeExpectancy,
                  # climat
                  juneAverageTemperature, decemberAverageTemperature, averageHumidity,
                  averageDurationOfWinter, averageRainfallPerMonth, averageNumberOfFoggyDaysPerYear,
                  averageNumberOfRainyDaysPerYear, averageNumberOfClearDays,
                  # security
                  situationInTheCountry, freedomOfSpeech,
                  assessmentOfFamilyLife, attitudeTowardsLGBT,
                  # population
                  populationCount, procentOfMales, procentOfFemales, populationDensityPerSquareKilometer,
                  speedOfLife, workPlaces, nightLifeEntertainment,
                  # citizenship
                  citizenshipGlobalRank,
                  # communication
                  communicationOnEnglish,
                  # transport
                  averageTravelTimeToWork, developmentLevelOfPublicTransport,
                  # internet
                  speedOfInternetMbps, freeWifi,
                  # education
                  rankingOfNationalEducationSystem, universities, faculties, programs, costs, links, images,
                  requirements,
                  hostel, scolarship, sights, beaches, mountains, skiResorts, lakes, rivers, friendlyToForeigners
                  )
    # cc.createManMadeDisaster(countryName, nameMMD, typeOfMMD, aomuntOfDeadPeople,
    #                           aomuntOfInjuredPeople, territoryOfPollution)
    # cc.createOceans()

    #############################   POLAND   #############################

    #############################   CZECH   ##############################

    # Country
    countryName = "Czech"
    officialLanguage = "Czech"

    # cities     name   isBig WashesBy
    cities = {'Prague': [True, True, None], 'Brno': [True, True, None], 'Pilsen': [True, True, None],
              'Ostrava': [True, True, None], 'Olomouc': [True, True, None]}

    # education
    universities = {'Prague': ['Czech Technical University in Prague', 'Prague City University'],
                    'Brno': ['Brno University of Technology', 'Masaryk University'],
                    'Pilsen': ['University of West Bohemia', 'Charles University'],
                    'Ostrava': ['University of Ostrava', 'Ostrava University of Technology'],
                    'Olomouc': ['Palacký University Olomouc', 'Moravian University Olomouc']}

    faculties = {
        'Czech Technical University in Prague': ['Faculty of Architecture', 'Faculty of Medicine',
                                                 'Faculty of Engineering',
                                                 'Faculty of Computer Engineering and Software'],
        'Prague City University': ['Faculty of Arts', 'Faculty of Economics',
                                   'Faculty of Computer Engineering and Software'],
        'Brno University of Technology': ['Faculty of Architecture', 'Faculty of Computer Engineering and Software',
                                          'Faculty of Economics',
                                          'Faculty of Engineering',
                                          'Faculty of Computer Engineering and Software',
                                          'Faculty of Arts'],
        'Masaryk University': ['Faculty of Law', 'Faculty of Medicine', 'Faculty of Science', 'Faculty of Arts',
                               'Faculty of Economics', 'Faculty of Computer Engineering and Software'],
        'University of West Bohemia': ['Faculty of Science', 'Faculty of Arts', 'Faculty of Economics',
                                       'Faculty of Engineering', 'Faculty of Law'],
        'Charles University': ['Faculty of Law', 'Faculty of Medicine', 'Faculty of Arts',
                               'Faculty of Science', 'Faculty of Social Sciences'],
        'University of Ostrava': ['Faculty of Science', 'Faculty of Arts', 'Faculty of Social Sciences',
                                  'Faculty of Medicine'],
        'Ostrava University of Technology': ['Faculty of Economics',
                                             'Faculty of Engineering', 'Faculty of Computer Engineering and Software'],
        'Palacký University Olomouc': ['Faculty of Medicine', 'Faculty of Arts', 'Faculty of Science',
                                       'Faculty of Education', 'Faculty of Law'],
        'Moravian University Olomouc': ['Faculty of Economics', 'Faculty of Social Sciences']}

    programs = {'Czech Technical University in Prague': ['Magistracy', 'Undergraduate'],
                'Prague City University': ['Magistracy', 'Undergraduate', 'MBA'],
                'Brno University of Technology': ['Magistracy', 'Undergraduate'],
                'Masaryk University': ['Foundation', 'Undergraduate', 'MBA'],
                'University of West Bohemia': ['Magistracy', 'Undergraduate'],
                'Charles University': ['Magistracy', 'Undergraduate', 'MBA'],
                'University of Ostrava': ['Magistracy', 'Undergraduate'],
                'Ostrava University of Technology': ['Magistracy', 'Undergraduate'],
                'Palacký University Olomouc': ['Magistracy', 'Undergraduate', 'MBA'],
                'Moravian University Olomouc': ['Magistracy', 'Undergraduate']}
    links = {'Czech Technical University in Prague': 'https://www.cvut.cz/en',
             'Prague City University': 'https://www.praguecityuniversity.cz/',
             'Brno University of Technology': 'https://www.vut.cz/en/',
             'Masaryk University': 'https://www.muni.cz/en',
             'University of West Bohemia': 'https://www.zcu.cz/en/index.html',
             'Charles University': 'https://cuni.cz/uken-1.html',
             'University of Ostrava': 'https://www.osu.eu/',
             'Ostrava University of Technology': 'https://www.vsb.cz/en',
             'Palacký University Olomouc': 'https://www.upol.cz/en/',
             'Moravian University Olomouc': 'https://www.mvso.cz/en'}

    images = {
        'Czech Technical University in Prague': 'https://keystoneacademic-res.cloudinary.com/image/upload/q_auto,f_auto,w_743,c_limit/element/13/136733_32cf6ae7-460a-4c2a-8f89-93860bb45f99.jpg',
        'Prague City University': 'https://upload.wikimedia.org/wikipedia/commons/7/7e/Prague_College%2C_Polska_10%2C_Prague_2%2C_Czechia.JPG',
        'Brno University of Technology': 'https://i.ytimg.com/vi/4bqqlkmjv-M/maxresdefault.jpg',
        'Masaryk University': 'https://www.em.muni.cz/cache-thumbs/kampus2-790x395-544916530.jpg',
        'University of West Bohemia': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/57/ZCU-FAV-FST-UUD1.jpg/1200px-ZCU-FAV-FST-UUD1.jpg',
        'Charles University': 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b1/Praha%2C_Star%C3%A9_M%C4%9Bsto%2C_N%C3%A1m%C4%9Bst%C3%AD_Jana_Palacha%2C_FF_UK_01.jpg/1200px-Praha%2C_Star%C3%A9_M%C4%9Bsto%2C_N%C3%A1m%C4%9Bst%C3%AD_Jana_Palacha%2C_FF_UK_01.jpg',
        'University of Ostrava': 'https://upload.wikimedia.org/wikipedia/commons/a/a2/Ostrava_dekanat_PrF_OU_20080426.jpg',
        'Ostrava University of Technology': 'https://www.timeshighereducation.com/sites/default/files/styles/article785xauto/public/image_2_2.jpg?itok=oVZR1sIr',
        'Palacký University Olomouc': 'https://msmstudy.eu/wp-content/uploads/2021/06/Sloj-15-5.jpg',
        'Moravian University Olomouc': 'https://image.free-apply.com/gallery/l/uni/gallery/lg/1020300050/e6c40d2985f1dbe6bd3b18ad42db6eac34b2cf5c.jpg?s=640'}
    # общага
    hostel = {'Czech Technical University in Prague': 'Yes',
              'Prague City University': 'Yes',
              'Brno University of Technology': 'Yes',
              'Masaryk University': 'Yes',
              'University of West Bohemia': 'Yes',
              'Charles University': 'No',
              'University of Ostrava': 'No',
              'Ostrava University of Technology': 'No',
              'Palacký University Olomouc': 'Yes',
              'Moravian University Olomouc': 'No'}
    # стипендия
    scolarship = {'Czech Technical University in Prague': 'Yes',
                  'Prague City University': 'Yes',
                  'Brno University of Technology': 'Yes',
                  'Masaryk University': 'Yes',
                  'University of West Bohemia': 'Yes',
                  'Charles University': 'Yes',
                  'University of Ostrava': 'Yes',
                  'Ostrava University of Technology': 'Yes',
                  'Palacký University Olomouc': 'Yes',
                  'Moravian University Olomouc': 'Yes'
                  }
    # требования к поступлению
    requirements = {
        'Czech Technical University in Prague': 'A certificate of successful graduation from a secondary school.'
                                                'A duly completed and submitted application for a study programme.'
                                                'Documentary evidence that fees and charges have been paid.'
                                                'Compliance with the requirements for the entrance procedures.',
        'Prague City University': 'Confirmation of English level upon entry. Letter of motivation. Portfolio (only School of Art & Design & Creative Media Production). Final interview.',
        'Brno University of Technology': 'Curriculum vitae. '
                                         'Statement of purpose '
                                         'Recommendation letter (if required) '
                                         'English language qualifications TOEFL (if required) ',
        'Masaryk University': 'diploma or statement of expected graduation. '
                              'diploma supplement/Transcript of records. '
                              'CV. '
                              'proof of English language level. '
                              'motivation letter. '
                              'own academic work/publication (e.g. bachelor, diploma thesis) '
                              'copy of passport.',
        'University of West Bohemia': 'Curriculum vitae. '
                                      'Statement of purpose '
                                      'Recommendation letter (if required) '
                                      'English language qualifications TOEFL (if required) ',
        'Charles University': 'Curriculum vitae. '
                              'Statement of purpose '
                              'Recommendation letter (if required) '
                              'English language qualifications TOEFL (if required) ',
        'University of Ostrava': 'Senior School Certificates. '
                                 'Official Transcripts. '
                                 'English Language Proficiency Scores. '
                                 'Norwegian Language Proficiency Scores. '
                                 'CV/Resume. '
                                 'Letter of Recommendations. '
                                 'Personal Statement. ',
        'Ostrava University of Technology': 'A certificate of successful graduation from a secondary school.'
                                            'A duly completed and submitted application for a study programme.'
                                            'Documentary evidence that fees and charges have been paid.'
                                            'Compliance with the requirements for the entrance procedures.',
        'Palacký University Olomouc': 'diploma or statement of expected graduation. '
                                      'diploma supplement/Transcript of records. '
                                      'CV. '
                                      'proof of English language level. '
                                      'motivation letter. '
                                      'own academic work/publication (e.g. bachelor, diploma thesis) '
                                      'copy of passport.',
        'Moravian University Olomouc': 'Student visa. '
                                       'Online Application form. '
                                       'TOEFL Certificate. '
                                       'World Education Services evaluation. '
                                       'Passport. '
                                       'Photographs. '
                                       'IELTS Certificate. '
                                       'Proof of fee payment. '
                                       'Health and Life Insurance'}

    costs = {'Czech Technical University in Prague': 4700,
             'Prague City University': 4500,
             'Brno University of Technology': 4900,
             'Masaryk University': 3900,
             'University of West Bohemia': 3700,
             'Charles University': 3750,
             'University of Ostrava': 4100,
             'Ostrava University of Technology': 4500,
             'Palacký University Olomouc': 3400,
             'Moravian University Olomouc': 3550}

    # resort
    sights = {'Prague Castle': [
        "One of the most important sights of the Czech Republic, which has literally become a symbol of the state, is the largest castle in Prague Castle, located in Prague. It is a whole complex of buildings, temples and fortifications surrounding the main squares and courtyards of the city. This is a whole district of the city, quite large in area, which performs a cultural, historical and political role. Previously, the castle served as the residence of Czech kings and emperors, today it plays the role of a representative office of the country's president. The residence is guarded by a large military unit, consisting of six hundred Guardians of the City. Every hour there is a changing of the guard, and at noon this action is even accompanied by a special orchestra. Guests of the city specially come to the walls of the complex in order to watch this solemn ceremony.",
        'https://www.tripzaza.com/ru/destinations/wp-content/uploads/2017/04/Czech-1-Prague-Castle-e1491202258920.jpg'],
        'The Charles Bridge': [
            "Speaking about what to visit in the Czech Republic in the first place, special attention should be paid to the Charles Bridge, which has become a real hallmark of the country in our time. By the way, there are 18 bridges in the capital of the Czech Republic, fraught with a rich history, but undoubtedly the Charles Bridge is the oldest and most beautiful among them. In addition to its immediate function - connecting the opposite banks of the Vltava River, this bridge has occupied an important place in the history of the city. The bridge was conceived by the Czech king Charles IV, opened in 1402, since then it has undergone some changes - a horse-drawn road passed through it, trams ran for a long time, but now the bridge has become pedestrian again, which attracts many tourists and is a favorite place for walking .",
            'https://www.tripzaza.com/ru/destinations/wp-content/uploads/2017/04/Czech-2-The-Charles-Bridge-e1491202450286.jpg'],
        'Wenceslas Square': [
            "While traveling around Prague, you don't have to think about what to see in the Czech Republic - sooner or later, by accident or on purpose, you will still find yourself in the very heart of the city - on Wenceslas Square. Here, even in the middle of the night, hundreds of people are walking and hurrying somewhere, luring countless shops and restaurants with their signs.",
            'https://www.tripzaza.com/ru/destinations/wp-content/uploads/2017/04/Czech-3-Wenceslas-Square--e1491202625918.jpg']}
    beaches = {}
    mountains = {'Jizera mountains': [
        "Located 120 km from Prague (Liberec Region). The northernmost mountain range, adjacent to the Krkonoše mountains. The name of the mountains comes from the local river. The largest peaks in the Czech Republic are Jizere and Smrk. Dozens of streams and streams that flow down from the mountains give special beauty.",
        'https://chezgid.ru/wp-content/uploads/2019/07/Jizerskie-gory.png'],
        'Giant Mountains': [
            "The mountain is located 160 km from the Czech capital. The highest point is 1601 m (Mount Snezhka). The ski season starts on December 1 and lasts until the end of April. The total length of the mountain range is 454 km. It is considered one of the most popular and unique mountain ranges in the country. At the foot of the mountain there is a ski resort - Pec pod Snezhkou, where there are slopes for both professionals and beginners. In winter, you can do both ski slopes and pedestrian crossings. In summer, the ideal option is to take a walk, enjoy the local scenic beauties and sights. There are special routes for conquering peaks.",
            'https://chezgid.ru/wp-content/uploads/2019/07/Krkonoshe.jpg'],
        'Eagle Mountains': [
            "Settled on the border. The highest point - Velka Deshtna - 1115 m. The area is ideal for active holidaymakers, those who love hiking and winter activities. In the circle you can visit castles and fortresses, a dam with a reservoir. There are 5 ski slopes for tourists with different levels of training and routes for hiking and cycling. You can visit the school of skiers and snowboarders, order an animation program. You can really get real relaxation on a summer vacation in the mountains.",
            'https://chezgid.ru/wp-content/uploads/2019/07/Orlitskie-gory.jpg']}
    skiResorts = {'Spindlerov Mlyn': [
        "One of the most famous resorts in the Czech Republic, located at an altitude of up to 1300 meters above sea level. It is located on the territory of the Krkonoše Nature Park. Spindlerov Mlyn became known as a resort in the 19th century. Today, sports competitions are constantly held here, and most tourists come from Russia, Poland, Holland and Germany. For snowboarders, there are ramps and a springboard. About 100 kilometers of trails for cross-country skiers have been laid in the forest. There are also ski schools, equipment rentals and cafes where you can have a cheap meal on St. Peter. Skiers are transported by a free bus that runs between St. Peter and Medvedin.",
        'https://www.krkonose.eu/sites/default/files/headers/krkonose-spindleruv-mlyn-10.jpg'],
        'Giant Mountains': [
            "This ski resort is located in the northeast of the country, almost on the border with Poland. The highest peak is called Śnieżka, its height is 1602 m. The Krkonoš Mountains Natural Mountain Park is located on the territory of the resort. In winter, it is usually very crowded here, but the snow here lasts from November to April, so there is plenty of time for everyone to ride. There are 16 ski slopes on the Krkonoše, as well as ski lifts and three cable cars. The length of the trails is about 4 km.",
            'https://pragagid.ru/wp-content/uploads/2012/11/k.jpg'],
        'Yested': [
            "Mount Jested, 1012 m high, is known as an excellent place for cycling and skiing. There are three ski jumps, training and sports tracks (5 of them are of increased difficulty). The necessary amount of snow is maintained with the help of 'snow cannons', some trails are suitable for evening skiing due to lighting. There are lifts on the territory of the resort, which can transport up to 4 thousand people per hour.",
            'https://www.vinegret.cz/wp-content/uploads/2014/04/%D0%BF%D0%B0%D0%BA%D1%83%D1%80%D1%86%D0%BD.jpg/640/1280']}
    lakes = {'Lhota': [
        "Lake Lhota is located just 40 kilometers from Prague. This is a very clean and beautiful reservoir, which arose by flooding a former quarry. The beach here is sandy, like the bottom of the lake; mighty pine trees grow along the shore, thanks to which the tart aroma of coniferous trees hovers here in summer. Entrance to the territory near the lake is paid - a ticket for the day costs 50 kroons. You can settle down anywhere near the lake, although one of the beaches is given over to nudist. There are always a lot of people here in the summer, but the lake is large and the whole crowd, dispersing along the beach, interferes little with each other.",
        'http://rupoint.cz/wp-content/uploads/2015/07/lhota-e1438346532698.jpg'],
        'Konětopy': [
            "The twin brother of Lake Lhota is located about a 15-minute drive from it and the same 40 kilometers from Prague. This is also a former flooded quarry. Konětopy differs only in that there is no pine forest here and no trees grow on the sandy beach. The water is just as clean and clear. Entrance ticket for the whole day - 50 kroons. The beach is also open until 21:00. It is forbidden to pitch tents on the territory.",
            'http://rupoint.cz/wp-content/uploads/2015/07/9421823549_1f973e0894_z-e1438346378197.jpg'],
        'Mahovo': [
            "The legendary Makhovo Lake is one of the busiest summer spots in the Czech Republic. In hot weather, young people, families with children and cheerful companies from all over the country flock here. Summer music festivals often take place here, the largest of which is Finlandia Macháč.",
            'http://rupoint.cz/wp-content/uploads/2015/07/m-chovo-jezero-e1438346123178.jpg']}
    rivers = {'Vltava': [
        "The Vltava is the largest river in the Czech Republic, its length is about 430 km, the basin area is slightly more than 28,000 km2. It flows through almost the entire territory of the country, originating on the Black Mountain in the Sumava National Park, just six hundred meters from the German border, and flowing into the Laba, or Elbe in German, in the northern part of the country near the town of Melnik.",
        'https://praga-praha.ru/pix/2014/01/%D0%92%D0%BB%D1%82%D0%B0%D0%B2%D0%B0-4_1000400.webp'],
        'Odra': [
            "The Odra River, or as it is also called the Oder, with a total length of 854 km, originates in the Eastern Sudetenland, flows through Poland, forming most of the Polish-German border, and flows into the Baltic Sea.",
            'https://praga-praha.ru/wp-content/uploads/2019/03/%D0%A0%D0%B5%D0%BA%D0%B0-%D0%9E%D0%B4%D1%80%D0%B0-3-800x598.jpg'],
        'Labe': [
            "The second longest river in the Czech Republic, the Laba, flows through the northwest of the country for 370.74. The middle and lower reaches are in Germany. Laba flows into the North Sea at a distance of 1165 km from the source.",
            'https://praga-praha.ru/pix/2019/01/%D0%A0%D0%B5%D0%BA%D0%B0-%D0%9B%D0%B0%D0%B1%D0%B0-4_740300.webp']}

    # currency
    currencyName = 'CZK'
    currencyEqualsToDollar = 23.39

    # military
    milPolBlock = "NATO"
    amountOfPeopleInArmy = 24900

    # healthcare
    numberOfDoctorsPer100kPopulation = 369
    menAverageLifeExpectancy = 73.9  # years
    womenAverageLifeExpectancy = 80.7  # years

    # climat
    juneAverageTemperature = 18  # °C
    decemberAverageTemperature = 0  # °C
    averageHumidity = 77  # %
    averageDurationOfWinter = 4  # month
    averageRainfallPerMonth = 43.75  # mm (?)
    averageNumberOfFoggyDaysPerYear = 157  # days
    averageNumberOfRainyDaysPerYear = 135  # days
    averageNumberOfClearDays = 73  # days

    # security
    situationInTheCountry = 3  # [1, 3] 1-bad, 3-good
    freedomOfSpeech = 3  # [1, 3]
    assessmentOfFamilyLife = 3  # [1, 3]
    attitudeTowardsLGBT = 2  # [1, 3]

    # population
    populationCount = 10700000
    procentOfMales = 49.1
    procentOfFemales = 50.9
    populationDensityPerSquareKilometer = 135.8
    speedOfLife = 2  # [1, 3]
    workPlaces = 3  # [1, 3]
    nightLifeEntertainment = 3  # [1, 3]

    # citizenship
    citizenshipGlobalRank = 4
    friendlyToForeigners = 2

    # communication
    communicationOnEnglish = 2  # [1, 3]

    # transport
    averageTravelTimeToWork = 20
    developmentLevelOfPublicTransport = 3  # [1, 3]

    # internet
    speedOfInternetMbps = 65  # Мегабиты в секунду
    freeWifi = 2  # [1, 3]

    # education
    rankingOfNationalEducationSystem = 29

    cc.createBase(countryName, cities, officialLanguage,
                  # currency
                  currencyName, currencyEqualsToDollar,
                  # military
                  milPolBlock, amountOfPeopleInArmy,
                  # healthcare
                  numberOfDoctorsPer100kPopulation, menAverageLifeExpectancy, womenAverageLifeExpectancy,
                  # climat
                  juneAverageTemperature, decemberAverageTemperature, averageHumidity,
                  averageDurationOfWinter, averageRainfallPerMonth, averageNumberOfFoggyDaysPerYear,
                  averageNumberOfRainyDaysPerYear, averageNumberOfClearDays,
                  # security
                  situationInTheCountry, freedomOfSpeech,
                  assessmentOfFamilyLife, attitudeTowardsLGBT,
                  # population
                  populationCount, procentOfMales, procentOfFemales, populationDensityPerSquareKilometer,
                  speedOfLife, workPlaces, nightLifeEntertainment,
                  # citizenship
                  citizenshipGlobalRank,
                  # communication
                  communicationOnEnglish,
                  # transport
                  averageTravelTimeToWork, developmentLevelOfPublicTransport,
                  # internet
                  speedOfInternetMbps, freeWifi,
                  # education
                  rankingOfNationalEducationSystem, universities, faculties, programs, costs, links, images,
                  requirements,
                  hostel, scolarship, sights, beaches, mountains, skiResorts, lakes, rivers, friendlyToForeigners
                  )
    # cc.createManMadeDisaster(countryName, nameMMD, typeOfMMD, aomuntOfDeadPeople,
    #                           aomuntOfInjuredPeople, territoryOfPollution)
    # cc.createOceans()

    #############################   CZECH   #############################

    #############################   GERMANY   #############################

    # Country
    countryName = "Germany"
    officialLanguage = "Deutsch"

    # cities     name   isBig WashesBy
    cities = {'Berlin': [True, True, None], 'Hamburg': [True, True, None], 'Bremen': [True, True, None],
              'Dresden': [True, True, None], 'Nuremberg': [True, True, None]}

    # education
    universities = {'Berlin': ['Humboldt University of Berlin', 'Technical University of Berlin'],
                    'Hamburg': ['University of Hamburg', 'HafenCity University Hamburg'],
                    'Bremen': ['University of Bremen', 'Jacobs University Bremen'],
                    'Dresden': ['Dresden University of Technology', 'Dresden University of Applied Sciences'],
                    'Nuremberg': ['Nuremberg Institute of Technology', 'Academy of Fine Arts']}
    faculties = {'Humboldt University of Berlin': ['Faculty of Law', 'Faculty of Science', 'Faculty of Arts',
                                                   'Faculty of Economics', 'Faculty of Education'],
                 'Technical University of Berlin': ['Faculty of Education',
                                                    'Faculty of Science',
                                                    'Faculty of Computer Engineering and Software',
                                                    'Faculty of Economics'],
                 'University of Hamburg': ['Faculty of Law', 'Faculty of Economics',
                                           'Faculty of Social Sciences', 'Faculty of Medicine', 'Faculty of Education',
                                           'Faculty of Science'],
                 'HafenCity University Hamburg': ['Faculty of Architecture', 'Faculty of Engineering',
                                                  'Faculty of Science'],
                 'University of Bremen': ['Faculty of Science',
                                          'Faculty of Computer Engineering and Software', 'Faculty of Law',
                                          'Faculty of Social Sciences'],
                 'Jacobs University Bremen': ['Faculty of Computer Engineering and Software', 'Faculty of Science',
                                              'Faculty of Economics', 'Faculty of Social Sciences'],
                 'Dresden University of Technology': ['Faculty of Science',
                                                      'Faculty of Social Sciences',
                                                      'Faculty of Education',
                                                      'Faculty of Arts', 'Faculty of Computer Engineering and Software',
                                                      'Faculty of Engineering'],
                 'Dresden University of Applied Sciences': ['Faculty of Science', 'Faculty of Social Sciences'],
                 'Nuremberg Institute of Technology': ['Faculty of Science',
                                                       'Faculty of Architecture',
                                                       'Faculty of Arts',
                                                       'Faculty of Computer Engineering and Software',
                                                       'Faculty of Engineering'],
                 'Academy of Fine Arts': ['Faculty of Arts', 'Faculty of Social Sciences',
                                          'Faculty of Architecture', 'Faculty of Law']}

    programs = {'Humboldt University of Berlin': ['Magistracy', 'Undergraduate', 'MBA'],
                'Technical University of Berlin': ['Magistracy', 'Undergraduate'],
                'University of Hamburg': ['Magistracy', 'Undergraduate'],
                'HafenCity University Hamburg': ['Foundation', 'Undergraduate', 'MBA'],
                'University of Bremen': ['Magistracy', 'Undergraduate'],
                'Jacobs University Bremen': ['Magistracy', 'Undergraduate', 'MBA'],
                'Dresden University of Technology': ['Magistracy', 'Undergraduate'],
                'Dresden University of Applied Sciences': ['Magistracy', 'Undergraduate'],
                'Nuremberg Institute of Technology': ['Magistracy', 'Undergraduate', 'MBA'],
                'Academy of Fine Arts': ['Magistracy', 'Undergraduate']}
    links = {'Humboldt University of Berlin': 'https://www.hu-berlin.de/en',
             'Technical University of Berlin': 'https://www.tu.berlin/en/',
             'University of Hamburg': 'https://www.uni-hamburg.de/en.html',
             'HafenCity University Hamburg': 'https://www.hcu-hamburg.de/',
             'University of Bremen': 'https://www.uni-bremen.de/',
             'Jacobs University Bremen': 'https://www.jacobs-university.de/',
             'Dresden University of Technology': 'https://tu-dresden.de/?set_language=en',
             'Dresden University of Applied Sciences': 'https://www.htw-dresden.de/',
             'Nuremberg Institute of Technology': 'https://www.th-nuernberg.eu/',
             'Academy of Fine Arts': 'https://www.academyoffinearts.in/'}

    images = {
        'Humboldt University of Berlin': 'https://www.ru.studies-in-europe.eu/img/uczelnie/a1673/g/Berlin-Universitat-zwischen-1890-und-1900-p2961.jpg',
        'Technical University of Berlin': 'https://www.easyuni.my/media/institution/photo/2016/07/16/Technical-University-of-Berlin.jpg.600x400_q85.jpg',
        'University of Hamburg': 'https://assets.rrz.uni-hamburg.de/instance_assets/uni/12806281/esa1-schell-screen-733x414-e6d55adb6924963e9d96a322f0a0e4be712b5b1c.jpg',
        'HafenCity University Hamburg': 'https://study-eu.s3.amazonaws.com/uploads/image/path/127/wide_fullhd_hcu-hamburg.jpg',
        'University of Bremen': 'https://welcometobremen.de/wp-content/uploads/2016/09/uni-mensa-von-oben-scaled.jpg',
        'Jacobs University Bremen': 'https://upload.wikimedia.org/wikipedia/commons/5/5b/Jacobs_University_Bremen_Campus.JPG',
        'Dresden University of Technology': 'https://upload.wikimedia.org/wikipedia/commons/7/7d/TU-Dresden-Georg-Schumann-Bau.jpg',
        'Dresden University of Applied Sciences': 'https://www.uni-assist.de/fileadmin/_processed_/f/c/csm_htw-dresden_Peter_Sebb_a636786b53.jpg',
        'Nuremberg Institute of Technology': 'https://lh3.googleusercontent.com/p/AF1QipOxSsHPztWk5UMayvik0qPfKxPRPTz_G1ZsHAYs=s680-w680-h510',
        'Academy of Fine Arts': 'https://upload.wikimedia.org/wikipedia/commons/5/5a/Dresden_Germany_City-views-from-tower-of-Frauenkirche-01.jpg'}
    # общага
    hostel = {'Humboldt University of Berlin': 'Yes',
              'Technical University of Berlin': 'Yes',
              'University of Hamburg': 'Yes',
              'HafenCity University Hamburg': 'Yes',
              'University of Bremen': 'Yes',
              'Jacobs University Bremen': 'No',
              'Dresden University of Technology': 'No',
              'Dresden University of Applied Sciences': 'No',
              'Nuremberg Institute of Technology': 'Yes',
              'Academy of Fine Arts': 'Yes'}
    # стипендия
    scolarship = {'Humboldt University of Berlin': 'Yes',
                  'Technical University of Berlin': 'Yes',
                  'University of Hamburg': 'Yes',
                  'HafenCity University Hamburg': 'Yes',
                  'University of Bremen': 'Yes',
                  'Jacobs University Bremen': 'Yes',
                  'Dresden University of Technology': 'Yes',
                  'Dresden University of Applied Sciences': 'Yes',
                  'Nuremberg Institute of Technology': 'Yes',
                  'Academy of Fine Arts': 'Yes'
                  }
    # требования к поступлению
    requirements = {'Humboldt University of Berlin': 'Academic records and transcripts.'
                                                     'Language Proficiency Proof.'
                                                     'A CV (from the commencement of education at school-level)'
                                                     'Fee Receipt produced by Uni-Assist.'
                                                     'Photocopy of Passport or an Identification Card ( Applicable only to EU Students)',
                    'Technical University of Berlin': 'Admission Requirement: To secure admission in TU berlin, Applicants are required to have a bachelors degree in a relevant field. Additionally, international students also have to demonstrate proficiency in English or German language depending upon the language of instruction of the program.',
                    'University of Hamburg': 'Higher education entrance eligibility- German Abitur. '
                                             'Academic transcripts. '
                                             'School leaving certificate. '
                                             'English language proficiency proof. '
                                             'German language proficiency proof. ',
                    'HafenCity University Hamburg': 'Language Proficiency Proof.'
                                                    'A CV (from the commencement of education at school-level)'
                                                    'Fee Receipt produced by Uni-Assist.'
                                                    'Photocopy of Passport or an Identification Card ( Applicable only to EU Students)',
                    'University of Bremen': 'Certificate of Bachelor degree or official academic transcript of Study Records of your Bachelor studies. '
                                            'Detailed and current curriculum vitae (CV), written in English. '
                                            'Letter of Motivation, explaining your interest for enrollment in the Master of Ecology program, written in English. ',
                    'Jacobs University Bremen': 'Academic transcripts. '
                                                'School leaving certificate. '
                                                'English language proficiency proof. '
                                                'German language proficiency proof.',
                    'Dresden University of Technology': 'Valid passport.'
                                                        'Two-recent Passport size photo.'
                                                        'University entrance qualification recognized by Germany (A-Levels or equivalent)'
                                                        'Proof of previous academic performance.'
                                                        'Proof of financial resources (8,700 EUR per year)'
                                                        'Letter of admission from the TU Dresden.',
                    'Dresden University of Applied Sciences': 'Valid passport.'
                                                              'Two-recent Passport size photo.'
                                                              'University entrance qualification recognized by Germany (A-Levels or equivalent)'
                                                              'Proof of previous academic performance.',
                    'Nuremberg Institute of Technology': 'Certificate of Bachelor degree or official academic transcript of Study Records of your Bachelor studies. '
                                                         'Detailed and current curriculum vitae (CV), written in English.',
                    'Academy of Fine Arts': 'Basic admissions materials. Application form or online application. '
                                            'Statement of Intent. One page essay explaining personal goals for graduate school or essay related to a topic as required by the Department. '
                                            'Resume. '
                                            'Portfolio/Demo Reel. '
                                            'Additional Materials. '
                                            'Complete Your Application. '
                    }

    costs = {'Humboldt University of Berlin': 3100,
             'Technical University of Berlin': 3500,
             'University of Hamburg': 2900,
             'HafenCity University Hamburg': 3200,
             'University of Bremen': 3150,
             'Jacobs University Bremen': 2750,
             'Dresden University of Technology': 3300,
             'Dresden University of Applied Sciences': 3150,
             'Nuremberg Institute of Technology': 3600,
             'Academy of Fine Arts': 2500}

    sights = {'Cologne Cathedral': [
        "At the highest point of the Cathedral Hill in Cologne is a true masterpiece of Gothic architecture - Cologne Cathedral. It is officially referred to as the Cathedral of Saints Peter and Mary. The mere appearance of this cathedral causes genuine admiration. The architecture of the majestic building seems to be woven from a lace of stone towers, columns and pilasters, united in a single architectural composition. And the general shape of the building, when viewed from above, is made in the form of a Latin cross. The Cologne Cathedral became the most important landmark of Germany not only due to its appearance, but also due to its rich history.",
        'https://www.tripzaza.com/ru/destinations/wp-content/uploads/2017/04/Germany-1-Cologne-Cathedral-e1492727734625.jpg'],
        'Neuschwanstein Castle': [
            "At the first glance at the facade of Neuschwanstein Castle from afar, there is a stable association of this amazingly beautiful building with a toy. So implausible seems this beauty of neat ivory turrets topped with pointed emerald domes. An incredibly beautiful natural background in the form of alpine slopes immersed in the greenery of forests gives even more fabulousness.",
            'https://www.tripzaza.com/ru/destinations/wp-content/uploads/2017/04/Germany-2-Neuschwanstein-Castle-e1492727971928.jpg'],
        'Brandenburg Gate': [
            "If you are wondering which landmark of Germany is the true symbol of the country, and what should be seen in Germany first of all, then you should definitely see the Brandenburg Gate. This is a truly legendary building, impressive in its size, architecture and symbolizing the most important milestones in the history of the country. The gates represent an almost complete copy of the Propylaea arch on the Parthenon. Their total height is 26 meters, the structure has 6 pillars and 5 corridors, the main of which is intended for the passage of ceremonial corteges.",
            'https://www.tripzaza.com/ru/destinations/wp-content/uploads/2017/04/Germany-3-The-Brandenburg-Gate-e1492728193602.jpg']}
    beaches = {'Westerland': [
        "the largest seaside resort on the North Sea in the city of Westerland. On the map, this island is recognizable, because it has the shape of a dancing ballerina on pointe shoes, and she has become a symbol of the island. Thanks to the excellent organization of tourism in this area, the resort received the popular name 'Beverly Hills' in Germany. Evening promenades along the coast of the North Sea during sunset will leave an unforgettable experience of visiting this beach.",
        'https://1001beach.ru/img/posts/966/750/westerland_beach-1.webp?t=1580401960'],
        "Langeoog": [
            "this is an ecologically clean resort, because there are no private vehicles on its territory. Bicycles or horse-drawn taxis are used to move around the city. The exceptions are the fire department and ambulance, they have several cars at their disposal. The beach is also known for its frequent and high tides. This was the main reason for the beach to move several hundred meters to the east in 50 years.",
            'https://1001beach.ru/img/posts/967/750/langeoog_beach-1.webp?t=1580401967'],
        'Binz': [
            "Binz Beach is recognized as one of the most beautiful and cleanest beaches on the Baltic coast. The reputation of the resort has been impeccable for over 150 years. Every year, Binz Beach receives the international environmental symbol 'Blue Flag' - a sign of compliance with water quality and safety standards. Binz Beach is a combination of seaside architecture with incredible seascapes. The coastal zone is buried in the greenery of centuries-old oaks, chestnuts, elms and poplars. And the waters surrounding the island are national protected areas.",
            'https://1001beach.ru/img/posts/965/750/binz_beach-1.webp?t=1580401954']}
    mountains = {'bavarian alps': [
        "On the territory of the Bavarian Alps there are a lot of convenient hiking trails and various routes for tourists. The forests of the foothills are represented by deciduous and coniferous trees, and there are also many diverse berry bushes or herbal plants. These are not only beautiful places for a walk, but also luxurious places for organizing a spa holiday in order to improve people's health.",
        'https://сезоны-года.рф/sites/default/files/resize/images/okruzhayushhij_mir/Germany_gory_1-500x328.jpg'],
        'black forest': [
            "In addition to the Alps in Germany, there is also the Black Forest massif (translated as 'Black Forest'), which is slightly smaller in size and is characterized by rather dark-looking forests with a large number of pines and firs. It is located in the south-west of the state, and also has a huge number of useful mineral springs on its territory.",
            'https://сезоны-года.рф/sites/default/files/resize/images/okruzhayushhij_mir/Germany_gory_2-500x333.jpg'],
        'Brocken': [
            "In the center of the country there is a small massif that does not have large peaks and the maximum height of the mountains here is only 1141 (Broken Peak). In appearance, these mountain formations resemble the Urals.",
            'https://сезоны-года.рф/sites/default/files/resize/images/okruzhayushhij_mir/Germany_gory_3-500x346.jpg']}
    skiResorts = {'Oberstdorf-Kleinwalsertal': [
        "Both on the German side and on the Austrian side in Vorarlberg, winter sports enthusiasts will find a variety of ski slopes of all difficulty levels.",
        'https://www.kleinwalsertal.com/Fotos/Fotoshootings/Bastian%20Morell/Ski%20Alpin/image-thumb__1088991__hero-img/Ifen%20Panorama%20%40Bastian%20Morell%20%282%29.jpg'],
        'Winterberg': [
            "With 34 pistes with a total length of 27.5 km over seven mountains and modern ski lifts, the largest ski resort in the Sauerland and the Northwest region ranks third in Cozy Cabins offering a holiday of the highest standard.",
            'https://upload.wikimedia.org/wikipedia/commons/3/39/Skiliftkarussell_Winterberg.jpg'],
        'Hörnerdörfer': [
            "Allgäu's five ski resorts have joined forces to create a network of ski lifts, offering excellent conditions for the whole family Children and beginners love the wide and level slopes. Experienced winter sports enthusiasts prefer the pistes around Riedbergerhorn-Grasgeren, Bolsterlang, Balderschwang and Ofterschwang.",
            'https://www.hoernerdoerfer.de/images/ogcyo3oq2k0-/winterliches-fischen-im-allgaeu-winterurlaub-in-den-hoernerdoerfern.jpg']}
    lakes = {'Königssee': [
        "The third deepest German lake is located in Bavaria, surrounded by mountains and, like many local lakes, has a glacial origin. This is one of the cleanest reservoirs, they move along it only on ships with an electric motor, pedal drive or oars. Tourists are sure to be shown how the mountain echo sounds. Worthy of admiration is the Church of St. Bartholomew in the middle of the lake and the old hunting castle with an ice non-melting chapel.",
        'https://must-see.top/wp-content/uploads/2018/06/kenigsze-700x464.jpg'],
        'Müritz': [
            "The largest lake in Germany is located on the territory of the national reserve of the same name, where you can see endangered species of plants, birds and animals up close. To observe them, more than 600 km of paths for pedestrians and cyclists have been laid, and special towers have also been erected. In total, there are more than a hundred small lakes in the park. Boating or boat trips are no less educational than walking.",
            'https://must-see.top/wp-content/uploads/2018/06/myurits-700x466.jpg'],
        'lake constance': [
            "In Europe, this is the third largest lake, its waters wash the coasts of three countries. The coastline of Germany is the longest and is 173 km long. The Germans call it the Swabian Sea. For lovers of water sports such as windsurfing, sailing, canoeing, yachting, the lake is indispensable. A ferry service runs between the coastal towns all year round. The lake has its own fleet of ships from three states.",
            'https://must-see.top/wp-content/uploads/2018/06/bodenskoe-ozero-700x438.jpg']}
    rivers = {'Danube': [
        "A huge river with crystal clear water. The Danube is considered the second longest river in Europe after the Volga. The Danube flows through half of the continent. The source of the river is located on the territory of Germany in the mountains of the Black Forest. The river crosses the territories of ten countries and passes through four vibrant capitals: Belgrade, Budapest, Bratislava and Vienna. It flows into the Black Sea.",
        'https://must-see.top/wp-content/uploads/2019/04/dunai--700x470.jpg'],
        'Rhine': [
            "It is the longest river in Germany. The Rhine can be considered the personification of all of Europe. The river starts in the Alps and flows into the North Sea. The Rhine plays a huge role in Germany's trade and economic relations with other countries, as well as in the cultural life of the country. Along the banks of the Rhine, a large number of ancient fortresses and castles have been preserved. A cruise ship runs regularly on the river.",
            'https://must-see.top/wp-content/uploads/2019/04/rei-n-700x467.jpg'],
        'Elbe': [
            "It flows through the lands of Germany and the Czech Republic. However, most of it is in the territory of the Germans. The Elbe originates in the Czech Republic high in the Giant Mountains (1368 km above sea level). The river flows into the North Sea. On the Elbe, there are beautiful German cities: Hamburg, Macdeburg, Dresden with spacious embankments and many places of interest for tourists.",
            'https://must-see.top/wp-content/uploads/2019/04/elba-700x453.jpg']}

    # currency
    currencyName = 'EUR'
    currencyEqualsToDollar = 1

    # military
    milPolBlock = "NATO"
    amountOfPeopleInArmy = 182832

    # healthcare
    numberOfDoctorsPer100kPopulation = 413
    menAverageLifeExpectancy = 77.2  # years
    womenAverageLifeExpectancy = 82.4  # years

    # climat
    juneAverageTemperature = 21  # °C
    decemberAverageTemperature = 0  # °C
    averageHumidity = 79  # %
    averageDurationOfWinter = 3  # month
    averageRainfallPerMonth = 52.08  # mm (?)
    averageNumberOfFoggyDaysPerYear = 89  # days
    averageNumberOfRainyDaysPerYear = 140  # days
    averageNumberOfClearDays = 136  # days

    # security
    situationInTheCountry = 3  # [1, 3] 1-bad, 3-good
    freedomOfSpeech = 3  # [1, 3]
    assessmentOfFamilyLife = 3  # [1, 3]
    attitudeTowardsLGBT = 3  # [1, 3]

    # population
    populationCount = 83130000
    procentOfMales = 49
    procentOfFemales = 51
    populationDensityPerSquareKilometer = 240
    speedOfLife = 2  # [1, 3]
    workPlaces = 3  # [1, 3]
    nightLifeEntertainment = 3  # [1, 3]

    # citizenship
    citizenshipGlobalRank = 3
    friendlyToForeigners = 0

    # communication
    communicationOnEnglish = 2  # [1, 3]

    # transport
    averageTravelTimeToWork = 42.1
    developmentLevelOfPublicTransport = 3  # [1, 3]

    # internet
    speedOfInternetMbps = 49  # Мегабиты в секунду
    freeWifi = 2  # [1, 3]

    # education
    rankingOfNationalEducationSystem = 16

    cc.createBase(countryName, cities, officialLanguage,
                  # currency
                  currencyName, currencyEqualsToDollar,
                  # military
                  milPolBlock, amountOfPeopleInArmy,
                  # healthcare
                  numberOfDoctorsPer100kPopulation, menAverageLifeExpectancy, womenAverageLifeExpectancy,
                  # climat
                  juneAverageTemperature, decemberAverageTemperature, averageHumidity,
                  averageDurationOfWinter, averageRainfallPerMonth, averageNumberOfFoggyDaysPerYear,
                  averageNumberOfRainyDaysPerYear, averageNumberOfClearDays,
                  # security
                  situationInTheCountry, freedomOfSpeech,
                  assessmentOfFamilyLife, attitudeTowardsLGBT,
                  # population
                  populationCount, procentOfMales, procentOfFemales, populationDensityPerSquareKilometer,
                  speedOfLife, workPlaces, nightLifeEntertainment,
                  # citizenship
                  citizenshipGlobalRank,
                  # communication
                  communicationOnEnglish,
                  # transport
                  averageTravelTimeToWork, developmentLevelOfPublicTransport,
                  # internet
                  speedOfInternetMbps, freeWifi,
                  # education
                  rankingOfNationalEducationSystem, universities, faculties, programs, costs, links, images,
                  requirements,
                  hostel, scolarship, sights, beaches, mountains, skiResorts, lakes, rivers, friendlyToForeigners
                  )
    # cc.createManMadeDisaster(countryName, nameMMD, typeOfMMD, aomuntOfDeadPeople,
    #                           aomuntOfInjuredPeople, territoryOfPollution)
    # cc.createOceans()

    #############################   GERMANY   #############################

    #############################   SLOVAKIA   #############################

    # Country
    countryName = "Slovakia"
    officialLanguage = "Slovak"

    # cities     name      isBig WashesBy
    cities = {'Bratislava': [True, True, None], 'Kosice': [True, True, None], 'Nitra': [True, True, None],
              'Presov': [True, True, None], 'Banska Bystrica': [True, True, None]}

    # education
    universities = {'Bratislava': ['Slovak University of Technology in Bratislava', 'Comenius University Bratislava'],
                    'Kosice': ['University of Veterinary Medicine in Kosice', 'Pavol Josef Safarik University'],
                    'Nitra': ['Slovak University of Agriculture in Nitra', 'Constantine the Philosopher University'],
                    'Presov': ['University of Presov', 'International Business College ISM Slovakia in Presov'],
                    'Banska Bystrica': ['Matej Bel University in Banská Bystrica',
                                        'Academy of Arts in Banská Bystrica']}
    faculties = {'Slovak University of Technology in Bratislava': ['Faculty of Engineering',
                                                                   'Faculty of Engineering',
                                                                   'Faculty of Science',
                                                                   'Faculty of Architecture'],
                 'Comenius University Bratislava': ['Faculty of Medicine', 'Faculty of Law', 'Faculty of Arts',
                                                    'Faculty of Science', 'Faculty of Education',
                                                    'Faculty of Medicine'],
                 'University of Veterinary Medicine in Kosice': ['Faculty of Medicine'],
                 'Pavol Josef Safarik University': ['Faculty of Medicine', 'Faculty of Science'],
                 'Slovak University of Agriculture in Nitra': ['Faculty of Forestry', 'Faculty of Science',
                                                               'Faculty of Engineering',
                                                               'Faculty of Economics'],
                 'Constantine the Philosopher University': ['Faculty of Arts', 'Faculty of Science',
                                                            'Faculty of Computer Engineering and Software'],
                 'University of Presov': ['Faculty of Arts', 'Faculty of Economics',
                                          'Faculty of Education', 'Faculty of Medicine'],
                 'International Business College ISM Slovakia in Presov': ['Faculty of Economics',
                                                                           'Faculty of Law'],
                 'Matej Bel University in Banská Bystrica': ['Faculty of Economics', 'Faculty of Science',
                                                             'Faculty of Arts', 'Faculty of Education',
                                                             'Faculty of Law'],
                 'Academy of Arts in Banská Bystrica': ['Faculty of Arts']}

    programs = {'Slovak University of Technology in Bratislava': ['Magistracy', 'Undergraduate'],
                'Comenius University Bratislava': ['Magistracy', 'Undergraduate'],
                'University of Veterinary Medicine in Kosice': ['Magistracy', 'Undergraduate'],
                'Pavol Josef Safarik University': ['Foundation', 'Undergraduate', 'MBA'],
                'Slovak University of Agriculture in Nitra': ['Magistracy', 'Undergraduate'],
                'Constantine the Philosopher University': ['Magistracy', 'Undergraduate'],
                'University of Presov': ['Magistracy', 'Undergraduate', 'MBA'],
                'International Business College ISM Slovakia in Presov': ['Magistracy', 'Undergraduate', 'MBA'],
                'Matej Bel University in Banská Bystrica': ['Magistracy', 'Undergraduate', 'MBA'],
                'Academy of Arts in Banská Bystrica': ['Magistracy', 'Undergraduate']}
    links = {'Slovak University of Technology in Bratislava': 'https://www.stuba.sk/english.html?page_id=132',
             'Comenius University Bratislava': 'https://uniba.sk/en/',
             'University of Veterinary Medicine in Kosice': 'https://www.uvlf.sk/en',
             'Pavol Josef Safarik University': 'https://www.upjs.sk/en/faculty-of-medicine/',
             'Slovak University of Agriculture in Nitra': 'https://www.uniag.sk/en/main-page',
             'Constantine the Philosopher University': 'https://www.ukf.sk/en/university',
             'University of Presov': 'https://www.unipo.sk/en/',
             'International Business College ISM Slovakia in Presov': 'https://free-apply.com/en/university/1070300002',
             'Matej Bel University in Banská Bystrica': 'https://www.umb.sk/ru/',
             'Academy of Arts in Banská Bystrica': 'https://www.aku.sk/en/'}

    images = {
        'Slovak University of Technology in Bratislava': 'https://www.stuba.sk/buxus/images/cache/stu.full_banner/stu/informacie_o/stu/str_7-8_STU.jpg',
        'Comenius University Bratislava': 'https://free-student-slovakia.org/wp-content/uploads/2022/02/181031_uk_cae3d20d78.jpg',
        'University of Veterinary Medicine in Kosice': 'https://lh3.googleusercontent.com/p/AF1QipMUQ-8AbsRqgjl3qxepLPSBIOKkTIrtFqpDLjpM=s680-w680-h510',
        'Pavol Josef Safarik University': 'https://image.free-apply.com/gallery/l/uni/gallery/lg/1070300007/c58b9fc854a6401f7e811d18d695e74346f35c43.jpg?s=640',
        'Slovak University of Agriculture in Nitra': 'https://image.free-apply.com/gallery/l/uni/gallery/lg/1070300020/b2c9719c09f88be391b1757dce4435a85d335560.jpg?s=640',
        'Constantine the Philosopher University': 'https://msmstudy.sk/wp-content/uploads/2021/01/filozof1.jpg',
        'University of Presov': 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Slovakia_Presov_926.JPG/1200px-Slovakia_Presov_926.JPG',
        'International Business College ISM Slovakia in Presov': 'https://image.free-apply.com/gallery/l/uni/gallery/lg/1070300002/4f4bbfe732b046dc0237f7106172a9003f46ba42.jpg?s=640',
        'Matej Bel University in Banská Bystrica': 'https://image.free-apply.com/gallery/l/uni/gallery/lg/1070300005/9f4b6c3eae377b7cc1ca9cabda09d395d8cfd1c5.jpg?s=640',
        'Academy of Arts in Banská Bystrica': 'https://image.free-apply.com/gallery/l/uni/gallery/lg/1070300001/a790c079076aa593450a78192a1c60ba67b07b63.jpg?s=640'}
    # общага
    hostel = {'Slovak University of Technology in Bratislava': 'Yes',
              'Comenius University Bratislava': 'Yes',
              'University of Veterinary Medicine in Kosice': 'Yes',
              'Pavol Josef Safarik University': 'Yes',
              'Slovak University of Agriculture in Nitra': 'Yes',
              'Constantine the Philosopher University': 'No',
              'University of Presov': 'Yes',
              'International Business College ISM Slovakia in Presov': 'No',
              'Matej Bel University in Banská Bystrica': 'Yes',
              'Academy of Arts in Banská Bystrica': 'No'}
    # стипендия
    scolarship = {'Slovak University of Technology in Bratislava': 'Yes',
                  'Comenius University Bratislava': 'Yes',
                  'University of Veterinary Medicine in Kosice': 'Yes',
                  'Pavol Josef Safarik University': 'Yes',
                  'Slovak University of Agriculture in Nitra': 'Yes',
                  'Constantine the Philosopher University': 'Yes',
                  'University of Presov': 'Yes',
                  'International Business College ISM Slovakia in Presov': 'Yes',
                  'Matej Bel University in Banská Bystrica': 'Yes',
                  'Academy of Arts in Banská Bystrica': 'Yes'
                  }
    # требования к поступлению
    requirements = {'Slovak University of Technology in Bratislava': 'Higher Certificate '
                                                                     '40% in English. '
                                                                     '30% in either Mathematics or Mathematical Literacy. '
                                                                     '40% in Life Orientation. '
                                                                     '50% in four vocational subjects.',
                    'Comenius University Bratislava': 'Maintain a minimum IB of 24 in order to stand a good chance to get admission into Comenius University in Bratislava',
                    'University of Veterinary Medicine in Kosice': '5 GCSEs at grades 9 to 4 (A* to C), or equivalent, including English, maths and science',
                    'Pavol Josef Safarik University': 'Valid passport.'
                                                      'Two-recent Passport size photo.'
                                                      'University entrance qualification recognized by Germany (A-Levels or equivalent)'
                                                      'Proof of previous academic performance.',
                    'Slovak University of Agriculture in Nitra': 'Application form '
                                                                 'Decision on recognition of documents on completed secondary education which is issued by the Regional Office of Education in Nitra, Department of Vocational and Methodological Activities, J. Vuruma 1, 949 01 Nitra (procedure for processing the above documents). '
                                                                 'Curriculum Vitae. '
                                                                 'Proof of payment of the fee for admission procedure. ',
                    'Constantine the Philosopher University': 'Higher Certificate '
                                                              '40% in English. '
                                                              '30% in either Mathematics or Mathematical Literacy. '
                                                              '40% in Life Orientation. '
                                                              '50% in four vocational subjects.',
                    'University of Presov': 'A copy of the passport (page with photo and personal data). '
                                            'Autobiography in Slovak. '
                                            'The original certificate of study of subjects and grades for the 8th, 9th, 10th and first six months of the 11th grade, plus a translation into Slovak (if there is no certificate yet). '
                                            'Statement of health '
                                            'Valid health insurance policy. '
                                            'The original document on recognition of the equivalence of the previous education of a foreigner in Slovakia, issued by the Presevo regional department of the education department. '
                                            '6 photo cards 30 x 35 mm.',
                    'International Business College ISM Slovakia in Presov': 'Application form '
                                                                             'Decision on recognition of documents on completed secondary education which is issued by the Regional Office of Education in Nitra, Department of Vocational and Methodological Activities, J. Vuruma 1, 949 01 Nitra (procedure for processing the above documents). '
                                                                             'Curriculum Vitae. '
                                                                             'Proof of payment of the fee for admission procedure. ',
                    'Matej Bel University in Banská Bystrica': 'Valid passport.'
                                                               'Two-recent Passport size photo.'
                                                               'University entrance qualification recognized by Germany (A-Levels or equivalent)'
                                                               'Proof of previous academic performance.',
                    'Academy of Arts in Banská Bystrica': 'Higher Certificate '
                                                          '40% in English. '
                                                          '30% in either Mathematics or Mathematical Literacy. '
                                                          '40% in Life Orientation. '
                                                          '50% in four vocational subjects.'}

    costs = {'Slovak University of Technology in Bratislava': 900,
             'Comenius University Bratislava': 890,
             'University of Veterinary Medicine in Kosice': 950,
             'Pavol Josef Safarik University': 990,
             'Slovak University of Agriculture in Nitra': 930,
             'Constantine the Philosopher University': 2500,
             'University of Presov': 1000,
             'International Business College ISM Slovakia in Presov': 1100,
             'Matej Bel University in Banská Bystrica': 970,
             'Academy of Arts in Banská Bystrica': 830}

    sights = {'Old town of Bratislava': [
        "It is not difficult to guess that a large number of historical monuments are concentrated in this place. It does not do on the streets without government agencies, offices. The western part of the settlement is represented by a hilly surface, there is a castle, embassies of various countries. The eastern section of the Old Town is the historical and administrative center. There are many monuments, churches and other sights on the territory.",
        'https://www.tripzaza.com/ru/destinations/wp-content/uploads/2018/02/1-The_Old_Town_of_Bratislava-e1518579004639.jpg'],
        'Yasovska cave': [
            "Excursions in Slovakia are often organized from the town of Stos in the direction of the village of Jasov. There is an underground formation interesting for tourists, namely, on the territory of a park of national importance. There is a Premonstratensian monastery nearby, so until some time the cave was used exclusively by monks. The total length of the dungeon reaches 2811 m, but only 720 m are open for excursions. The described landmark of Slovakia is interesting for its bizarre limestone layers, underground waterfalls. The halls inside are located at different levels, the differences between them sometimes reach 30 m.",
            'https://www.tripzaza.com/ru/destinations/wp-content/uploads/2018/02/2-Jasovska_Cave-e1518579440564.jpg'],
        'Spissky Castle': [
            "Not everyone knows, but in this country it is customary to call castles “grads”. The one that will be discussed is one of the largest in the country. The construction of Spišský began in the 11th century, based on the remains of a Celtic settlement. The castle repeatedly successfully repelled enemy attacks, all because it was built on dolomite rocks, 200 m high. It was repeatedly rebuilt, reconstructed, so the Renaissance, Romanesque Gothic can be traced in the architecture of the building. Today, the building houses a museum that presents medieval utensils, furniture, weapons and armor to the attention of guests.",
            'https://www.tripzaza.com/ru/destinations/wp-content/uploads/2018/02/3-Spissky_Hrad-e1518579928122.jpg']}
    beaches = {}
    mountains = {'High Tatras': [
        "The highest Slovak mountains, the High Tatras, are the biggest tourist and climbing attraction in the entire country. Their main ridge, 26 km long, practically does not fall below 2,000 meters above sea level. The highest peak - Gerlakhovsky shtit (2655 m above sea level) is also the highest peak in all the Carpathians. Attractions are beautiful views, mountain lakes, beautiful waterfalls and local antelope - chamois.",
        'https://cdn.gigaplaces.com/storage_thumbs/301/301_1170_531_60.webp?v=1659950559'],
        'Western Tatras': [
            "The Western Tatras are located in both Slovakia and Poland and belong to two national parks - the Tatra National Park and the Tatrza National Park. The highest peak is Banikov (2178 m above sea level). The most popular part of the mountains is Rogache with sharp rocky ridges.",
            'https://cdn.gigaplaces.com/storage_thumbs/40862/40862_1170_531_60.webp?v=1659958709'],
        'Belianske Tatras': [
            'In the very east of the Tatras there is a beautiful limestone part - Belianske Tatras. Due to the protection of nature, the Tatra National Park has the fewest hiking trails, and even the highest peak of Gavran (2152 m) is not officially open for tourism.',
            'https://cdn.gigaplaces.com/storage_thumbs/40864/40864_1170_531_60.webp?v=1659952218']}
    skiResorts = {'Jasna Low Tatras': [
        "Unique views, a wide range of slopes and modern cable cars - all this is Jasná Nízke Tatry, the largest ski resort in Slovakia. Jasná offers 46 km of slopes, 30 transport units, 15 bars and restaurants.",
        'http://sacr3-files.s3-eu-west-1.amazonaws.com/_processed_/csm_Jasn%25C3%25A1%2520N%25C3%25ADzke%2520Tatry%252001%2520%25283%2529_e9a1c0edd3.jpg'],
        'SNOW PARK Donovaly': [
            "The PARK SNOW Donovaly ski resort is located on the border of the Low Tatra and Velka Fatra national parks. It is one of the most famous in Slovakia. Landmark Donoval - the second largest children's complex in Europe.",
            'http://sacr3-files.s3-eu-west-1.amazonaws.com/_processed_/csm_DJI_0465_resize_79d7fcefb6.jpg'],
        'Vratna Mala Fatra': [
            "Vratna Free Time Zone is located in the Malá Fatra National Park and is one of the four highest resorts in Slovakia. The height of the slopes is up to 1520 meters above sea level.",
            'http://sacr3-files.s3-eu-west-1.amazonaws.com/_processed_/csm_Vr%25C3%25A1tna%2520Mal%25C3%25A1%2520Fatra%2520003_046af4a4a1.jpg']}
    lakes = {'Wieliczke Pleso': [
        "Velice Pleso is a lake on the lower level of the upper part of the Velicka Valley in the High Tatras. The name of the lake is associated with the expansion of the former city of Velka (now the urban quarter of Poprad). This territory originally belonged to the Gerlakhovsky and Velkoslavkovsky districts, but got its name from the city of Velka.",
        'https://waterresources.ru/wp-content/uploads/2020/09/velicke-pleso.jpg'],
        'Kuhaida': [
            "Kuhaida is a natural place for relaxing and swimming in Bratislava. Its name comes from the German Kuhheide, which indicates the original purpose of this area.",
            'https://waterresources.ru/wp-content/uploads/2020/09/kuhajda-ozero-bratislava.jpg'],
        'Zlate-Pieski': [
            'Zlate Pieski is a lake in Bratislava, in the Ruzhinov region. The width is about 400 meters, the depth is about 30 meters. Around the lake there are places for sports, in the center of the lake there is a wooded island. Used for swimming.',
            'https://waterresources.ru/wp-content/uploads/2020/09/zlate-peski.jpg']}
    rivers = {'Danube': [
        "The second longest river in Europe (after the Volga), 'international' river, the longest river in the European Union. Length - 2960 km. The river takes its source in Germany, in the mountains of the Black Forest.",
        'https://travelfotokor.ru/bratislava/picbig/40dunay.jpg'],
        'Tisza': [
            "A river in central Europe, the left and longest tributary of the Danube. Tisza originates in the east of the Transcarpathian region of Ukraine. It is formed by merging near the city of Rakhova, the Black Tisa and White Tisa rivers. The source of the Black Tisa is located on the northeastern slopes of the Svidovets ridge at an altitude of 1400 m above sea level. Belaya Tisa originates on the southwestern slopes of the Chernogora massif, at an altitude of 1650 m above sea level.",
            'https://upload.wikimedia.org/wikipedia/commons/4/4c/Szeged-tisza3.jpg'],
        'Bebrava': [
            "A river in western Slovakia, a tributary of the Nitra. It flows through Banovce nad Bebravou.",
            'https://womanadvice.ru/sites/default/files/imagecache/width_660/49/2019-04-23_2034/reka_gron_slovakiya.jpg']}

    # currency
    currencyName = 'EUR'
    currencyEqualsToDollar = 1

    # military
    milPolBlock = "NATO"
    amountOfPeopleInArmy = 26200

    # healthcare
    numberOfDoctorsPer100kPopulation = 300
    menAverageLifeExpectancy = 75.8  # years
    womenAverageLifeExpectancy = 75.8  # years

    # climat
    juneAverageTemperature = 19.6  # °C
    decemberAverageTemperature = 1.7  # °C
    averageHumidity = 75  # %
    averageDurationOfWinter = 3.5  # month
    averageRainfallPerMonth = 48.3  # mm (?)
    averageNumberOfFoggyDaysPerYear = 70  # days
    averageNumberOfRainyDaysPerYear = 142  # days
    averageNumberOfClearDays = 153  # days

    # security
    situationInTheCountry = 3  # [1, 3] 1-bad, 3-good
    freedomOfSpeech = 3  # [1, 3]
    assessmentOfFamilyLife = 3  # [1, 3]
    attitudeTowardsLGBT = 2  # [1, 3]

    # population
    populationCount = 5447000
    procentOfMales = 49
    procentOfFemales = 51
    populationDensityPerSquareKilometer = 114
    speedOfLife = 2  # [1, 3]
    workPlaces = 2  # [1, 3]
    nightLifeEntertainment = 3  # [1, 3]

    # citizenship
    citizenshipGlobalRank = 9
    friendlyToForeigners = 1

    # communication
    communicationOnEnglish = 1  # [1, 3]

    # transport
    averageTravelTimeToWork = 44.3
    developmentLevelOfPublicTransport = 2  # [1, 3]

    # internet
    speedOfInternetMbps = 45.47  # Мегабиты в секунду
    freeWifi = 2  # [1, 3]

    # education
    rankingOfNationalEducationSystem = 38

    cc.createBase(countryName, cities, officialLanguage,
                  # currency
                  currencyName, currencyEqualsToDollar,
                  # military
                  milPolBlock, amountOfPeopleInArmy,
                  # healthcare
                  numberOfDoctorsPer100kPopulation, menAverageLifeExpectancy, womenAverageLifeExpectancy,
                  # climat
                  juneAverageTemperature, decemberAverageTemperature, averageHumidity,
                  averageDurationOfWinter, averageRainfallPerMonth, averageNumberOfFoggyDaysPerYear,
                  averageNumberOfRainyDaysPerYear, averageNumberOfClearDays,
                  # security
                  situationInTheCountry, freedomOfSpeech,
                  assessmentOfFamilyLife, attitudeTowardsLGBT,
                  # population
                  populationCount, procentOfMales, procentOfFemales, populationDensityPerSquareKilometer,
                  speedOfLife, workPlaces, nightLifeEntertainment,
                  # citizenship
                  citizenshipGlobalRank,
                  # communication
                  communicationOnEnglish,
                  # transport
                  averageTravelTimeToWork, developmentLevelOfPublicTransport,
                  # internet
                  speedOfInternetMbps, freeWifi,
                  # education
                  rankingOfNationalEducationSystem, universities, faculties, programs, costs, links, images,
                  requirements,
                  hostel, scolarship, sights, beaches, mountains, skiResorts, lakes, rivers, friendlyToForeigners
                  )
    # cc.createManMadeDisaster(countryName, nameMMD, typeOfMMD, aomuntOfDeadPeople,
    #                           aomuntOfInjuredPeople, territoryOfPollution)
    # cc.createOceans()

    #############################   SLOVAKIA   #############################

    #############################   HUNGARY   #############################

    # Country
    countryName = "Hungary"
    officialLanguage = "Hungarian"

    # cities     name      isBig WashesBy
    cities = {'Budapest': [True, True, None], 'Debrecen': [True, True, None], 'Szeged': [True, True, None],
              'Miskolc': [True, True, None], 'Pecs': [True, True, None]}

    # education
    universities = {'Budapest': ['Eötvös Loránd University', 'Semmelweis University'],
                    'Debrecen': ['University of Debrecen', 'Debrecen University of Reformed Theology'],
                    'Szeged': ['University of Szeged'],
                    'Miskolc': ['University of Miskolc'],
                    'Pecs': ['University of Pecs']}
    faculties = {'Eötvös Loránd University': ['Faculty of Economics', 'Faculty of Education',
                                              'Faculty of Computer Engineering and Software', 'Faculty of Law',
                                              'Faculty of Science',
                                              'Faculty of Social Science'],
                 'Semmelweis University': ['Faculty of Medicine'],
                 'University of Debrecen': ['Faculty of Economics',
                                            'Faculty of Engineering', 'Faculty of Law',
                                            'Faculty of Computer Engineering and Software',
                                            'Faculty of Medicine', 'Faculty of Arts'],
                 'Debrecen University of Reformed Theology': ['Faculty of Social Sciences', 'Faculty of Medicine'],
                 'University of Szeged': ['Faculty of Forestry', 'Faculty of Social Sciences',
                                          'Faculty of Medicine', 'Faculty of Economics', 'Faculty of Engineering'],
                 'University of Miskolc': ['Faculty of Engineering', 'Faculty of Computer Engineering and Software',
                                           'Faculty of Engineering', 'Faculty of Economics',
                                           'Faculty of Arts', 'Faculty of Law'],
                 'University of Pecs': ['Faculty of Economics',
                                        'Faculty of Education', 'Faculty of Engineering',
                                        'Faculty of Computer Engineering and Software', 'Faculty of Law']}

    programs = {'Eötvös Loránd University': ['Magistracy', 'Undergraduate', 'MBA'],
                'Semmelweis University': ['Magistracy', 'Undergraduate', 'MBA'],
                'University of Debrecen': ['Magistracy', 'Undergraduate'],
                'Debrecen University of Reformed Theology': ['Foundation', 'Undergraduate'],
                'University of Szeged': ['Magistracy', 'Undergraduate'],
                'University of Miskolc': ['Magistracy', 'Undergraduate', 'MBA'],
                'University of Pecs': ['Magistracy', 'Undergraduate']}
    links = {'Eötvös Loránd University': 'https://www.elte.hu/en/',
             'Semmelweis University': 'https://semmelweis.hu/english/',
             'University of Debrecen': 'https://www.edu.unideb.hu/',
             'Debrecen University of Reformed Theology': 'https://drhe.hu/',
             'University of Szeged': 'https://u-szeged.hu/',
             'University of Miskolc': 'https://www.uni-miskolc.hu/',
             'University of Pecs': 'https://ajk.pte.hu/hu'}

    images = {
        'Eötvös Loránd University': 'https://dynamic-media-cdn.tripadvisor.com/media/photo-o/11/59/1b/07/eotvos-lorand-tudomanyegyetem.jpg?w=1200&h=-1&s=1',
        'Semmelweis University': 'https://images.squarespace-cdn.com/content/v1/565f850be4b020f4bf35b831/1645194846588-M7UZOWPJI4B4RBKQFY3Z/semmelweis-1.jpg?format=2500w',
        'University of Debrecen': 'https://upload.wikimedia.org/wikipedia/commons/7/73/DebrecenDSCN3583.JPG',
        'Debrecen University of Reformed Theology': 'https://image.free-apply.com/gallery/l/uni/gallery/lg/1034800047/1498844e9143feac370d0e377d8b3c3c43837d67.jpg?s=640',
        'University of Szeged': 'https://study-eu.s3.amazonaws.com/uploads/image/path/335/social_1200_university-of-szeged.jpg',
        'University of Miskolc': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/0b/UnivMiskolc_Main.jpg/1200px-UnivMiskolc_Main.jpg',
        'University of Pecs': 'https://img.emg-services.net/institutes/institute28808/universityofpecs_institute-1-1-1-1-1-1-1-1-1.png'}
    # общага
    hostel = {'Eötvös Loránd University': 'No',
              'Semmelweis University': 'Yes',
              'University of Debrecen': 'Yes',
              'Debrecen University of Reformed Theology': 'Yes',
              'University of Szeged': 'Yes',
              'University of Miskolc': 'Yes',
              'University of Pecs': 'No'}
    # стипендия
    scolarship = {'Eötvös Loránd University': 'Yes',
                  'Semmelweis University': 'Yes',
                  'University of Debrecen': 'Yes',
                  'Debrecen University of Reformed Theology': 'Yes',
                  'University of Szeged': 'Yes',
                  'University of Miskolc': 'Yes',
                  'University of Pecs': 'Yes'
                  }
    # требования к поступлению
    requirements = {'Eötvös Loránd University': 'discrpt',
                    'Semmelweis University': 'discrpt',
                    'University of Debrecen': 'discrpt',
                    'Debrecen University of Reformed Theology': 'discrpt',
                    'University of Szeged': 'discrpt',
                    'University of Miskolc': 'discrpt',
                    'University of Pecs': 'discrpt'}

    costs = {'Eötvös Loránd University': 4800,
             'Semmelweis University': 13000,
             'University of Debrecen': 6500,
             'Debrecen University of Reformed Theology': 5000,
             'University of Szeged': 3000,
             'University of Miskolc': 1000,
             'University of Pecs': 1650}

    sights = {'Buda Castle': [
        "This monumental building opens in all its grandeur and splendor from Gellert Mountain, although its dome can be seen from almost anywhere in the center of Budapest.",
        'https://www.tripzaza.com/ru/destinations/wp-content/uploads/2017/04/Hungary-2-Buda-Castle-e1492062571682.jpg'],
        'Eger Castle': [
            "Its heroic story began in 1552, during the attack of thousands of Turkish troops. According to documents, at that time there were no more than 2,300 defenders in the fortress, who managed to resist the enemy and prevent him from entering the city. But in 1701, the Austrian army managed to come close to the structure and blow up most of it. Restoration of the destroyed building began only in 1925.",
            'https://www.tripzaza.com/ru/destinations/wp-content/uploads/2017/04/Hungary-4-The-Castle-of-Eger-e1492062934254.jpg'],
        'Bükk National Park': [
            "The park is located on the hills of the same name, the tops of which are covered with huge oaks and beeches. On all slopes there are walking and cycling paths, there are many signs and benches for rest. At the foot of the hills there are orchards and vineyards, from which excellent local wine is made.",
            'https://www.tripzaza.com/ru/destinations/wp-content/uploads/2017/04/Gloriette_meadow_and_B--kk_hills_Szilv--sv--rad_Hungary-e1508401430953.jpg']}
    beaches = {'Shifok': [
        "Siofok beaches are very popular among tourists. The extensive length allows you to comfortably accommodate everyone who wants to relax near the water. The entrance to the lake is gentle, the shore is sandy, so you can swim here with your children. Resort guests are offered various types of entertainment: cycling, beach volleyball, horseback riding.",
        'https://blog.ufs-online.ru/media/2217/shutterstock_4620976.jpg?anchor=center&mode=crop&width=1440&height=872&rnd=132206560600000000'],
        "Helikon Beach": [
            "Lake Balaton is beautiful in any weather. A great place for walking and relaxing: feed the swans, ride a ship, take a leisurely walk along the embankment, swim or have a bite to eat in a cafe - everyone will find entertainment to their liking.",
            'https://dynamic-media-cdn.tripadvisor.com/media/photo-o/12/84/cf/a1/una-spiaggia-immersa.jpg?w=1200&h=-1&s=1'],
        'Roman Beach': [
            "If you ever come to Bp you must take a visit to “Római Part”. It is a little bit far away from the center but if the weather is good and you want to have a little rest from the busy city visit this place. There are a lot of small restaurat where you can eat fish, chicken and some other tipical hungarian food. There are a lot of place where you can drink or eat an icecream. The place is just next to the Danube and you can go down to the coast. It is wort to come to this place.",
            'https://dynamic-media-cdn.tripadvisor.com/media/photo-o/13/35/d2/3f/romai-part.jpg?w=1200&h=-1&s=1']}
    mountains = {'Kekesh': [
        "Mount Kekes rises 12 kilometers northeast of Gyöngyös in the district of Heves and is part of the Matra massif. In terms of popularity among tourists visiting Hungary, it is second only to Lake Balaton and the Danube. There are several hotels and ski slopes, and at the top is the Kekes-teto TV tower.",
        'https://top10a.ru/wp-content/uploads/2019/12/1-22.jpg'],
        'Hidas Berk': [
            "the second highest peak in Hejvs and also the second highest mountain in Hungary. It is located near the Parade in the already mentioned county of Heves. Hidas Berk is a steep-sided volcanic mountain and one of the country's top tourist attractions, loved by hikers and rock climbers.",
            'https://top10a.ru/wp-content/uploads/2019/12/2-22-2048x1365.jpg'],
        'Galia-teto': [
            'Galia-teto is the third highest mountain in Hungary and in the Matra mountain range (after Kekes and Hidas-Berk, which we will talk about later). It is a major tourist attraction with an altitude of 964 meters.',
            'https://top10a.ru/wp-content/uploads/2019/12/3-21.jpg']}
    skiResorts = {'Matra': [
        "In the Matra mountain range (Matra, 100 km from Budapest) there are slopes with three lifts. Matra provides guests with arguably the best skiing spots in Hungary. Snow covers the ground here for 80-100 days a year. The two highest peaks of the massif - Kekesteto (Kekesteto, 1014 m) and Galyateto (Galyateto, 965 m) - are great for winter sports.",
        'https://www.yestravel.ru/upload/information_system_29/5/2/1/item_521/information_items_property_47949.jpg'],
        'bukk': [
            "You can also go skiing in the Bukk mountain range, 30 km from the city of Miskolc, in the Bankut ski park. This is the largest (and most popular) ski park in the most picturesque corner of northern Hungary, where snow lies until the end of March. There are 8 slopes (including 2 for beginners), a 10 km cross-country skiing track and a toboggan run, 8 lifts and a 'children's lift' for beginners. There are evening lighting, rental, ski schools. The restaurant is right next to the ski lifts. You can get there by bus from Miskolc or by car on the M3 road.",
            'https://imigrant-hungary.com/media/2015/02/2015-08-20-imigrant-8.jpg'],
        'Magas Hill': [
            "The longest training runs in Hungary are located on the slopes of Magas Hill in Šatoraljayhöy. This northern city, lying literally near the border of Slovakia, is the center of a region famous for its winemaking. Since December 2001, the longest lift in Hungary (1332 m) has been operating here.",
            'https://journeying.ru/images/stories/fabf309000c8e2f279a4c41ae51822ac(1).jpg']}
    lakes = {'Heviz': [
        "Lake Heviz is located in the west of Hungary in a small town of the same name. This popular holiday destination is open all year round and is the largest thermal lake in Europe.",
        'https://img.tourister.ru/files/1/7/5/2/5/1/2/1/original.jpg'],
        'Balaton': [
            "Lake Balaton in Hungary is often called the 'Hungarian Sea', since there is no sea in the country, but this body of water resembles it - both in size and color. Depending on the sunlight, Lake Balaton acquires either a light green or an azure blue hue. The fresh lake Balaton has long become a popular resort in Europe: people from different countries, with different levels of income, alone and with the whole family come here in winter and summer.",
            'https://img.tourister.ru/files/1/9/5/0/2/6/4/0/original.jpg'],
        'Tisza': [
            "Lake Tisza is one of the most famous resorts in Hungary. Being a creation of human hands, it covers an area of 127 square meters. Like a children's mosaic, the artificial reservoir consists of several parts, has 16 islands and 10 culverts.",
            'https://s1.1zoom.ru/big0/85/339620-svetik.jpg']}
    rivers = {'Atea': [
        "A small river in the Somesh river basin. It starts in Romania, flows through the village of Atea and then crosses the border with Hungary, where it becomes a tributary of the Somes River.",
        'https://upload.wikimedia.org/wikipedia/commons/4/4c/Szeged-tisza3.jpg'],
        'Baltsaia': [
            "A tributary of the Somesh River. The river starts in the area of the village of Dacia, Romania, is all covered with canals and today is part of the irrigation system of the Somes Plain, also called the Keleti River or the Keleti Canal. The canal crosses the border of Hungary, where it reaches the Somesh River.",
            'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5b/Villach_Drau.JPG/250px-Villach_Drau.JPG'],
        'Barkau': [
            "A river originating in Salaj County, Romania. It has a length of 134 kilometers and a basin area of 2025 km². It flows into Crisul Repede near Seghalom.",
            'https://upload.wikimedia.org/wikipedia/commons/thumb/2/26/Zala_rzeka.jpg/250px-Zala_rzeka.jpg']}

    # currency
    currencyName = 'HUF'
    currencyEqualsToDollar = 390.46

    # military
    milPolBlock = "NATO"
    amountOfPeopleInArmy = 31080

    # healthcare
    numberOfDoctorsPer100kPopulation = 332
    menAverageLifeExpectancy = 71  # years
    womenAverageLifeExpectancy = 78.8  # years

    # climat
    juneAverageTemperature = 24  # °C
    decemberAverageTemperature = 1  # °C
    averageHumidity = 68.1  # %
    averageDurationOfWinter = 3.5  # month
    averageRainfallPerMonth = 46.9  # mm (?)
    averageNumberOfFoggyDaysPerYear = 76  # days
    averageNumberOfRainyDaysPerYear = 135  # days
    averageNumberOfClearDays = 154  # days

    # security
    situationInTheCountry = 3  # [1, 3] 1-bad, 3-good
    freedomOfSpeech = 3  # [1, 3]
    assessmentOfFamilyLife = 3  # [1, 3]
    attitudeTowardsLGBT = 2  # [1, 3]

    # population
    populationCount = 9_710_000
    procentOfMales = 47.62
    procentOfFemales = 52.38
    populationDensityPerSquareKilometer = 107
    speedOfLife = 2  # [1, 3]
    workPlaces = 2  # [1, 3]
    nightLifeEntertainment = 2  # [1, 3]

    # citizenship
    citizenshipGlobalRank = 4
    friendlyToForeigners = 0

    # communication
    communicationOnEnglish = 2  # [1, 3]

    # transport
    averageTravelTimeToWork = 29
    developmentLevelOfPublicTransport = 2  # [1, 3]

    # internet
    speedOfInternetMbps = 42.11  # Мегабиты в секунду
    freeWifi = 2  # [1, 3]

    # education
    rankingOfNationalEducationSystem = 33

    cc.createBase(countryName, cities, officialLanguage,
                  # currency
                  currencyName, currencyEqualsToDollar,
                  # military
                  milPolBlock, amountOfPeopleInArmy,
                  # healthcare
                  numberOfDoctorsPer100kPopulation, menAverageLifeExpectancy, womenAverageLifeExpectancy,
                  # climat
                  juneAverageTemperature, decemberAverageTemperature, averageHumidity,
                  averageDurationOfWinter, averageRainfallPerMonth, averageNumberOfFoggyDaysPerYear,
                  averageNumberOfRainyDaysPerYear, averageNumberOfClearDays,
                  # security
                  situationInTheCountry, freedomOfSpeech,
                  assessmentOfFamilyLife, attitudeTowardsLGBT,
                  # population
                  populationCount, procentOfMales, procentOfFemales, populationDensityPerSquareKilometer,
                  speedOfLife, workPlaces, nightLifeEntertainment,
                  # citizenship
                  citizenshipGlobalRank,
                  # communication
                  communicationOnEnglish,
                  # transport
                  averageTravelTimeToWork, developmentLevelOfPublicTransport,
                  # internet
                  speedOfInternetMbps, freeWifi,
                  # education
                  rankingOfNationalEducationSystem, universities, faculties, programs, costs, links, images,
                  requirements,
                  hostel, scolarship, sights, beaches, mountains, skiResorts, lakes, rivers, friendlyToForeigners
                  )
    # cc.createManMadeDisaster(countryName, nameMMD, typeOfMMD, aomuntOfDeadPeople,
    #                           aomuntOfInjuredPeople, territoryOfPollution)
    # cc.createOceans()

    #############################   HUNGARY   #############################

    #############################   UNITED KINGDOM   #############################

    # Country
    countryName = "United Kingdom"
    officialLanguage = "English"

    # cities     name      isBig WashesBy
    cities = {'London': [True, True, None], 'Edinburgh': [True, True, "Northern ocean"],
              'Birmingham': [True, True, None],
              'Manchester': [True, True, None], 'Belfast': [True, True, "Irish sea"]}

    # education
    universities = {'London': ['University College London', 'Imperial College London'],
                    'Edinburgh': ['University of Edinburgh', 'Heriot-Watt University'],
                    'Birmingham': ['University of Birmingham', 'Aston University'],
                    'Manchester': ['University of Manchester', 'University of Salford'],
                    'Belfast': ["Queen's University Belfast"]}
    faculties = {'University College London': ['Faculty of Arts', 'Faculty of Engineering', 'Faculty of Law',
                                               'Faculty of Medicine', 'Faculty of Architecture',
                                               'Faculty of Science'],
                 'Imperial College London': ['Faculty of Engineering', 'Faculty of Medicine',
                                             'Faculty of Science'],
                 'University of Edinburgh': ['Faculty of Law', 'Faculty of Arts', 'Faculty of Medicine',
                                             'Faculty of Education',
                                             'Faculty of Science'],
                 'Heriot-Watt University': ['Faculty of Engineering', 'Faculty of Social Sciences', 'Faculty of Arts',
                                            'Faculty of Economics', 'Faculty of Computer Engineering and Software'],
                 'University of Birmingham': ['Faculty of Arts', 'Faculty of Social Sciences',
                                              'Faculty of Economics', 'Faculty of Law',
                                              'Faculty of Education', 'Faculty of Computer Engineering and Software',
                                              'Faculty of Engineering'],
                 'Aston University': ['Faculty of Economics', 'Faculty of Social Sciences', 'Faculty of Engineering',
                                      'Faculty of Science', 'Faculty of Education'],
                 'University of Manchester': ['Faculty of Medicine',
                                              'Faculty of Science', 'Faculty of Engineering', 'Faculty of Education'],
                 'University of Salford': ['Faculty of Science', 'Faculty of Engineering', 'Faculty of Arts',
                                           'Faculty of Medicine', 'Faculty of Economics'],
                 "Queen's University Belfast": ['Faculty of Arts', 'Faculty of Education', 'Faculty of Social Science',
                                                'Faculty of Engineering', 'Faculty of Science', 'Faculty of Medicine']}

    programs = {'University College London': ['Magistracy', 'Undergraduate'],
                'Imperial College London': ['Magistracy', 'Undergraduate'],
                'University of Edinburgh': ['Magistracy', 'Undergraduate'],
                'Heriot-Watt University': ['Foundation', 'Undergraduate', 'MBA'],
                'University of Birmingham': ['Magistracy', 'Undergraduate'],
                'Aston University': ['Magistracy', 'Undergraduate'],
                'University of Manchester': ['Magistracy', 'Undergraduate'],
                'University of Salford': ['Magistracy', 'Undergraduate'],
                "Queen's University Belfast": ['Magistracy', 'Undergraduate', 'MBA']}
    links = {'University College London': 'https://www.ucl.ac.uk/',
             'Imperial College London': 'https://www.imperial.ac.uk/',
             'University of Edinburgh': 'https://www.ed.ac.uk/',
             'Heriot-Watt University': 'https://www.hw.ac.uk/',
             'University of Birmingham': 'https://www.birmingham.ac.uk/index.aspx',
             'Aston University': 'https://www.aston.ac.uk/',
             'University of Manchester': 'https://www.manchester.ac.uk/',
             'University of Salford': 'https://www.salford.ac.uk/international',
             "Queen's University Belfast": 'https://www.qub.ac.uk/'}

    images = {
        'University College London': 'https://www.ucl.ac.uk/prospective-students/undergraduate/sites/prospective_students_undergraduate/files/contact-details/porticowelcomesized.png',
        'Imperial College London': 'https://www.imperial.ac.uk/ImageCropToolT4/imageTool/uploaded-images/homepage-default-social--tojpeg_1523872141375_x1.jpg',
        'University of Edinburgh': 'https://www.scotland.org/images/uploads/general/The_University_of_Edinburgh_Hero_Image.jpg',
        'Heriot-Watt University': 'https://www.hw.ac.uk/malaysia/img/schema-malaysia-campus-4x3_rdax_800x600_100s.jpg',
        'University of Birmingham': 'https://cdn.rt.emap.com/wp-content/uploads/sites/4/2022/11/08092427/University-of-Birmingham-shutterstock.jpg',
        'Aston University': 'https://www.aston.ac.uk/sites/default/files/2021-07/aston-university-clearing-2021.jpg',
        'University of Manchester': 'https://images3.content-hci.com/commimg/video/CH/myhc_301811.jpg',
        'University of Salford': 'http://intake.education/sites/default/files/salford.jpg',
        "Queen's University Belfast": 'https://blog.intostudy.com/wp-content/uploads/2020/12/QUB-Lanyon-Building_3542-1.jpg'}
    # общага
    hostel = {'University College London': 'Yes',
              'Imperial College London': 'Yes',
              'University of Edinburgh': 'Yes',
              'Heriot-Watt University': 'Yes',
              'University of Birmingham': 'Yes',
              'Aston University': 'No',
              'University of Manchester': 'No',
              'University of Salford': 'No',
              "Queen's University Belfast": 'Yes'}
    # стипендия
    scolarship = {'University College London': 'Yes',
                  'Imperial College London': 'Yes',
                  'University of Edinburgh': 'Yes',
                  'Heriot-Watt University': 'Yes',
                  'University of Birmingham': 'Yes',
                  'Aston University': 'Yes',
                  'University of Manchester': 'Yes',
                  'University of Salford': 'Yes',
                  "Queen's University Belfast": 'Yes'
                  }
    # требования к поступлению
    requirements = {
        'University College London': 'High School Diploma + Recognition of 1 year university rejection recognized by UCL with a GPA of at least 4.5/5.0. If there is a discrepancy, the samples are taken for the preparatory year. '
                                     'The level of English proficiency depends on the program. ',
        'Imperial College London': 'Education at the university in English; all students for whom it is not native must confirm a good level of English',
        'University of Edinburgh': 'Applicants must have an excellent level of English, having passed the TOEFL iBT exam with at least 90 points or IELTS at least 6.5',
        'Heriot-Watt University': 'certificate of successful completion of the Foundation (Heriot-Watt University Degree Entry Program) with grades not lower than “B”; IELTS 6.0, not less than 5.5 for each part.',
        'University of Birmingham': '12 years of education or Foundation Certificate. '
                                    'Certificate of complete secondary education '
                                    'IELTS (Academic): minimum 6.0 (not lower than 5.5 in each part) '
                                    'Motivation letter',
        'Aston University': 'Education at the university in English; all students for whom it is not native must confirm a good level of English',
        'University of Manchester': 'high school diploma with a high GPA. '
                                    'score sheet. '
                                    'IELTS - 5.5-6.0',
        'University of Salford': 'certificate of successful completion of the Foundation (Heriot-Watt University Degree Entry Program) with grades not lower than “B”; IELTS 6.0, not less than 5.5 for each part.',
        "Queen's University Belfast": 'high school diploma with a high GPA. '
                                      'score sheet. '
                                      'IELTS - 5.5-6.0'}

    costs = {'University College London': 11000,
             'Imperial College London': 10000,
             'University of Edinburgh': 9000,
             'Heriot-Watt University': 9500,
             'University of Birmingham': 9600,
             'Aston University': 8900,
             'University of Manchester': 9700,
             'University of Salford': 9500,
             "Queen's University Belfast": 9400}

    sights = {'Buckingham Palace': [
        "residence of the Queen of Great Britain. Since the 19th century, this place has been considered permanent for official receptions. In addition, the British royal family lives here.",
        'https://tripmydream.cc/travelhub/travel/blocks/20/986/block_20986.jpg?v1'],
        'Big Ben': [
            "British symbol of greatness. If you ask a local resident what is considered the most popular attraction in the UK, he will immediately name this majestic building.",
            'https://tripmydream.cc/travelhub/travel/blocks/20/988/block_20988.jpg?v1'],
        'Trafalgar Square': [
            "UK National Treasure. Those who want to take a break from the bustle of the city and admire the magnificent fountains come here.",
            'https://tripmydream.cc/travelhub/travel/blocks/20/990/block_20990.jpg?v1']}
    beaches = {'Whitstable Beach, Kent': [
        "This is a pebble city beach. It is still considered one of the best coastlines in the UK. Although walking on the rocks is quite unpleasant, the clear water and wonderful view make up for the inconvenience. In addition, for those who hate sand in slippers, this beach is a win-win option. The nearby city lures tourists with various festivals and performances. For example, in Kent they began to organize an annual oyster festival. Near the shore there are many shops and cafes where you can hide from the rain, have a bite to eat and buy souvenirs. On your way from the beach, you won't be able to resist stopping by Eliot's at 1 Harbor Street for the best crab sandwich on the coast.",
        'https://assets.gq.ru/photos/5d9f40e3fa7d480009651a25/master/w_1600,c_limit/1-WHITSTABLE%20BEACH-getty.jpg'],
        "Seven Sisters Beach, Sussex": [
            "one of the most spectacular coastlines in Britain. It is famous for the pristine white chalk cliffs that skirt this beach. They seem to protect vacationers from the rest of the unromantic world. The place has such a name because these rocks have seven peaks located along the sea. At the very edge of the cliff above the beach stretches a winding path. Not everyone will be able to walk along it, because this activity is not for the faint of heart. Seven Sisters is a great place for outdoor activities, as well as lovers of unforgettable views and wild birds, of which there are a lot.",
            'https://assets.gq.ru/photos/5d9f40e312ff0a0008b0fcb4/master/w_1600,c_limit/2-SEVEN%20SISTERS-gettyimages-494984827.jpg'],
        'Brancaster Beach, Norfolk': [
            "North Norfolk is known for its many beautiful beaches. To enjoy the modest and pristine beauty of nature, head to Brancaster. This sandy beach stretches for miles - there is a place for everyone on the golden sand. This beach is ideal for long walks with dogs or for morning runs. For wildlife lovers, the Titchwell Marsh Preserve is only two miles from the beach. In it, if you're lucky, you can even see seals basking in the sun. On the beach, it is worth following the tide schedule. When the waves go far enough, the wreckage of a sunken ship from the Second World War opens up to the eyes of tourists. If you get tired of looking at the ruins, you can visit the always crowded 'Crab Shack', which serves incredibly tasty lobsters and crab rolls.",
            'https://assets.gq.ru/photos/5d9f40e32129f20008bdbb89/master/w_1600,c_limit/3-BRANCASTER%20BEACH-getty.jpg']}
    mountains = {'ben nevis': [
        "mountain in the Grampian Mountains (Highland region, Scotland). It is the highest point in the British Isles. Locals call the mountain abbreviated - Ben.",
        'http://t2.gstatic.com/licensed-image?q=tbn:ANd9GcQWXv-L8z6gN--5q6Lx04jDPEanqGLj5a8ctgC8EBn4mpOYlNSOf4T9PJVZyY707Nfo'],
        'snowdon': [
            "the highest mountain in Wales. Highest mountain in Great Britain south of the Scottish Highlands. Located in the Snowdonia National Park in Gwynedd. The summit of Snowdon is known as Yr Wyddfa (mound) and is 1085 meters above sea level. The name 'Snowdon' comes from the Old English Snow Dun, meaning 'snowy hill'.",
            'http://t2.gstatic.com/licensed-image?q=tbn:ANd9GcQyYFnF3gqXICWcFhdU386XZAHXwfLgYTT0b6Lg-xN1BEPNZGqYVOn9rVlTpTyRj7hF'],
        'Scafell Pike': [
            'It is located in Cumbria, on the territory of the Lake District National Park or the Lake District. It has an altitude of 978 m (3209 ft) above sea level. Scafell Pike is the highest mountain in England.',
            'http://t3.gstatic.com/licensed-image?q=tbn:ANd9GcTJg-Gm0KZt6CTHe8ZXrT0JxAma5KUmH6sLhAcaHkqoasd5_fYcaHN2yUCXRnbVA27-']}
    skiResorts = {'Nevis Range': [
        "The Nevis Range ski resort is located in Fort William, near Scotland. There are 20 km of slopes for skiing and snowboarding. There are also 12 lifts for transporting guests. The winter sports area is located between 655 and 1221 m.",
        'https://ski-atlas.ru/wp-content/uploads/2019/10/NevisRange-4-780x405.jpg'],
        'glenshee': [
            "Glenshee ski resort is located in the mountains of Great Britain and Scotland. There are 40 km of slopes for skiing and snowboarding. There are also 21 lifts for transporting guests. The winter sports area is located between 650 and 900 m.",
            'https://ski-atlas.ru/wp-content/uploads/2019/10/Glenshee-1-700x405.jpeg'],
        'Glencoe Mountain': [
            "The ski resort of Glencoe Mountain is located in the mountains of Great Britain and Scotland. There are 24.3 km of slopes for skiing and snowboarding. There are also 8 lifts for transporting guests. The winter sports area is located between 360 and 1070 m.",
            'https://ski-atlas.ru/wp-content/uploads/2019/10/Glencoe-3-780x405.jpg']}
    lakes = {'Derwentwater': [
        "The picturesque reservoir is located in the north-west of England, on the territory of the Lake District National Park (Lake District) in the county of Cumbria. It is worth noting that free access to the lake is allowed only five days a year.",
        'https://s.zagranitsa.com/images/articles/3879/870x486/a715d9b737e6e529f0a1241e8a058589.jpg?1466784935'],
        'Bassenthwaite Lake': [
            "The lake is also located on the territory of the Lake District National Park, two kilometers from the village of the same name. It is notable for the fact that a huge number of species of birds are found in the vicinity. There are about seventy of them here. That is why Bassenthwaite is considered the best place to watch feathered friends.",
            'https://s.zagranitsa.com/images/articles/3879/870x486/237ce9b248dde8e03c82632880cb5ced.jpg?1466784935'],
        'Windermere': [
            "This is the largest of the natural lakes in England, and it is also located in the national park in the county of Cumbria. There are 18 small islands on the reservoir, which create landscapes of amazing beauty.",
            'https://s.zagranitsa.com/images/articles/3879/870x486/cdb73f21066209957587a801903c6aaa.jpg?1466784935']}
    rivers = {'Thames': [
        "With a channel length of 346 kilometers (215 miles), the Thames is the longest river in England and the second longest in the United Kingdom. It originates at Thames Head in Gloucestershire and flows into the North Sea, forming the Thames Estuary. Of particular significance is that the river flows through London, the capital of the United Kingdom. However, in London there is only a short section of it. In London, the Thames is dependent on tides that are 7 meters (23 feet) high and reach the lock at Teddington. The drainage basin of the river covers a vast area in the southeast and west of England. The river is fed by more than 20 tributaries. More than 80 islands and areas with both fresh and salt water are located on the Thames, which guarantees a variety of wildlife.",
        'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b9/River.thames.viewfromtowerbridge.london.arp.jpg/1200px-River.thames.viewfromtowerbridge.london.arp.jpg'],
        'Esk': [
            "The River Esk flows through two areas of Scotland at once (Dumfries and Galloway) and flows into the mouth of the Solway River. Before flowing into the mouth of the Solway River, its streams pass through a small area of the rural English county of Cumbria. The river originates in the high ground east of the town of Moffat and its two main tributaries, the Black Esk and the White Esk, merge at the southern end of Castle Air Forest. Its waters flow through the Eskdale meadow before its confluence with the Lidder Water, which defines the border between Scotland and England, passing the town of Lanen in a southerly and easterly direction. Before passing the small rural town of Loguetown, the River Esk enters England, mixing its waters with the River Lane, and near the mouth of the Eden flows into the mouth of another river, the Solway.",
            'https://thumbs.dreamstime.com/b/river-esk-cutting-tourist-fishing-town-whitby-north-yorkshire-england-uk-river-esk-whitby-195012827.jpg'],
        'Lyne': [
            "The Line is an English river that flows through the county of Cumbria. The Line originates near the village of Stepolton, where the Black Line and White Line rivers mix their waters to form a single Line. Both of these rivers are fed by waters flowing further to the north-east, namely in the wooded area of Kerpshope, belonging to the county of Cumbria, which is located close to the border of Scotland and Northumberland. Thus, the Black Line is fed by waters from the Blackline Comman source, and the White Line from the Whiteline Comman. After these streams meet each other, the river continues its course in a southwesterly direction to the town of Linefoot, where it flows into Frontier Esk. This river should not be confused with the tributary of the Tweed - Water Line, flowing in one of the regions of Scotland - Scotland Borders.",
            'https://upload.wikimedia.org/wikipedia/commons/6/66/Black_Lyne_-_geograph.org.uk_-_663740.jpg']}

    # currency
    currencyName = 'GBP'
    currencyEqualsToDollar = 0.84

    # military
    milPolBlock = "NATO"
    amountOfPeopleInArmy = 188000

    # healthcare
    numberOfDoctorsPer100kPopulation = 264
    menAverageLifeExpectancy = 79.0  # years
    womenAverageLifeExpectancy = 82.9  # years

    # climat
    juneAverageTemperature = 21  # °C
    decemberAverageTemperature = 8  # °C
    averageHumidity = 79  # %
    averageDurationOfWinter = 4  # month
    averageRainfallPerMonth = 59.3  # mm (?)
    averageNumberOfFoggyDaysPerYear = 56  # days
    averageNumberOfRainyDaysPerYear = 149  # days
    averageNumberOfClearDays = 160  # days

    # security
    situationInTheCountry = 3  # [1, 3] 1-bad, 3-good
    freedomOfSpeech = 3  # [1, 3]
    assessmentOfFamilyLife = 3  # [1, 3]
    attitudeTowardsLGBT = 3  # [1, 3]

    # population
    populationCount = 67_330_000
    procentOfMales = 48
    procentOfFemales = 52
    populationDensityPerSquareKilometer = 277.12
    speedOfLife = 3  # [1, 3]
    workPlaces = 2  # [1, 3]
    nightLifeEntertainment = 3  # [1, 3]

    # citizenship
    citizenshipGlobalRank = 4
    friendlyToForeigners = 1

    # communication
    communicationOnEnglish = 3  # [1, 3]

    # transport
    averageTravelTimeToWork = 58.8
    developmentLevelOfPublicTransport = 3  # [1, 3]

    # internet
    speedOfInternetMbps = 50.4  # Мегабиты в секунду
    freeWifi = 3  # [1, 3]

    # education
    rankingOfNationalEducationSystem = 6

    cc.createBase(countryName, cities, officialLanguage,
                  # currency
                  currencyName, currencyEqualsToDollar,
                  # military
                  milPolBlock, amountOfPeopleInArmy,
                  # healthcare
                  numberOfDoctorsPer100kPopulation, menAverageLifeExpectancy, womenAverageLifeExpectancy,
                  # climat
                  juneAverageTemperature, decemberAverageTemperature, averageHumidity,
                  averageDurationOfWinter, averageRainfallPerMonth, averageNumberOfFoggyDaysPerYear,
                  averageNumberOfRainyDaysPerYear, averageNumberOfClearDays,
                  # security
                  situationInTheCountry, freedomOfSpeech,
                  assessmentOfFamilyLife, attitudeTowardsLGBT,
                  # population
                  populationCount, procentOfMales, procentOfFemales, populationDensityPerSquareKilometer,
                  speedOfLife, workPlaces, nightLifeEntertainment,
                  # citizenship
                  citizenshipGlobalRank,
                  # communication
                  communicationOnEnglish,
                  # transport
                  averageTravelTimeToWork, developmentLevelOfPublicTransport,
                  # internet
                  speedOfInternetMbps, freeWifi,
                  # education
                  rankingOfNationalEducationSystem, universities, faculties, programs, costs, links, images,
                  requirements,
                  hostel, scolarship, sights, beaches, mountains, skiResorts, lakes, rivers, friendlyToForeigners
                  )
    # cc.createManMadeDisaster(countryName, nameMMD, typeOfMMD, aomuntOfDeadPeople,
    #                           aomuntOfInjuredPeople, territoryOfPollution)
    # cc.createOceans()

    #############################   UNITED KINGDOM   #############################

    #############################   FINLAND   #############################

    # Country
    countryName = "Finland"
    officialLanguage = "Finnish"

    # cities     name      isBig WashesBy
    cities = {'Helsinki': [True, True, "The Gulf of Finland"], 'Turku': [True, True, "Baltic Sea"],
              'Tampere': [True, True, None],
              'Oulu': [True, True, "Baltic Gulf"], 'Rovaniemi': [True, True, None]}

    # education
    universities = {'Helsinki': ['University of Helsinki', 'Hanken School of Economics'],
                    'Turku': ['University of Turku', 'Abo Akademi University'],
                    'Tampere': ['University of Tampere'],
                    'Oulu': ['University of Oulu', 'Oulu University of Applied Sciences'],
                    'Rovaniemi': ['University of Lapland', 'Lapland University of Applied Sciences']}
    faculties = {'University of Helsinki': ['Faculty of Forestry', 'Faculty of Arts',
                                            'Faculty of Education', 'Faculty of Law', 'Faculty of Medicine',
                                            'Faculty of Science', 'Faculty of Social Sciences'],
                 'Hanken School of Economics': ['Faculty of Economics'],
                 'University of Turku': ['Faculty of Education', 'Faculty of Law',
                                         'Faculty of Medicine', 'Faculty of Science', 'Faculty of Engineering'],
                 'Abo Akademi University': ['Faculty of Arts',
                                            'Faculty of Education', 'Faculty of Science', 'Faculty of Engineering',
                                            'Faculty of Social Sciences', 'Faculty of Economics'],
                 'University of Tampere': ['Faculty of Architecture', 'Faculty of Education', 'Faculty of Engineering',
                                           'Faculty of Science', 'Faculty of Computer Engineering and Software',
                                           'Faculty of Economics', 'Faculty of Medicine'],
                 'University of Oulu': ['Faculty of Science', 'Faculty of Medicine',
                                        'Faculty of Education', 'Faculty of Engineering'],
                 'Oulu University of Applied Sciences': ['Faculty of Education',
                                                         'Faculty of Medicine',
                                                         'Faculty of Science', 'Faculty of Engineering',
                                                         'Faculty of Economics'],
                 'University of Lapland': ['Faculty of Arts', 'Faculty of Education',
                                           'Faculty of Law', 'Faculty of Social Sciences'],
                 'Lapland University of Applied Sciences': ['Faculty of Social Sciences',
                                                            'Faculty of Engineering',
                                                            'Faculty of Computer Engineering and Software']}

    programs = {'University of Helsinki': ['Magistracy', 'Undergraduate'],
                'Hanken School of Economics': ['Magistracy', 'Undergraduate'],
                'University of Turku': ['Magistracy', 'Undergraduate'],
                'Abo Akademi University': ['Foundation', 'Undergraduate', 'MBA'],
                'University of Tampere': ['Magistracy', 'Undergraduate'],
                'University of Oulu': ['Magistracy', 'Undergraduate'],
                'Oulu University of Applied Sciences': ['Magistracy', 'Undergraduate'],
                'University of Lapland': ['Magistracy', 'Undergraduate'],
                'Lapland University of Applied Sciences': ['Magistracy', 'Undergraduate', 'MBA']}
    links = {'University of Helsinki': 'https://www.helsinki.fi/en',
             'Hanken School of Economics': 'https://www.hanken.fi/en',
             'University of Turku': 'https://www.utu.fi/en',
             'Abo Akademi University': 'https://www.abo.fi/en/',
             'University of Tampere': 'https://www.tuni.fi/en',
             'University of Oulu': 'https://www.oulu.fi',
             'Oulu University of Applied Sciences': 'https://www.oamk.fi',
             'University of Lapland': 'https://www.ulapland.fi',
             'Lapland University of Applied Sciences': 'https://www.lapinamk.fi'}

    images = {
        'University of Helsinki': 'https://www.helsinki.fi/assets/drupal/styles/og_images/s3/media-image/we-stand-with-ukraine_0.jpg?itok=xwhNgkys',
        'Hanken School of Economics': 'https://upload.wikimedia.org/wikipedia/commons/f/fb/Svenska_Handelsh%C3%B6gskolan_Helsingfors.jpg',
        'University of Turku': 'https://www.turku.fi/sites/default/files/thumbnails/image/turun-yliopisto-paarakennus.jpg',
        'Abo Akademi University': 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/64/%C3%85bo_Akademi_main_building.jpg/1200px-%C3%85bo_Akademi_main_building.jpg',
        'University of Tampere': 'https://smapse.ru/storage/2020/05/1-85.jpg',
        'University of Oulu': 'https://smapse.com/storage/2021/02/converted/825_585_9054-hires.jpg',
        'Oulu University of Applied Sciences': 'https://trail.fi/static/f02d0baec78d366d4807f38534d847b0/OAMK_kampus_722A1206_kuvaaja_Antti_J_Leinonen.jpg',
        'University of Lapland': 'https://eddanorden.files.wordpress.com/2015/03/university_of_lapland3.jpg',
        'Lapland University of Applied Sciences': 'https://www.edunation.co/wp-content/uploads/2022/01/Rovaniemi-Campus.jpg'}
    # общага
    hostel = {'University of Helsinki': 'Yes',
              'Hanken School of Economics': 'Yes',
              'University of Turku': 'Yes',
              'Abo Akademi University': 'Yes',
              'University of Tampere': 'Yes',
              'University of Oulu': 'No',
              'Oulu University of Applied Sciences': 'No',
              'University of Lapland': 'No',
              'Lapland University of Applied Sciences': 'Yes'}
    # стипендия
    scolarship = {'University of Helsinki': 'Yes',
                  'Hanken School of Economics': 'Yes',
                  'University of Turku': 'Yes',
                  'Abo Akademi University': 'Yes',
                  'University of Tampere': 'Yes',
                  'University of Oulu': 'Yes',
                  'Oulu University of Applied Sciences': 'Yes',
                  'University of Lapland': 'Yes',
                  'Lapland University of Applied Sciences': 'Yes'
                  }
    # требования к поступлению
    requirements = {
        'University of Helsinki': 'To enter the University of Helsinki, you must submit a document confirming your education (diploma or certificate). '
                                  'Along with the application for admission, it is necessary to send a motivation letter, resume and letters of recommendation from the previous place of study.',
        'Hanken School of Economics': 'the applicant must provide information about previous academic performance and passed exams',
        'University of Turku': 'For admission to the bachelors degree, you must provide a school leaving certificate and pass an exam in Finnish',
        'Abo Akademi University': 'the applicant must provide information about previous academic performance and passed exams',
        'University of Tampere': 'the applicant must provide information about previous academic performance and passed exams',
        'University of Oulu': 'To enter the University of Oulu, a Russian applicant must provide the original diploma and transcript or school certificate.',
        'Oulu University of Applied Sciences': 'Fill out an online application. Provide educational documents. Pass the entrance exams. Write a resume and a motivation letter (masters degree).',
        'University of Lapland': 'the applicant must provide information about previous academic performance and passed exams',
        'Lapland University of Applied Sciences': 'the applicant must provide information about previous academic performance and passed exams'
    }

    costs = {'University of Helsinki': 1500,
             'Hanken School of Economics': 1100,
             'University of Turku': 1500,
             'Abo Akademi University': 10000,
             'University of Tampere': 3000,
             'University of Oulu': 1100,
             'Oulu University of Applied Sciences': 1000,
             'University of Lapland': 1000,
             'Lapland University of Applied Sciences': 1000
             }

    sights = {'Senate Square and Cathedral (Helsinki)': [
        "The main square of the country's capital. Three buildings form the basis of the architectural ensemble of the square. One of them is the building of the State Council, on its facade there is the oldest clock in Finland. Nearby is the building of the University of Helsinki and its library. Above them rises the Cathedral. Snow-white walls, five green domes and 12 statues of the apostles on the roof make the cathedral majestic and solemn.",
        'https://top10.travel/wp-content/uploads/2015/05/senatskaya-ploshchad-1.jpg'],
        'Esplanade Park (Helsinki)': [
            "The park is 400 meters long, with lime trees planted around the perimeter. Founded in the 1830s. The undoubted decoration of the park are beautifully decorated luxurious flower beds. The park contains many monuments to famous and historical figures. Cultural entertainment is represented by the Swedish Theatre, as well as one of the oldest restaurants, Kappeli. Artists of various genres perform daily on its stage.",
            'https://top10.travel/wp-content/uploads/2015/05/park-esplanadi.jpg'],
        'Sveaborg Fortress (Helsinki)': [
            "The impregnable bastions of the walled city of Sveaborg are located on rocky islands near Helsinki. This place is under the protection of UNESCO. The fortress houses a large number of museums of various subjects - a military museum, a customs museum, a weapons museum, a toy museum. Guided tours of the submarine, which participated in the Second World War. On two islands, you can see the remains of military fortifications.",
            'https://top10.travel/wp-content/uploads/2015/05/krepost-sveaborg-1.jpg']}
    beaches = {'Hietaniemi': [
        "Hietaniemi Beach is one of the most popular Finnish beaches among vacationers. A special attraction, along with a long sandy shore, is given by its convenient location right in the center of Helsinki, in the Töölö area, and easy accessibility. It is curious that the beach was created artificially at the beginning of the 20th century, in the place where the sand unloaded from barges was originally stored. Now it is a popular holiday destination, which the Finns themselves call Hietsu, which means “fine sandy”.",
        'https://1001beach.ru/img/posts/1995/750/hietaniemi-1.webp?t=1580386695'],
        "Yuyuteri": [
            "Yyteri Beach is the most picturesque sandy beach in Western Finland. It is located in the resort of the same name, about 17 km from the center of Pori. Incredible white sand dunes, surf-friendly waves and an easy-to-reach location have made this coast one of the northern country's most popular beach destinations.",
            'https://1001beach.ru/img/posts/1996/750/yyteri-1.webp?t=1580386702'],
        'Nallikari': [
            "A well-developed beach near the village called Hietasaari. You can get to the place by buses that run monthly, or by a trackless train, but only in summer. The beach covers an area of almost half a kilometer, is considered public and free.",
            'https://1001beach.ru/img/posts/1982/750/nallikari-1.webp?t=1580386616']}
    mountains = {'Kovddoskaisi': [
        "It is considered one of the most dangerous and its height is 1242 m. It is the fourth highest mountain in Finland, but only experienced climbers can climb it, as it may not be safe for amateurs.",
        'https://fin-ware.ru/wp-content/uploads/2021/09/gori_finland_5.jpg'],
        'Aavasaksa': [
            "Mount Aavasaksa is located in Lapland, Finland. It is considered the southernmost point of the country. Its height is 242 meters. The mountain is included in the list of National Heritage, in 1876 it was visited by Emperor Alexander II. At the top of the mountain, for a long time, a cafe famous throughout the district worked, the decor of which was hunting trophies.",
            'http://openarium.ru/foto/IyXgHiijsF60Lm.jpg'],
        'Aakenustunturi': [
            "Mount Aakenustunturi is located in Lapland, Finland. Its height is 570 meters. Not far from the mountain is the resort of Kittila, popular among skiers, and Mount Ylläs, whose height is 719 meters.",
            'http://openarium.ru/foto/3zL8f6cF51fC5s.jpg']}
    skiResorts = {'Levi': [
        "The ski resort Levi (hereinafter in Finnish - Levi) is a great example of the fact that for winter adventures it is not necessary to fly to the Alps or the Tatras. Unforgettable impressions can be obtained right here at the northern neighbors. There are 27 ski lifts, 42 ski slopes, a snow park and 7 cafes, cross-country trails, trails for snowshoe hikers and snowmobile trails.",
        'https://ee.tallink.com/documents/10192/31064102/southpointlevi-soome-suusatama.jpg/6ba4e21f-b360-612b-099e-852572ab3a1a?t=1547109046874'],
        'Ylläs': [
            "The ski resort of Ylläs, about 1,000 kilometers from Helsinki, in Lapland, is a wonderfully peaceful place. If queues for lifts have long been a characteristic feature of large resorts, then in Ylläs on 63 slopes with 28 lifts there is enough space for everyone. The length of the longest route is as much as 3 kilometers. If you are going to Ylläs with the whole family, it is worth making a stop in Rovaniemi along the way, where the Finnish Santa Claus lives.",
            'https://ee.tallink.com/documents/10192/31064102/yllas-suusakeskus-soomes.jpg/97172ad8-7a1a-d7ec-041a-4725beff08cd?t=1547109668375'],
        'Tahko': [
            "Tahko, located about 450 kilometers from Helsinki, is a well-known ski resort with 32 slopes and 21 ski lifts. The length of one of the slopes exceeds one kilometer. For lovers of extreme sports, a recently renovated snow park and trick area (Jukulautastriitti) with various rails and jumps are open.",
            'https://ee.tallink.com/documents/10192/31064102/tahko-suusakeskus-soomes.jpg/c545aaa5-13f0-72d2-a363-1a7649bdaae3?t=1547110340898']}
    lakes = {'saima': [
        "The largest lake in Finland, also one of the four largest lakes in Europe. Its mascot and symbol is the seal, the Saimaa seal. The Finns carefully guard the declining population of this rare freshwater seal (they resemble, by the way, the Baikal seals). Neat safaris are organized for tourists on the lake to observe the seals from a safe distance, and in 2018, WWF launched live broadcasts from their rookeries (permissions for filming were hardly taken from them). In winter, they go skating right on the lake, ride reindeer sleds, and fish.",
        'https://cdn2.tu-tu.ru/image/pagetree_node_data/1/28451c14dd79fc8c291ac51133df4cac/'],
        'Päijanne': [
            "The second largest Finnish lake is also very deep - up to 95 meters. This does not prevent it from completely freezing in winter, so since December it has already been full of skaters and skiers. There are almost 2 thousand islands of different sizes in this lake - it's very beautiful. In addition to being part of a national park, the lake is also connected to Helsinki by an underground aqueduct. But there are also many old nice cities around the lake that are worth visiting, for example, after drinking a different drink in each: Lahti, Sysmä, Muurame, Luhanka, Assikkala, Padasjoki.",
            'https://cdn2.tu-tu.ru/image/pagetree_node_data/1/5089ac33276d621308e56c7c17fdf058/'],
        'Oulujärvi': [
            "This shallow, only 7 meters, lake is located almost in the center of Finland. Thanks to this shallow depth, it warms up, and thanks to the swamps around it, it fills with nutritious brown water, where many species of fish live and thrive - even pike fishing competitions take place here. There are also several hundred islands here, the largest of which have accommodations.",
            'https://cdn2.tu-tu.ru/image/pagetree_node_data/1/19bb45ea6b7895269742d8339e57b3b9/']}
    rivers = {'Muonioelven': [
        "Muonioelven is a river in the north of Sweden and Finland, the largest tributary of the Turneelven River. Both rivers together form the state border between the two countries.",
        'https://waterresources.ru/wp-content/uploads/2020/08/muonioelven.jpg'],
        'Turneelven': [
            "Turneelven (Turne-elv) is a river in the north of Sweden and Finland. The basin area is 40.2 thousand km². Average water consumption - 380 m³ / s",
            'https://waterresources.ru/wp-content/uploads/2020/08/turneelven-1-2048x1536.jpg'],
        'Velikaya (river, flows into the Gulf of Finland)': [
            "Great (Vilajoki) and Russia. It flows into the Baltiets Bay of the Gulf of Finland. The catchment area is 344 km², of which 73.4% in Finland and 26.6% in Russia. The length of the Russian part of the river is 20 km.",
            'https://waterresources.ru/wp-content/uploads/2020/08/velikaya-reka-vpadaet-v-finskij-zaliv.jpg']}

    # currency
    currencyName = 'FIM'
    currencyEqualsToDollar = 5.73

    # military
    milPolBlock = "Finnish Defense Forces"
    amountOfPeopleInArmy = 23800

    # healthcare
    numberOfDoctorsPer100kPopulation = 302
    menAverageLifeExpectancy = 79.2  # years
    womenAverageLifeExpectancy = 84.0  # years

    # climat
    juneAverageTemperature = 22  # °C
    decemberAverageTemperature = -6  # °C
    averageHumidity = 77  # %
    averageDurationOfWinter = 5  # month
    averageRainfallPerMonth = 80  # mm (?)
    averageNumberOfFoggyDaysPerYear = 82  # days
    averageNumberOfRainyDaysPerYear = 139  # days
    averageNumberOfClearDays = 144  # days

    # security
    situationInTheCountry = 2  # [1, 3] 1-bad, 3-good
    freedomOfSpeech = 3  # [1, 3]
    assessmentOfFamilyLife = 2  # [1, 3]
    attitudeTowardsLGBT = 3  # [1, 3]

    # population
    populationCount = 5_542_000
    procentOfMales = 49
    procentOfFemales = 51
    populationDensityPerSquareKilometer = 18
    speedOfLife = 3  # [1, 3]
    workPlaces = 3  # [1, 3]
    nightLifeEntertainment = 2  # [1, 3]

    # citizenship
    citizenshipGlobalRank = 2
    friendlyToForeigners = 0

    # communication
    communicationOnEnglish = 3  # [1, 3]

    # transport
    averageTravelTimeToWork = 45
    developmentLevelOfPublicTransport = 2  # [1, 3]

    # internet
    speedOfInternetMbps = 79.40  # Мегабиты в секунду
    freeWifi = 2  # [1, 3]

    # education
    rankingOfNationalEducationSystem = 8

    cc.createBase(countryName, cities, officialLanguage,
                  # currency
                  currencyName, currencyEqualsToDollar,
                  # military
                  milPolBlock, amountOfPeopleInArmy,
                  # healthcare
                  numberOfDoctorsPer100kPopulation, menAverageLifeExpectancy, womenAverageLifeExpectancy,
                  # climat
                  juneAverageTemperature, decemberAverageTemperature, averageHumidity,
                  averageDurationOfWinter, averageRainfallPerMonth, averageNumberOfFoggyDaysPerYear,
                  averageNumberOfRainyDaysPerYear, averageNumberOfClearDays,
                  # security
                  situationInTheCountry, freedomOfSpeech,
                  assessmentOfFamilyLife, attitudeTowardsLGBT,
                  # population
                  populationCount, procentOfMales, procentOfFemales, populationDensityPerSquareKilometer,
                  speedOfLife, workPlaces, nightLifeEntertainment,
                  # citizenship
                  citizenshipGlobalRank,
                  # communication
                  communicationOnEnglish,
                  # transport
                  averageTravelTimeToWork, developmentLevelOfPublicTransport,
                  # internet
                  speedOfInternetMbps, freeWifi,
                  # education
                  rankingOfNationalEducationSystem, universities, faculties, programs, costs, links, images,
                  requirements,
                  hostel, scolarship, sights, beaches, mountains, skiResorts, lakes, rivers, friendlyToForeigners
                  )
    # cc.createManMadeDisaster(countryName, nameMMD, typeOfMMD, aomuntOfDeadPeople,
    #                           aomuntOfInjuredPeople, territoryOfPollution)
    # cc.createOceans()

    #############################   FINLAND   #############################

    #############################   NORWAY   #############################

    # Country
    countryName = "Norway"
    officialLanguage = "Norwegian"

    # cities     name      isBig WashesBy
    cities = {'Oslo': [True, True, None], 'Drammen': [True, True, None], 'Bergen': [True, True, "Northern ocean"],
              'Trondheim': [True, True, "Trondheimsfjorden"], 'Stavanger': [True, True, "Northern ocean"]}

    # education
    universities = {'Oslo': ['University of Oslo', 'Oslo Metropolitan University'],
                    'Bergen': ['University of Bergen', 'Norwegian School of Economics'],
                    'Trondheim': ['Norwegian University of Science and Technology'],
                    'Stavanger': ['University of Stavanger']}
    faculties = {'University of Oslo': ['Faculty of Medicine', 'Faculty of Education', 'Faculty of Social Sciences',
                                        'Faculty of Engineering', 'Faculty of Arts'],
                 'Oslo Metropolitan University': ['Faculty of Medicine', 'Faculty of Education',
                                                  'Faculty of Social Sciences',
                                                  'Faculty of Engineering', 'Faculty of Arts'],
                 'University of Bergen': ['Faculty of Arts',
                                          'Faculty of Education', 'Faculty of Law', 'Faculty of Science',
                                          'Faculty of Medicine', 'Faculty of Social Sciences'],
                 'Norwegian School of Economics': ['Faculty of Economics',
                                                   'Faculty of Social Science'],
                 'Norwegian University of Science and Technology': ['Faculty of Architecture', 'Faculty of Arts',
                                                                    'Faculty of Education',
                                                                    'Faculty of Computer Engineering and Software',
                                                                    'Faculty of Engineering',
                                                                    'Faculty of Medicine'],
                 'University of Stavanger': ['Faculty of Arts', 'Faculty of Education', 'Faculty of Science',
                                             'Faculty of Engineering', 'Faculty of Medicine']}

    programs = {'University of Oslo': ['Magistracy', 'Undergraduate', 'MBA'],
                'Oslo Metropolitan University': ['Magistracy', 'Undergraduate'],
                'University of Bergen': ['Foundation', 'Undergraduate', 'MBA'],
                'Norwegian School of Economics': ['Magistracy', 'Undergraduate'],
                'Norwegian University of Science and Technology': ['Magistracy', 'Undergraduate'],
                'University of Stavanger': ['Magistracy', 'Undergraduate']}
    links = {'University of Oslo': 'https://www.uio.no/english/',
             'Oslo Metropolitan University': 'https://www.oslomet.no/en/',
             'University of Bergen': 'https://www.uib.no/en',
             'Norwegian School of Economics': 'https://www.nhh.no/en/',
             'Norwegian University of Science and Technology': 'https://www.ntnu.edu/',
             'University of Stavanger': 'https://www.uis.no/en'}

    images = {
        'University of Oslo': 'https://study-eu.s3.amazonaws.com/uploads/image/path/90/wide_fullhd_university-of-oslo.jpg',
        'Oslo Metropolitan University': 'https://www.oslomet.no/var/oslomet/storage/images/5/5/1/9/119155-2-eng-GB/P35-2400-1200.jpg',
        'University of Bergen': 'http://univero.cc/public/media/university/imgs/2/02268120008aauj2nEED4_R_550_412_R5.png',
        'Norwegian School of Economics': 'https://ap-production-media-archive.s3.eu-north-1.amazonaws.com/uploads/6iXnN53VwnoxQyMlmxQnoQsobID0SRdCXfhEj9zu.jpg',
        'Norwegian University of Science and Technology': 'https://www.lifeinnorway.net/wp-content/uploads/2021/07/ntnu-trondheim-main-building.jpg',
        'University of Stavanger': 'https://www.uis.no/sites/default/files/styles/gutenberg_align_left/public/2021-12/Semsterstart%202021%20EOJ%20plen%202_0.jpg'}
    # общага
    hostel = {'University of Oslo': 'Yes',
              'Oslo Metropolitan University': 'Yes',
              'University of Bergen': 'Yes',
              'Norwegian School of Economics': 'No',
              'Norwegian University of Science and Technology': 'Yes',
              'University of Stavanger': 'No'}
    # стипендия
    scolarship = {'University of Oslo': 'Yes',
                  'Oslo Metropolitan University': 'Yes',
                  'University of Bergen': 'Yes',
                  'Norwegian School of Economics': 'No',
                  'Norwegian University of Science and Technology': 'Yes',
                  'University of Stavanger': 'Yes'
                  }
    # требования к поступлению
    requirements = {'University of Oslo': 'exams in Norwegian. the minimum results should be as follows: '
                                          'PTE Academic - 62;'
                                          'TOEFL - 90;'
                                          'IELTS - 6.5.',
                    'Oslo Metropolitan University': 'Confirm knowledge of Norwegian, you need to pass all parts of the Bergentest at the B2 + level or the language test at the university at the C + mark',
                    'University of Bergen': 'a high level of previous academic achievement and a language proficiency certificate are required',
                    'Norwegian School of Economics': 'The admission committee makes admission to the university based on the applicants performance and the results of the exams passed',
                    'Norwegian University of Science and Technology': 'provide a certificate or diploma of previously received education. Documents must be officially translated into English, Norwegian or another Scandinavian language.',
                    'University of Stavanger': 'higher specialized education, resume, letter of intent, TOEFL 80, IELTS 6.0.'
                    }

    costs = {'University of Oslo': 73,
             'Oslo Metropolitan University': 9000,
             'University of Bergen': 700,
             'Norwegian School of Economics': 800,
             'Norwegian University of Science and Technology': 500,
             'University of Stavanger': 100}

    sights = {'Geirangerfjord': [
        "It is unlikely that you will remain indifferent if you see this creation of nature with your own eyes. We are talking about a small, but with a magnificent landscape, a fjord. Its length is 20 km, but this does not prevent it from being the most visited. Assessing all the sights of Norway, seasoned tourists put in the first place exactly the deep-water emerald sea bay with rocky shores. If your soul craves entertainment, you can fish, go kayaking, try rafting. It also offers horseback riding and even in the summer you can go skiing.",
        'https://www.tripzaza.com/ru/destinations/wp-content/uploads/2018/02/1-Geiranger_Fjord-e1518234899683.jpg'],
        'Roros': [
            "Numerous positive reviews has one of the UNESCO sites. In the past, it was a city where copper ore miners lived, now this place is associated with tourism. From the history of the sights of Norway, it is known that the city was designed and built by King Christian IV, he was an architect. In the period 1678-1718. the settlement was attacked by the Swedes, they burned it, but the life of the city did not end there. Over time, it was restored, today every tourist can appreciate the splendor of the restored living open-air museum.",
            'https://www.tripzaza.com/ru/destinations/wp-content/uploads/2018/02/2-Roros-e1518235473603.jpg'],
        'Vöringsfossen': [
            "The Hardangerfjord contains the sights of Norway, and more than one. Among them, the famous waterfall far beyond the borders of the country deserves special attention. It is located in the county of Hordaland, its height is 182 m. The official description of this place says that there is an observation deck nearby, from which you can clearly see the waterfall and the often appearing rainbow.",
            'https://www.tripzaza.com/ru/destinations/wp-content/uploads/2018/02/3-Voringsfossen-e1518236720135.jpg']}
    beaches = {'Godalen': ["Godalen is the number one beach area for swimmers and picnic lovers.",
                           'https://1001beach.ru/img/posts/2473/750/godalen-1.webp?t=1580389144'],
               "Sellesanden": [
                   "On the west coast of Norway, there is the romantic town of Selje. One of the secrets of its attraction is a wonderful beach called Sellesanden. It is incredibly popular with tourists.",
                   'https://1001beach.ru/img/posts/2474/750/seljesanden-1.webp?t=1580389149'],
               'Hellest': ["Hellest Beach is located in the southwestern region of Norway, Rogaland.",
                           'https://1001beach.ru/img/posts/2477/750/uttakleiv-1.webp?t=1580389167']}
    mountains = {'Hardangervidda': [
        "This is the largest high-altitude European plateau with an area of 8 thousand km2. The first mountains appeared here 5 million years ago, and the current ridges were fixed in the last 10 thousand years. A lot of glaciers have been preserved here, for example, Hardangerjokulen (the largest), Solfonn, Napsfonn. The decoration is a hat-shaped mountain - Horteigen. The largest peaks reach 1.6 thousand meters above the sea in the south and west of the plateau. Several small rivers and waterfalls flow here.",
        'https://сезоны-года.рф/sites/default/files/resize/images/okruzhayushhij_mir/Norway_gory_1-500x375.jpg'],
        'Lyngsalpene': [
            "This array of mountains, only 300 km from the Arctic Circle, is distinguished by very harsh climatic conditions. There are peaks under a thousand meters, as well as gorges, glaciers and reservoirs. Mount Sturgalten, 1200 meters high, is popular among athletes and winter lovers.",
            'https://сезоны-года.рф/sites/default/files/resize/images/okruzhayushhij_mir/Norway_gory_2-500x332.jpg'],
        'Sunnmør Alps': [
            "Tourism activities are also developed in these mountainous regions. Climbing Mount Slogen, whose height is one and a half thousand meters above sea level, is especially in demand.",
            'https://сезоны-года.рф/sites/default/files/resize/images/okruzhayushhij_mir/Norway_gory_3-500x333.jpg']}
    skiResorts = {'Hemsedal': [
        "Hemsedal is located in a picturesque area called the 'Scandinavian Alps' and located halfway between the two largest cities in the country - Oslo and Bergen. This resort is well-deservedly popular among both Norwegians and foreign tourists. Whole companies or families usually come here, since Hemsedal has excellent conditions not only for skiing, but also for additional recreation.",
        'https://guide-tours.ru/wp-content/uploads/2021/11/hemsedal-gornolyzhnyj-kurort.jpg'],
        'Trysil': [
            "Trysil is a winter resort located 160 km from the Norwegian capital, near the border with Sweden. It is great for a family holiday, as there are a large number of tracks for children and beginners, a high level of infrastructure and service. The tracks in Trysil are located on the slopes of Trysilfjellet, which towers over the area by 1.1 km. The slopes and the surrounding area are covered with coniferous forests, which gives the local air a healing effect.",
            'https://guide-tours.ru/wp-content/uploads/2021/11/trjusil-gornolyzhnyj-kurort.jpg'],
        'Voss': [
            "Voss is a ski center in the western part of Norway, near the Oslo-Bergen highway. The slopes on which the downhill slopes are equipped are located in close proximity to the railway station, so that tourists, leaving the car, immediately enter the territory of the ski resort. On the slopes of a nearby mountain, 24 tracks are equipped, of which 14 are for alpine skiing, and the rest for snowboarding, freestyle, slalom",
            'https://guide-tours.ru/wp-content/uploads/2021/11/voss-gornolyzhnyj-kurort.jpg']}
    lakes = {'Bondhus': [
        "Bondhus is rightfully considered the most beautiful Norwegian lake. This picturesque reservoir of glacial origin is located in the Folgefonna nature reserve. The lake is formed by the melt waters of the glacier of the same name, which tourists can also see. The path to the valley where Bondhus is located lies in the middle of a protected forest of extraordinary beauty. Surrounded by forested mountains, the lake is the best place for a romantic photo shoot. Literally every frame from here is a real magazine shot.",
        'https://mirsg.ru/shared/upload/IMAGES/Articles/Lakes/2.jpg'],
        'Myosa': [
            "Mjøsa is the largest lake in Norway. The lake is located in three local provinces at once - Hedmark, Oppland and Akershus; By the way, it is on the banks of the Mjøsa that the famous Norwegian town of Lillehammer is located. It is a resort town that hosted the 1994 Winter Olympics. Mjøsa is also included in the list of the deepest lakes in Norway. Its depth is 449 meters.",
            'https://mirsg.ru/shared/upload/IMAGES/Articles/Lakes/3.jpg'],
        'Hornindalsvatnet': [
            "Hornindalsvatnet is the Norwegian deepest lake record holder. In this case, the depth of the lake is 514 meters, and this fact allows the reservoir to rightfully be considered the deepest lake not only in Norway, but throughout Europe.",
            'https://mirsg.ru/shared/upload/IMAGES/Articles/Lakes/4-1.jpg']}
    rivers = {'Lakselv': [
        "flows in the Finnmark region. Its name in translation means 'Salmon River'. It is most convenient for fly fishing, due to the lack of dense vegetation along the banks and the many bends at the confluence of the river into the Pursangenfjord. Salmon begin to enter Lakselv around mid-July, so August is considered the best time for fishing.",
        'https://dynamic-media-cdn.tripadvisor.com/media/photo-o/07/1c/b4/85/stabbursdalen-lodge.jpg?w=500&h=300&s=1'],
        'Gaula': [
            "Gaula (Gaula) in the Trondelag region is considered one of the best salmon rivers in Europe for sport fishing. It belongs to the Trondheimfjord basin and is known for both large salmon and its large numbers.",
            'https://thumbs.dreamstime.com/z/%D1%80%D0%B5%D0%BA%D0%B0-gaula-%D0%BD%D0%BE%D1%80%D0%B2%D0%B5%D0%B3%D0%B8%D1%8F-127315808.jpg'],
        'Namsen': [
            "Namsen in Trondelag, where the beginning of fishing was laid by the English lords who came here in the 1850s. They also invented the most popular method of fishing on the river at present - harling.",
            'https://upload.wikimedia.org/wikipedia/commons/a/a3/Namsen_sett_fra_Kvatningenfjell%2C_Namsos_i_bakgrunnen.jpg']}

    # currency
    currencyName = 'NOK'
    currencyEqualsToDollar = 10.14

    # military
    milPolBlock = "NATO"
    amountOfPeopleInArmy = 29000

    # healthcare
    numberOfDoctorsPer100kPopulation = 442
    menAverageLifeExpectancy = 81.1  # years
    womenAverageLifeExpectancy = 84.1  # years

    # climat
    juneAverageTemperature = 20  # °C
    decemberAverageTemperature = -3  # °C
    averageHumidity = 77  # %
    averageDurationOfWinter = 3.3  # month
    averageRainfallPerMonth = 73  # mm (?)
    averageNumberOfFoggyDaysPerYear = 65  # days
    averageNumberOfRainyDaysPerYear = 133  # days
    averageNumberOfClearDays = 167  # days

    # security
    situationInTheCountry = 2  # [1, 3] 1-bad, 3-good
    freedomOfSpeech = 3  # [1, 3]
    assessmentOfFamilyLife = 3  # [1, 3]
    attitudeTowardsLGBT = 3  # [1, 3]

    # population
    populationCount = 5_408_000
    procentOfMales = 50.57
    procentOfFemales = 49.43
    populationDensityPerSquareKilometer = 15
    speedOfLife = 3  # [1, 3]
    workPlaces = 3  # [1, 3]
    nightLifeEntertainment = 2  # [1, 3]

    # citizenship
    citizenshipGlobalRank = 3
    friendlyToForeigners = 0

    # communication
    communicationOnEnglish = 3  # [1, 3]

    # transport
    averageTravelTimeToWork = 70
    developmentLevelOfPublicTransport = 2  # [1, 3]

    # internet
    speedOfInternetMbps = 23.5  # Мегабиты в секунду
    freeWifi = 1  # [1, 3]

    # education
    rankingOfNationalEducationSystem = 11

    cc.createBase(countryName, cities, officialLanguage,
                  # currency
                  currencyName, currencyEqualsToDollar,
                  # military
                  milPolBlock, amountOfPeopleInArmy,
                  # healthcare
                  numberOfDoctorsPer100kPopulation, menAverageLifeExpectancy, womenAverageLifeExpectancy,
                  # climat
                  juneAverageTemperature, decemberAverageTemperature, averageHumidity,
                  averageDurationOfWinter, averageRainfallPerMonth, averageNumberOfFoggyDaysPerYear,
                  averageNumberOfRainyDaysPerYear, averageNumberOfClearDays,
                  # security
                  situationInTheCountry, freedomOfSpeech,
                  assessmentOfFamilyLife, attitudeTowardsLGBT,
                  # population
                  populationCount, procentOfMales, procentOfFemales, populationDensityPerSquareKilometer,
                  speedOfLife, workPlaces, nightLifeEntertainment,
                  # citizenship
                  citizenshipGlobalRank,
                  # communication
                  communicationOnEnglish,
                  # transport
                  averageTravelTimeToWork, developmentLevelOfPublicTransport,
                  # internet
                  speedOfInternetMbps, freeWifi,
                  # education
                  rankingOfNationalEducationSystem, universities, faculties, programs, costs, links, images,
                  requirements,
                  hostel, scolarship, sights, beaches, mountains, skiResorts, lakes, rivers, friendlyToForeigners
                  )
    # cc.createManMadeDisaster(countryName, nameMMD, typeOfMMD, aomuntOfDeadPeople,
    #                           aomuntOfInjuredPeople, territoryOfPollution)
    # cc.createOceans()

    #############################   NORWAY   #############################

    #############################   SWEDEN   #############################

    # Country
    countryName = "Sweden"
    officialLanguage = "Swedish"

    # cities     name      isBig WashesBy
    cities = {'Stockholm': [True, True, "Baltic Sea"], 'Orebro': [True, True, None], 'Linkoping': [True, True, None],
              'Jonkoping': [True, True, "Vättern"], 'Goteborg': [True, True, "Kattegat"]}

    # education
    universities = {'Stockholm': ['Karolinska Institute', 'Stockholm University'],
                    'Orebro': ['Orebro University'],
                    'Linkoping': ['Linkoping University'],
                    'Jonkoping': ['Jonkoping University'],
                    'Goteborg': ['University of Gothenburg', 'Chalmers University of Technology']}
    faculties = {'Karolinska Institute': ['Faculty of Medicine',
                                          'Faculty of Science', 'Faculty of Social Sciences'],
                 'Stockholm University': ['Faculty of Education', 'Faculty of Law', 'Faculty of Social Sciences',
                                          'Faculty of Science'],
                 'Orebro University': ['Faculty of Economics', 'Faculty of Science', 'Faculty of Engineering',
                                       'Faculty of Education', 'Faculty of Social Sciences', 'Faculty of Medicine'],
                 'Linkoping University': ['Faculty of Arts', 'Faculty of Science', 'Faculty of Education',
                                          'Faculty of Medicine', 'Faculty of Science',
                                          'Faculty of Engineering'],
                 'Jonkoping University': ['Faculty of Computer Engineering and Software', 'Faculty of Engineering',
                                          'Faculty of Science'],
                 'University of Gothenburg': ['Faculty of Computer Engineering and Software',
                                              'Faculty of Education',
                                              'Faculty of Arts', 'Faculty of Science', 'Faculty of Social Sciences'],
                 'Chalmers University of Technology': ['Faculty of Architecture',
                                                       'Faculty of Computer Engineering and Software',
                                                       'Faculty of Social Sciences',
                                                       'Faculty of Engineering']}
    programs = {'Karolinska Institute': ['Magistracy', 'Undergraduate'],
                'Stockholm University': ['Magistracy', 'Undergraduate', 'MBA'],
                'Orebro University': ['Magistracy', 'Undergraduate'],
                'Linkoping University': ['Foundation', 'Undergraduate', 'MBA'],
                'Jonkoping University': ['Magistracy', 'Undergraduate'],
                'University of Gothenburg': ['Magistracy', 'Undergraduate', 'MBA'],
                'Chalmers University of Technology': ['Magistracy', 'Undergraduate']}
    links = {'Karolinska Institute': 'https://ki.se/en',
             'Stockholm University': 'https://www.su.se/cmlink/stockholm-university',
             'Orebro University': 'https://www.oru.se/english/',
             'Linkoping University': 'https://liu.se/en',
             'Jonkoping University': 'https://ju.se/en',
             'University of Gothenburg': 'https://www.gu.se/en',
             'Chalmers University of Technology': 'https://www.chalmers.se/en/Pages/default.aspx'}

    images = {
        'Karolinska Institute': 'https://ehef.id/storage/app/uploads/public/5d1/9cc/ce3/5d19ccce38e24274187271.jpg',
        'Stockholm University': 'https://civis.eu/storage/files/atmosfar-miljo-webb-034.jpg',
        'Orebro University': 'https://www.oru.se/globalassets/oru-sv/om-universitetet/bilder/campus/campus-uso-mv.jpg?w=720',
        'Linkoping University': 'https://liu.se/dfsmedia/dd35e243dfb7406993c1815aaf88a675/35182-50065/campus-valla-vinterljus-20191202-liu-3678?as=1&w=640&h=360&cr=1&crw=640&crh=360&bc=%23ffffff',
        'Jonkoping University': 'https://study-eu.s3.amazonaws.com/uploads/image/path/689/wide_fullhd_jonkoping-university-sweden-patrik-svedberg-HLK-JIBS_STUD_130906-4131.jpg',
        'University of Gothenburg': 'https://www.gu.se/sites/default/files/styles/100_10_5_xlarge_1x/public/2019-11/Vasaparken-universitetets-huvudbyggnad.jpg?h=ba76c1ff&itok=83TrW1sU',
        'Chalmers University of Technology': 'https://smapse.com/storage/2020/11/chalmers-university-of-technology-smapse8.jpg'}
    # общага
    hostel = {'Karolinska Institute': 'Yes',
              'Stockholm University': 'Yes',
              'Orebro University': 'Yes',
              'Linkoping University': 'Yes',
              'Jonkoping University': 'Yes',
              'University of Gothenburg': 'No',
              'Chalmers University of Technology': 'No'}
    # стипендия
    scolarship = {'Karolinska Institute': 'Yes',
                  'Stockholm University': 'Yes',
                  'Orebro University': 'Yes',
                  'Linkoping University': 'Yes',
                  'Jonkoping University': 'Yes',
                  'University of Gothenburg': 'Yes',
                  'Chalmers University of Technology': 'Yes'
                  }
    # требования к поступлению
    requirements = {
        'Karolinska Institute': 'English proficiency at least 7.0 on the IELTS scale and an average score close to the maximum',
        'Stockholm University': 'English proficiency at least 7.0 on the IELTS scale and an average score close to the maximum',
        'Orebro University': 'It is noteworthy that the main factor in terms of recruiting students for a special admissions committee is considered to be the academic performance of each applicant.',
        'Linkoping University': 'Certificate of general secondary education with grades and a certified translation Confirmation of the study of mathematics Motivation letter IELTS or TOEFL certificate (IELTS not lower than 6.5).',
        'Jonkoping University': 'Certificate of general secondary education with grades and a certified translation Confirmation of the study of mathematics Motivation letter IELTS or TOEFL certificate (IELTS not lower than 6.5).',
        'University of Gothenburg': 'application for participation in the scholarship program; copy of the passport; summary; motivation letter (no more than 500 words); the title page of an application for one of the masters programs that was submitted on the site.',
        'Chalmers University of Technology': 'High School Diploma Swedish as a Second Language 3 Certificate English 6 Certificate.'}

    costs = {'Karolinska Institute': 4300,
             'Stockholm University': 11000,
             'Orebro University': 12000,
             'Linkoping University': 1300,
             'Jonkoping University': 8600,
             'University of Gothenburg': 900,
             'Chalmers University of Technology': 27000}

    sights = {'Wadsten Castle': [
        "It is worth starting acquaintance with an impressive reminder of the glorious history of the state. On its territory, the described fortress is one of the oldest, because it began to be built back in 1545. Not all tourists know that Vadsten Castle originally had 4 round towers, 3 residential buildings made of stone, and several outbuildings. At a certain point, the need for fortifications disappeared, so they were hidden. The decision to turn the building into a historical monument was made in the 20th century, for which large-scale restoration work was carried out.",
        'https://www.tripzaza.com/ru/destinations/wp-content/uploads/2018/02/1-The_Vadstena_castle-e1519091907580.jpg'],
        'Vasa Museum': [
            "The sights of Sweden cannot but surprise with their diversity and uniqueness. A vivid proof of this is the museum in the form of a ship, which has survived to this day from the 17th century. Until now, it is considered the pride of the Swedish navy. Presumably, he sank from the fact that not quite correct calculations were made, there were too many jewelry and gold. The ship ended up at the bottom of Stockholm harbor during its first voyage, which happened in 1628.",
            'https://www.tripzaza.com/ru/destinations/wp-content/uploads/2018/02/2-he_Vasa_Museum-e1519092120105.jpg'],
        'Old town Gamla Stan': [
            "Thinking about what to visit in Sweden? Take a look at the historical center of Stockholm, which until the 80s was called the City Between Bridges. It was founded back in the 13th century, which is easy to guess from its medieval paths, cobbled streets, houses in the North German Gothic style. In the very center there is a picturesque square known as Stortorget. In 1520, it was on it that the Danish king brutally cracked down on the Swedish nobles. Many more attractions in Sweden are concentrated in the Old Town of Gamla Stan.",
            'https://www.tripzaza.com/ru/destinations/wp-content/uploads/2018/02/3-Gamla_Stan-e1519092337257.jpg']}
    beaches = {'Ribersborg': [
        "Ribersborg beach is a popular holiday destination in Malmö at any time of the year in Sweden. The beach and coastal zone of the largest city surprises tourists not only with its history, but also with daily entertainment events along the entire coast of Öresund. The beach is so popular that locals and tourists recognize it even by other names - 'Ribban', as the people of Sweden call it, or 'Scandinavian Copacobana', this name is firmly entrenched in tourist publications.",
        'https://1001beach.ru/img/posts/1569/750/ribersborg_beach-1.webp?t=1580384392'],
        "Sandhammaren": [
            "Sandhammaren beach rightfully competes for the title of the best beach holiday destination in Sweden. Surprisingly warm sands and cool waters of the Baltic are located in the southeast of the country, in Osterlen. More precisely, the beach covers an area of several kilometers from the village of Löderups-Strandbad in the eastern part of the region to the famous Skåne province (southeastern part).",
            'https://1001beach.ru/img/posts/1570/750/sandhammaren_beach-1.webp?t=1580384406'],
        'Smedsuddsbadet': [
            "Despite the hard-to-pronounce name for tourists, this beach is considered one of the best in Sweden and regularly makes lists of the most popular places for summer holidays near the water. It is located directly in the capital of the country - Stockholm - in the Kungsholmen district, and it can be easily reached by taxi or get off at the Fridhemsplan metro station.",
            'https://1001beach.ru/img/posts/1730/750/smedsuddsbadet-1.webp?t=1580385208']}
    mountains = {'Kebnekaise': [
        "Kebnekaise is located in Lapland, about 150 km north of the Arctic Circle and west of Kiruna. The summit is composed of gabbro and quartz syenites. It has two peaks - the southern one, covered with a glacier, 2106 meters high, and the northern one, 2097 meters high.",
        'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b7/Duolbagorni.jpg/310px-Duolbagorni.jpg'],
        'Sarekchokko': [
            "It is located in the county of Norrbotten, in the Sarek National Park. The mountain is easy to climb, except for the north side. The most convenient route goes along the western ridge of the mountain. It is the second highest mountain in Sweden after Kebnekaise and the sixth in the Scandinavian Peninsula. For the first time, the Swede G.W. Bucht climbed the mountain on July 8, 1879 with 4 Saami guides. The first winter ascent took place in 1916.",
            'https://upload.wikimedia.org/wikipedia/commons/thumb/7/7c/Sarektj%C3%A5kko-fr%C3%A5n-ruotes-25.jpg/1200px-Sarektj%C3%A5kko-fr%C3%A5n-ruotes-25.jpg'],
        'Cascasapakte': [
            "Kaskasapakte is a mountain peak in Sweden, one of the highest in the country. The summit is located in the historic province of Lappland, northeast of Mount Kebnekaise, Sweden's highest peak. At the foot of Kaskasapakte is the glacial lake Tarfala.",
            'https://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/Tarfala.jpg/280px-Tarfala.jpg']}
    skiResorts = {'Ore': [
        "Åre is the largest ski center in Scandinavia, which has been recognized as the best in Sweden for several years in a row. It consists of four villages - Duved, Tegefjäll, Åre By and Åre Björnen. There are 89 ski slopes, 41 ski lifts, a trick park, slopes for children and beginner skiers, cross-country trails and 75 restaurants and cafes. The total length of the slopes is about 100 kilometers, and the longest of them is 6.5 kilometers. The highest point of the resort is at an altitude of 1274 meters above sea level.",
        'https://ee.tallink.com/documents/10192/31064102/are-suusakuurort-rootsis.jpg/4f7f35c8-b2f8-4c0b-aeea-809841f628de?t=1512466871125'],
        'Salen': [
            "Sälen is very popular among Swedes thanks in large part to its reputation as the best family ski resort in all of Sweden. In addition to skiing, there are many other interesting activities here. For example, you can combine your mountain ticket with the entrance ticket to the Experium water park and, after an active day on the slopes, relax in the jacuzzi or ride the water slides.",
            'https://ee.tallink.com/documents/10192/31064102/saleni-suusakuurort-rootsis.jpg/865f7785-9e09-4a00-b4e9-ef90a561d82d?t=1512466870999'],
        'Vemdalen': [
            "A small but quite comfortable ski center in Central Sweden. Vemdalen has four ski resorts: Björnrike, Klövsjö, Storhogna and Vemdalsskalet, as well as very picturesque nature. The snow cover here appears quite early, and the slopes open already in November. Pleasant atmosphere, groomed pistes and stable snow make Vemdalen one of the most popular ski resorts among Estonian tourists. In addition, it is not as far to get here as in Are.",
            'https://ee.tallink.com/documents/10192/31064102/vemdaleni-suusakuurort-rootsis.jpg/40258b1c-c41b-4278-bedb-1233b9101696?t=1512466871000']}
    lakes = {'Vättern': [
        "The total area of the lake is 1912 km², with a coastal zone - about 4503 km²; height above sea level is 88 m. The deepest point is located south of the island of Visingsö (Swedish Visingsö) and has a depth of 128 meters. The average depth of the lake is 40 meters. The length of the coastline is about 642 km. The volume is 74 km³, the water level in the lake is maintained by special equipment (previously, the water level often changed).",
        'https://waterresources.ru/wp-content/uploads/2020/09/vettern-2.jpg'],
        'Venern': [
            "Vänern is a lake in southern Sweden on the border of the counties of Västra Götaland and Värmland. Vänern is the largest lake in Sweden and Western Europe, and also the third largest in Europe after Lake Ladoga and Lake Onega.",
            'https://waterresources.ru/wp-content/uploads/2020/09/venern.jpg'],
        'Sommen': [
            "Sommen is a lake in southern Sweden. It is located in the historical province of Östergötland in the historical region of Götaland on the border with the province of Småland, 40 km east of Lake Vättern, the second largest lake in Sweden. The nearest city is Tranos.",
            'https://waterresources.ru/wp-content/uploads/2020/09/sommen-ozero.jpg']}
    rivers = {'Muonioelven': [
        "Muonioelven is a river in the north of Sweden and Finland, the largest tributary of the Turneelven River. Both rivers together form the state border between the two countries.",
        'https://waterresources.ru/wp-content/uploads/2020/08/muonioelven.jpg'],
        'Tourneelven': [
            "Tourne Elv originates from Lake Tourneträsk in the Scandinavian mountains in Sweden near the border with Norway and flows in a southeasterly direction through the Lapland plateau to the Gulf of Bothnia. After taking in the largest tributary, the Muonyoelven forms the border with Finland. The length of the river is 565 km (this is the hydrological length measured from the sources of Muonyoelven). In the upper reaches there are waterfalls, rapids and numerous lakes. Freezes from November to May.",
            'https://waterresources.ru/wp-content/uploads/2020/08/turneelven-1-2048x1536.jpg'],
        'Kalixelven': [
            "The length of the river is 460.65 km. The catchment area is 18.130 km². The average water consumption is 289 m³/s. Kalikselven originates on the slopes of Mount Kebnekaise and flows eastward to the Gulf of Bothnia. In the upper reaches there are waterfalls and numerous lakes. Freezes from November to May.",
            'https://waterresources.ru/wp-content/uploads/2020/08/kalikselven.jpg']}
    # currency
    currencyName = 'CHF'
    currencyEqualsToDollar = 0.95

    # military
    milPolBlock = "None"
    amountOfPeopleInArmy = 140304

    # healthcare
    numberOfDoctorsPer100kPopulation = 411
    menAverageLifeExpectancy = 80.8  # years
    womenAverageLifeExpectancy = 84.0  # years

    # climat
    juneAverageTemperature = 21  # °C
    decemberAverageTemperature = -2  # °C
    averageHumidity = 75  # %
    averageDurationOfWinter = 4.0  # month
    averageRainfallPerMonth = 51  # mm (?)
    averageNumberOfFoggyDaysPerYear = 70  # days
    averageNumberOfRainyDaysPerYear = 136  # days
    averageNumberOfClearDays = 159  # days

    # security
    situationInTheCountry = 2  # [1, 3] 1-bad, 3-good
    freedomOfSpeech = 3  # [1, 3]
    assessmentOfFamilyLife = 3  # [1, 3]
    attitudeTowardsLGBT = 3  # [1, 3]

    # population
    populationCount = 10_420_000
    procentOfMales = 50
    procentOfFemales = 50
    populationDensityPerSquareKilometer = 25
    speedOfLife = 2  # [1, 3]
    workPlaces = 3  # [1, 3]
    nightLifeEntertainment = 2  # [1, 3]

    # citizenship
    citizenshipGlobalRank = 2
    friendlyToForeigners = 1

    # communication
    communicationOnEnglish = 3  # [1, 3]

    # transport
    averageTravelTimeToWork = 41
    developmentLevelOfPublicTransport = 2  # [1, 3]

    # internet
    speedOfInternetMbps = 55.18  # Мегабиты в секунду
    freeWifi = 2  # [1, 3]

    # education
    rankingOfNationalEducationSystem = 5

    cc.createBase(countryName, cities, officialLanguage,
                  # currency
                  currencyName, currencyEqualsToDollar,
                  # military
                  milPolBlock, amountOfPeopleInArmy,
                  # healthcare
                  numberOfDoctorsPer100kPopulation, menAverageLifeExpectancy, womenAverageLifeExpectancy,
                  # climat
                  juneAverageTemperature, decemberAverageTemperature, averageHumidity,
                  averageDurationOfWinter, averageRainfallPerMonth, averageNumberOfFoggyDaysPerYear,
                  averageNumberOfRainyDaysPerYear, averageNumberOfClearDays,
                  # security
                  situationInTheCountry, freedomOfSpeech,
                  assessmentOfFamilyLife, attitudeTowardsLGBT,
                  # population
                  populationCount, procentOfMales, procentOfFemales, populationDensityPerSquareKilometer,
                  speedOfLife, workPlaces, nightLifeEntertainment,
                  # citizenship
                  citizenshipGlobalRank,
                  # communication
                  communicationOnEnglish,
                  # transport
                  averageTravelTimeToWork, developmentLevelOfPublicTransport,
                  # internet
                  speedOfInternetMbps, freeWifi,
                  # education
                  rankingOfNationalEducationSystem, universities, faculties, programs, costs, links, images,
                  requirements,
                  hostel, scolarship, sights, beaches, mountains, skiResorts, lakes, rivers, friendlyToForeigners
                  )
    # cc.createManMadeDisaster(countryName, nameMMD, typeOfMMD, aomuntOfDeadPeople,
    #                           aomuntOfInjuredPeople, territoryOfPollution)
    # cc.createOceans()

    #############################   SWEDEN   #############################

    #############################   FRANCE   #############################

    # Country
    countryName = "France"
    officialLanguage = "French"

    # cities
    cities = {  # isBig isResort washesBy
        'Paris': [True, True, None],
        'Nantes': [True, True, None],
        'Toulouse': [True, False, None],
        'Montpellier': [True, False, None],
        'Lyon': [True, False, None],
        'Colmar': [False, True, None],
        'Arcshon': [True, True, 'Bay of Biscay'],
        'Quimper': [False, True, 'Celtic sea']}

    # education
    universities = {'Paris': ['Superior Normal School, Paris', 'Pierre and Marie Curie University (Paris VI)'],
                    'Nantes': ['Nantes University'],
                    'Toulouse': ['University of Toulouse - Jean Jaurès']}
    faculties = {
        'Superior Normal School, Paris': ['Faculty of Social Sciences', 'Faculty of Science'],
        'Pierre and Marie Curie University (Paris VI)': ['Faculty of Medicine', 'Faculty of Engineering',
                                                         'Faculty of Science'],
        'Nantes University': ['Faculty of Medicine', 'Faculty of Social Sciences', 'Faculty of Science',
                              'Faculty of Law', 'Faculty of Arts'],
        'University of Toulouse - Jean Jaurès': ['Faculty of Arts', 'Faculty of Social Sciences']}
    programs = {
        'Superior Normal School, Paris': ['Magistracy', 'Undergraduate', 'MBA'],
        'Pierre and Marie Curie University (Paris VI)': ['Magistracy', 'Undergraduate'],
        'Nantes University': ['Magistracy', 'Undergraduate'],
        'University of Toulouse - Jean Jaurès': ['Magistracy', 'Undergraduate']}
    links = {'Superior Normal School, Paris': 'https://www.ens.psl.eu/en',
             'Pierre and Marie Curie University (Paris VI)': 'https://www.sorbonne-universite.fr/',
             'Nantes University': 'https://english.univ-nantes.fr/',
             'University of Toulouse - Jean Jaurès': 'https://www.univ-tlse2.fr/home'}
    images = {
        'Superior Normal School, Paris': 'https://smapse.com/storage/2018/11/ecole-normale-superieure.jpg',
        'Pierre and Marie Curie University (Paris VI)': 'https://smapse.com/storage/2018/09/related-image-1.jpeg',
        'Nantes University': 'https://www.euniwell.eu/fileadmin/_processed_/5/6/csm_2020-07-20-Uni-Nantes-Main-picture_f6ef389ede.jpg',
        'University of Toulouse - Jean Jaurès': 'https://www.univ-tlse2.fr/medias/photo/universite_1500638826879-jpg?ID_FICHE=191397'}
    # общага
    hostel = {'Superior Normal School, Paris': 'Yes',
              'Pierre and Marie Curie University (Paris VI)': 'Yes',
              'Nantes University': 'Yes',
              'University of Toulouse - Jean Jaurès': 'Yes'}
    # стипендия
    scolarship = {'Superior Normal School, Paris': 'Yes',
                  'Pierre and Marie Curie University (Paris VI)': 'Yes',
                  'Nantes University': 'Yes',
                  'University of Toulouse - Jean Jaurès': 'Yes'}
    # требования к поступлению
    requirements = {
        'Superior Normal School, Paris': 'Upon admission to Ecole Normal, an applicant must provide documents translated into French or English about previous education: a diploma or an extract from a record book, as well as a school certificate or a diploma of secondary specialized education. Notarization of the diploma is not required.',
        'Pierre and Marie Curie University (Paris VI)': 'foreign applicants must demonstrate a high level of French language proficiency - at least B2, backed up by a TCF or DELF language certificate.',
        'Nantes University': 'For admission to the university, the student is required to provide information about the results of the exams passed.',
        'University of Toulouse - Jean Jaurès': 'To enroll in the University of Toulouse, you will need to submit a registration application on the official website of the university, sign up for a meeting with the admissions committee, at which you should provide: School certificate, Diplomas from previous places of study, if available, Certificate of knowledge of the French language (minimum TCF B2, DELF B2 or DUEF B2), Certificate of payment of CVEC (registration fee).'}
    costs = {'Superior Normal School, Paris': 1055,
             'Pierre and Marie Curie University (Paris VI)': 1385,
             'Nantes University': 950,
             'University of Toulouse - Jean Jaurès': 1000}

    sights = {'Eiffel Tower': [
        "If you are still thinking about what to see in France, immediately go to its capital, because there are so many sights of Paris that even a partial study of them will not fit in one trip. The symbol of Paris, as you might guess, has become the main attraction of France - the Eiffel Tower - one of the most visited and recognizable architectural objects in the world.",
        'https://www.tripzaza.com/ru/destinations/wp-content/uploads/2017/04/France-1-The-Eiffel-Tower-e1492754610997.jpg'],
        'Louvre': [
            "A former fortress, once a palace, and now a museum - all these reincarnations have gone through the Louvre in Paris in its lifetime, which has become the most visited museum, where millions of people from all over the world come every year. The most distant past and present are intertwined here in hundreds of thousands of exhibits, of which only 35 thousand we can see with our own eyes. The thing is that there will not be enough exhibition space to display all these values, while many exhibits also require special storage conditions.",
            'https://www.tripzaza.com/ru/destinations/wp-content/uploads/2017/04/France-2-The-Louvre-e1492754751417.jpg'],
        'Palace of Versailles': [
            "Having wondered what to see in France, without hesitation go to one of the most respectable cities located 20 km from the capital. After all, here is a luxurious and relatively young palace and park complex, which once served as the residence of the French kings, and today has also become a famous landmark of France. This is the Palace of Versailles - an outstanding masterpiece in the history of world architecture. The layout of the park of the Palace of Versailles is also the highest achievement in the park art of France.",
            'https://www.tripzaza.com/ru/destinations/wp-content/uploads/2017/04/France-3-The-Palace-of-Versailles-e1492754919622.jpg']}
    beaches = {'Porto-Vecchio': [
        "Corsica - that's where the best beaches of France are located !!! Porto-Vecchio, or Portivechju in the Corsican dialect, has one of the most beautiful beaches of the Isle of Beauty. Corsica is already famous for its beautiful beaches, but the magnificent Santa Giulia beach is picturesque cliffs, white sand and turquoise sea - everything you need for a paradise.",
        'https://frenchtrip.ru/wp-content/uploads/2016/02/Porto-Vecchio-beaches-Plyazh-Santa-Dzhuliya-plyazhi-Porto-Vekko.png'],
        "Biarritz": [
            "Beach lovers and surfers gather at the Grande Plage in Biarritz, one of the most beautiful beaches in the Basque country. It extends from the rock de la Vierge to the lighthouse.",
            'http://www.planetware.com/photos-large/F/france-biarritz-port-vieux-beach.jpg']
    }
    mountains = {'Mont Blanc': [
        "What could be more legendary than the top of Mont Blanc? This 4,809 m high mountain, nicknamed the “roof of Europe”, proudly rises above the Alps and is able to enchant everyone, young and old, with its beauty. However, you do not need to be an experienced climber to truly enjoy a mountain holiday. We offer you several ideas for walks, views and exciting excursions where you absolutely do not need climbing crampons!",
        'https://images.france.fr/zeaejvyq9bhj/63b08MuCp8ZmvxuvsndjXA/5eb1f4521f86d25d0851baec03ffe831/Les_Contamines_Montjoie__5_-header.jpg?w=1120&h=490&q=70&fm=webp&fit=fill'],
        'Contamine-Montjoie': [
            "Contamine-Montjoie is the highest natural reserve in France and the only protected natural area in the Mont Blanc massif. Spread at an altitude of 1,000 to 4,000 meters, this reserve features landscapes of all kinds, from forests to glaciers, as well as a rich variety of biological species. Among them is the black grouse, a typical alpine bird that lives in Contamines-Montjoie and hibernates during the winter, comfortably nestled in a snow igloo. To enjoy the walk without disturbing this alpine bird's sleep, follow the signs for places to avoid.",
            'https://images.france.fr/zeaejvyq9bhj/78lmMpURJyZ829eigWwEdi/00098b219520c7cfbc0c1ad9d8ee04a2/Les_Contamines_Montjoie__7_.jpg?w=680&h=680&q=70&fm=webp&fit=fill'],
    }
    skiResorts = {'Le Carro dArache': [
        "Perched on a mountain balcony, this charming village is the gateway to 265 km of pistes in the Grand Massif ski area, linked to Morillon, Flaine, Samoens and Sixt-Fer-à-Cheval. The predominantly forested ski area of Les Carro d'Arache (External link) offers stunning views of the surrounding peaks and Mont Blanc. For several years now, the resort has been implementing the concept of sustainable development: for example, a bioclimatic hotel (the only one in the resort) has been created here, and the ski area has been awarded the Green Globe mark.",
        'https://dynamic-media-cdn.tripadvisor.com/media/photo-o/06/a0/4b/40/les-carroz-d-araches.jpg?w=700&h=500&s=1'],
        'Le Contamine-Montjoie': [
            "This resort, located in the heart of the Pays du Mont Blanc, consists of several small villages. From the local ski area, you can easily get to the resorts of Hautelus and Val Joly. The vast expanses of snow and spruce forests of the Contamines-Montjoie Nature Reserve (External link) can also be explored on snowshoes or on the touring skis offered by the racing guides.",
            'https://cdn.france-montagnes.com/sites/default/files/styles/facebook/public/station/hiver/Village-3.jpg?itok=nfHdsdwI'],
        'Champagny-en-Vanoise': [
            "Offering guests access to 225 km of Paradiski pistes, the resort of Champagny is the perfect option for a fabulous ski holiday in La Grande Plagne: an extensive ski area that stretches to glaciers at an altitude of more than 3000 m, perfect snow cover, an endless variety of landscapes and reliefs, and all this - over 425 km of tracks! Champagny is divided into 2 districts:",
            'https://img.pac.ru/resorts/213098/259133/big/FE8039CB7F0001012DB955B94B701D1C.jpg']}
    lakes = {'Lake Geneva': [
        "The largest alpine lake, divided between the two countries by the will of history, Geneva is one of the most popular tourist destinations in Europe. Its northern shores belong to Switzerland, the southern shores belong to France, and they are separated by several kilometers of impeccably clear blue water. Lake Geneva in France is patriotically called Lac-Leman - and it actually consists of two reservoirs: Big and Small. Despite the fact that tourism in full swing is observed mainly on the Swiss coast, the French coast has also not been left out of the tourist boom. The most popular resort of the Republic of Thonon-les-Bains is not very well known in the Russian market, but its younger brother Evian annually receives a significant portion of domestic tourists.",
        'https://fs.tonkosti.ru/sized/f700x700/88/bd/88bdsfy9jugw4kksw8cgwww80.jpg'],
        'Allo': [
            "The most “non-resort” and one of the most picturesque lakes in France, Lake Allo (Lac d’Allos) is comfortably located in a valley between the mountain peaks of the Alpes Haute Provence. There is no tourist life on its shores at all, but this does not prevent the lake from being among the most desirable places for hiking. Lake Allo was formed a couple of tens of thousands of years ago as a result of the descent of a glacier, and the water in it is exceptionally clean and just as cold. And it is also one of the largest high-altitude lakes in Europe - with an area of 60 hectares, Lake Allo is located at an altitude of 2200 meters above sea level.",
            'https://fs.tonkosti.ru/sized/f700x700/36/1q/361qgqrbbm2o8so8w80cg8swo.jpg'],
        'Annecy': [
            "Incredibly beautiful Lake Annecy, located in the department of Haute-Savoie in the Pre-Alpine region of France, is the second largest inland reservoir of the Republic and a popular place for a “non-hot” beach holiday. The city of the same name boasts a considerable number of significant historical sights, including a medieval castle and a palace on an island in the center of the city channel. And in small resorts along the shores of the lake, you can have a great rest surrounded by very beautiful nature, among silence and blessed solitude.",
            'https://fs.tonkosti.ru/sized/f700x700/bh/vl/bhvl3ynlids8g4000k0ggcssw.jpg']}
    rivers = {'Loire': [
        "Loire with a length of 1012 kilometers, flowing through Orleans, Tours, Nantes, has become the longest French river. The Loire river basin covers a fifth of the territory of France, but in terms of average water flow, the river is inferior to the Rhone and the Seine.",
        'https://s9.travelask.ru/system/images/files/001/461/409/wysiwyg_jpg/19537.jpg?1615371497'],
        'Rhone': [
            "The full-flowing Rhone begins in Switzerland (Rhone Glacier, Valais canton) and flows into the Mediterranean Sea (Gulf of Lion). Therefore, out of the total length of the Rhone (812 km), French territory accounts for 'only' 545 kilometers.",
            'https://s9.travelask.ru/system/images/files/001/460/800/wysiwyg_jpg/%D1%84%D0%BE%D1%82%D0%BE_5._%D0%A0%D0%BE%D0%BD%D0%B0.jpg?1615042708'],
        'Seine': [
            "Russian tourists associate the name of the Seine with Paris. This is natural, since the Seine flows through the center of the metropolis, its channel flows around the Ile de la Cité, the historical center of Paris, on both sides. But the Seine basin, which begins and ends within France, covers 78,650 square kilometers, which is up to 10% of the country's area. On the main channel of the long river (776 km) there are such large cities as Le Havre, Rouen, Poissy. In these cities, in addition to Poissy, cargo and passenger river ports operate. The Seine is characterized by a high level of industrial pollution, floods reaching up to 8.68 meters in Paris (2010). In Le Havre and Rouen, the level of the Seine is influenced by sea tides (2–7 meters high).",
            'https://s9.travelask.ru/system/images/files/001/460/801/wysiwyg_jpg/%D1%84%D0%BE%D1%82%D0%BE_6._%D0%A1%D0%B5%D0%BD%D0%B0.jpg?1615042788']}
    # currency
    currencyName = 'EUR'
    currencyEqualsToDollar = 1

    # military
    milPolBlock = "NATO"
    amountOfPeopleInArmy = 203250

    # healthcare
    numberOfDoctorsPer100kPopulation = 323
    menAverageLifeExpectancy = 79.4
    womenAverageLifeExpectancy = 85.2

    # climat
    juneAverageTemperature = 25
    decemberAverageTemperature = 9
    averageHumidity = 65
    averageDurationOfWinter = 4
    averageRainfallPerMonth = 49
    averageNumberOfFoggyDaysPerYear = 125
    averageNumberOfRainyDaysPerYear = 90
    averageNumberOfClearDays = 150

    # security
    situationInTheCountry = 3  # [1, 3] 1-bad, 3-good
    freedomOfSpeech = 2  # [1, 3]
    assessmentOfFamilyLife = 2  # [1, 3]
    attitudeTowardsLGBT = 3  # [1, 3]

    # population
    populationCount = 67500000
    procentOfMales = 48.7
    procentOfFemales = 51.3
    populationDensityPerSquareKilometer = 119.8
    speedOfLife = 3  # [1, 3]
    workPlaces = 2  # [1, 3]
    nightLifeEntertainment = 3  # [1, 3]

    # citizenship
    citizenshipGlobalRank = 2
    friendlyToForeigners = 0

    # communication
    communicationOnEnglish = 2  # [1, 3]

    # transport
    averageTravelTimeToWork = 26
    developmentLevelOfPublicTransport = 3  # [1, 3]

    # internet
    speedOfInternetMbps = 192.25  # Мегабиты в секунду
    freeWifi = 3  # [1, 3]

    # education
    rankingOfNationalEducationSystem = 17
    cc.createBase(countryName, cities, officialLanguage,
                  # currency
                  currencyName, currencyEqualsToDollar,
                  # military
                  milPolBlock, amountOfPeopleInArmy,
                  # healthcare
                  numberOfDoctorsPer100kPopulation, menAverageLifeExpectancy, womenAverageLifeExpectancy,
                  # climat
                  juneAverageTemperature, decemberAverageTemperature, averageHumidity,
                  averageDurationOfWinter, averageRainfallPerMonth, averageNumberOfFoggyDaysPerYear,
                  averageNumberOfRainyDaysPerYear, averageNumberOfClearDays,
                  # security
                  situationInTheCountry, freedomOfSpeech,
                  assessmentOfFamilyLife, attitudeTowardsLGBT,
                  # population
                  populationCount, procentOfMales, procentOfFemales, populationDensityPerSquareKilometer,
                  speedOfLife, workPlaces, nightLifeEntertainment,
                  # citizenship
                  citizenshipGlobalRank,
                  # communication
                  communicationOnEnglish,
                  # transport
                  averageTravelTimeToWork, developmentLevelOfPublicTransport,
                  # internet
                  speedOfInternetMbps, freeWifi,
                  # education
                  rankingOfNationalEducationSystem, universities, faculties, programs, costs, links, images,
                  requirements,
                  hostel, scolarship, sights, beaches, mountains, skiResorts, lakes, rivers, friendlyToForeigners
                  )

    # cc.createManMadeDisaster(countryName, nameMMD, typeOfMMD, aomuntOfDeadPeople,
    #                           aomuntOfInjuredPeople, territoryOfPollution)
    # cc.createOceans()
    #############################   FRANCE   #############################
    #############################   Brazil   #############################

    # Country
    countryName = "Brazil"
    officialLanguage = "Portuguese"

    # cities    name   isBig  washesBy
    cities = {
        'Brasilia': [True, False, None],
        'Sao Paulo': [True, False, None],
        'Rio de Janeiro': [True, True, 'Atlantic ocean'],
        'Salvador': [True, True, 'Atlantic ocean'],
        'Fortaleza': [True, True, 'Atlantic ocean'],
        'Florianopolis': [False, True, 'Atlantic ocean'],
        'Porto Seguro': [False, True, 'Atlantic ocean']}

    # education
    universities = {'Brasili': ['University of Brasília'],
                    'Sao Paulo': ['University of Sao Paulo'],
                    'Rio de Janeiro': ['Universidade do Estado do Rio de Janeiro'],
                    'Fortaleza': ['Universidade Federal do Ceará']}
    faculties = {
        'University of Brasília': ['Faculty of Architecture', 'Faculty of Science', 'Faculty of Social Sciences',
                                   'Faculty of Medicine', 'Faculty of Arts',
                                   'Faculty of Computer Engineering and Software'],
        'University of Sao Paulo': ['Faculty of Economics', 'Faculty of Law', 'Faculty of Education'],
        'Universidade do Estado do Rio de Janeiro': ['Faculty of Social Sciences', 'Faculty of Education',
                                                     'Faculty of Economics'],
        'Universidade Federal do Ceará': ['Faculty of Medicine', 'Faculty of Social Sciences', 'Faculty of Science',
                                          'Faculty of Law', 'Faculty of Arts']}
    programs = {
        'University of Brasília': ['Magistracy', 'Undergraduate'],
        'University of Sao Paulo': ['Magistracy', 'Undergraduate'],
        'Universidade do Estado do Rio de Janeiro': ['Magistracy', 'Undergraduate'],
        'Universidade Federal do Ceará': ['Magistracy', 'Undergraduate']}
    links = {'University of Brasília': 'https://international.unb.br',
             'University of Sao Paulo': 'https://www.fearp.usp.br',
             'Universidade do Estado do Rio de Janeiro': 'https://www.uerj.br',
             'Universidade Federal do Ceará': 'https://www.ufc.br'}
    images = {
        'University of Brasília': 'https://smapse.ru/storage/2018/10/1200px-ib-unb.jpg',
        'University of Sao Paulo': 'https://global.ncsu.edu/wp-content/uploads/sites/90/2019/03/USP.jpg',
        'Universidade do Estado do Rio de Janeiro': 'https://cdn.osaogoncalo.com.br/img/normal/90000/uerj-divulgacao_00091014_0.jpg?xid=259075',
        'Universidade Federal do Ceará': 'https://melhoresescolasmedicas.com/wp-content/uploads/2021/03/image_processing20200516-30496-1nwh9yc.jpeg'}
    # общага
    hostel = {'University of Brasília': 'Yes',
              'University of Sao Paulo': 'Yes',
              'Universidade do Estado do Rio de Janeiro': 'Yes',
              'Universidade Federal do Ceará': 'Yes'}
    # стипендия
    scolarship = {'University of Brasília': 'Yes',
                  'University of Sao Paulo': 'Yes',
                  'Universidade do Estado do Rio de Janeiro': 'Yes',
                  'Universidade Federal do Ceará': 'Yes'}
    # требования к поступлению
    requirements = {
        'University of Brasília': "Enrollment of applicants is based on the results of entrance examinations. "
                                  "To get a bachelor's degree in education, you need to pay about 1000 USD per year. "
                                  "Although this amount is not large (compared to other higher prestigious institutions), "
                                  "the quality of the knowledge and skills acquired at the University of Brasília is at the proper level, "
                                  "it corresponds to the title of one of the best universities in the country. "
                                  "At the university, an individual approach to each student and the possibility of distance learning are possible. "
                                  "The University of Brasilia is also happy to open its doors to students from other countries who have come on a student "
                                  "exchange program or a student program for students to jointly develop doctoral and master's degrees.",
        'University of Sao Paulo': 'Passing the competition for admission to the University of Sao Paulo is not easy. '
                                   'The applicant is enrolled only after passing serious exams. '
                                   'Usually, out of ten young people who apply, only one remains to study. '
                                   'Such a large competition is based not only on the demographic situation in the country, but also on low tuition fees. '
                                   'It is approximately 1000 USD. for the annual rate. More detailed and final prices are based on the chosen specialty. '
                                   'Information about them and the rules for admission can be found on the official USP website.',
        'Universidade do Estado do Rio de Janeiro': 'To be enrolled in the chosen faculty, the student must successfully pass the entrance exams. '
                                                    'The learning process of one academic year is divided into two approximately equal semesters. '
                                                    "The cost of obtaining knowledge for applicants for a bachelor's degree is determined by the amount equivalent to $ 1,000 and paid in local currency. "
                                                    "For a university with such ranking indicators, tuition fees are considered quite low. "
                                                    "Those who study under the master's program pay the same amount for one year of stay within the walls of UERJ.",
        'Universidade Federal do Ceará': 'For admission to the university, the student is required to provide information about the results of the exams passed.'}
    costs = {'University of Brasília': 1000,
             'University of Sao Paulo': 1000,
             'Universidade do Estado do Rio de Janeiro': 1000,
             'Universidade Federal do Ceará': 1000}

    sights = {'Christ statue': ["The statue of Christ the Redeemer is the most recognizable in the country. "
                                "It is located on Mount Corcovado. The outstretched arms of Christ symbolize the blessing of the city. "
                                "Millions of tourists seek to get to Rio de Janeiro in order to see the statue of Christ the Redeemer. "
                                "This famous landmark of Brazil was erected in honor of the 100th anniversary of independence. "
                                "Work began in 1922. It is noteworthy that the fundraising for the construction was carried out by volunteers with the active participation of Bishop Sebastian Leme. "
                                "It was originally planned that the statue of Christ would stand on the globe. "
                                "But later the project was changed. "
                                "The idea of the figure of Christ with outstretched arms belongs to the artist Carlos Osvaldo. "
                                "The arm span reaches 28 meters. The pedestal is 8 meters, and the figure of Christ itself is 30 meters.",
                                'https://www.tripzaza.com/ru/destinations/wp-content/uploads/2017/03/Brazil-1-Christ-the-Redeemer-e1490429791222.jpg'],
              'Waterfall Adam and Eve': [
                  'The waterfall Adam and Eve can rightfully be considered the greatest natural attraction in Brazil. '
                  'The complex of waterfalls on the Iguazu River delights everyone who sees them. '
                  'They are on the border of Brazil and Argentina. '
                  'The complex of waterfalls became a UNESCO heritage site in the 80s of the last century. '
                  'Adam and Eve is located in Iguazu Park near the Bossetti Falls. '
                  'The waterfall Adam and Eve is especially beautiful on a sunny day, when millions of sprays reflect rays shimmering '
                  'with all the colors of the rainbow. At the same time, the spray cloud itself rises several meters - the force of the falling water flow is so great. '
                  'For tourists, solid viewing platforms are arranged here.',
                  'https://www.tripzaza.com/ru/destinations/wp-content/uploads/2017/03/Brazil-2-Adam-and-Eve-waterfall-e1490430110461.jpg'],
              "Devil's Throat": ["There is a unique set of waterfalls on the Iguazu River. "
                                 "There are 275 of them here. The most impressive is the 700-meter ledge, which has a horseshoe shape. "
                                 "Devil's Throat Falls consists of 14 streams of water that continuously fall from a height of 350 feet. "
                                 "The waterfall is in a huge cloud of spray sparkling in the sun. "
                                 "The Devil's Throat was opened to the Western world in 1541 by the famous traveler El Dorado Cabeza de Vaca. "
                                 "The strength and power of the waterfall will be of interest to those who are thinking about what to see in Brazil. "
                                 "The observation decks here are very strong, there is no danger for tourists. "
                                 "Multi-stage platforms stretch for many kilometers, which makes it possible to admire this landmark of Brazil at any time.",
                                 'https://www.tripzaza.com/ru/destinations/wp-content/uploads/2017/03/Brazil-6-The-Devils-Throat-e1490431348162.jpg']}
    beaches = {'Ipanema': [
        'Many people know about this beach not from geography lessons and not from their own tourist experience, '
        'but thanks to the popular bossa nova jazz song Girl from Ipanema. '
        'Its authors, Antonio Carlos Jobim and Vinicius de Moraes, made this beach no less famous than Copacabana. '
        'Interestingly, in translation from the Tupi language, this toponym is translated as bad, dangerous waters. '
        'In fact, the waves in this section are quite aggressive, so the beach is definitely worth a visit for surfers, '
        'but be careful for those who go here just to swim.',
        'https://1001beach.ru/img/posts/2346/750/ipanema-1.webp?t=1580388523'],
               "Copacabana": ["Copacabana Beach is one of the visiting cards of Rio de Janeiro. "
                              "It is famous for its white sand, developed infrastructure, huge size and picturesque landscapes. "
                              "It is also loved for its cheerful and noisy atmosphere, a large number of entertainment and proximity to one "
                              "of the most beautiful cities in the world.",
                              'https://1001beach.ru/img/posts/2343/750/copacabana-1.webp?t=1580388500'],
               'Campeche': ["Campeche Beach (Praia do Campeche) is one of the best holiday destinations in Brazil. "
                            "On Santa Catarina, it occupies a leading position in the ratings of the tourism sector and is included "
                            "in the top 5 famous resorts. Archaeological sites, gentle sun, kilometers of sand and clear water "
                            "leave an indelible impression of the island. Therefore, having come here once, you want to come back again and again, "
                            "which is what most tourists do, because the territory of the resort is only getting better every year.",
                            'https://1001beach.ru/img/posts/2344/750/campeche-1.webp?t=1580388508']}
    mountains = {'Neblin': ['Neblina is a mountain in South America, the highest point of the Guiana Highlands. '
                            'Located on the border of Venezuela and Brazil. Lonely flat-topped mountain with steep slopes. '
                            'Discovered in 1962 from a plane flying past. It rises above the sea of clouds in the form of an island. '
                            'It is connected by a pass with the mountain on March 31.',
                            'http://photos.wikimapia.org/p/00/00/58/66/85_big.jpg'],
                 'March 31': [
                     "March 31 - a mountain on the border of Brazil and Venezuela with an absolute height of 2974.18 m above sea level. "
                     "It is part of the Neblina massif and the second highest mountain in Brazil after Mount Neblina.",
                     'https://upload.wikimedia.org/wikipedia/commons/6/64/Pico_31_de_Mar%C3%A7o.JPG']}
    skiResorts = {}
    lakes = {'Lagoa Mirin': ["Lagoon lake, located on the coast in southern Brazil, on the border with Uruguay. "
                             "It stretches for 220 km in length, and has a maximum width of 42 km. "
                             "The total area is about 2000 km². Lagoa Mirin is separated from the Atlantic Ocean by an alluvial sandy marshy spit. "
                             "The narrow channel of San Gonzalo Lake Lagoa Mirin is connected to Lake Patus. "
                             "Shallow. Many rivers flow into it, the largest of which is the Jaguaran.",
                             'https://upload.wikimedia.org/wikipedia/commons/7/72/Vista_da_Praia_da_Capilla%2C_Rio_Grande%2C_RS_%28cropped%29.jpg']}
    rivers = {'Amazon': ["The most full-flowing river on the planet. The basin area is 7180 thousand km². "
                         "In 2011, the river was recognized as one of the seven wonders of the world. "
                         "The Amazon is a border river. "
                         "The largest area is in Brazil, the western part flows to Bolivia, Peru, as well as Ecuador and Colombia. "
                         "The Amazon flows into the Atlantic, flows near the equator. The river also has the largest delta on earth. "
                         "The total length of the river is 6400 km",
                         'https://must-see.top/wp-content/uploads/2019/09/amazonka-700x465.jpg'],
              'San Francisco': ["The third longest river in South America. The basin area is 641 thousand km². "
                                "Some areas of Sao Francisco are suitable for extreme tourism. "
                                "In the 20th century, a cascade of hydroelectric power stations was built on the river. "
                                "The beginning at San Francisco is in the heights of the Brazilian Plateau. "
                                "The water area flows into the Atlantic Ocean. Waterfalls on the river reach 80 m. "
                                "During the rainy season, the water level in this basin rises by 7 meters. "
                                "Part of the river is navigable, the banks are considered inhabited. "
                                "The length of the river is 2830 km",
                                'https://must-see.top/wp-content/uploads/2019/09/san-fransisku-700x468.jpg'],
              'Rio Negro': ["Left tributary of the famous Amazon River. "
                            "The territory of the river basin is 600 thousand km². "
                            "Rio Negro has the ability to spill over the nearby selva for 35 km in both directions. "
                            "The navigable section of the river is 600 km. "
                            "It differs from its tributaries by large seasonal fluctuations in water levels. "
                            "The color of the waters of the Rio Negro is brown. "
                            "The total length of the river is 2300 km",
                            'https://must-see.top/wp-content/uploads/2019/09/riu-negru-700x462.jpg']}
    # currency
    currencyName = 'BRL'
    currencyEqualsToDollar = 5.24

    # military
    milPolBlock = 'TIAR'
    amountOfPeopleInArmy = 366500

    # healthcare
    numberOfDoctorsPer100kPopulation = 317
    menAverageLifeExpectancy = 72.4
    womenAverageLifeExpectancy = 79.4

    # climat
    juneAverageTemperature = 24
    decemberAverageTemperature = 26
    averageHumidity = 78
    averageDurationOfWinter = 3.5
    averageRainfallPerMonth = 191
    averageNumberOfFoggyDaysPerYear = 34
    averageNumberOfRainyDaysPerYear = 128
    averageNumberOfClearDays = 197

    # security
    situationInTheCountry = 3  # [1, 3] 1-bad, 3-good
    freedomOfSpeech = 2  # [1, 3]
    assessmentOfFamilyLife = 2  # [1, 3]
    attitudeTowardsLGBT = 3  # [1, 3]

    # population
    populationCount = 215681045
    procentOfMales = 49.2
    procentOfFemales = 50.8
    populationDensityPerSquareKilometer = 25.3
    speedOfLife = 3  # [1, 3]
    workPlaces = 3  # [1, 3]
    nightLifeEntertainment = 3  # [1, 3]

    # citizenship
    citizenshipGlobalRank = 11
    friendlyToForeigners = 3

    # communication
    communicationOnEnglish = 1  # [1, 3]

    # transport
    averageTravelTimeToWork = 41
    developmentLevelOfPublicTransport = 2  # [1, 3]

    # internet
    speedOfInternetMbps = 4  # Мегабиты в секунду
    freeWifi = 3  # [1, 3]

    # education
    rankingOfNationalEducationSystem = 41

    cc.createBase(countryName, cities, officialLanguage,
                  # currency
                  currencyName, currencyEqualsToDollar,
                  # military
                  milPolBlock, amountOfPeopleInArmy,
                  # healthcare
                  numberOfDoctorsPer100kPopulation, menAverageLifeExpectancy, womenAverageLifeExpectancy,
                  # climat
                  juneAverageTemperature, decemberAverageTemperature, averageHumidity,
                  averageDurationOfWinter, averageRainfallPerMonth, averageNumberOfFoggyDaysPerYear,
                  averageNumberOfRainyDaysPerYear, averageNumberOfClearDays,
                  # security
                  situationInTheCountry, freedomOfSpeech,
                  assessmentOfFamilyLife, attitudeTowardsLGBT,
                  # population
                  populationCount, procentOfMales, procentOfFemales, populationDensityPerSquareKilometer,
                  speedOfLife, workPlaces, nightLifeEntertainment,
                  # citizenship
                  citizenshipGlobalRank,
                  # communication
                  communicationOnEnglish,
                  # transport
                  averageTravelTimeToWork, developmentLevelOfPublicTransport,
                  # internet
                  speedOfInternetMbps, freeWifi,
                  # education
                  rankingOfNationalEducationSystem, universities, faculties, programs, costs, links, images,
                  requirements,
                  hostel, scolarship, sights, beaches, mountains, skiResorts, lakes, rivers, friendlyToForeigners
                  )

    # cc.createManMadeDisaster(countryName, nameMMD, typeOfMMD, aomuntOfDeadPeople,
    #                           aomuntOfInjuredPeople, territoryOfPollution)
    # cc.createOceans()
    #############################   Brazil   ##############################

    #############################   Panama   #############################

    # Country
    countryName = "Panama"
    officialLanguage = "Spanish"

    # cities    name   isBig  washesBy
    cities = {
        'Panama': [True, True, 'Pacific ocean'],
        'David': [True, True, 'Pacific ocean'],
        'Colon': [True, True, 'Caribbean sea'],
        'Changinola': [True, True, 'Caribbean sea'],
        'Achutupo': [True, True, 'Caribbean sea']}

    # education
    universities = {}
    faculties = {}
    programs = {}
    links = {}
    images = {}
    # общага
    hostel = {}
    # стипендия
    scolarship = {}
    # требования к поступлению
    requirements = {}
    costs = {}

    sights = {'Panama Canal': ["One of the most popular places in Panama is its canal. "
                               "The amazing creation of human hands was officially opened in 1920, although the first ideas for such construction arose as early as the 16th century. "
                               "There are many tourist excursions on the Panama Canal, the best place to watch the ships is at the walls of the Miraflores locks.",
                               'https://top10.travel/wp-content/uploads/2016/05/panamskiy-kanal.jpg'],
              'Coiba National Park': [
                  "One of the largest islands in Panama gave its name to the unique national park of this country. "
                  "About 760 species of fish live in the waters of the park, and from April to September, many turtles come to Coiba to lay their eggs. "
                  "For its excellent diving conditions, Coiba is called the new Galapagos.",
                  'https://top10.travel/wp-content/uploads/2016/05/park-koiba.jpg'],
              'Islands of the San Blas Archipelago': [
                  "The extraordinarily beautiful San Blas Archipelago is only half an hour by boat from Panama City. "
                  "Kuna Indians live here, who managed to maintain an economy and culture independent of Panama. "
                  "People come to San Blas to go diving, go fishing, see the daily life of the Indians, or just relax on the cleanest local beaches.",
                  'https://top10.travel/wp-content/uploads/2016/05/ostrova-san-blas.jpg']}
    beaches = {
        'Isla Pelicano': ["Isla Pelicano is a tiny Robinson Crusoe-style island in the San Blas Archipelago, Panama. "
                          "There are no hotels here, but there is a kiosk selling food and drinks. "
                          "Sometimes there is a lot of garbage here, but this is the problem of many uninhabited islands - "
                          "today the sea will bring all the dirt to the beach, and tomorrow it will wash it back.",
                          'http://www.beach-on-map.com/img/11/panama-san-blas-cayos-limones-isla-pelicano-orig.jpg'],
        "Kuanidup Island": ["Kuanidup is a small island near the port of Carti in the San Blas group, Panama. "
                            "This is a creepy atmospheric place with a great beach. "
                            "There are not many palm trees, but they look very picturesque, and the sand is perfectly white. "
                            "Where there is no sand - excellent snorkeling.",
                            'http://www.beach-on-map.com/img/11/panama-san-blas-kuanidup-island-beach-orig.jpg'],
        'Red Frog': ["Red Frog is the best beach on the island of Bastimentos in the Bocas del Toro archipelago. "
                     "There are always strong waves here, so this place is not suitable for children.",
                     'http://www.beach-on-map.com/img/7/panama-bocas-del-toro-bastimentos-island-red-frog-beach-view-from-the-top-orig.jpg']}
    mountains = {'Baru': [
        "Baru, formerly Chiriqui, is a volcano in Panama, the highest point in the country, the highest volcano in southern Central America.",
        'https://peakfinder.ru/image/original/40_baru.jpg'],
        'El Valle': [
            "El Valle is a dormant stratovolcano in Panama, in the province of Cocle, 80 km from the country's capital city of Panama. Height - 1185 m. "
            "The last eruption occurred about 13,000 years ago. In the center of the volcano is a caldera with a diameter of 6 kilometers. "
            "It was formed 56,000 years ago as a result of the collapse of the cone of Mount Paquita.",
            'https://upload.wikimedia.org/wikipedia/commons/c/cf/El_valle.jpg']}
    skiResorts = {}
    lakes = {'Gatun': ["From the shore, Lake Gatun looks endless. "
                       "On its surface, here and there, one can see small islands, densely overgrown with trees. "
                       "Traveling by boat, you can admire the steep red cliffs that have been washed away by waves and trees over the years, hanging right above the water. "
                       "Snow-white herons and sluggish pelicans are found here. You can often see flocks of kites in the sky. "
                       "Lake Gatun will please fans of fishing - here tuna jumps out of the water by itself. "
                       "You can try to catch a sergeant fish, nicknamed so in memory of the American military. "
                       "The lake attracts not only lovers of measured rest and ecotourists, but also divers. "
                       "There are several possible dive sites in Panama at Lake Gatun and Alajuela. "
                       "At the bottom of them you can see the remains of the railway that ran all the way to the Isthmus of Panama, "
                       "and a lot of construction equipment that was used to lay tracks and build the Panama Canal.",
                       'http://openarium.ru/foto/ozhyl6cNFRXHsE.jpg']}
    rivers = {}
    # currency
    currencyName = 'USD'
    currencyEqualsToDollar = 1

    # military
    milPolBlock = "TIAR"
    amountOfPeopleInArmy = 30000

    # healthcare
    numberOfDoctorsPer100kPopulation = 284
    menAverageLifeExpectancy = 76.7
    womenAverageLifeExpectancy = 82.1

    # climat
    juneAverageTemperature = 30
    decemberAverageTemperature = 30
    averageHumidity = 85
    averageDurationOfWinter = 2.9
    averageRainfallPerMonth = 68
    averageNumberOfFoggyDaysPerYear = 13
    averageNumberOfRainyDaysPerYear = 129
    averageNumberOfClearDays = 217

    # security
    situationInTheCountry = 2  # [1, 3] 1-bad, 3-good
    freedomOfSpeech = 2  # [1, 3]
    assessmentOfFamilyLife = 2  # [1, 3]
    attitudeTowardsLGBT = 2  # [1, 3]

    # population
    populationCount = 4382000
    procentOfMales = 50.4
    procentOfFemales = 49.6
    populationDensityPerSquareKilometer = 81
    speedOfLife = 2  # [1, 3]
    workPlaces = 2  # [1, 3]
    nightLifeEntertainment = 2  # [1, 3]

    # citizenship
    citizenshipGlobalRank = 30
    friendlyToForeigners = 3

    # communication
    communicationOnEnglish = 1  # [1, 3]

    # transport
    averageTravelTimeToWork = 35.14
    developmentLevelOfPublicTransport = 2  # [1, 3]

    # internet
    speedOfInternetMbps = 14  # Мегабиты в секунду
    freeWifi = 3  # [1, 3]

    # education
    rankingOfNationalEducationSystem = 51

    cc.createBase(countryName, cities, officialLanguage,
                  # currency
                  currencyName, currencyEqualsToDollar,
                  # military
                  milPolBlock, amountOfPeopleInArmy,
                  # healthcare
                  numberOfDoctorsPer100kPopulation, menAverageLifeExpectancy, womenAverageLifeExpectancy,
                  # climat
                  juneAverageTemperature, decemberAverageTemperature, averageHumidity,
                  averageDurationOfWinter, averageRainfallPerMonth, averageNumberOfFoggyDaysPerYear,
                  averageNumberOfRainyDaysPerYear, averageNumberOfClearDays,
                  # security
                  situationInTheCountry, freedomOfSpeech,
                  assessmentOfFamilyLife, attitudeTowardsLGBT,
                  # population
                  populationCount, procentOfMales, procentOfFemales, populationDensityPerSquareKilometer,
                  speedOfLife, workPlaces, nightLifeEntertainment,
                  # citizenship
                  citizenshipGlobalRank,
                  # communication
                  communicationOnEnglish,
                  # transport
                  averageTravelTimeToWork, developmentLevelOfPublicTransport,
                  # internet
                  speedOfInternetMbps, freeWifi,
                  # education
                  rankingOfNationalEducationSystem, universities, faculties, programs, costs, links, images,
                  requirements,
                  hostel, scolarship, sights, beaches, mountains, skiResorts, lakes, rivers, friendlyToForeigners
                  )

    #############################   Panama   #############################

    #############################   Egypt   #############################

    # Country
    countryName = "Egypt"
    officialLanguage = "Arabic"

    # cities    name   isBig  washesBy
    cities = {
        'Cairo': [True, False, None],
        'Alexandria': [True, True, 'Mediterranean sea'],
        'Giza': [True, False, None],
        'Shubra al-Kheima': [True, False, None],
        'Port Said': [True, False, 'Mediterranean sea'],
        'Hurghada': [False, True, 'Red sea'],
        'Sahl Hasheesh': [False, True, 'Red sea'],
        'Makadi Bay': [False, True, 'Red sea']}

    # education
    universities = {'Cairo': ['Ain Shams University', 'Al Azhar University', 'Sinai University'],
                    'Alexandria': ['Alexandria University']}
    faculties = {
        'Ain Shams University': ['Faculty of Science', 'Faculty of Engineering', 'Faculty of Medicine',
                                 'Faculty of Education'],
        'Al Azhar University': ['Faculty of Medicine'],
        'Sinai University': ['Faculty of Engineering', 'Faculty of Computer Engineering and Software',
                             'Faculty of Economics'],
        'Alexandria University': ['Faculty of Economics', 'Faculty of Education']}
    programs = {
        'Ain Shams University': ['Magistracy', 'Undergraduate'],
        'Al Azhar University': ['Magistracy', 'Undergraduate'],
        'Sinai University': ['Undergraduate'],
        'Alexandria University': ['Magistracy', 'Undergraduate']}
    links = {'Ain Shams University': 'https://www.asu.edu.eg',
             'Al Azhar University': 'http://www.azhar.edu.eg/',
             'Sinai University': 'https://www.su.edu.eg/',
             'Alexandria University': 'https://alexu.edu.eg'}
    images = {
        'Ain Shams University': 'https://www.asu.edu.eg/storage//uploads/2022/slider/nUIegg3j.jpg',
        'Al Azhar University': 'https://studioarabiya.com/images/easyblog_articles/blog_images/Al-Azhar__1757629c.jpg',
        'Sinai University': 'https://www.dbse.co/uploads/5b62fa713a161.png',
        'Alexandria University': 'https://upload.wikimedia.org/wikipedia/commons/b/b1/Alexandria_University%2C_The_Main_Building.JPG'}
    # общага
    hostel = {'Ain Shams University': 'Yes',
              'Al Azhar University': 'Yes',
              'Sinai University': 'No',
              'Alexandria University': 'Yes'}
    # стипендия
    scolarship = {'Ain Shams University': 'No',
                  'Al Azhar University': 'Yes',
                  'Sinai University': 'No',
                  'Alexandria University': 'Yes'}
    # требования к поступлению
    requirements = {
        'Ain Shams University': 'The entire admission process and details of admission to a particular faculty should be clarified on the ASU university website. '
                                'The educational process is formed here from two semesters of one academic year.',
        'Al Azhar University': 'When planning to enter Al-Azhar University, you must first visit the official website of the university. '
                               'There you can find the rules of admission and selection criteria. '
                               'The educational process in the institution consists of two semesters of one academic year.',
        'Sinai University': 'In order to become a student of Sinai University, an applicant must fill out an application on the website and provide: '
                            'Certificate of general secondary education with a certified translation; Motivation letter; '
                            'Certificate of payment of the registration fee; A certificate confirming the language proficiency of the chosen program. '
                            'Enrollment in some specialties requires passing entrance exams.',
        'Alexandria University': "The admissions committee begins accepting documents with an assessment of the success of the applicant's studies at the previous place of study. "
                                 "After that, there are entrance exams in the chosen direction. "
                                 "In principle, Alexandria University is not distinguished by the rigor of selection, therefore 90% of all applicants become full students of this educational institution. "
                                 "The educational process includes two semesters of one academic year."}
    costs = {'Ain Shams University': 1000,
             'Al Azhar University': 2500,
             'Sinai University': 6000,
             'Alexandria University': 1000}

    sights = {'Pyramids of Giza': [
        "In the Libyan desert, on the Giza plateau, is the most important place of power on the continent and, perhaps, one of the most beautiful places on our planet. "
        "These are the Great Pyramids of Giza, which are a whole city-cemetery with temples, tombs, roads. "
        "The ancient necropolis includes the Pyramid of Khufu (also known as the Pyramid of Cheops, one of the 7 wonders of the world), "
        "the slightly smaller Pyramid of Khafre and the much more modest Pyramid of Menkaure, as well as several smaller satellite pyramids. "
        "In fact, this complex is a cemetery for real aristocrats, where the pharaohs were buried, "
        "as well as all their close associates - wives, servants, close relatives and everyone who had a noble origin and wanted to go to the next world after their master. "
        "In general, the entire complex, in addition to the pyramids, consists of: temples located at the beginning of the memorial road that leads to the pyramids; "
        "cemeteries where close relatives and courtiers of the pharaohs were buried; "
        "the most ancient monument in the world - the sculpture of the Sphinx.",
        'https://www.tripzaza.com/ru/destinations/wp-content/uploads/2017/04/Egypt-1-Giza-Pyramid-e1491277079103.jpg'],
              'Valley of the pharaohs': [
                  "In the 16th century BC. in order to bury the rulers of Egypt, the Valley of the Kings was created - a place in a rocky gorge, where a number of tombs were organized. "
                  "At one time, this place was secret and was strictly guarded by caretakers who protected it from raids and robbery. "
                  "The tradition of the burial of the pharaohs was laid by one of them - Thutmose I, who, fearing for the looting of his own tomb, "
                  "ordered to organize it in an inaccessible, impassable place. And so the valley of Thebes appeared - the most important sight of Egypt, "
                  "which has preserved its appearance to this day. "
                  "The place for the Great Magic Necropolis was not chosen by chance: the material for the construction of tombs - limestone - in this rocky area is quite hard, "
                  "which makes it possible to protect the tombs from cracks and destruction; the path to the Valley allows the funeral procession to move quickly and unhindered; "
                  "at the same time, there is only one single entrance to the Valley, passing along a narrow path and protected by steep cliffs; the location of the Valley is at a great distance"
                  " from the mortuary temple, the tombs of which have been plundered more than once. To date, more than 60 pharaohs, as well as the wives and children of the rulers, rest in the Valley. "
                  "Inside the Valley, a whole system of complex tunnels and wells has been formed, and the walls are covered with frescoes that tell about the life of the buried persons.",
                  'https://www.tripzaza.com/ru/destinations/wp-content/uploads/2017/04/Egypt-2-The-Valley-of-the-Kings-e1491277275454.jpg'],
              'Temple of Luxor': [
                  "If during your travels you, by the will of fate, ended up in the ancient city of history and magic - Luxor, then the question of what to visit in Egypt can be considered resolved. "
                  "Of course, this is the majestic Luxor Temple - a monumental religious building built in the 14th century BC. "
                  "The temple strikes with the perfection and harmony of forms, especially when you realize the degree of antiquity of this historical monument. "
                  "One of the largest temples in Egypt has a total length of about 260 meters, and massive trapezoidal towers - pylons that adorn the entrance, "
                  "reach 20 meters in height and 70 meters in length. The temple was erected by order of the pharaoh Amenhotep III, "
                  "who ruled at that time, who dedicated it to the sun god Amon-Ra, his wife Mut and their son Khons. "
                  "In ancient times, 6 huge statues of Pharaoh Ramses II towered at the entrance to the temple, but only two of them have survived to this day. "
                  "Here you can also admire a huge 25-meter obelisk painted with frescoes. Initially there were two of them, "
                  "but one of them was presented to France by order of the ruler Mohamed Ali in 1819.",
                  'https://www.tripzaza.com/ru/destinations/wp-content/uploads/2017/04/Egypt-3-Luxor-Temple-e1491278052766.jpg']}
    beaches = {'Agiba': [
        "Miracle - this is how the name of the small beach Agiba is translated from Arabic. The 40-meter sandy strip is hidden in the golden-yellow rocks: bays, caves, "
        "islets and walls hanging over the sea beckon to climb higher and take the most unusual photo. "
        "When you swim in plenty in the azure waters of the Mediterranean Sea and explore the unusual relief, you can relax in a cafe overlooking the sea.",
        'https://content.skyscnr.com/f1128d59413ede49d75d1adfd893a469/agiba.jpg'],
               "Haram": [
                   "Haram, or the Coast of Love, is the largest beach in the vicinity of Mersa Matruh, the main resort town of the Mediterranean coast of Egypt. On its white sand, there is enough space for everyone even in the hottest summer months. "
                   "A smooth entry into the water will appeal to families with children and is suitable for those who feel insecure on the water.",
                   'https://infomedicspb.ru/wp-content/uploads/4/2/9/429c045dd065c83ff6c70df6ec9b5d86.jpeg']}
    mountains = {'Sinai': ["In Egypt, there is one interesting place that keeps a history of thousands of years. "
                           "The significance of this place has recently faded somewhat against the backdrop of popular attractions in Egypt - such as the pyramids of Giza or the resort of Sharm el-Sheikh. "
                           "Mount Sinai, located on the Sinai Peninsula, is perhaps the first thing to visit in Egypt for those who are interested in local shrines. "
                           "Mount Sinai, also known as Mount Moses, is a place with which one biblical story is connected. "
                           "It is believed that it was here that the prophet Moses received the ten commandments from the Lord and passed them on to his people. "
                           "Since this story exists not only in Christianity, the Jewish and Islamic religions also adhere to these commandments. "
                           "Therefore, here, on the top of the mountain, at an altitude of 2,285 m, each of these religions has its own temple dedicated to it. "
                           "There is also a chapel dedicated to the Trinity, and a mosque of about the same size, and the Jews will show the way to the cave, which, "
                           "according to legend, served as a refuge for Moses for 40 days while he communicated with God.",
                           'https://www.tripzaza.com/ru/destinations/wp-content/uploads/2017/04/Egypt-7-Mount-Sinai-e1491279059652.jpg']}
    skiResorts = {}
    lakes = {
        'Karun': ["Karun is a salt lake in Egypt, on the territory of the Faiyum oasis. The area is about 233 km². "
                  "It is located at a level of 45 m below sea level. The modern lake Karun is the remnant of a large lake located in the same place and having an area of 1270 to 1700 km². "
                  "Initially, it was a vast expanse of water, which gradually dried up for reasons still unknown.",
                  'https://rutraveller.ru/icache/place/2/343/2343_603x354.jpg']}
    rivers = {'Nile': ["The Nile River is the country's main waterway. "
                       "This is, first of all, a source of fresh water for the Egyptians (although the quality of this water, from the point of view of hygienists, leaves a very big question). "
                       "The Nile carries its waters along a narrow valley, surrounded by rocks on both sides, from Sudan to the Mediterranean Sea. "
                       "The total length of the river is about 1,545 kilometers. In the north, in the Cairo region, the width of the river delta reaches 250 kilometers.",
                       'https://switki.ru/assets/i/ai/4/7/6/i/3275005.jpg']}
    # currency
    currencyName = 'EGP'
    currencyEqualsToDollar = 24.57

    # military
    milPolBlock = "None"
    amountOfPeopleInArmy = 438500

    # healthcare
    numberOfDoctorsPer100kPopulation = 309
    menAverageLifeExpectancy = 69.8
    womenAverageLifeExpectancy = 75.1

    # climat
    juneAverageTemperature = 34
    decemberAverageTemperature = 19
    averageHumidity = 52
    averageDurationOfWinter = 3
    averageRainfallPerMonth = 27
    averageNumberOfFoggyDaysPerYear = 12
    averageNumberOfRainyDaysPerYear = 14
    averageNumberOfClearDays = 317

    # security
    situationInTheCountry = 2  # [1, 3] 1-bad, 3-good
    freedomOfSpeech = 1  # [1, 3]
    assessmentOfFamilyLife = 1  # [1, 3]
    attitudeTowardsLGBT = 1  # [1, 3]

    # population
    populationCount = 104300000
    procentOfMales = 50.2
    procentOfFemales = 49.8
    populationDensityPerSquareKilometer = 105.7
    speedOfLife = 1  # [1, 3]
    workPlaces = 2  # [1, 3]
    nightLifeEntertainment = 2  # [1, 3]

    # citizenship
    citizenshipGlobalRank = 76
    friendlyToForeigners = 3

    # communication
    communicationOnEnglish = 1  # [1, 3]

    # transport
    averageTravelTimeToWork = 48
    developmentLevelOfPublicTransport = 2  # [1, 3]

    # internet
    speedOfInternetMbps = 2  # Мегабиты в секунду
    freeWifi = 1  # [1, 3]

    # education
    rankingOfNationalEducationSystem = 51

    cc.createBase(countryName, cities, officialLanguage,
                  # currency
                  currencyName, currencyEqualsToDollar,
                  # military
                  milPolBlock, amountOfPeopleInArmy,
                  # healthcare
                  numberOfDoctorsPer100kPopulation, menAverageLifeExpectancy, womenAverageLifeExpectancy,
                  # climat
                  juneAverageTemperature, decemberAverageTemperature, averageHumidity,
                  averageDurationOfWinter, averageRainfallPerMonth, averageNumberOfFoggyDaysPerYear,
                  averageNumberOfRainyDaysPerYear, averageNumberOfClearDays,
                  # security
                  situationInTheCountry, freedomOfSpeech,
                  assessmentOfFamilyLife, attitudeTowardsLGBT,
                  # population
                  populationCount, procentOfMales, procentOfFemales, populationDensityPerSquareKilometer,
                  speedOfLife, workPlaces, nightLifeEntertainment,
                  # citizenship
                  citizenshipGlobalRank,
                  # communication
                  communicationOnEnglish,
                  # transport
                  averageTravelTimeToWork, developmentLevelOfPublicTransport,
                  # internet
                  speedOfInternetMbps, freeWifi,
                  # education
                  rankingOfNationalEducationSystem, universities, faculties, programs, costs, links, images,
                  requirements,
                  hostel, scolarship, sights, beaches, mountains, skiResorts, lakes, rivers, friendlyToForeigners
                  )
    #############################   Egypt   #############################

    cc.createBorders()
    cc.close()