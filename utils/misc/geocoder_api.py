import aiohttp


async def request_geocoder_api(city):
    url = f"https://nominatim.openstreetmap.org/search?city={city}&country=Russia&format=json"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            response_text = await response.json()
            if len(response_text) != 0:
                latitude = response_text[0]['lat']
                longitude = response_text[0]['lon']
                return [latitude, longitude]
            else:
                return False
