import requests
import random

map_sectors = {
    'A1': [{'lat': 51.097297, 'lon': 71.414138}, {'lat': 51.093427, 'lon': 71.412509},
           {'lat': 51.092003, 'lon': 71.423560}, {'lat': 51.095740, 'lon': 71.424906}],
    'A2': [{'lat': 51.093427, 'lon': 71.412509}, {'lat': 51.087019, 'lon': 71.409959},
           {'lat': 51.085373, 'lon': 71.421010}, {'lat': 51.092003, 'lon': 71.423560}],
    'B1': [{'lat': 51.099655, 'lon': 71.426465}, {'lat': 51.098899, 'lon': 71.431778},
           {'lat': 51.094951, 'lon': 71.430486}, {'lat': 51.095740, 'lon': 71.424906}],
    'B2': [{'lat': 51.092003, 'lon': 71.423560}, {'lat': 51.095740, 'lon': 71.424906},
           {'lat': 51.094951, 'lon': 71.430486}, {'lat': 51.091291, 'lon': 71.428944}],
    'B3': [{'lat': 51.092003, 'lon': 71.423560}, {'lat': 51.088176, 'lon': 71.422088},
           {'lat': 51.087286, 'lon': 71.427740}, {'lat': 51.091291, 'lon': 71.428944}],
    'B4': [{'lat': 51.088176, 'lon': 71.422088}, {'lat': 51.085373, 'lon': 71.421010},
           {'lat': 51.084438, 'lon': 71.426748}, {'lat': 51.087286, 'lon': 71.427740}],
    'C1': [{'lat': 51.098899, 'lon': 71.431778}, {'lat': 51.098009, 'lon': 71.437728},
           {'lat': 51.094227, 'lon': 71.436241}, {'lat': 51.094951, 'lon': 71.430486}],
    'C2': [{'lat': 51.094951, 'lon': 71.430486}, {'lat': 51.094227, 'lon': 71.436241},
           {'lat': 51.090446, 'lon': 71.434824}, {'lat': 51.091291, 'lon': 71.428944}],
    'C3': [{'lat': 51.091291, 'lon': 71.428944}, {'lat': 51.090446, 'lon': 71.434824},
           {'lat': 51.086574, 'lon': 71.433407}, {'lat': 51.087286, 'lon': 71.427740}],
    'C4': [{'lat': 51.087286, 'lon': 71.427740}, {'lat': 51.084438, 'lon': 71.426748},
           {'lat': 51.083726, 'lon': 71.432344}, {'lat': 51.086574, 'lon': 71.433407}],
    'D1': [{'lat': 51.098009, 'lon': 71.437728}, {'lat': 51.097119, 'lon': 71.444246},
           {'lat': 51.093249, 'lon': 71.442900}, {'lat': 51.094227, 'lon': 71.436241}],
    'D2': [{'lat': 51.094227, 'lon': 71.436241}, {'lat': 51.090446, 'lon': 71.434824},
           {'lat': 51.089553, 'lon': 71.441352}, {'lat': 51.093249, 'lon': 71.442900}],
}

def random_point_in_sector(sector):
    """Generate a random point within a given map sector (polygon)."""
    latitudes = [point['lat'] for point in sector]
    longitudes = [point['lon'] for point in sector]
    
    min_lat, max_lat = min(latitudes), max(latitudes)
    min_lon, max_lon = min(longitudes), max(longitudes)
    
    random_lat = random.uniform(min_lat, max_lat)
    random_lon = random.uniform(min_lon, max_lon)
    
    return random_lat, random_lon

def generate_random_data():
    """Generate random data for the air quality signal."""
    # Randomly choose a sector
    sector_key = random.choice(list(map_sectors.keys()))
    sector = map_sectors[sector_key]
    
    # Generate random coordinates within the sector
    lat, lon = random_point_in_sector(sector)
    
    # Generate random PM values between 0 and 50
    pm_1_0 = random.randint(0, 50)
    pm_2_5 = random.randint(0, 50)
    pm_10 = random.randint(0, 50)
    
    return {
        'pm_1_0': pm_1_0,
        'pm_2_5': pm_2_5,
        'pm_10': pm_10,
        'lat': lat,
        'lon': lon
    }

def send_post_request(data):
    """Send a POST request to the API endpoint with the given data."""
    url = 'http:/api/v1/air-signals'
    response = requests.post(url, json=data)
    return response.status_code, response.text

def main():
    for _ in range(500):
        data = generate_random_data()
        status_code, response_text = send_post_request(data)
        print(f"Request sent with status code {status_code}. Response: {response_text}")

if __name__ == '__main__':
    main()
