from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/crawl', methods=['GET'])
def crawl_url():
    # Send a GET request to the target URL
    url = "https://bugcrowd.com/crowdstream?filter=disclosures"
    response = requests.get(url)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all div elements with class "bc-crowdstream-item__wrapper"
    divs = soup.find_all('div', {'class': 'bc-crowdstream-item__wrapper'})

    # Extract the link from the first paragraph of each div element
    results = []
    for div in divs:
        link = div.find('p').find('a').get('href')
        results.append(link)

    # Return the link as a JSON object
    return jsonify({'links': results})

if __name__ == '__main__':
    app.run(debug=True)