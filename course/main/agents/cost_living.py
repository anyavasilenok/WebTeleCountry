from ..database.cost_living import cost_living_db


coefficients = {"dress": 0.1,
                "jeans": 0.1,
                "pairOfMenLeatherBusinessShoes": 0.1,
                "pairOfNikeRunningShoes": 0.1,
                "domesticBeerRestaurant": 0.2325,
                "importedBeerRestaurant": 0.2325,
                "mcMealAtMcDonalds": 0.93,
                "mealFor2PeopleMidRestaurant": 1.55,
                "mealInexpensiveRestaurant": 2.17,
                "water": 1.1625,
                "internationalPrimarySchool": 0.08333333,
                "mobileTariffLocal": 20.0,
                "internet": 0.5,
                "basic": 0.6071429,
                "cinema": 2.10,
                "cappuccino": 3.50,
                "fitnessClub": 1,
                "tennisCourt": 3,
                "gasoline": 120,
                "monthlyPass": 1,
                "oneWayTicketLocal": 12.60,
                "taxi1hourWaiting": 1.40,
                "taxi1km": 109.20,
                "taxiStart": 16.80,
                "apples": 8.68,
                "banana": 7.233333,
                "beefRound": 4.34,
                "bottleOfWine": 0.3839286,
                "chickenFillets": 4.34,
                "domesticBeer": 2.5595238,
                "eggs": 5.7866667,
                "importedBeer": 0.5119048,
                "lettuce": 5.7866667,
                "loafOfFreshWhiteBread": 7.233333,
                "localCheese": 2.893333,
                "milk": 7.2333333,
                "onion": 2.8933333,
                "oranges": 8.68,
                "potato": 5.78666667,
                "rice": 2.8933333,
                "tomato": 5.7866667,
                "waterBigBottle": 7.50}


