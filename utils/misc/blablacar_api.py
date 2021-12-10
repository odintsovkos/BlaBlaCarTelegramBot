import aiohttp

from data import config


async def request_blablacar_api(from_location_data, to_location_data, date_data, time_data):
    start_date_local = f"{date_data[2]}-{date_data[1]}-{date_data[0]}T{time_data[0]}:{time_data[1]}:00"
    url = f"https://public-api.blablacar.com/api/v3/trips?" \
          f"from_coordinate={from_location_data[0]},{from_location_data[1]}&" \
          f"to_coordinate={to_location_data[0]},{to_location_data[1]}&" \
          f"locale=ru-RU&" \
          f"currency=RUB&" \
          f"start_date_local={start_date_local}&" \
          f"key={config.BLABLACAR_API_TOKEN}"

    responses = []
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            result = await response.json()
            responses.append(result)
        status = response.status
        next_cursor = result['next_cursor']
        while next_cursor != 0:
            url_next = url + f"&from_cursor={next_cursor}"
            async with session.get(url_next) as response_next:
                result_next = await response_next.json()
                responses.append(result_next)
            if 'next_cursor' in result_next:
                next_cursor = result_next['next_cursor']
            else:
                next_cursor = 0

    return responses, status
