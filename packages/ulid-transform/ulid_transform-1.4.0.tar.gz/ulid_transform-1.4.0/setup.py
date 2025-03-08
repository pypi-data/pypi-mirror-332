# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['ulid_transform']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'ulid-transform',
    'version': '1.4.0',
    'description': 'Create and transform ULIDs',
    'long_description': '# Fast ULID transformations\n\n<p align="center">\n  <a href="https://github.com/bluetooth-devices/ulid-transform/actions/workflows/ci.yml?query=branch%3Amain">\n    <img src="https://img.shields.io/github/actions/workflow/status/bluetooth-devices/ulid-transform/ci.yml?branch=main&label=CI&logo=github&style=flat-square" alt="CI Status" >\n  </a>\n  <a href="https://codecov.io/gh/bluetooth-devices/ulid-transform">\n    <img src="https://img.shields.io/codecov/c/github/bluetooth-devices/ulid-transform.svg?logo=codecov&logoColor=fff&style=flat-square" alt="Test coverage percentage">\n  </a>\n</p>\n<p align="center">\n  <a href="https://python-poetry.org/">\n    <img src="https://img.shields.io/badge/packaging-poetry-299bd7?style=flat-square&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA4AAAASCAYAAABrXO8xAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAJJSURBVHgBfZLPa1NBEMe/s7tNXoxW1KJQKaUHkXhQvHgW6UHQQ09CBS/6V3hKc/AP8CqCrUcpmop3Cx48eDB4yEECjVQrlZb80CRN8t6OM/teagVxYZi38+Yz853dJbzoMV3MM8cJUcLMSUKIE8AzQ2PieZzFxEJOHMOgMQQ+dUgSAckNXhapU/NMhDSWLs1B24A8sO1xrN4NECkcAC9ASkiIJc6k5TRiUDPhnyMMdhKc+Zx19l6SgyeW76BEONY9exVQMzKExGKwwPsCzza7KGSSWRWEQhyEaDXp6ZHEr416ygbiKYOd7TEWvvcQIeusHYMJGhTwF9y7sGnSwaWyFAiyoxzqW0PM/RjghPxF2pWReAowTEXnDh0xgcLs8l2YQmOrj3N7ByiqEoH0cARs4u78WgAVkoEDIDoOi3AkcLOHU60RIg5wC4ZuTC7FaHKQm8Hq1fQuSOBvX/sodmNJSB5geaF5CPIkUeecdMxieoRO5jz9bheL6/tXjrwCyX/UYBUcjCaWHljx1xiX6z9xEjkYAzbGVnB8pvLmyXm9ep+W8CmsSHQQY77Zx1zboxAV0w7ybMhQmfqdmmw3nEp1I0Z+FGO6M8LZdoyZnuzzBdjISicKRnpxzI9fPb+0oYXsNdyi+d3h9bm9MWYHFtPeIZfLwzmFDKy1ai3p+PDls1Llz4yyFpferxjnyjJDSEy9CaCx5m2cJPerq6Xm34eTrZt3PqxYO1XOwDYZrFlH1fWnpU38Y9HRze3lj0vOujZcXKuuXm3jP+s3KbZVra7y2EAAAAAASUVORK5CYII=" alt="Poetry">\n  </a>\n  <a href="https://github.com/ambv/black">\n    <img src="https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square" alt="black">\n  </a>\n  <a href="https://github.com/pre-commit/pre-commit">\n    <img src="https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white&style=flat-square" alt="pre-commit">\n  </a>\n  <a href="https://codspeed.io/bluetooth-devices/ulid-transform"><img src="https://img.shields.io/endpoint?url=https://codspeed.io/badge.json" alt="CodSpeed Badge"/></a>\n</p>\n<p align="center">\n  <a href="https://pypi.org/project/ulid-transform/">\n    <img src="https://img.shields.io/pypi/v/ulid-transform.svg?logo=python&logoColor=fff&style=flat-square" alt="PyPI Version">\n  </a>\n  <img src="https://img.shields.io/pypi/pyversions/ulid-transform.svg?style=flat-square&logo=python&amp;logoColor=fff" alt="Supported Python versions">\n  <img src="https://img.shields.io/pypi/l/ulid-transform.svg?style=flat-square" alt="License">\n</p>\n\nCreate and transform ULIDs\n\nThis library will use the CPP implementation from https://github.com/suyash/ulid if cython is available, and will fallback to pure python if it is not.\n\n## Example\n\n```python\n>>> import ulid_transform\n>>> ulid_transform.ulid_hex()\n\'01869a2ea5fb0b43aa056293e47c0a35\'\n>>> ulid_transform.ulid_now()\n\'0001HZX0NW00GW0X476W5TVBFE\'\n>>> ulid_transform.ulid_at_time(1234)\n\'000000016JC62D620DGYNG2R8H\'\n>>> ulid_transform.ulid_to_bytes(\'0001HZX0NW00GW0X476W5TVBFE\')\nb\'\\x00\\x00c\\xfe\\x82\\xbc\\x00!\\xc0t\\x877\\x0b\\xad\\xad\\xee\'\n>> ulid_transform.bytes_to_ulid(b"\\x01\\x86\\x99?\\xe8\\xf3\\x11\\xbc\\xed\\xef\\x86U.9\\x03z")\n\'01GTCKZT7K26YEVVW6AMQ3J0VT\'\n>>> ulid_transform.ulid_to_bytes_or_none(\'0001HZX0NW00GW0X476W5TVBFE\')\nb\'\\x00\\x00c\\xfe\\x82\\xbc\\x00!\\xc0t\\x877\\x0b\\xad\\xad\\xee\'\n>>> ulid_transform.ulid_to_bytes_or_none(None)\n>>> ulid_transform.bytes_to_ulid_or_none(b\'\\x00\\x00c\\xfe\\x82\\xbc\\x00!\\xc0t\\x877\\x0b\\xad\\xad\\xee\')\n\'0001HZX0NW00GW0X476W5TVBFE\'\n>>> ulid_transform.bytes_to_ulid_or_none(None)\n```\n\n## Installation\n\nInstall this via pip (or your favourite package manager):\n\n`pip install ulid-transform`\n\n## Contributors ✨\n\nThanks to https://github.com/suyash/ulid which provides the cython implementation guts.\n\nThanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):\n\n<!-- prettier-ignore-start -->\n<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->\n<!-- markdownlint-disable -->\n<!-- markdownlint-enable -->\n<!-- ALL-CONTRIBUTORS-LIST:END -->\n<!-- prettier-ignore-end -->\n\nThis project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!\n\n## Credits\n\nThis package was created with\n[Copier](https://copier.readthedocs.io/) and the\n[browniebroke/pypackage-template](https://github.com/browniebroke/pypackage-template)\nproject template.\n',
    'author': 'J. Nick Koston',
    'author_email': 'nick@koston.org',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/bluetooth-devices/ulid-transform',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.11,<4.0',
}
from build_ext import *
build(setup_kwargs)

setup(**setup_kwargs)