class CostLiving:
    def __init__(self):
        super().__init__()
        self.prices = []
        self.coefficients = coefficients
        self.rent = ["1-к в центре",
                     "3-к в центре",
                     "1-к на окраине",
                     "3-к на окраине",
                     "своё жильё"]
        self.transportation = ["такси",
                               "своя машина",
                               "общественный транспорт"]

    def get_information(self):
        self.prices = cost_living_db.findAllPrices()
        cost_living_db.close()

    def get_countries(self):
        countries = cost_living_db.findCountryNames()
        cost_living_db.close()
        return countries

    def to_fixed(self, numObj: float):
        digits = 2
        return f"{numObj:.{digits}f}"

    def count_function(self,
                       children_preschool: int,
                       children_school: int,
                       family_member_amount: int,
                       smoking_packs: float,
                       transportation: str,
                       rent: str,
                       result: dict,
                       i: int
                       ):
        # Учёт стоимости проживания не включая проезд
        sum = (family_member_amount * (self.prices[i]["dress"] * self.coefficients["dress"]
                                       + self.prices[i]["jeans"] * self.coefficients["jeans"]
                                       + self.prices[i]["pairOfMenLeatherBusinessShoes"] * self.coefficients[
                                           "pairOfMenLeatherBusinessShoes"]
                                       + self.prices[i]["pairOfNikeRunningShoes"] * self.coefficients[
                                           "pairOfNikeRunningShoes"]
                                       + self.prices[i]["domesticBeerRestaurant"] * self.coefficients[
                                           "domesticBeerRestaurant"]
                                       + self.prices[i]["importedBeerRestaurant"] * self.coefficients[
                                           "importedBeerRestaurant"]
                                       + self.prices[i]["mcMealAtMcDonalds"] * self.coefficients["mcMealAtMcDonalds"]
                                       + self.prices[i]["mealFor2PeopleMidRestaurant"] * self.coefficients[
                                           "mealFor2PeopleMidRestaurant"]
                                       + self.prices[i]["mealInexpensiveRestaurant"] * self.coefficients[
                                           "mealInexpensiveRestaurant"]
                                       + self.prices[i]["water"] * self.coefficients["water"]
                                       + self.prices[i]["mobileTariffLocal"] * self.coefficients["mobileTariffLocal"]
                                       + self.prices[i]["internet"] * self.coefficients["internet"]
                                       + self.prices[i]["basic"] * self.coefficients["basic"]
                                       + self.prices[i]["cinema"] * self.coefficients["cinema"]
                                       + self.prices[i]["cappuccino"] * self.coefficients["cappuccino"]
                                       + self.prices[i]["fitnessClub"] * self.coefficients["fitnessClub"]
                                       + self.prices[i]["tennisCourt"] * self.coefficients["tennisCourt"]
                                       + self.prices[i]["apples"] * self.coefficients["apples"]
                                       + self.prices[i]["banana"] * self.coefficients["banana"]
                                       + self.prices[i]["beefRound"] * self.coefficients["beefRound"]
                                       + self.prices[i]["bottleOfWine"] * self.coefficients["bottleOfWine"]
                                       + self.prices[i]["chickenFillets"] * self.coefficients["chickenFillets"]
                                       + self.prices[i]["domesticBeer"] * self.coefficients["domesticBeer"]
                                       + self.prices[i]["eggs"] * self.coefficients["eggs"]
                                       + self.prices[i]["importedBeer"] * self.coefficients["importedBeer"]
                                       + self.prices[i]["lettuce"] * self.coefficients["lettuce"]
                                       + self.prices[i]["loafOfFreshWhiteBread"] * self.coefficients[
                                           "loafOfFreshWhiteBread"]
                                       + self.prices[i]["localCheese"] * self.coefficients["localCheese"]
                                       + self.prices[i]["milk"] * self.coefficients["milk"]
                                       + self.prices[i]["onion"] * self.coefficients["onion"]
                                       + self.prices[i]["oranges"] * self.coefficients["oranges"]
                                       + self.prices[i]["potato"] * self.coefficients["potato"]
                                       + self.prices[i]["rice"] * self.coefficients["rice"]
                                       + self.prices[i]["tomato"] * self.coefficients["tomato"]
                                       + self.prices[i]["waterBigBottle"] * self.coefficients["waterBigBottle"])
               + self.prices[i]["preschool"] * children_preschool
               + self.prices[i]["internationalPrimarySchool"] * self.coefficients["internationalPrimarySchool"]
               * children_school
               + self.prices[i]["cigarettesPack"] * smoking_packs * 30)

        # Учёт стоимости проживания с арендой квартиры
        if rent == self.rent[0]:  # 1-комнатная квартира в центре города (аренда)
            sum += self.prices[i]["apartment1RoomInCityCentre"]
        elif rent == self.rent[1]:  # 3-комнатная квартира в центре города (аренда)
            sum += self.prices[i]["apartment3RoomsInCityCentre"]
        elif rent == self.rent[2]:  # 1-комнатная квартира на окраине города (аренда)
            sum += self.prices[i]["apartment1RoomOutsideOfCentre"]
        elif rent == self.rent[3]:  # 3-комнатная квартира на окраине города (аренда)
            sum += self.prices[i]["apartment3RoomsOutsideOfCentre"]
        elif rent == self.rent[4]:  # своё жильё
            pass
        else:
            print("Некорректный ввод")

        # Учёт стоимости проживания с проездом
        if transportation == self.transportation[0]:  # такси
            sum += family_member_amount * (self.prices[i]["oneWayTicketLocal"] * self.coefficients["oneWayTicketLocal"]
                                           + self.prices[i]["taxi1hourWaiting"] * self.coefficients["taxi1hourWaiting"]
                                           + self.prices[i]["taxi1km"] * self.coefficients["taxi1km"]
                                           + self.prices[i]["taxiStart"] * self.coefficients["taxiStart"])
        elif transportation == self.transportation[1]:  # своя машина
            sum += family_member_amount * self.prices[i]["gasoline"] * self.coefficients["gasoline"]
        elif transportation == self.transportation[2]:  # общественный транспорт
            sum += family_member_amount * self.prices[i]["monthlyPass"] * self.coefficients["monthlyPass"]

        # result_sum = self.to_fixed(sum)
        result[self.prices[i]["Country"]] = sum
        # result_cost_living += f'{self.prices[i]["Country"]} -- {result_sum} $\n'
        return result

    def count_cost_living(self,
                          children_preschool: int,
                          children_school: int,
                          family_member_amount: int,
                          smoking_packs: float,
                          transportation: str,
                          rent: str,
                          country: str):
        result = {}
        if country in self.get_countries():
            for i in range(len(self.prices)):
                if country == self.prices[i]['Country']:
                    result = self.count_function(children_preschool,
                                                 children_school,
                                                 family_member_amount,
                                                 smoking_packs,
                                                 transportation,
                                                 rent,
                                                 result,
                                                 i)
                    break

        elif country == "Рейтинг стран":
            for i in range(len(self.prices)):
                result = self.count_function(children_preschool,
                                             children_school,
                                             family_member_amount,
                                             smoking_packs,
                                             transportation,
                                             rent,
                                             result,
                                             i)

        string_result = ""
        sorted_values = sorted(result.values())
        for i in sorted_values:
            for key, value in result.items():
                if i == value:
                    string_result += f'{key} -- {self.to_fixed(i)} $\n'

        return string_result

    def out_for_html(self, result: str):
            rez_list = result.split("\n")
            rez_list.pop()
            return rez_list

    def out(self,
            children_preschool: int,
            children_school: int,
            family_member_amount: int,
            smoking_packs: float,
            transportation: str,
            rent: str,
            country: str):

        count = self.count_cost_living(children_preschool,
                                       children_school,
                                       family_member_amount,
                                       smoking_packs,
                                       transportation,
                                       rent,
                                       country)

        rez_list = count.split("\n")
        string_result = ""

        if country == "Рейтинг стран":
            for i in range(len(rez_list)):
                if i >= 10:
                    break
                string_result += f"{i+1}) {rez_list[i]}\n"
        else:
            string_result += f"{rez_list[0]}\n"

        string_result = self.out_for_html(string_result)

        return string_result


