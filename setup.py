# -*- coding: utf-8 -*-
from setuptools import setup

packages = ["guap", "guap.metrics"]

package_data = {"": ["*"]}

install_requires = ["loguru>=0.5.3,<0.6.0", "numpy>=1.20.2,<2.0.0", "sklearn>=0.0,<0.1"]

setup_kwargs = {
    "name": "guap",
    "version": "0.1.4",
    "description": "",
    "long_description": '<h1 align="center">\n  guap\n</h1>\n\n<h3 align="center">\n From algorithms outputs to business outcomes.\n</h3>\n<p align="center">\nguap is an open-source python package that helps the data team to get ML evaluation metrics everyone can agree on by converting your model output to business outcomes, a.k.a. profits.</p>\n\n<h3 align="center">\n 🤖 \U0001fa84 📈\n</h3>\n\n\n<p align="center">\n  <img src="https://i.imgur.com/sCfpF6d.png">\n</p>\n<p align="center">\n    <a href="https://guap.gitbook.io/guap-docs/">Documentation</a> |\n    <a href="https://colab.research.google.com/drive/1XmqitZzUtK-rohKXgKpjqR16npKjx6m9#offline=true&sandboxMode=true">Colab Demo</a> |\n    <a href="https://twitter.com/guap_ml">Twitter</a> |\n    <a href="https://ulyssebottello.com/">Blog</a> |\n    <a href="https://github.com/guap-ml/guap/projects/1">Public roadmap</a> \n    <br />\n</p>\n\n<p align="center">\n    <a href="https://github.com/chetanraj/awesome-github-badges">\n        <img alt="Made with love" src="https://img.shields.io/badge/Made%20With-Love-orange.svg">\n    </a>\n\t<a href="https://github.com/chetanraj/awesome-github-badges">\n        <img alt="py version" src="https://img.shields.io/badge/python-3.6_|_3.7_|_3.8-blue">\n    </a>\n\t    </a>\n\t<a href="https://github.com/chetanraj/awesome-github-badges">\n        <img alt="version" src="https://img.shields.io/badge/version-0.1.0-gree">\n    </a>\n\n</p>\n\n\n## 🧞\u200d♂️ Why should I use guap?\nOur mission with guap is to align all stakeholders with measurable business outcomes by including the three core teams — business, data science, and IT — throughout the life cycle of the AI models.\n\n* Make collaboration healthier and clearer between tech and non-tech people\n* Make better decisions at every stage of the ML project lifecycle\n\nWant to know more? Read [Why guap exist](https://ulyssebottello.com/why-guap/).\n\n## ✨ Features\nWe\'re on the journey to make sure every ML use-case that goes to production is a valuable one. And it starts with a simple way to estimate the expected profit/cost of a model based on its confusion matrix.\n\n* **Get the total profit** Based on the test set, guap will give you the total expected profit based on the cost matrix. A great way to have an overview of the model profitability.\n* **Average profit per prediction** Along with the total profit score, guap will give you the average profit/cost per prediction. Perfect if you have costs per prediction, or if you need to estimate the profitability while scaling.\n\nThat\'s it...for now! Keep up-to-date with release announcements on Twitter [@guap_ml](https://twitter.com/guap_ml)!\n\n## \U0001fa84 Quick tour\nTo immediately use guap, here is how to quickly generate a profit/cost evaluation metric for a given confusion matrix: \n\nInstall `guap` library:\n```\npip install guap\n```\nFlexible integration for any Python script:\n```python\n>>> !pip install guap\n>>> from guap.metrics import guap_metric\n\n# Set the confusion matrix\n>>> y_true = ["cat", "ant", "cat", "cat", "ant", "bird"]\n>>> y_pred = ["ant", "ant", "cat", "cat", "ant", "cat"]\n\n# Set the cost matrix\n>>> cost_matrix = [[200, -1500], [0, 1000]]\n\n# Generate guap scores\n>>> output = guap_metric(y_true, y_pred, cost_matrix)\n[{\'sum\': -9600, \'average\': -3200}]\n```\n\nEasy, right? \n\n## 👀 Demo\nDo you need a step-by-step guide on how to use guap on a very simple ML use case? We got you.\n\nYou can use guap metrics at every step of the ML lifecycle and on unlimited use-cases. But we think an interactive demo is worth thousands and thousands of words.\n\nWe\'ve picked a situation where we evaluate and compare two simple models on a Kaggle dataset, and a use-case deeply rooted with cost savings: credit card fraud detection.\n\n[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1XmqitZzUtK-rohKXgKpjqR16npKjx6m9#offline=true&sandboxMode=true)\n\n## ⌛ Status\n- [x] Alpha: We are demoing guap to users and receiving feedback\n- [ ] Private Beta\n- [ ] Public Beta\n- [ ] Official Launch\n\nWatch "releases" of this repo to get notified of major updates, and give the star button a click whilst you\'re there.\n\n## 🙏 Contributing\nPull requests are welcome. You don\'t know where to start? let\'s talk [@guap_ml](https://twitter.com/guap_ml)!\n\n## 💖 License\n[Apache License 2.0](http://www.apache.org/licenses/)\n',
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
