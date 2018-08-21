import requests


def download_image(image_url):

    try:
        image_name = image_url.split('/')[-1]
    except TypeError:
        image_name = 'image.jpg'

    with open(image_name, 'wb') as handle:
        response = requests.get(image_url, stream=True)

        if not response.ok:
            print(response)
            raise ValueError

        for block in response.iter_content(1024):
            if not block:
                break

            handle.write(block)
