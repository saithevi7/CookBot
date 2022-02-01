import sys

countries = {"1": "Italian",
             "2": "Chinese", }

foods_itly = {"A": "Ragu with sage pesto",
              "B": "Risotto",
              "C": "Gnocchi",
              "D": "Baslamic Bruchetta"}

foods_chin = {"A": "General Tso Chicken",
              "B": "Soup Dumplings",
              "C": "Stir Fried Tofu with Rice",
              "D": "Honey Garlic Chicken"}

name = None
while not name:
    name = input("What is your name?: ")
    print("")
print("hello " + name + " nice to meet you! ")
print("")
answer_two = (input("Okay " + name + " shall we get started? (yes or no): "))
print("")
if answer_two == "yes":
    print("Alright lets go")

elif answer_two == "no":
    print("Maybe next time!")
    sys.exit()

else:
    print("yes or no..... please try again")
    sys.exit()

print("pick a cuisine!: ")
# to organize dictionary
for key, value in countries.items():
    print(key, value)

answer = input("Please input one of the number options specified above: ")
valid_answer = False
while not valid_answer:
    if answer.upper() in countries:
        valid_answer = True
        print("cool choice!")
        print("")
    else:
        print(countries)
        answer = input("Please input one of the number options specified above: ")
        print("")

# Italian Cuisine
if answer == "1":
    print("what sort of foods do you like?: ")
    for key, value in foods_itly.items():
        print(key, value)

    answer = input("Please input one of the letter options specified above: ")
    valid_answer = False
    while not valid_answer:
        if answer in foods_itly:
            valid_answer = True
            print("Cool choice!")
            print("")
            print("You picked Italian cuisine!")

        else:
            print(foods_itly)
            answer = input("Please input one of the letter options specified above: ")

    if answer == "A":
        ragu_pasta = {"1": "100ml extra virgin olive oil",
                      "2": "1 eggplant, cut into 1cm cubes",
                      "3": "1 large onion, finely chopped",
                      "4": "3 garlic cloves, crushed",
                      "5": "1½ tsp dried chilli flakes",
                      "6": "3 garlic cloves, crushed",
                      "7": "1½ tsp dried chilli flakes",
                      "8": "500g beef mince",
                      "9": "2 x 410g cans crushed tomatoes",
                      "10": "½ tsp Worcestershire sauce",
                      "11": "1½ cups (375ml) beef stock",
                      "12": "400g spaghetti",
                      "13": "Finely grated parmesan and small basil leaves, to serve",
                      "Sage": "Pesto",
                      "14": "1 small garlic clove, roughly chopped",
                      "15": "½ bunch sage, leaves picked",
                      "16": "½ cup (40g) finely grated parmesan",
                      "17": "¼ cup (40g) pine nuts, toasted",
                      "18": " tbs red wine vinegar",
                      "19": "1/3 cup (80ml) extra virgin olive oil"

                      }
        print("Cool pick!, here are the ingredients for Ragu with sage pesto")
        print("")
        print("use this link to see the steps required: https://www.delicious.com.au/recipes/ragu-sage-pesto/De6uN6e5")

        for key, value in ragu_pasta.items():
            print(key, value)
    elif answer == "B":
        risotto = {"1": "6 cups low-sodium chicken stock, or vegetable stock",
                   "2": "2 tablespoons olive oil",
                   "3": "1 shallot, finely chopped",
                   "4": "1 lb shiitake mushroom(455 g), stemmed and thinly sliced",
                   "5": "2 tablespoons unsalted butter",
                   "6": "2 cloves garlic, minced",
                   "7": "1 teaspoon fresh thyme, finely chopped",
                   "8": "1 ½ cups arborio rice(200 g)",
                   "9": "½ cup white wine(120 mL)",
                   "10": "1 cup grated parmesan cheese(110 g), plus more for serving",
                   "11": "¼ cup fresh parsley(10 g), for serving",
                   }
        print("Cool pick!, here are the ingredients for Risotto")
        print("")
        print("use this link to see the steps required: https://tasty.co/recipe/mushroom-risotto")
        for key, value in risotto.items():
            print(key, value)




    elif answer == "C":

        gnocchi = {"1": "2 potatoes",
                   "2": "2 cups all-purpose flour",
                   "3": "1 egg",

                   }
        print("Cool pick!, here are the ingredients for Gnocchi")
        print("")
        print("use this link to see the steps required: https://www.allrecipes.com/recipe/18465/gnocchi-i/")
        for key, value in gnocchi.items():
            print(key, value)

    elif answer == "D":
        baslsamic_bruchetta = {"1": "6 cups low-sodium chicken stock, or vegetable stock",
                               "2": "2 tablespoons olive oil",
                               "3": "1 shallot, finely chopped",
                               "4": "1 lb shiitake mushroom(455 g), stemmed and thinly sliced",
                               "5": "2 tablespoons unsalted butter",
                               "6": "2 cloves garlic, minced",
                               "7": "1 teaspoon fresh thyme, finely chopped",
                               "8": "1 ½ cups arborio rice(200 g)",
                               "9": "½ cup white wine(120 mL)",
                               "10": "1 cup grated parmesan cheese(110 g), plus more for serving",
                               "11": "¼ cup fresh parsley(10 g), for serving",
                               }
        print("Cool pick!, here are the ingredients for Baslamic Bruchetta")
        print("")
        print("use this link to see the steps required: https://www.allrecipes.com/recipe/54165/balsamic-bruschetta/")
        for key, value in baslsamic_bruchetta.items():
            print(key, value)

    print("Its been nice finding ingredients for you!")
    print("Run the bot to start again!")







