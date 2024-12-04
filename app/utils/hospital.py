import math
import requests

def haversine(lat1: int, lon1: int, lat2: int, lon2: int):
    # Radius bumi dalam kilometer
    R = 6371.0
    print(lat1, lon1, lat2, lon2)
    # Konversi derajat ke radian
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)
    
    # Perbedaan koordinat
    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad
    
    # Rumus haversine
    a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    
    # Jarak dalam kilometer
    distance = R * c
    return distance

def get_hospital_details(lat, lon, radius=15000):
    url = "https://overpass-api.de/api/interpreter"
    query = f"""
    [out:json];
    node
      ["amenity"="hospital"]
      (around:{radius},{lat},{lon});
    out body;
    """
    response = requests.post(url, data=query)
    if response.status_code == 200:
        data = response.json()
        hospitals = []

        print(data)

        for element in data.get('elements', []):
            tags = element.get('tags', {})

            element_lat = float(element.get("lat", 0))
            element_lon = float(element.get("lon", 0))
            
            distance = haversine(float(lat), float(lon), element_lat, element_lon)
            distance = round(distance, 2)

            hospitals.append({
                "name": tags.get("name", "Unknown"),
                "latitude": element.get("lat"),
                "longitude": element.get("lon"),
                "contact": {
                    "phone": tags.get("contact:phone"),
                    "website": tags.get("contact:website"),
                },
                "distance": distance
            })
        return True, hospitals
    else:
        return False, response.json