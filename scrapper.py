from bs4 import BeautifulSoup
import requests

url = 'https://www.flipkart.com/try-checkered-men-hooded-neck-green-t-shirt/p/itm41965040653f6?pid=TSHGQH82YZK4PZYU&lid=LSTTSHGQH82YZK4PZYU0XFKH0&marketplace=FLIPKART&store=clo%2Fash%2Fank%2Fedy&srno=b_1_1&otracker=hp_rich_navigation_2_1.navigationCard.RICH_NAVIGATION_Fashion~Men%2527s%2BTop%2BWear~Men%2527s%2BT-Shirts_IF56C41VGEYS&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_2_L2_view-all&fm=organic&iid=en_LQhOj2FC1kCJb59clpgS58NprPTYf4qcmqy7b0vFE_bxeB4UPURSVwnc1jVv-yi8oy_fJVPc-UjrIq1faH2jsg%3D%3D&ppt=hp&ppn=homepage&ssid=5iklje08ps0000001714490004375'

request1 = requests.get(url)
# print(request1)

soup = BeautifulSoup(request1.text, 'html.parser')


reviews = soup.findAll('div', {'class':'_11pzQk'})

for review in reviews:
    print(review.get_text() + "\n")

ratings = soup.find('div', {'class' : 'XQDdHH _6er70b'}).get_text()
print(ratings)

allRatings = soup.findAll('div', {'class':'XQDdHH Ga3i8K _9lBNRY'})

for rating in allRatings:
    print(rating.get_text() + "\n")

custName = soup.findAll('p', {'class' : '_2NsDsF AwS1CA MDcJkH'})

for cName in custName:
    print(cName.get_text() + "\n")