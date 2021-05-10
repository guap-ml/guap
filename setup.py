# -*- coding: utf-8 -*-
from setuptools import setup

packages = ["guap", "guap.metrics"]

package_data = {"": ["*"]}

install_requires = ["loguru>=0.5.3,<0.6.0", "numpy>=1.20.2,<2.0.0", "sklearn>=0.0,<0.1"]

setup_kwargs = {
    "name": "guap",
    "version": "0.1.0",
    "description": "",
    "long_description": '<h3 align="center">\n<img src="https://github.com/guap-ml/guap-docs/blob/main/guap.png?raw=true" alt="guap" width="300"></a>\n</h3>\n<h3 align="center">The ✨magical✨ ML evaluation metric everyone can agree on</h3>\n\n<p align="center">\n<strong>\n  <a href="#why-should-i-use-guap">Why Guap?</a> •\n  <a href="#quickstart-install">Quickstart</a> •\n  <a href="https://guap-ml.github.io/guap-docs/">Docs</a> •\n  <a href="https://guap-ml.github.io/guap-docs/blog">Blog</a> •\n  <a href="#license">License</a>\n</strong>\n</p>\n\n<p align="center">\n    <a href="https://github.com/chetanraj/awesome-github-badges">\n        <img alt="Made with love" src="https://img.shields.io/badge/Made%20With-Love-orange.svg">\n    </a>\n\t<a href="https://github.com/chetanraj/awesome-github-badges">\n        <img alt="py version" src="https://img.shields.io/badge/python-3.6_|_3.7_|_3.8-blue">\n    </a>\n\t    </a>\n\t<a href="https://github.com/chetanraj/awesome-github-badges">\n        <img alt="version" src="https://img.shields.io/badge/version-0.1.0-gree">\n    </a>\n</p>\n\n\n\n## Why should I use guap?\nOur mission with guap is to align all stakeholders with measurable business outcomes by including the three core teams — business, data science and IT — throughout the life cycle of the AI models.\n\n- Make collaboration healthier and clearer between tech and non-tech people\n- Make better decisions at every stage of the ML project lifecycle\n\nWant to know more? Read [Why guap exist](https://guap-ml.github.io/guap-docs/blog/why-guap).\n\n## Quickstart Install\n🚧 Under construction, too\n\n## Contributing\nPull requests are welcome. You want to contribute? let\'s talk [@guap_ml](https://twitter.com/guap_ml)!\n\n## License\n[Apache License 2.0](http://www.apache.org/licenses/)\n',
    "author": "Ulysse Bottello",
    "author_email": "ulysse@guap.ml",
    "maintainer": None,
    "maintainer_email": None,
    "url": "https://github.com/guap-ml/guap",
    "packages": packages,
    "package_data": package_data,
    "install_requires": install_requires,
    "python_requires": ">=3.7,<4.0",
}


setup(**setup_kwargs)
