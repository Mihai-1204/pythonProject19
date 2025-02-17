from utils.fuel import Fuel
from utils.init_config import config


class Diesel(Fuel):
    def __init__(self, config: dict):
        super().__init__(config)


if __name__ == '__main__':
    diesel1 = Diesel(config)
    diesel1.get_prices()
    print(diesel1.last_price, diesel1.average_price)