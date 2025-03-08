# Trading 212 API ( Beta )

This is a python wrapper for the trading 212 beta API. https://t212public-api-docs.redoc.ly/

## DISCLAIMER
The api is a straight mapping to the trading 212 endpoints.  
- No liability is assumed by me for you using this library.  
- Any trading activity you undertake using this library is solely your own responsibility. 
- No liability will be assumed if you lose your KEY.

## Installation
```
$ pip install trading212-connector
```

## Creating a client

You will need to create a API key from your trading 212 account. Follow trading212's instructions around usage and safeguarding this KEY.

```
>>> from trading212 import Client
>>> client = Client("YOUR_API_KEY")
```
