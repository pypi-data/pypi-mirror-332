# Zero-Shot Time Series Forecasting with TabPFN

[![PyPI version](https://badge.fury.io/py/tabpfn-time-series.svg)](https://badge.fury.io/py/tabpfn-time-series)
[![colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/liam-sbhoo/tabpfn-time-series/blob/main/demo.ipynb)
[![Discord](https://img.shields.io/discord/1285598202732482621?color=7289da&label=Discord&logo=discord&logoColor=ffffff)](https://discord.com/channels/1285598202732482621/)
[![arXiv](https://img.shields.io/badge/arXiv-2501.02945-<COLOR>.svg)](https://arxiv.org/abs/2501.02945)

## 📌 News
- **27-01-2025**: 🚀 Ranked _**1st**_ on [GIFT-EVAL](https://huggingface.co/spaces/Salesforce/GIFT-Eval) benchmark<sup>[1]</sup>!
- **10-10-2024**: 🚀 TabPFN-TS [paper](https://arxiv.org/abs/2501.02945) accepted to NeurIPS 2024 [TRL](https://table-representation-learning.github.io/NeurIPS2024/) and [TSALM](https://neurips-time-series-workshop.github.io/) workshops!

_[1] Last checked on: 10/03/2025_

## ✨ Introduction
We demonstrate that the tabular foundation model **[TabPFN](https://github.com/PriorLabs/TabPFN)**, when paired with minimal featurization, can perform zero-shot time series forecasting. Its performance on point forecasting matches or even slightly outperforms state-of-the-art methods.

## 📖 How does it work?

Our work proposes to frame **univariate time series forecasting** as a **tabular regression problem**.

![How it works](docs/tabpfn-ts-method-overview.png)

Concretely, we:
1. Transform a time series into a table
2. Extract features from timestamp and add them to the table
3. Perform regression on the table using TabPFN
4. Use regression results as time series forecasting outputs

For more details, please refer to our [paper](https://arxiv.org/abs/2501.02945) and our [poster](docs/tabpfn-ts-neurips-poster.pdf) (presented at NeurIPS 2024 TRL and TSALM workshops).

## 👉 **Why gives us a try?**
- **Zero-shot forecasting**: this method is extremely fast and requires no training, making it highly accessible for experimenting with your own problems.
- **Point and probabilistic forecasting**: it provides accurate point forecasts as well as probabilistic forecasts.
- **Support for exogenous variables**: if you have exogenous variables, this method can seemlessly incorporate them into the forecasting model.

On top of that, thanks to **[tabpfn-client](https://github.com/automl/tabpfn-client)** from **[Prior Labs](https://priorlabs.ai)**, you won’t even need your own GPU to run fast inference with TabPFN. 😉 We have included `tabpfn-client` as the default engine in our implementation.

## How to use it?

[![colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/liam-sbhoo/tabpfn-time-series/blob/main/demo.ipynb)

The demo should explain it all. 😉

## 📊 GIFT-EVAL Benchmark

We have submitted our results to the [GIFT-EVAL](https://huggingface.co/spaces/Salesforce/GIFT-Eval) benchmark. Stay tuned for results!

For more details regarding the evaluation setup, please refer to [README.md](gift_eval/README.md).