# Chinese Cuisine
elif answer == "2":
    for key, value in foods_chin.items():
        print(key, value)

    answer = input("Please input one of the letter options specified above: ")
    valid_answer = False
    while not valid_answer:
        if answer.upper() in foods_chin:
            valid_answer = True
            print("Cool choice!")
            print("")
            print("You picked Chinese cuisine!")
        else:
            print(foods_chin)
            answer = input("Please input one of the letter options specified above: ")

    if answer == "A":
        gen_tso = {"1": "1 pound chicken thighs cut into 1 inch chunks",
                   "2": "1/4 cup cornstarch",
                   "3": "oil for frying",
                   "4": "1 tablespoon minced ginger",
                   "5": "1/2 teaspoon red chili flakes",
                   "6": "2 cloves garlic minced",
                   "7": "3 tablespoons rice vinegar",
                   "8": "3 tablespoons soy sauce",
                   "9": "2 teaspoons hoisin sauce",
                   "10": "1/4 cup water",
                   "11": "3 tablespoons sugar",
                   "12": "1 tablespoon cornstarch",
                   }
        print("Cool pick!, here are the ingredients for General Tso Chicken")
        print("")
        print("use this link to see the steps required: https://dinnerthendessert.com/general-tsos-chicken/")
        for key, value in gen_tso.items():
            print(key, value)

    elif answer == "B":
        soup_dump = {"1": "1 cup all-purpose flour",
                     "2": "2 teaspoons baking powder",
                     "3": "1 teaspoon white sugar",
                     "4": "½ teaspoon salt",
                     "5": "1 tablespoon margarine",
                     "6": "½ cup milk",

                     }
        print("Cool pick!, here are the ingredients for Soup Dumplings")
        print("")
        print("use this link to see the steps required: https://www.allrecipes.com/recipe/6900/dumplings/")
        for key, value in soup_dump.items():
            print(key, value)

    elif answer == "C":
        stir_fry = {"1": "1 cup extra firm tofu, pressed and crumbled or cubed",
                    "2": "1 Tbsp coconut aminos",
                    "3": "1 tsp chili garlic sauce (optional)",
                    "4": "2 tsp sesame oil (if avoiding oil, sub water or use a non-stick pan)",
                    "Time For": "The Sauce",
                    "5": "2 Tbsp peanut butter (or other nut butter)",
                    "6": "2-3 Tbsp coconut aminos / tamari",
                    "7": "1 Tbsp maple syrup",
                    "8": "1 Tbsp lime juice",
                    "9": "1-2 tsp chili garlic sauce",
                    "Now For": "Stir Fry",
                    "10": "2 tsp sesame oil (if avoiding oil, sub water or use a non-stick pan",
                    "11": "1 cup chopped shiitake mushrooms",
                    "12": "1 cup thinly sliced red cabbage",
                    "13": "1 cup thinly sliced red bell pepper",
                    "14": "2 cloves garlic, minced",
                    "15": "1/4 cup thinly sliced green onion",
                    "16": "1 Tbsp fresh minced ginger"
                    }
        print("Cool pick!, here are the ingredients for Stir Fried Tofu with Rice")
        print("")
        print("use this link to see the steps required: https://minimalistbaker.com/20-minute-tofu-stir-fry/")
        print("")
        for key, value in stir_fry.items():
            print(key, value)

    elif answer == "D":
        hon_chick = {"1": "500g / 1 lb chicken breast , boneless and skinless (2 pieces)",
                     "2": "Salt and pepper",
                     "3": "1 1/4 cup flour",
                     "4": "3 1/2 tbsp (50g) unsalted butter (or 2 1/2 tbsp olive oil)",
                     "5": "2 garlic cloves , minced",
                     "6": "1 1/2 tbsp apple cider vinegar (or white or other clear vinegar)",
                     "7": "1 tbsp soy sauce , light or all purpose ",
                     "8": "1/3 cup honey (or maple syrup)",

                     }
        print("Cool pick!, here are the ingredients for Soup Dumplings")
        print("")
        print("use this link to see the steps required: https://www.recipetineats.com/honey-garlic-chicken/")
        for key, value in hon_chick.items():
            print(key, value)

    print("Its been nice finding ingredients for you!")
    print("")
    print("Run the bot to start again!")










