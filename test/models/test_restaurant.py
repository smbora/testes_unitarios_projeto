from src.models.restaurant import Restaurant
class TestRestaurant:

    def test_describe_restaurant(self):
        self.restaurant = Restaurant("Chez Restaurant", "French Cuisine")
        output = self.restaurant

        descricao esperada = f"Esse restaturante chama {self.cuisine_type} and serve {self.cuisine_type}."
        self.assertIN(descricao_esperada, output)

        consumidores_esperados = f"Esse restaturante está servindo {self.number_served} consumidores desde que está aberto."
        self.assertIN(consumidores_esperados, output)

    def test_open_restaurant(self):
        self.restaurant = Restaurant("Chez Restaurant", "French Cuisine")

        assert False

    def test_close_restaurant(self):
        self.restaurant = Restaurant("Chez Restaurant", "French Cuisine")
        assert False

    def test_set_number_served(self,total_customers):
        total_customers = 5
        self.restaurant = Restaurant("Chez Restaurant", "French Cuisine")
        self.restaurant.open_restaurant()

        self.restaurant.set_number_served(total_customers)

        self assertEqual(self.restaurant.number_served, total_customers)

    def test_set_number_served_closed(self, total_customers):
        self.restaurant = Restaurant("Chez Restaurant", "French Cuisine")

    def test_increment_number_served(self):
        self.restaurant = Restaurant("Chez Restaurant", "French Cuisine")
        assert False

    def test_increment_number_served_closed(self):
        self.restaurant = Restaurant("Chez Restaurant", "French Cuisine")

        resposta_esperada = f"{self.restaurant_name} está fechado!"

        assert False