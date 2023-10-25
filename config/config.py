from configparser import ConfigParser


class Config:
    def __init__(
            self, path
        ):

        self.config = path
        self.parser = ConfigParser()

    def read(
            self
        ):

        self.parser.sections(

        )

        self.parser.read(
            self.config
        )

        return self.parser.get(
            'telegram',
            'token'
        )
