import re
from osn_currencies_tools.data import tag_to_symbol
from osn_requests import (
	find_web_element,
	get_html
)
from osn_currencies_tools.errors import (
	CurrencyTagNotFoundError,
	ExchangeRateNotFoundError
)


def get_exchange_rate(from_currency_tag: str, to_currency_tag: str) -> float:
	"""
	Fetches the live exchange rate between two currencies from currencylive.com.

	This function scrapes the exchange rate from the currencylive.com website.
	It searches for the exchange rate of 1000 units of the base currency to the target currency.

	Args:
		from_currency_tag (str): The currency tag to exchange from (e.g., 'USD').
		to_currency_tag (str): The currency tag to exchange to (e.g., 'EUR').

	Returns:
		float: The exchange rate between the two currencies.

	Raises:
		ExchangeRateNotFoundError: If the exchange rate is not found on currencylive.com.
		CurrencyTagNotFoundError: If from_currency_tag or to_currency_tag is not a valid currency tag.
	"""
	if from_currency_tag.lower() not in tag_to_symbol.keys():
		raise CurrencyTagNotFoundError(from_currency_tag)
	
	if to_currency_tag.lower() not in tag_to_symbol.keys():
		raise CurrencyTagNotFoundError(to_currency_tag)
	
	exchange_rate_element = find_web_element(
			get_html(
					f"https://currencylive.com/exchange-rate/1000-{from_currency_tag.lower()}-to-{to_currency_tag.lower()}-exchange-rate-today/"
			),
			'//div[@class="rate-info"]/p[@class="text-bold"]',
	)
	
	if exchange_rate_element is None:
		raise ExchangeRateNotFoundError(from_currency_tag, to_currency_tag)
	
	found_exchange_rate = re.search(
			r"\d+\s+%s\s+=\s+(\d+(?:\.\d+)?)\s+%s" % (from_currency_tag.upper(), to_currency_tag.upper()),
			exchange_rate_element.text,
	)
	
	if found_exchange_rate is None:
		raise ExchangeRateNotFoundError(from_currency_tag, to_currency_tag)
	
	return float(found_exchange_rate.group(1))


def exchange_currency(currency_amount: float, from_currency_tag: str, to_currency_tag: str) -> float:
	"""
	Exchanges a given amount of currency from one currency to another using the live exchange rate from currencylive.com.

	Args:
		currency_amount (float): The amount of currency to exchange.
		from_currency_tag (str): The currency tag to exchange from (e.g., 'USD').
		to_currency_tag (str): The currency tag to exchange to (e.g., 'EUR').

	Returns:
	  float: The converted amount of currency in the target currency.

	Raises:
		ExchangeRateNotFoundError: If the exchange rate is not found on currencylive.com.
		CurrencyTagNotFoundError: If from_currency_tag or to_currency_tag is not a valid currency tag.
	"""
	return currency_amount * get_exchange_rate(from_currency_tag, to_currency_tag)
