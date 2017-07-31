import configparser


class PropertyReader(object):
    def __init__(self, file_name: str):
        self._config = configparser.ConfigParser()
        self._config_file = file_name

    def get_browser_name(self) -> str:
        self._config.read(self._config_file)
        return self._config.get('browser settings', 'browser')

    def get_browser_port(self) -> int:
        self._config.read(self._config_file)
        return int(self._config.get('browser settings', 'browser_port'))
