import pytest

from tradex.utils.derivative import DerivativeConverter


@pytest.mark.parametrize(
    ("index_price", "derivative_price", "tgt_index_price", "expected"),
    [
        (683.397, 0.78, 1021.3213, 1.17),
        (683.397, 0.782, 1135, 1.299),
        (683.397, 1, 1700, 2.49),
    ],
)
def test_tgt_derivative_price(index_price, derivative_price, tgt_index_price, expected):
    converter = DerivativeConverter(index_price=index_price, derivative_price=derivative_price)
    tgt_derivative_price = converter.tgt_derivative_price(tgt_index_price)
    assert tgt_derivative_price == expected
