from decimal import Decimal
from datetime import datetime
from thirdwave_sdk.proto import evm_wallet_pb2

class CoinExchangeRate:
    def __init__(self, currency: str, price: Decimal, updated_at: datetime):
        self._currency = currency
        self._price = price
        self._updated_at = updated_at

    @property
    def currency(self) -> str:
        return self._currency
    @property
    def price(self) -> Decimal:
        return self._price
    @property
    def updated_at(self) -> datetime:
        return self._updated_at

    def __repr__(self):
        return f"CoinExchangeRate: currency = {self._currency}, price = {self._price}, updated_at = {self._updated_at}"

class CoinMarketData:
    def __init__(self, exchange_rate, market_cap: Decimal):
        self._exchange_rate = exchange_rate
        self._market_cap = market_cap

    @property
    def exchange_rate(self) -> CoinExchangeRate:
        return self._exchange_rate
    @property
    def market_cap(self) -> Decimal:
        return self._market_cap

    def __repr__(self):
        return f"Coin market data: exchange_rate = {self.exchange_rate}, market_cap = {self.market_cap}"

class NativeTokenMetadata:
    def __init__(self, name: str, symbol: str, image_url: str, market_data: CoinMarketData):
        self._name = name
        self._symbol = symbol
        self._image_url = image_url
        self._market_data = market_data

    @property
    def name(self) -> str:
        return self._name
    @property
    def symbol(self) -> str:
        return self._symbol
    @property
    def image_url(self) -> str:
        return self._image_url
    @property
    def market_data(self) -> CoinMarketData:
        return self._market_data

    def __repr__(self):
        return f"Native token meta-data: name = {self.name}, symbol = {self.symbol}, image_url = {self.image_url}, market_data = {self.market_data}"

    @staticmethod
    def from_grpc(response: evm_wallet_pb2.EvmWalletNativeTokenMetadataResponse):
        return NativeTokenMetadata(
            name=response.token.name,
            symbol=response.token.symbol,
            image_url=response.token.image_url,
            market_data=CoinMarketData(
                exchange_rate=CoinExchangeRate(
                    currency=response.token.market_data.exchange_rate.currency,
                    price=Decimal(response.token.market_data.exchange_rate.price),
                    updated_at=response.token.market_data.exchange_rate.updated_at
                ),
                market_cap=Decimal(response.token.market_data.market_cap)
            )
        )


class Erc20TokenMetadata:
     def __init__(self, name: str, symbol: str, image_url: str, market_data: CoinMarketData):
         self._name = name
         self._symbol = symbol
         self._image_url = image_url
         self._market_data = market_data

     @property
     def name(self) -> str:
         return self._name
     @property
     def symbol(self) -> str:
         return self._symbol
     @property
     def image_url(self) -> str:
         return self._image_url
     @property
     def market_data(self) -> CoinMarketData:
         return self._market_data

     def __repr__(self):
         return f"Erc20 token meta-data: name = {self.name}, symbol = {self.symbol}, image_url = {self.image_url}, market_data = {self.market_data}"

     @staticmethod
     def from_grpc(response: evm_wallet_pb2.EvmWalletErc20TokenMetadataResponse):
         return Erc20TokenMetadata(
             name=response.token.name,
             symbol=response.token.symbol,
             image_url=response.token.image_url,
             market_data=CoinMarketData(
                 exchange_rate=CoinExchangeRate(
                     currency=response.token.market_data.exchange_rate.currency,
                     price=Decimal(response.token.market_data.exchange_rate.price),
                     updated_at=response.token.market_data.exchange_rate.updated_at
                 ),
                 market_cap=Decimal(response.token.market_data.market_cap)
             )
         )