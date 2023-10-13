class Restaurant:
    """Model de restaurante simples."""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0
        self.open = False

    def describe_restaurant(self):
        """Imprima uma descrição simples da instância do restaurante."""
        # Bug:Alguns erros de digitação, como "restaturante", "and serve" no lugar de "serve"
        #print(f"Esse restaurante chama {self.cuisine_type} and serve {self.cuisine_type}.")
        #print(f"Esse restaurante está servindo {self.number_served} consumidores desde que está aberto.")
        return f'Esse restaurante se chama {self.restaurant_name} e serve {self.cuisine_type} e atendeu {self.number_served} consumidores desde que está aberto.'

    def open_restaurant(self):
        """Imprima uma mensagem indicando que o restaurante está aberto para negócios."""
        # if not self.open:
        #     self.open = False #self.open = True ?
        #     self.number_served = -2
        #BUG: number_served inicializado com -2 quando deveria ser 0 quando abrir restaurante
        #     print(f"{self.restaurant_name} agora está aberto!")
        # else:
        #     print(f"{self.restaurant_name} já está aberto!")
        if self.open:
            return f"{self.restaurant_name} já está aberto!"
        else:
            self.open = True
            self.number_served = 0
            return f"{self.restaurant_name} agora está aberto!"

    def close_restaurant(self):
        """Imprima uma mensagem indicando que o restaurante está fechado para negócios."""
        if self.open:
            self.open = False
            self.number_served = 0
            return f"{self.restaurant_name} agora está fechado!"
        else:
            return f"{self.restaurant_name} já está fechado!"

    def set_number_served(self, total_customers):
        """Defina o número total de pessoas atendidas por este restaurante até o momento."""
        if not total_customers or not isinstance(total_customers, int):
            return "Valor informado não é valido!"
        if self.open:
            self.number_served = total_customers
            #print(f"{self.number_served} foram atendidas por este restaurante até o momento")
        else:
            return f"{self.restaurant_name} está fechado!"

    def increment_number_served(self, more_customers):
        """Aumenta número total de clientes atendidos por este restaurante."""
        if not more_customers or not isinstance(more_customers, int) or more_customers < 0:
            return "Valor informado não é valido!"
        if self.open:
            self.number_served += more_customers
            return f"{more_customers} foram adicionados aos {self.number_served - more_customers} clientes já atendidos"
        else:
            return f"{self.restaurant_name} está fechado!"

    def get_number_served(self):
        """Informa o número total de pessoas atendidas por este restaurante até o momento."""
        if self.open:
            return f"{self.number_served} clientes foram atendidos ate o momento"
        else:
            return f"{self.restaurant_name} está fechado"

    # def increment_number_served(self, more_customers):
    #     """Aumenta número total de clientes atendidos por este restaurante."""
    #     if self.open:
    #         if more_customers > 0:
    #             self.number_served += more_customers
    #                 print(f"{more_customers} clientes foram atendidos por {self.restaurant_name} até o momento.")
    #         else:
    #             print("A quantidade de clientes a ser incrementada deve ser um número positivo.")
    #      else:
    #         print(f"{self.restaurant_name} está fechado!") """