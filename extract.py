import requests
from bs4 import BeautifulSoup
import csv
import json
import gc

# URL of the AllRecipes category/search page
URL = "https://www.allrecipes.com/recipes-a-z-6735880#alphabetical-list"
# Send HTTP request
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(URL, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")
pages=soup('a', class_='mntl-link-list__link')

# Classes used for recipe cards
CARD_CONTAINER = "tax-sc__recirc-list-container"
CARD_CLASS = "mntl-card-list-items"
CARD_TITLE = "card__title-text"

# Classes used for recipe details
DETAIL_CONTAINER = "mm-recipes-details__content"
DETAIL_CLASS = "mm-recipes-details__item"
DETAIL_LABEL = "mm-recipes-details__label"
DETAIL_VAL = "mm-recipes-details__value"

for page in pages:
    URL=page['href']
    response = requests.get(URL, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    
    del response
    gc.collect()

    # Find all recipe cards
    recipe_cards=[]
    for container in soup("div", class_=CARD_CONTAINER):
        for card in container("a", class_=CARD_CLASS):
            recipe_cards.append(card)

    del soup
    gc.collect()

    # Extract titles and hrefs
    for card in recipe_cards:
        title_tag = card.find("span", class_=CARD_TITLE)
        title = title_tag.get_text(strip=True) if title_tag else "No title"
        link = card["href"]

        response = requests.get(link, headers=headers)
        soup = BeautifulSoup(response.content, "html.parser").body.article
        details = soup.find(class_=DETAIL_CONTAINER)

        del response
        del soup
        gc.collect()

        if not details:
            continue
        deets={}
        for detail in details(class_=DETAIL_CLASS):
            deets[detail.find(class_=DETAIL_LABEL).get_text(strip=True)] = detail.find(class_=DETAIL_VAL).get_text(strip=True)
            
        with open("recipes.jsonl", "a", encoding="utf-8") as f:
            json.dump({"title": title, "url": link, "website": "Allrecipes", "details": deets}, f)
            f.write("\n")
'''
        with open("recipes.csv", mode="a", newline='', encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["title", "url", "website"] + list(deets.keys()))
            if f.tell() == 0:  # File is empty
                writer.writeheader()
            writer.writerow({"title": title, "url": link, "website": "Allrecipes", **deets})
            '''




'''
# Optional: generate HTML file
def generate_html(data, filename="index.html"):
    html = "<html><head><title>Recipes</title></head><body><h1>Recipe Links</h1><ul>"
    for item in data:
        html += f"<li><a href='{item['url']}' target='_blank'>{item['title']}</a></li>\n"
    html += "</ul></body></html>"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(html)

generate_html(recipes)
'''