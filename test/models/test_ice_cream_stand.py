from src.models.ice_cream_stand import IceCreamStand


class TestIceCreamStand:
    def test_add_flavor_sucessfully(self):
        # Inicializa um stand
        stand = IceCreamStand("Ice Cream Shop", "Ice Cream", "")
        # Adiciona um sabor ao stand
        flavor = "Menta"
        resposta = stand.add_flavor(flavor)
        # Valida resposta
        resposta_esperada = f"{flavor} adicionado ao estoque!"
        assert resposta_esperada == resposta

    def test_add_flavor_allready_exists(self): #verificar se está certo
        # Inicializa um stand
        stand = IceCreamStand("Ice Cream Shop", "Ice Cream", "Menta")
        # Adicona um sabor ao stand
        flavor = "Menta"
        resposta = stand.add_flavor(flavor)
        # Valida resposta
        resposta_esperada = "\n Sabor já disponivel!"
        assert resposta_esperada != resposta

    # def test_add_flavor_empty(self): faz sentido ter esse teste??
    #     # Inicializa um stand
    #     stand = IceCreamStand("Ice Cream Shop", "Ice Cream", None)
    #
    #     # Adicona um sabor ao stand
    #     flavor = "Menta"
    #     resposta = stand.add_flavor(flavor)
    #     # Valida resposta
    #     resposta_esperada = "Estamos sem estoque atualmente!"
    #     assert resposta_esperada == resposta

    def test_find_flavor(self):
        stand = IceCreamStand("Ice Cream Shop", "Ice Cream", "Morango")
        stand.add_flavor("Morango")
        flavor = "Morango"
        resposta = stand.find_flavor(flavor)
        resposta_esperada = f"Temos {flavor} no momento !"
        assert resposta_esperada == resposta

    def test_find_flavor_not_available(self):
        stand = IceCreamStand("Ice Cream Shop", "Ice Cream",  "Morango")
        flavor = stand.add_flavor("Menta")
        resposta = stand.find_flavor(flavor)
        resposta_esperada = f"Não temos {flavor} no momento!"
        assert resposta_esperada == resposta

    def test_find_flavor_empty(self):
        stand = IceCreamStand("Ice Cream Shop", "Ice Cream",  None)
        resposta = stand.find_flavor("Menta")
        resposta_esperada = "Estamos sem estoque atualmente!"
        assert resposta_esperada == resposta

    def test_flavors_available(self):
        flavors = ["Chocolate", "Menta", "Baunilia", "Creme", "Nata"]
        stand = IceCreamStand("Ice Cream Shop", "Ice Cream", flavors)

        for flavor in flavors:
            stand.add_flavor(flavor)

        resposta = stand.flavors_available()
        resposta_esperada = f"No momento temos os seguintes sabores de sorvete disponíveis: {', '.join(flavors)}"

        assert resposta_esperada == resposta

    def test_flavors_available_empty(self):
        stand = IceCreamStand("Ice Cream Shop", "Ice Cream", None)
        resposta = stand.flavors_available()
        resposta_esperada = "Estamos sem estoque atualmente!"
        assert resposta_esperada == resposta