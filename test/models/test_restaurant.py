import pytest
from src.models.restaurant import Restaurant


class TestRestaurant:

    restaurant_name = "Chez Restaurant"
    cuisine_type = "French cuisine"

    @pytest.fixture
    def restaurant(self):
        return Restaurant(self.restaurant_name, self.cuisine_type)

    @pytest.fixture
    def restaurant_open(self, restaurant):
        restaurant.open_restaurant()
        return restaurant

    def test_describe_restaurant(self, restaurant):
        resultado_esperado = f'Esse restaurante se chama {self.restaurant_name} e serve {self.cuisine_type} e atendeu  0 consumidores desde que está aberto.'
        resultado = restaurant.describe_restaurant()
        assert resultado == resultado_esperado

    def test_open_restaurant_aberto(self, restaurant_open):
        resultado = restaurant_open.open_restaurant()
        resultado_esperado = f"{self.restaurant_name} já está aberto!"
        assert resultado == resultado_esperado

    def test_open_restaurant_fechado(self, restaurant):
        resultado = restaurant.open_restaurant()
        resultado_esperado = f"{self.restaurant_name} agora está aberto!"
        assert resultado == resultado_esperado

    def test_close_restaurant_aberto(self, restaurant_open):
        resultado = restaurant_open.close_restaurant()
        resultado_esperado = f"{self.restaurant_name} agora está fechado!"
        assert resultado == resultado_esperado

    def test_close_restaurant_fechado(self, restaurant):
        resultado = restaurant.close_restaurant()
        resultado_esperado = f"{self.restaurant_name} já está fechado!"
        assert resultado == resultado_esperado

    def test_set_number_served(self, restaurant_open):
        total_customers = 5
        restaurant_open.set_number_served(total_customers)
        resultado = restaurant_open.get_number_served()
        resultado_esperado = f"{total_customers} clientes foram atendidos ate o momento"
        assert resultado == resultado_esperado

    def test_set_number_served_closed(self, restaurant):
        total_customers = 5
        resposta_esperada = f"{self.restaurant_name} está fechado!"
        resposta = restaurant.set_number_served(total_customers)
        assert (resposta == resposta_esperada)
        assert (restaurant.number_served == 0)

    def test_set_number_served_invalid(self, restaurant_open):
        total_customers = "Cinco"
        resposta = restaurant_open.set_number_served(total_customers)
        resposta_esperada = "Valor informado não é valido!"
        assert (resposta == resposta_esperada)

    def test_increment_number_served(self, restaurant_open):
        more_customers = 10
        resposta_esperada = f"{more_customers} foram adicionados aos 0 clientes já atendidos"
        resposta = restaurant_open.increment_number_served(more_customers)
        assert (resposta == resposta_esperada)
        assert (restaurant_open.get_number_served() == f"{more_customers} clientes foram atendidos ate o momento")

    def test_increment_number_served_not_empty(self, restaurant_open):
        more_customers = 10
        restaurant_open.increment_number_served(more_customers)
        even_more_customers = 15
        resposta_esperada = f"{even_more_customers} foram adicionados aos {more_customers} clientes já atendidos"
        resposta = restaurant_open.increment_number_served(even_more_customers)
        assert (resposta == resposta_esperada)
        assert (restaurant_open.get_number_served() == f"{more_customers+even_more_customers} clientes foram atendidos ate o momento")

    def test_increment_number_served_closed(self, restaurant):
        more_customers = 10
        resposta_esperada = f"{self.restaurant_name} está fechado!"
        resposta = restaurant.increment_number_served(more_customers)
        assert (resposta == resposta_esperada)

    def test_increment_number_served_open_invalid(self, restaurant_open):
        more_customers = "Dez"
        resposta_esperada = "Valor informado não é valido!"
        resposta = restaurant_open.increment_number_served(more_customers)
        assert (resposta == resposta_esperada)

    def test_increment_number_served_clode_invalid(self, restaurant):
        more_customers = "Dez"
        resposta_esperada = "Valor informado não é valido!"
        resposta = restaurant.increment_number_served(more_customers)
        assert (resposta == resposta_esperada)