import pytest
from src.models.ice_cream_stand import IceCreamStand


class TestIceCreamStand:

    @pytest.fixture
    def stand(self):
         stand_name = "Ice Cream Shop"
         stand_cousine = "Ice Cream"
         return IceCreamStand(stand_name, stand_cousine)
    def test_add_flavor_sucessfully(self, stand):
        flavor = "Menta"
        resposta = stand.add_flavor(flavor)
        resposta_esperada = f"{flavor} adicionado ao estoque!"
        assert resposta_esperada == resposta

    def test_add_flavor_already_exists(self, stand):
        flavor = "Menta"
        stand.add_flavor(flavor)
        resposta = stand.add_flavor(flavor)
        resposta_esperada = "Sabor já disponivel!"
        assert resposta_esperada == resposta

    def test_add_flavor_empty(self, stand):
        flavor = ""
        resposta = stand.add_flavor(flavor)
        resposta_esperada = "Sabor informado não é valido!"
        assert resposta_esperada == resposta
    def test_add_flavor_invalid(self, stand):
        flavor = 500
        resposta = stand.add_flavor(flavor)
        resposta_esperada = "Sabor informado não é valido!"
        assert resposta_esperada == resposta

    def test_find_flavor(self,stand):
        stand.add_flavor("Manga")
        stand.add_flavor("Morango")
        stand.add_flavor("Kiwi")
        flavor = "Morango"
        resposta = stand.find_flavor(flavor)
        resposta_esperada = f"Temos {flavor} no momento !"
        assert resposta_esperada == resposta

    def test_find_flavor_not_available(self, stand):
        stand.add_flavor("Manga")
        stand.add_flavor("Morango")
        stand.add_flavor("Kiwi")
        flavor = stand.add_flavor("Creme")
        resposta = stand.find_flavor(flavor)
        resposta_esperada = f"Não temos {flavor} no momento!"
        assert resposta_esperada == resposta

    def test_find_flavor_empty(self, stand):
        resposta = stand.find_flavor("Menta")
        resposta_esperada = "Estamos sem estoque atualmente!"
        assert resposta_esperada == resposta
    def test_find_flavor_invalid(self, stand):
        resposta = stand.find_flavor(500)
        resposta_esperada = "Sabor informado não é valido!"
        assert resposta_esperada == resposta
    def test_flavors_available(self, stand):
        flavors = ["Chocolate", "Menta", "Baunilia", "Creme", "Nata"]
        for flavor in flavors:
            stand.add_flavor(flavor)
        resposta = stand.flavors_available()
        resposta_esperada = f"No momento temos os seguintes sabores de sorvete disponíveis: {', '.join(flavors)}"

        assert resposta_esperada == resposta
    def test_flavors_available_empty(self, stand):
        resposta = stand.flavors_available()
        resposta_esperada = "Estamos sem estoque atualmente!"
        assert resposta_esperada == resposta