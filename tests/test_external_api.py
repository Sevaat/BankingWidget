from unittest.mock import patch

import src.external_api as ext_api


@patch("requests.request")
def test_currency_conversions(mock_request):
    mock_data = {
        "operationAmount": {"amount": "1", "currency": {"code": "USD"}},
    }
    mock_request.return_value.text = '{"result": 78.52}'
    assert ext_api.currency_conversions(mock_data) == 78.52
