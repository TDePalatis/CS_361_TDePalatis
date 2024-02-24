#Image Socket
#Author:Trevor DePalatis

import socket
import hashlib, io, requests, pandas
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from bs4 import BeautifulSoup
from pathlib import Path
from PIL import Image

host = socket.gethostbyname(socket.gethostname())
HOST = '127.0.0.1'
PORT = 9092
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST,PORT))
server.listen(5)

image_list = []

def get_content_from_url(url):
    options = ChromeOptions()
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    pageInfo = driver.page_source
    driver.quit()
    return pageInfo

def parse_image_urls(content, location, source):
    soup = BeautifulSoup(content, "html.parser")
    results = []
    name = soup.find(location)
    if name not in results:
        results.append(name.get(source))
    return results

def get_and_save_image_to_file(image_url, output_path):
    image_visual = requests.get(image_url).content
    image_file = io.BytesIO(image_visual)
    image = Image.open(image_file).convert("RGB")
    filename = hashlib.sha1(image_visual).hexdigest()[:10] + ".png"
    file_path = output_path / filename
    image.save(file_path, "PNG", quality=80)

    image_list.append(file_path)

while True:
    communication_socket, address = server.accept()
    print(f"Connected to {address}")
    url = communication_socket.recv(1024).decode('utf-8')
    print(f"Message from client is: {url}")

    url_content = get_content_from_url(url)
    image_urls = parse_image_urls(
        content=url_content, location="img", source="src")

    for image_url in image_urls:
        get_and_save_image_to_file(#This is where you place the path to where you want your image to appear.
            image_url, output_path=Path("YOUR/PATH/HERE")
        )

    path_address = str(image_list[0])

    communication_socket.send(path_address.encode('utf-8'))

    image_list = []

    communication_socket.close()
    print(f"Connection with {address} ended!")


