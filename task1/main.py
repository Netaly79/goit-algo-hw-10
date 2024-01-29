import pulp


def main():
    model = pulp.LpProblem("Maximize Profit", pulp.LpMaximize)

    lemonade = pulp.LpVariable('lemonade', lowBound=0, cat='Integer')
    juice = pulp.LpVariable('juice', lowBound=0, cat='Integer')

    model += lemonade + juice, "Profit"

    model += 2 * lemonade + juice <= 100, "Water"
    model += lemonade <= 50, "Sugar"
    model += lemonade <= 30, "Lemon"
    model += 2 * juice <= 40, "Fruit"

    model.solve()

    print("Max amount of Lemonade:", lemonade.value())
    print("Max amount of Fruit Juice:", juice.value())


if __name__ == "__main__":
    main()
