import yaml
from pathlib import Path


class Config:
    def __init__(self, url_resources=None):
        self.path = self._Path(url_resources)
        self.config = self._Config(self)

    class _Path:
        def __init__(self, url_resources):
            self.base_dir = Path().cwd()
            self.resources = self.base_dir / 'simera_resources' if url_resources is None else url_resources
            self.config = self.base_dir / 'simera/config'

    class _Config:
        def __init__(self, parent):
            self._parent = parent
            self.country = self.read_yaml('country.yaml')
            self.currency = self.read_yaml('currency.yaml')  # future via API (e.g. https://exchangeratesapi.io/)
            self.uom = self.read_yaml('uom.yaml')

        def read_yaml(self, filename):
            file_url = self._parent.path.config / filename
            with open(file_url, 'r') as file:
                file_content = yaml.safe_load(file)
            return file_content


if __name__ == '__main__':
    sc = Config()
    print(sc.config.country['PL']['fullname'])
    print(sc.config.currency.get('EUR').get('PLN'))

