

class Car:

    ''' Constructor '''
    def __init__(self, *args, **kwargs):

        if len(args) > 0 and isinstance(args[0], dict):
            hash = args[0]
            name = hash.get('name')
            brand = hash.get('brand')
            nb_doors = hash.get('nb_doors')
        else:
            name = kwargs.get('name')
            brand = kwargs.get('brand')
            nb_doors = kwargs.get('nb_doors')

        if name == "" or not isinstance(str(name), str):
            raise Exception("name is not a string")
        if name == "" or not isinstance(str(brand), str):
            raise Exception("brand is not a string")
        if not isinstance(nb_doors, int) or nb_doors <= 0:
            raise Exception("nb_doors is not > 0")

        ''' Declared private attributes '''
        self.__name = name
        self.__brand = brand
        self.__nb_doors = nb_doors

    ''' Using getters to return its cooresponding attribute value '''
    def get_name(self):
        return self.__name
    def get_brand(self):
        return self.__brand
    def get_nb_doors(self):
        return self.__nb_doors

    ''' to_hash will return arguments in a hash with its designated keys '''
    def to_hash(self):
        return {'name': self.__name, 'brand': self.__brand, 'nb_doors': self.__nb_doors}

    ''' Overloading a printed string to the following format '''
    def __str__(self):
        return "%s %s (%s)" % (self.__name, self.__brand, self.__nb_doors)
