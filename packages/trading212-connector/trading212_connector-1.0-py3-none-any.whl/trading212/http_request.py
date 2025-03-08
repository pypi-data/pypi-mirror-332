import requests
import json


class Client:
    """
    Trading212 http client.
    """
    END_POINTS = dict(
        get_exchanges='/equity/metadata/exchanges',
        get_instruments='/equity/metadata/instruments',
        get_pies='/equity/pies',
        get_pie='/equity/pies/{id}',
        create_pie='/equity/pies',
        update_pie='/equity/pies/{id}',
        delete_pie='/equity/pies/{id}',
        get_orders='/equity/orders/',
        get_order='/equity/orders/{id}',
        delete_order='/equity/orders/{id}',
        place_limit_order='/equity/orders/limit',
        place_market_order='/equity/orders/market',
        place_stop_order='/equity/orders/stop',
        place_stop_limit_order='/equity/orders/stop_limit',
        get_account_cash='/equity/account/cash',
        get_account='/equity/account/info',
        get_all_open_positions='/equity/portfolio',
        search_position_by_ticker='/equity/portfolio/ticker',
        get_position='/equity/portfolio/{ticker}',
        get_order_history='/equity/history/orders',
        get_dividends='/history/dividends',
        get_exports='/history/exports',
        get_transactions='/history/transactions',
        get_exports_as_csv='/history/exports'
    )

    def __init__(self, api_key: str, domain: str = None, version: str = 'v0'):
        """
        Constructor for the trading212 client.

        >>> from trading212 import Client
        >>> c = Client('YOUR_API_KEY')
        >>> c = Client('YOUR_API_KEY', domain='demo.trading212.com', version='v0')

        :param str api_key: The API key for authentication.
        :param str domain: The domain for the API (default is 'live.trading212.com').
        :param str version: The API version (default is 'v0').
        """
        self.API_KEY = api_key
        self.DOMAIN = domain or 'live.trading212.com'
        self.VERSION_PATH = f'/api/{version}'
        self.BASE_URL = f'https://{self.DOMAIN}{self.VERSION_PATH}'
        self.AUTH = {'Authorization': self.API_KEY}

    def _get(self, url: str, headers: dict, params: dict = None) -> dict:
        """
        This method handles all HTTP GET requests.

        :param str url: The URL for this request.
        :param dict headers: The HTTP headers to be applied to this request.
        :param dict params: The query parameters to be included in the request (default is None).
        :return: The JSON response from the GET request.
        :rtype: dict
        :raises Exception: If the HTTP request fails, an exception is raised with the status code and response text.
        """
        headers.update(self.AUTH)
        resp = requests.get(f'{self.BASE_URL}{url}', headers=headers, params=params)
        if resp.ok:
            return resp.json()
        else:
            raise Exception(f"{resp.status_code} - {resp.text}")

    def _delete(self, url: str, headers: dict, params: dict = None) -> dict:
        """
        Sends a DELETE request to the specified URL with the given headers and parameters.

        :param str url: The URL for this request.
        :param dict headers: The HTTP headers to be applied to this request.
        :param dict params: The query parameters to be included in the request (default is None).
        :return: The JSON response from the DELETE request.
        :rtype: dict
        :raises requests.HTTPError: If the HTTP request fails, an HTTPError is raised with the status code and response text.
        """
        headers.update(self.AUTH)
        resp = requests.delete(f'{self.BASE_URL}{url}', headers=headers, params=params)
        if resp.ok:
            return resp.json()
        else:
            raise requests.HTTPError(f"{resp.status_code} - {resp.text}")

    def _post(self, url: str, headers: dict, payload: dict) -> dict:
        """
        Sends a POST request to the specified URL with the given headers and payload.

        :param str url: The URL for this request.
        :param dict headers: The HTTP headers to be applied to this request.
        :param dict payload: The JSON payload to be included in the request.
        :return: The JSON response from the POST request.
        :rtype: dict
        :raises requests.HTTPError: If the HTTP request fails, an HTTPError is raised with the status code and response text.
        """
        headers.update(self.AUTH)
        resp = requests.post(f'{self.BASE_URL}{url}', headers=headers, json=payload)
        if resp.ok:
            return resp.json()
        else:
            raise requests.HTTPError(f"HTTP {resp.status_code} - {resp.text}")

    def get_exchanges(self) -> dict:
        """
        Returns an array of all exchanges.

        https://t212public-api-docs.redoc.ly/#operation/exchanges
        """
        return self._get(self.END_POINTS['get_exchanges'], {})

    def get_instruments(self) -> dict:
        """
        Returns a list of all instruments ( Stocks, ETFs, CFDs etc. )

        https://t212public-api-docs.redoc.ly/#operation/instruments
        """
        return self._get(self.END_POINTS['get_instruments'], {})

    def get_pies(self) -> dict:
        """
        Returns a list of pies.

        https://t212public-api-docs.redoc.ly/#operation/getAll
        """
        return self._get(self.END_POINTS['get_pies'], {})

    def get_pie(self, id: int) -> dict:
        """
        Gets a specific pie by id.

        https://t212public-api-docs.redoc.ly/#operation/getDetailed

        :params int id: the id of the pie.
        """
        return self._get(self.END_POINTS['get_pie'].format(id=id), {})

    def create_pie(self, dividend_cash_action: str, end_date: str, goal: float, icon: str, instrument_shares: dict, name: str) -> dict:
        """
        Creates a new pie.

        https://t212public-api-docs.redoc.ly/#operation/create

        :param str dividend_cash_action: The action to take with dividend cash.
        :param str end_date: The end date for the pie.
        :param float goal: The goal amount for the pie.
        :param str icon: The icon for the pie.
        :param dict instrument_shares: The shares of instruments in the pie.
        :param str name: The name of the pie.
        """
        payload = dict(
            dividendCashAction=dividend_cash_action,
            endData=end_date,
            goal=goal,
            icon=icon,
            instrumentShares=instrument_shares,
            name=name
        )
        headers = {'Content-Type': 'application/json'}
        return self._post(self.END_POINTS['create_pie'], headers, payload)

    def update_pie(self, id: int, dividend_cash_action: str, end_date: str, goal: float, icon: str, instrument_shares: dict, name: str) -> dict:
        """
        Save changes and update an existing pie.

        https://t212public-api-docs.redoc.ly/#operation/create

        :param int id: The id of the pie to update.
        :param str dividend_cash_action: The action to take with dividend cash.
        :param str end_date: The end date for the pie.
        :param float goal: The goal amount for the pie.
        :param str icon: The icon for the pie.
        :param dict instrument_shares: The shares of instruments in the pie.
        :param str name: The name of the pie.
        """
        payload = dict(
            dividendCashAction=dividend_cash_action,
            endDate=end_date,
            goal=goal,
            icon=icon,
            instrumentShares=instrument_shares,
            name=name
        )
        headers = {'Content-Type': 'application/json'}
        return self._post(self.END_POINTS['update_pie'].format(id=id), headers, payload)

    def delete_pie(self, id: int) -> dict:
        """
        Remove or delete an existing pie created by for this account.

        https://t212public-api-docs.redoc.ly/#operation/delete

        :param int id: The id of the pie to delete.
        """
        return self._delete(self.END_POINTS['delete_pie'].format(id=id), {})

    def get_orders(self) -> dict:
        """
        Get a list of all orders for this account.

        https://t212public-api-docs.redoc.ly/#operation/orders
        """
        return self._get(self.END_POINTS['get_orders'], {})

    def get_order(self, id: int) -> dict:
        """
        Get a specific order for this account.

        https://t212public-api-docs.redoc.ly/#operation/orders

        :param int id: The id of the order.
        """
        return self._get(self.END_POINTS['get_order'].format(id=id), {})

    def delete_order(self, id: int) -> dict:
        """
        Delete an existing order for this account.

        https://t212public-api-docs.redoc.ly/#operation/cancelOrder

        :param int id: The id of the order.
        """
        return self._delete(self.END_POINTS['delete_order'].format(id=id), {})

    def place_limit_order(self, limit_price: float, quantity: float, ticker: str, time_validity: str) -> dict:
        """
        Place a new limit order for an instrument on this account.
        Limit orders activate when the asset price reaches the limit order price.
        There is no guarantee that the limit order will fill when volatility is high.

        https://t212public-api-docs.redoc.ly/#operation/placeLimitOrder

        :param float limit_price: The limit price for the order.
        :param float quantity: The quantity of the instrument to order.
        :param str ticker: The ticker symbol of the instrument.
        :param str time_validity: The time validity of the order.
        """
        payload = dict(
            limitPrice=limit_price,
            quantity=quantity,
            ticker=ticker,
            timeValidity=time_validity
        )
        headers = {'Content-Type': 'application/json'}
        return self._post(self.END_POINTS['place_limit_order'], headers, payload)

    def place_market_order(self, quantity: float, ticker: str) -> dict:
        """
        Place a new market order for an instrument on this account.
        The market order can settle at an unexpected price during volatility.

        https://t212public-api-docs.redoc.ly/#operation/placeLimitOrder

        :param float quantity: The quantity of the instrument to order.
        :param str ticker: The ticker symbol of the instrument.
        """
        payload = dict(
            quantity=quantity,
            ticker=ticker
        )
        headers = {'Content-Type': 'application/json'}
        return self._post(self.END_POINTS['place_market_order'], headers, payload)

    def place_stop_order(self, stop_price: float, quantity: float, ticker: str, time_validity: str) -> dict:
        """
        The stop order will convert to a market order when the stop price is reached.

        https://t212public-api-docs.redoc.ly/#operation/placeStopOrder

        :param float stop_price: The stop price for the order.
        :param float quantity: The quantity of the instrument to order.
        :param str ticker: The ticker symbol of the instrument.
        :param str time_validity: The time validity of the order.
        """
        payload = dict(
            stopPrice=stop_price,
            quantity=quantity,
            ticker=ticker,
            timeValidity=time_validity
        )
        headers = {'Content-Type': 'application/json'}
        return self._post(self.END_POINTS['place_stop_order'], headers, payload)

    def place_stop_limit_order(self, limit_price: float, stop_price: float, quantity: float, ticker: str, time_validity: str) -> dict:
        """
        The stop order will convert to a limit order when the stop price is reached.

        https://t212public-api-docs.redoc.ly/#operation/placeStopLimitOrder

        :param float limit_price: The limit price for the order.
        :param float stop_price: The stop price for the order.
        :param float quantity: The quantity of the instrument to order.
        :param str ticker: The ticker symbol of the instrument.
        :param str time_validity: The time validity of the order.
        """
        payload = dict(
            limitPrice=limit_price,
            stopPrice=stop_price,
            quantity=quantity,
            ticker=ticker,
            timeValidity=time_validity
        )
        headers = {'Content-Type': 'application/json'}
        return self._post(self.END_POINTS['place_stop_limit_order'], headers, payload)

    def get_account_cash(self) -> dict:
        """
        Get the account balance.

        https://t212public-api-docs.redoc.ly/#operation/accountCash
        """
        return self._get(self.END_POINTS['get_account_cash'], {})

    def get_account(self) -> dict:
        """
        Get the account detals.
        https://t212public-api-docs.redoc.ly/#operation/account
        """
        return self._get(self.END_POINTS['get_account'], {})

    def get_positions(self) -> dict:
        """
        Get a list of all open positions.

        https://t212public-api-docs.redoc.ly/#operation/portfolio
        """
        return self._get(self.END_POINTS['get_all_open_positions'], {})

    def get_position(self, ticker: str) -> dict:
        """
        Get a specific position by id.

        https://t212public-api-docs.redoc.ly/#operation/positionByTicker

        :param str ticker: The ticker symbol of the position.
        """
        return self._get(self.END_POINTS['get_position'].format(ticker=ticker), {})

    def get_order_history(self, cursor: int, ticker: str, limit: int) -> dict:
        """
        Get a page of order history for a ticker where the page id is the cursor.
        The number of items in the page is set by the limit variable.

        https://t212public-api-docs.redoc.ly/#operation/orders_1

        :param int cursor: The cursor for pagination.
        :param str ticker: The ticker symbol of the instrument.
        :param int limit: The number of items to return per page.
        """
        query = {
            "cursor": cursor,
            "ticker": ticker,
            "limit": limit
        }
        return self._get(self.END_POINTS['get_order_history'], {}, query)

    def get_dividends(self, cursor: int, ticker: str, limit: int) -> dict:
        """
        Get a page of dividend payments for a ticker where the page id is the cursor.
        The number of items in the page is set by the limit variable.

        https://t212public-api-docs.redoc.ly/#operation/dividends

        :param int cursor: The cursor for pagination.
        :param str ticker: The ticker symbol of the instrument.
        :param int limit: The number of items to return per page.
        """
        query = {
            "cursor": cursor,
            "ticker": ticker,
            "limit": limit
        }
        return self._get(self.END_POINTS['get_dividends'], {}, query)

    def get_exports(self) -> dict:
        """
        Get a list of exports.

        https://t212public-api-docs.redoc.ly/#operation/getReports
        """
        return self._get(self.END_POINTS['get_exports'], {})

    def get_transactions(self, cursor: int, limit: int) -> dict:
        """
        Get a page of transactions data where the page id is cursor.
        The number of items in the page is set by the limit variable.

        https://t212public-api-docs.redoc.ly/#operation/transactions

        :param int cursor: The cursor for pagination.
        :param int limit: The number of items to return per page.
        """
        query = {
            "cursor": cursor,
            "limit": limit
        }
        return self._get(self.END_POINTS['get_transactions'], {}, query)

    def get_exports_as_csv(self, data_included: dict, time_from: str, time_to: str) -> dict:
        """
        Get export as a csv file. The records in the csv file are for dates
        between time_from and time_to.

        https://t212public-api-docs.redoc.ly/#operation/placeStopLimitOrder

        :param dict data_included: The data to be included in the export.
        :param str time_from: The start time for the export.
        :param str time_to: The end time for the export.
        """
        payload = dict(
            dataIncluded=data_included,
            timeFrom=time_from,
            timeTo=time_to
        )
        headers = {'Content-Type': 'application/json'}
        return self._post(self.END_POINTS['get_exports_as_csv'], headers, payload)
