import csv
import time

import requests
from bs4 import BeautifulSoup


# Open the CSV file and read its contents into a list of strings
def read_csv(file_path):
    data_list = []
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        # Extract the first element from each row (assuming there's only one element in each row)
        data_list = [row[0] for row in csv_reader]
    return data_list

# Example usage
file_path = 'filtered.csv'
csv_data = read_csv(file_path)

links = csv_data


# with open('unique_links.csv', 'r', newline='', encoding='utf-8') as csvfile:
#     reader = csv.reader(csvfile)
#     rows = [row for row in reader if 'https' in row[0]]
#
# # Write filtered rows back to the CSV file
# with open('filtered.csv', 'w', newline='', encoding='utf-8') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerows(rows)
data_list = []


def extract_data_from_link(url):

    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.find('div', class_='offer__advert-title').find('h1').text.strip()
        address = soup.find('div', class_='offer__location').text.strip()
        address = address.split('\n')
        address = address[0]

        room_number = title[0][0]

        var1 = soup.find('div', {'class': 'offer__info-item', 'data-name': 'flat.building'})
        if var1:
            construction_type = var1.find('div', class_='offer__advert-short-info').text.strip()
        else:
            construction_type = None

        var2 = soup.find('div', {'class': 'offer__info-item', 'data-name': 'map.complex'})
        if var2:
            name_of_JK = var2.find('div', class_='offer__advert-short-info').text.strip()
        else:
            name_of_JK = None

        var3 = soup.find('div', {'class': 'offer__info-item', 'data-name': 'house.year'})
        if var3:
             year = var3.find('div', class_='offer__advert-short-info').text.strip()
        else:
            year = None

        var4 = soup.find('div', {'class': 'offer__info-item', 'data-name': 'flat.floor'})
        if var4:
            floor = var4.find('div', class_='offer__advert-short-info').text.strip()
        else:
            floor = None

        var5 = soup.find('div', {'class': 'offer__info-item', 'data-name': 'live.square'})
        if var5:
            area = var5.find('div', class_='offer__advert-short-info').text.strip()
        else:
            area = None

        var6 = soup.find('div', {'class': 'offer__info-item', 'data-name': 'flat.renovation'})
        if var6:
            condition = var6.find('div', class_='offer__advert-short-info').text.strip()
        else:
            condition = None

        sanuzel_element = soup.find('dt', {'data-name': 'flat.toilet'})
        if sanuzel_element and sanuzel_element.find_next('dd'):
            sanuzel_value = sanuzel_element.find_next('dd').text.strip()
        else:
            sanuzel_value = None

        # Extract and handle balcony
        balcony_element = soup.find('dt', {'data-name': 'flat.balcony'})
        if balcony_element and balcony_element.find_next('dd'):
            balcony_value = balcony_element.find_next('dd').text.strip()
        else:
            balcony_value = None

        # Extract and handle balcony_glass
        balcony_element1 = soup.find('dt', {'data-name': 'flat.balcony_g'})
        if balcony_element1 and balcony_element1.find_next('dd'):
            balcony_glass = balcony_element1.find_next('dd').text.strip()
        else:
            balcony_glass = None

        # Extract and handle door
        flat_d = soup.find('dt', {'data-name': 'flat.door'})
        if flat_d and flat_d.find_next('dd'):
            door = flat_d.find_next('dd').text.strip()
        else:
            door = None

        # Extract and handle phone
        flat_phone = soup.find('dt', {'data-name': 'flat.phone'})
        if flat_phone and flat_phone.find_next('dd'):
            phone = flat_phone.find_next('dd').text.strip()
        else:
            phone = None

        # Extract and handle internet
        flat_internet = soup.find('dt', {'data-name': 'inet.type'})
        if flat_internet and flat_internet.find_next('dd'):
            internet = flat_internet.find_next('dd').text.strip()
        else:
            internet = None

        # Extract and handle parking
        flat_parking = soup.find('dt', {'data-name': 'flat.parking'})
        if flat_parking and flat_parking.find_next('dd'):
            parking = flat_parking.find_next('dd').text.strip()
        else:
            parking = None

        # Extract and handle furniture
        flat_furniture = soup.find('dt', {'data-name': 'live.furniture'})
        if flat_furniture and flat_furniture.find_next('dd'):
            furniture = flat_furniture.find_next('dd').text.strip()
        else:
            furniture = None

        # Extract and handle flooring
        flat_flooring = soup.find('dt', {'data-name': 'flat.flooring'})
        if flat_flooring and flat_flooring.find_next('dd'):
            flooring = flat_flooring.find_next('dd').text.strip()
        else:
            flooring = None

        # Extract and handle ceil
        flat_ceil = soup.find('dt', {'data-name': 'ceiling'})
        if flat_ceil and flat_ceil.find_next('dd'):
            ceil = flat_ceil.find_next('dd').text.strip()
        else:
            ceil = None

        # Extract and handle security
        flat_security = soup.find('dt', {'data-name': 'flat.security'})
        if flat_security and flat_security.find_next('dd'):
            security = flat_security.find_next('dd').text.strip()
        else:
            security = None

        # Extract and handle dorm
        flat_dorm = soup.find('dt', {'data-name': 'flat.priv_dorm'})
        if flat_dorm and flat_dorm.find_next('dd'):
            dorm = flat_dorm.find_next('dd').text.strip()
        else:
            dorm = None

        # Extract and handle change
        flat_change = soup.find('dt', {'data-name': 'has_change'})
        if flat_change and flat_change.find_next('dd'):
            change = flat_change.find_next('dd').text.strip()
        else:
            change = None

        extracted_data = {

            "room number": room_number,
            "district": address,
            "construction type": construction_type,
            "name_of_complex": name_of_JK,
            "built_year": year,
            "floor": floor,
            "area": area,
            "condition": condition,
            "sanuzel": sanuzel_value,
            "balcony": balcony_value,
            "balcony_glass": balcony_glass,
            "door": door,
            "phone": phone,
            "internet": internet,
            "parking": parking,
            "furniture": furniture,
            "flooring": flooring,
            "ceiling height": ceil,
            "security": security,
            "was_dormitory": dorm,
            "change": change
        }
        return extracted_data


# Iterate through the list of links and extract data
for index, link in enumerate(links, start=1):
    print(f"Extracting data from link {index}: {link}")
    extracted_data = extract_data_from_link(link)
    if extracted_data:
        extracted_data["link_to_data"] = link
        data_list.append(extracted_data)
    time.sleep(1)


# Save the list of dictionaries to a CSV file
with open('extracted_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = extracted_data.keys()
    csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    csv_writer.writeheader()
    csv_writer.writerows(data_list)

print('Data saved to extracted_data.csv')

