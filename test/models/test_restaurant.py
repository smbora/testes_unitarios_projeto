from src.models.restaurant import Restaurant
class TestRestaurant:

    restaurant_name = "Chez Restaurant"
    cuisine_type = "French cuisine"
    def test_describe_restaurant(self):
        restaurant = Restaurant(self.restaurant_name, self.cuisine_type)
        resultado_esperado = f'Esse restaurante se chama {self.restaurant_name} e serve {self.cuisine_type} e atendeu  {self.number_served} consumidores desde que está aberto.'
        resultado = restaurant.describe_restaurant()
        assert resultado == resultado_esperado
    def test_open_restaurant_aberto(self):
        restaurant = Restaurant(self.restaurant_name, self.cuisine_type)
        restaurant.open_restaurant()
        resultado_esperado = f"{self.restaurant_name} já está aberto!"
        assert restaurant.open_restaurant() == resultado_esperado
    def test_open_restaurant_fechado(self):
        restaurant = Restaurant(self.restaurant_name, self.cuisine_type)
        restaurant.open_restaurant()
        resultado_esperado = f"{self.restaurant_name} agora está aberto!"
        assert restaurant.open_restaurant() == resultado_esperado
    def test_close_restaurant(self):
        restaurant = Restaurant(self.restaurant_name, self.cuisine_type)
        restaurant.close_restaurant()
        assert False
    def test_close_restaurant_aberto (self):
        restaurant = Restaurant(self.restaurant_name, self.cuisine_type)
        restaurant.close_restaurant()
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