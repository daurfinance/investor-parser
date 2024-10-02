import requests
from bs4 import BeautifulSoup

def get_investor_contacts(keyword, page_limit=5):
    contacts = []
    base_url = f"https://example.com/search?q={keyword}"  # Замените URL на реальный
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    for page in range(1, page_limit + 1):
        url = f"{base_url}&page={page}"
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')

        for investor in soup.find_all('div', class_='investor-contact'):
            name = investor.find('h2').get_text()
            email = investor.find('a', class_='email').get('href').replace('mailto:', '')
            contacts.append({'name': name, 'email': email})

    return contacts

if __name__ == "__main__":
    keyword = input("Введите ключевое слово для поиска инвесторов: ")
    contacts = get_investor_contacts(keyword)

    for contact in contacts:
        print(contact)
