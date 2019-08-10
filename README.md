# DeepTrade Python Library


The DeepTrade Python library provides convenient access to the DeepTrade API from
applications written in the Python language. It includes a pre-defined set of
classes for API resources that initialize themselves dynamically from API
responses.

## Documentation

See the [Python API docs](https://deeptrade.ch/docs/).

## Installation

You don't need this source code unless you want to modify the package. If you just
want to use the package, just run:

```sh
pip install --upgrade deeptrade
```

Install from source with:

```sh
python setup.py install
```

### Requirements

- Python 2.7+ or Python 3.4+ (PyPy supported)

## Usage

The library needs to be configured with your account's secret key which is
available in your [DeepTrade Dashboard][api-keys]. Set `deeptrade.api_key` to its
value:

```python
import deeptrade
deeptrade.api_key = "123abc_..."

# get sentiment by date
deeptrade.Sentiment().by_date(date='2018-02-23',dataframe=True)
```