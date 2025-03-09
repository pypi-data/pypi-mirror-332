from osn_requests import get_req
from osn_currencies_tools.data import tag_to_symbol
from osn_currencies_tools.errors import (
	CurrencyTagNotFoundError,
	ExchangeRateNotFoundError
)


def get_exchange_rate(app_id: str, from_currency_tag: str, to_currency_tag: str) -> float:
	"""
	Gets the exchange rate between two currencies using Open Exchange Rates API.

	Args:
		app_id (str): App ID for Open Exchange Rates API.
		from_currency_tag (str): The currency tag to exchange from (e.g., 'USD').
		to_currency_tag (str): The currency tag to exchange to (e.g., 'EUR').

	Returns:
		float: The exchange rate between the two currencies.

	Raises:
		ExchangeRateNotFoundError: If the exchange rate API returns an error or does not provide a success response.
		CurrencyTagNotFoundError: If either `from_currency_tag` or `to_currency_tag` is not found in the list of supported currency tags.
	"""
	if from_currency_tag.lower() not in tag_to_symbol.keys():
		raise CurrencyTagNotFoundError(from_currency_tag)
	
	if to_currency_tag.lower() not in tag_to_symbol.keys():
		raise CurrencyTagNotFoundError(to_currency_tag)
	
	response = get_req(
			url=f"https://openexchangerates.org/api/latest.json?app_id={app_id}&base={from_currency_tag.upper()}"
	)
	response.raise_for_status()
	
	if to_currency_tag.upper() not in response.json()["rates"].keys():
		ExchangeRateNotFoundError(from_currency_tag, to_currency_tag)
	
	found_exchange_rate = response.json()["rates"][to_currency_tag.upper()]
	
	return float(found_exchange_rate)


def exchange_currency(
		app_id: str,
		currency_amount: float,
		from_currency_tag: str,
		to_currency_tag: str
) -> float:
	"""
	Exchanges a given amount of currency from one currency to another using the exchange rate from Open Exchange Rates API.

	Args:
		app_id (str): App ID for Open Exchange Rates API.
		currency_amount (float): The amount of currency to exchange.
		from_currency_tag (str): The currency tag to exchange from (e.g., 'USD').
		to_currency_tag (str): The currency tag to exchange to (e.g., 'EUR').

	Returns:
		float: The converted amount of currency in the target currency.

	Raises:
		ExchangeRateNotFoundError: If the exchange rate cannot be retrieved.
		CurrencyTagNotFoundError: If either `from_currency_tag` or `to_currency_tag` is invalid.
	"""
	return currency_amount * get_exchange_rate(app_id, from_currency_tag, to_currency_tag)
