from osn_requests import get_req
from osn_currencies_tools.data import tag_to_symbol
from osn_currencies_tools.errors import (
	CurrencyTagNotFoundError,
	ExchangeRateNotFoundError
)


def get_exchange_rate(api_key: str, from_currency_tag: str, to_currency_tag: str) -> float:
	"""
	Retrieves the exchange rate between two specified currencies using an external API.

	This function fetches the exchange rate from exchangerate-api.com for the given pair of currencies.
	It also validates the provided currency tags against a list of known currency tags.

	Args:
		api_key (str): API key for accessing the exchangerate-api.com.
		from_currency_tag (str): The currency tag to exchange from (e.g., 'USD').
		to_currency_tag (str): The currency tag to convert to (e.g., 'EUR').

	Returns:
		float: The exchange rate representing the value of one unit of `from_currency_tag` in `to_currency_tag`.

	Raises:
		ExchangeRateNotFoundError: If the exchange rate API returns an error or does not provide a success response.
		CurrencyTagNotFoundError: If either `from_currency_tag` or `to_currency_tag` is not found in the list of supported currency tags.
	"""
	if from_currency_tag.lower() not in tag_to_symbol.keys():
		raise CurrencyTagNotFoundError(from_currency_tag)
	
	if to_currency_tag.lower() not in tag_to_symbol.keys():
		raise CurrencyTagNotFoundError(to_currency_tag)
	
	response = get_req(
			url=f"https://v6.exchangerate-api.com/v6/{api_key}/pair/{from_currency_tag.upper()}/{to_currency_tag.upper()}"
	)
	response.raise_for_status()
	
	if response.json()["result"] != "success":
		ExchangeRateNotFoundError(from_currency_tag, to_currency_tag)
	
	found_exchange_rate = response.json()["conversion_rate"]
	
	return float(found_exchange_rate)


def exchange_currency(
		api_key: str,
		currency_amount: float,
		from_currency_tag: str,
		to_currency_tag: str
) -> float:
	"""
	Converts a specified amount from one currency to another using the current exchange rate.

	This function utilizes the `get_exchange_rate` function to fetch the exchange rate and then applies it to convert the given `currency_amount`.

	Args:
		api_key (str): API key for accessing the exchangerate-api.com.
		currency_amount (float): The amount of currency to be exchanged.
		from_currency_tag (str): The currency tag to exchange from (e.g., 'USD').
		to_currency_tag (str): The currency tag to convert to (e.g., 'EUR').

	Returns:
		float: The converted amount in the `to_currency_tag`.

	Raises:
		ExchangeRateNotFoundError: If the exchange rate cannot be retrieved.
		CurrencyTagNotFoundError: If either `from_currency_tag` or `to_currency_tag` is invalid.
	"""
	return currency_amount * get_exchange_rate(api_key, from_currency_tag, to_currency_tag)
