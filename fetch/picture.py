from requests import get
from shutil import copyfileobj


class Picture:
    def __init__(
            self, src,
        ):

        self.page = src


    def download(
            self, id
        ):

        response = get(
            self.page, stream=True
        )

        if (response.status_code == 200):
            with open(
                f'../imgs/{id}.png', 'wb'
            ) as file:
                copyfileobj(
                    response.raw, file
                )
