

def add_car():
    success = True
    make = input("Make: ").strip().title()
    model = input("Model: ").strip().title()
    year = 0

    while success:
        try:
            year = int(input("Year of vehicle: ").split())
            success = False
        except ValueError:
            print("The year of the vehicle needs to be a numeric value")

    with open("cars.csv", "a") as car_list:
        car_list.write(f"{make}, {model}, {year}\n")


def get_all_cars():
    cars = []
    with open("cars.csv", "r") as car_list:
        for car in car_list:
            make, model, year = car.strip().split(",")
            cars.append(({
                "make": make,
                "model": model,
                "year": year
            }))
        return cars


def find_car():
    car_list = get_all_cars()
    if not car_list:
        print("Your car list is empty")
    else:
        matching_cars = []
        search_term = input("Please enter car make to search for: ").strip().lower()
        for car in car_list:
            if search_term in car["make"].lower():
                matching_cars.append(car)
        return matching_cars


