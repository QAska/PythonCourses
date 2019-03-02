def make_car(manufacturer, model, **description):
    car = {manufacturer: manufacturer, model: model}
    for key, value in description.items():
        car[key] = value
    return car
