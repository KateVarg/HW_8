import pytest


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product_1):
        # TODO напишите проверки на метод check_quantity
        request_quantity = product_1.quantity
        assert product_1.check_quantity(request_quantity) is True  # на складе есть весь товар
        assert product_1.check_quantity(request_quantity - 1) is True  # на складе есть на единицу товара меньше
        assert product_1.check_quantity(request_quantity + 1) is False  # на складе нет товара на единицу больше
        assert product_1.check_quantity(request_quantity // 2) is True  # на складе есть примерно половина товара

    def test_product_buy(self, product_1):
        # TODO напишите проверки на метод buy
        request_quantity = product_1.quantity
        product_1.buy(50)
        assert product_1.quantity == request_quantity - 50

        product_1.buy(product_1.quantity)
        assert product_1.quantity == 0

    def test_product_buy_more_than_available(self, product_1):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError):
            product_1.buy(product_1.quantity + 43)


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """
    def test_add_product(self, cart, product_1, product_2):
        cart.add_product(product_1, 2)
        cart.add_product(product_2, 1)

        assert product_1 and product_2 in cart.products
        assert cart.products[product_1] == 2
        assert cart.products[product_2] == 1

    def test_remove_product(self, cart, product_1, product_2):
        cart.add_product(product_1, 2)
        cart.remove_product(product_1, 4)

        assert product_1 not in cart.products

        cart.clear()
        cart.add_product(product_2, 15)
        cart.remove_product(product_2, 7)

        assert cart.products[product_2] == 8

    def test_clear(self, cart, product_1):
        cart.add_product(product_1, 5)
        cart.clear()

        assert cart.products == {}

    def test_get_total_price(self, cart, product_1, product_2):
        cart.add_product(product_1, 67)
        assert cart.get_total_price(product_1) == product_1.price * 67

    def test_buy(self, cart, product_1, product_2):
        cart.add_product(product_1, 67)
        cart.add_product(product_2, 33)
        cart.buy()

        assert product_1.quantity == 933
        assert product_2.quantity == 567
        assert cart.products == {}

    def test_buy_more_than_available(self, cart, product_1, product_2):
        cart.add_product(product_1, 1067)

        with pytest.raises(ValueError):
            cart.buy()

