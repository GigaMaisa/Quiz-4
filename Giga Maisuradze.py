# from bs4 import BeautifulSoup
# import requests
# import csv
# from time import sleep
# from random import randint
#
# file = open('test.csv', 'w', encoding='utf-8_sig', newline='\n')
# file_obj = csv.writer(file)
# file_obj.writerow(['ოთახების რაოდენობა', 'მისამართი', 'ფართი', 'სართული', 'ფასი'])
#
# url_page_ind = 1
# while url_page_ind<6:
#
#     url = f'https://ss.ge/ka/udzravi-qoneba/l/bina/iyideba?Page={url_page_ind}&RealEstateTypeId=5&RealEstateDealTypeId=4&MunicipalityId=95&CityIdList=95&subdistr=47&PrcSource=1&StatusField.FieldId=34&StatusField.Type=SingleSelect&StatusField.StandardField=Status&StatusField.SelectedValues=2&QuantityFrom=120&PriceType=false&CurrencyId=2'
#     r = requests.get(url)
#     content = r.text
#     soup = BeautifulSoup(content, 'html.parser')
#
#     section = soup.find('div', class_='latest_articles_block listing-section')
#     flats = section.find_all('div', class_='latest_article_each_in')
#
#     for flat in flats:
#         flat_title_div = flat.find('div', class_='latest_title')
#         flat_street_adress_div = flat.find('div', class_='StreeTaddressList')
#         flat_square_meters_div = flat.find('div', class_='latest_flat_km')
#         flat_floor_div = flat.find('div', class_='latest_stair_count')
#         flat_price_div = flat.find('div', class_='latest_price')
#
#         flat_room_numbers = flat_title_div.span.text[8:9]
#         flat_street_adress = flat_street_adress_div.a.text.strip()
#         flat_square_meters = flat_square_meters_div.text.strip()[0:3]
#         flat_floor = flat_floor_div.text.strip()[:2].strip()
#         flat_price_gel = flat_price_div.text.strip()[:9].strip()
#
#         file_obj.writerow([flat_room_numbers,
#                            flat_street_adress,
#                            flat_square_meters,
#                            flat_floor,
#                            flat_price_gel
#                            ]
#                           )
#
#     url_page_ind += 1
#     sleep(randint(1, 5))
#
#         # print(flat_room_numbers)
#         # print(flat_street_adress)
#         # print(flat_square_meters)
#         # print(flat_floor)
#         # print(flat_price_gel)
