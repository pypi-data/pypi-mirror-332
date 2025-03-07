class DerivativeConverter:
    """Main index price convert into financial derivative price"""

    _default_precision = 2

    def __init__(self, index_price: float, derivative_price: float) -> None:
        self.index_price = index_price
        self.derivative_price = derivative_price

    @property
    def derivative_price_precision(self) -> int:
        return len(str(self.derivative_price).split(".")[1]) if "." in str(self.derivative_price) else self._default_precision

    def tgt_derivative_price(self, tgt_index_price: float) -> float:
        return round(self.derivative_price * tgt_index_price / self.index_price, self.derivative_price_precision)
