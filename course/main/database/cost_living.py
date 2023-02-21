from .request import Request


class CostLivingRequest(Request):

    def findAllPrices(self):
        with self.driver.session() as session:
            info = session.execute_write(self._findAllPrices)
            return info

    def findCountryNames(self):
        with self.driver.session() as session:
            info = session.execute_write(self._findCounryNames)
            return info

    @staticmethod
    def _findCounryNames(tx):
        result = tx.run("""
        match(n:Country) return n.name as Country
        """)
        return [info["Country"] for info in result]

    @staticmethod
    def _findAllPrices(tx):
        result = tx.run("""match (c:Country)-[:economic_situation]-(r)-[:salaries]-(s), 
        (r)-[:clothing_prices]-(cp), 
        (r)-[:prices_in_restaurants]-(pr), 
        (r)-[:childcare_prices]-(chcp), 
        (r)-[:buy_prices]-(bp), 
        (r)-[:utilities_prices]-(up), 
        (r)-[:rent_prices]-(rp), 
        (r)-[:sports_prices]-(spp), 
        (r)-[:transportation_prices]-(tp), 
        (r)-[:prices_in_markets]-(pm) 
        return c.name as Country, 
        s.averageMonthlyNetSalary as averageMonthlyNetSalary, 
        cp.dress as dress, 
        cp.jeans as jeans, 
        cp.pairOfMenLeatherBusinessShoes as pairOfMenLeatherBusinessShoes, 
        cp.pairOfNikeRunningShoes as pairOfNikeRunningShoes, 
        pr.cappuccino as cappuccino, 
        pr.domesticBeerRestaurant as domesticBeerRestaurant, 
        pr.importedBeerRestaurant as importedBeerRestaurant, 
        pr.mcMealAtMcDonalds as mcMealAtMcDonalds, 
        pr.mealFor2PeopleMidRestaurant as mealFor2PeopleMidRestaurant, 
        pr.mealInexpensiveRestaurant as mealInexpensiveRestaurant, 
        pr.pepsi as pepsi, pr.water as water, 
        chcp.internationalPrimarySchool as internationalPrimarySchool, 
        chcp.preschool as preschool,
        bp.pricePerSquareMeterToBuyApartmentInCityCentre as pricePerSquareMeterToBuyApartmentInCityCentre, 
        bp.pricePerSquareMeterToBuyApartmentOutsideOfCentre as pricePerSquareMeterToBuyApartmentOutsideOfCentre, 
        up.mobileTariffLocal as mobileTariffLocal, 
        up.internet as internet, 
        up.basic as basic, 
        rp.apartment1RoomInCityCentre as apartment1RoomInCityCentre, 
        rp.apartment1RoomOutsideOfCentre as apartment1RoomOutsideOfCentre, 
        rp.apartment3RoomsInCityCentre as apartment3RoomsInCityCentre, 
        rp.apartment3RoomsOutsideOfCentre as apartment3RoomsOutsideOfCentre, 
        spp.cinema as cinema, 
        spp.fitnessClub as fitnessClub, 
        spp.tennisCourt as tennisCourt, 
        tp.gasoline as gasoline, 
        tp.monthlyPass as monthlyPass, 
        tp.oneWayTicketLocal as oneWayTicketLocal, 
        tp.taxi1hourWaiting as taxi1hourWaiting, 
        tp.taxi1km as taxi1km, tp.taxiStart as taxiStart, 
        tp.toyotaCorollaSedan as toyotaCorollaSedan, 
        tp.volkswagenGolf as volkswagenGolf, 
        pm.apples as apples, 
        pm.banana as banana, 
        pm.beefRound as beefRound, 
        pm.bottleOfWine as bottleOfWine, 
        pm.chickenFillets as chickenFillets, 
        pm.cigarettesPack as cigarettesPack, 
        pm.domesticBeer as domesticBeer, 
        pm.eggs as eggs, 
        pm.importedBeer as importedBeer, 
        pm.lettuce as lettuce, 
        pm.loafOfFreshWhiteBread as loafOfFreshWhiteBread, 
        pm.localCheese as localCheese, 
        pm.milk as milk, 
        pm. onion as onion, 
        pm.oranges as oranges, 
        pm.potato as potato, 
        pm.rice as rice, 
        pm.tomato as tomato, 
        pm.waterBigBottle as waterBigBottle
        """)
        return [{"Country": info["Country"],
                 "averageMonthlyNetSalary": info["averageMonthlyNetSalary"],
                 "dress": info["dress"],
                 "jeans": info["jeans"],
                 "pairOfMenLeatherBusinessShoes": info["pairOfMenLeatherBusinessShoes"],
                 "pairOfNikeRunningShoes": info["pairOfNikeRunningShoes"],
                 "cappuccino": info["cappuccino"],
                 "domesticBeerRestaurant": info["domesticBeerRestaurant"],
                 "importedBeerRestaurant": info["importedBeerRestaurant"],
                 "mcMealAtMcDonalds": info["mcMealAtMcDonalds"],
                 "mealFor2PeopleMidRestaurant": info["mealFor2PeopleMidRestaurant"],
                 "mealInexpensiveRestaurant": info["mealInexpensiveRestaurant"],
                 "water": info["water"],
                 "internationalPrimarySchool": info["internationalPrimarySchool"],
                 "preschool": info["preschool"],
                 "pricePerSquareMeterToBuyApartmentInCityCentre": info["pricePerSquareMeterToBuyApartmentInCityCentre"],
                 "pricePerSquareMeterToBuyApartmentOutsideOfCentre": info["pricePerSquareMeterToBuyApartmentOutsideOfCentre"],
                 "mobileTariffLocal": info["mobileTariffLocal"],
                 "internet": info["internet"],
                 "basic": info["basic"],
                 "apartment1RoomInCityCentre": info["apartment1RoomInCityCentre"],
                 "apartment1RoomOutsideOfCentre": info["apartment1RoomOutsideOfCentre"],
                 "apartment3RoomsInCityCentre": info["apartment3RoomsInCityCentre"],
                 "apartment3RoomsOutsideOfCentre": info["apartment3RoomsOutsideOfCentre"],
                 "cinema": info["cinema"],
                 "fitnessClub": info["fitnessClub"],
                 "tennisCourt": info["tennisCourt"],
                 "gasoline": info["gasoline"],
                 "monthlyPass": info["monthlyPass"],
                 "oneWayTicketLocal": info["oneWayTicketLocal"],
                 "taxi1hourWaiting": info["taxi1hourWaiting"],
                 "taxi1km": info["taxi1km"],
                 "taxiStart": info["taxiStart"],
                 "toyotaCorollaSedan": info["toyotaCorollaSedan"],
                 "volkswagenGolf": info["volkswagenGolf"],
                 "apples": info["apples"],
                 "banana": info["banana"],
                 "beefRound": info["beefRound"],
                 "bottleOfWine": info["bottleOfWine"],
                 "chickenFillets": info["chickenFillets"],
                 "cigarettesPack": info["cigarettesPack"],
                 "domesticBeer": info["domesticBeer"],
                 "eggs": info["eggs"],
                 "importedBeer": info["importedBeer"],
                 "lettuce": info["lettuce"],
                 "loafOfFreshWhiteBread": info["loafOfFreshWhiteBread"],
                 "localCheese": info["localCheese"],
                 "milk": info["milk"],
                 "onion": info["onion"],
                 "oranges": info["oranges"],
                 "potato": info["potato"],
                 "rice": info["rice"],
                 "tomato": info["tomato"],
                 "waterBigBottle": info["waterBigBottle"]} for info in result]


cost_living_db = CostLivingRequest()

if __name__ == "__main__":
    pass

