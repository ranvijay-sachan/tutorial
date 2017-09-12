import abc


class BasePizza(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_ingredients(self):
        return "love"
        """Returns the ingredient list."""


class DietPizza(BasePizza):
    # @staticmethod
    def get_ingredients(self):
        print "nsdjkcs"

a = DietPizza()
print a.get_ingredients()