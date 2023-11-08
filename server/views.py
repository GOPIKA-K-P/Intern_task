from django.http import HttpResponse
import requests
import json
import csv

def download_csv(request):
    # Make an API request to get JSON data
    api_url = 'https://www.asterank.com/api/skymorph/search?target=J99TS7A'
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
    else:
        return HttpResponse("API request failed")

    # Save JSON data to a file
    with open("data.json", "w") as json_file:
        json.dump(data, json_file, indent=4)

    # Load JSON data from the file
    with open("data.json") as file:
        data1 = json.load(file)

    result_data = data1['results']

    # Create a CSV response
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="data.csv"'

    if result_data and isinstance(result_data, list) and len(result_data) > 0:
        # Check if data is a non-empty list
        # Create a CSV writer and write the header row
        csv_writer = csv.writer(response)

        # Write header row with keys from the first item
        header = result_data[0].keys()
        csv_writer.writerow(header)

        # Write data rows
        for item in result_data:
            csv_writer.writerow(item.values())
    else:
        return HttpResponse("API data is not in the expected format")

    return response

