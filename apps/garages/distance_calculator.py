from geopy.distance import geodesic

def calculate_distance(garage_location, driver_location):
    garage_point = (garage_location['latitude'], garage_location['longitude'])
    driver_point = (driver_location['latitude'], driver_location['longitude'])

    distance = geodesic(garage_point, driver_point).km

    return distance