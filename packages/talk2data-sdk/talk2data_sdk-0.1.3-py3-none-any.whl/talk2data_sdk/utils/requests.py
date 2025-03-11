from json import JSONDecodeError
from typing import Union

import requests
from requests.auth import HTTPBasicAuth
from requests.cookies import RequestsCookieJar

from talk2data_sdk.constants import REQUEST_TIME_OUT
from talk2data_sdk.logging import logger


def post(
    url: str,
    *,
    json: dict = None,
    headers: dict = None,
    cookies: dict = None,
    auth: tuple = None,
    timeout: int = REQUEST_TIME_OUT,
) -> Union[list, dict]:
  """
  Send a POST request to the given URL with the given data and headers.
  """
  cookie_jar = RequestsCookieJar()
  if cookies:
    for key, value in cookies.items():
      cookie_jar.set(key, value)
  res = requests.post(
      url,
      json=json,
      headers=headers,
      cookies=cookie_jar,
      timeout=timeout,
      auth=HTTPBasicAuth(*auth) if auth else None,
  )
  try:
    res.raise_for_status()
  except requests.exceptions.HTTPError as e:
    logger.error("Failed to send POST request to %s: %s", url, res.text)
    raise e
  try:
    return res.json()
  except JSONDecodeError as e:
    logger.error("Failed to decode response as JSON: %s", res.text)
    raise e
