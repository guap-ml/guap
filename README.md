<h1 align="center">
  guap
</h1>

<h3 align="center">
 From algorithms outputs to business outcomes.
</h3>
<p align="center">
guap is an open-source python package that helps data team to get an ML evaluation metrics everyone can agree on by converting your model output to business outcomes, a.k.a. profits.</p>

<h3 align="center">
 🤖 🪄 📈
</h3>


<p align="center">
  <img src="https://i.imgur.com/sCfpF6d.png">
</p>
<p align="center">
    <a href="https://guap.gitbook.io/guap-docs/">Documentation</a> |
    <a href="https://colab.research.google.com/drive/1XmqitZzUtK-rohKXgKpjqR16npKjx6m9#offline=true&sandboxMode=true">Colab Demo</a> |
    <a href="https://twitter.com/guap_ml">Twitter</a> |
    <a href="https://ulyssebottello.com/">Blog</a> |
    <a href="https://github.com/guap-ml/guap/projects/1">Public roadmap</a> 
    <br />
</p>

<p align="center">
    <a href="https://github.com/chetanraj/awesome-github-badges">
        <img alt="Made with love" src="https://img.shields.io/badge/Made%20With-Love-orange.svg">
    </a>
	<a href="https://github.com/chetanraj/awesome-github-badges">
        <img alt="py version" src="https://img.shields.io/badge/python-3.6_|_3.7_|_3.8-blue">
    </a>
	    </a>
	<a href="https://github.com/chetanraj/awesome-github-badges">
        <img alt="version" src="https://img.shields.io/badge/version-0.1.0-gree">
    </a>

</p>


## 🧞‍♂️ Why should I use guap?
Our mission with guap is to align all stakeholders with measurable business outcomes by including the three core teams — business, data science and IT — throughout the life cycle of the AI models.

* Make collaboration healthier and clearer between tech and non-tech people
* Make better decisions at every stage of the ML project lifecycle

Want to know more? Read [Why guap exist](https://ulyssebottello.com/why-guap/).

## ✨ Features
We're on the journey to make sure every ML use-case that go to production is a valuable one. And it starts with a simple way to estimate the expected profit/cost of a model based on its confusion matrix.

* **Get the total profit** Based on the test set, guap will give you the total expected profit based on the cost matrix. A great way to have an overview of the model profitability.
* **Average profit per prediction** Along the total profit score, guap will give you the average profit/cost per prediction. Perfect if you have costs per prediction, or if you need to estimate the profitability while scaling.

That's it...for now! Keep up-to-date with release announcements on Twitter [@guap_ml](https://twitter.com/guap_ml)!

## 🪄 Quick tour
To immediately use guap, here is how to quickly generate a profit/cost evaluation metric for a given confusion matrix: 

Install `guap` library:
```
pip install guap
```
Flexible integration for any Python script:
```python
>>> !pip install guap
>>> from guap.metrics import guap_metric

# Set the confusion matrix
>>> y_true = ["cat", "ant", "cat", "cat", "ant", "bird"]
>>> y_pred = ["ant", "ant", "cat", "cat", "ant", "cat"]

# Set the cost matrix
>>> cost_matrix = [[200, -1500], [0, 1000]]

# Generate guap scores
>>> output = guap_metric(y_true, y_pred, cost_matrix)
[{'sum': -9600, 'average': -3200}]
```

Easy, right? 

## 👀 Demo
You need a step-by-step guide on how to use guap on a very simple ML use-case? We got you.

You can use guap metrics at every step of the ML lifecycle and on unlimited use-cases. But we think an interactive demo is worth thousands and thousands of words.

We've picked a situation where we evaluate and compare two simple models on a Kaggle dataset, and a use-case deeply rooted with cost savings: credit card fraud detection.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1XmqitZzUtK-rohKXgKpjqR16npKjx6m9#offline=true&sandboxMode=true)

## ⌛ Status
- [x] Alpha: We are demoing guap to users and receiving feedback
- [ ] Private Beta
- [ ] Public Beta
- [ ] Official Launch

Watch "releases" of this repo to get notified of major updates, and give the star button a click whilst you're there.

## 🙏 Contributing
Pull requests are welcome. You don't know where to start? let's talk [@guap_ml](https://twitter.com/guap_ml)!

## 💖 License
[Apache License 2.0](http://www.apache.org/licenses/)
