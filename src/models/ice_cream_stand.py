from src.models.restaurant import Restaurant


class IceCreamStand(Restaurant):
    """Um tipo especializado de restaurante."""

    def __init__(self, restaurant_name, cuisine_type, flavors_list = None):
        """
        Inicialize os atributos da classe pai.
        Em seguida, inicialize os atributos específicos de uma sorveteria.
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors_list if flavors_list else []
        
    # def flavors_available(self):
    #     """Percorra a lista de sabores disponíveis e imprima."""
    #     if self.flavors:
    #         return (f"\nNo momento temos os seguintes sabores de sorvete disponíveis: {self.flavors}")
    #         for flavor in self.flavors:
    #             print(f"\t-{flavor}")
    #
    #     else:
    #         print("Estamos sem estoque atualmente!")

    def flavors_available(self):
        """Percorra a lista de sabores disponíveis e imprima."""

        if not self.flavors:
            return "Estamos sem estoque atualmente!"

        else:
            flavors_list = ", ".join(self.flavors)
            return f"No momento temos os seguintes sabores de sorvete disponíveis: {flavors_list}"

    def find_flavor(self, flavor):
        """Verifica se o sabor informado está disponível."""

        #if self.flavors:
        if not flavor or not isinstance(flavor, str):
            return "Sabor informado não é valido!"
        if not self.flavors:
            return "Estamos sem estoque atualmente!"

        if flavor in self.flavors:
            return f"Temos {flavor} no momento !"
        else:
            return f"Não temos {flavor} no momento!"
        #else:
            #print("Estamos sem estoque atualmente!")

    def add_flavor(self, flavor):
        """Add o sabor informado ao estoque."""
        #if self.flavors:
        if not flavor or not isinstance(flavor, str):
            return "Sabor informado não é valido!"
        if flavor in self.flavors:
            return "Sabor já disponivel!"

        else:
            self.flavors.append(flavor)
            return f"{flavor} adicionado ao estoque!"

        #else:
            #print("Estamos sem estoque atualmente!")
