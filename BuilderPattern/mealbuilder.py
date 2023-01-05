from meal import Meal
from vegburger import VegBurger
from chickenburger import ChickenBurger
from coke import Coke
from pepsi import Pepsi


class MealBuilder():
    def prepareVegMeal(self):
        meal = Meal()
        meal.add(VegBurger())
        meal.add(Coke())
        return meal;

    def prepareNonVegMeal(self):
        meal = Meal()
        meal.add(ChickenBurger())
        meal.add(Pepsi())
        return meal

if __name__ == "__main__":
    mb = MealBuilder()

    vegm = mb.prepareVegMeal()
    print("Veg Meal")
    vegm.show()
    print("Total Cost:", vegm.get_cost())

    nvegm = mb.prepareNonVegMeal()
    print("Non-Veg Meal")
    nvegm.show()
    print("Total Cost:", nvegm.get_cost())