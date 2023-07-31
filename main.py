import os
import sys

import requests
from bs4 import BeautifulSoup


def download_image(image_url, save_directory):
    # Send an HTTP request to get the image data
    response = requests.get(image_url)
    if response.status_code == 200:
        # Get the file name from the URL
        file_name = image_url.split('/')[-1]

        # Combine the file name with the save directory to get the full file path
        file_path = os.path.join(save_directory, file_name)

        # Save the image to the specified directory
        with open(file_path, 'wb') as f:
            f.write(response.content)
        print(f"Image '{file_name}' downloaded successfully.")
    else:
        print(f"Failed to download image. Status code: {response.status_code}")


def is_folder_empty(folder_path):
    # Check if the folder exists
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)

    # Get the list of files and directories in the folder
    items = os.listdir(folder_path)

    # Check if the list is empty
    return len(items) == 0


def main():
    root_url = sys.argv[1]
    temp_url = root_url.replace('index.html', '')
    folder_name = root_url.split('/')[-2]
    save_directory = os.path.join(r'D:\UDEMY_Workspace\__downloads\_images', folder_name)
    if is_folder_empty(save_directory):
        print(f"folder path is empty, you can save the files.")
    else:
        raise Exception(f"Folder path not empty: {save_directory}")

    result = requests.get(root_url)
    content = result.text

    soup = BeautifulSoup(content, 'lxml')
    # print(soup.prettify())
    anchor_links = soup.find_all('a', href=True)

    href_links = []
    img_links = []
    for link in anchor_links:
        href_link = link['href']
        if href_link.startswith('pages/'):
            img_tag = link.find('img')
            img_link = img_tag['src']
            img_links.append(img_link.replace('th_', ''))
        href_links.append(href_link)

    for img_link in img_links:
        img_url = temp_url + img_link
        try:
            download_image(image_url=img_url, save_directory=save_directory)
        except Exception as E:
            print(f"Exception: {E}")
            continue
    print('completed.')


if __name__ == '__main__':
    main()
