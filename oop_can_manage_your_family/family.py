import os.path
import json

class Person():

    '''Class Attributes'''
    EYES_COLORS = ["Blue", "Green", "Brown"]
    GENRES = ["Female", "Male"]

    '''Constructor'''
    def __init__(self, id, first_name, date_of_birth, genre, eyes_color):

        if id < 0 or not isinstance(id, int):
            raise Exception("id is not an integer")

        if first_name == None or not isinstance(first_name, str):
            raise Exception("string is not a string")

        if type(date_of_birth) == str or len(date_of_birth) != 3 or date_of_birth[0] not in range(1, 13) or date_of_birth[1] not in range(1, 32):
            raise Exception("date_of_birth is not a valid date")

        if not isinstance(genre, str) and genre not in self.GENRES:
            raise Exception("genre is not valid")

        if not isinstance(eyes_color, str) and eyes_color not in self.EYES_COLORS:
                raise Exception("eyes_color is not valid")

        '''Declaring all the private attributes'''
        self.__id = id
        self.__first_name = first_name
        self.__date_of_birth = date_of_birth
        self.__genre = genre
        self.__eyes_color = eyes_color

        # task 4
        '''Declaring public attribute'''


    # task 3
    '''Declaring a dictionary'''
    def json(self):
        return {'kind': self.__class__.__name__,
        'id': self.__id,
        'first_name': self.__first_name,
        'date_of_birth': self.__date_of_birth,
        'genre': self.__genre,
        'eyes_color': self.__eyes_color}


    '''Ensure data loaded from JSON is formatted correctly'''
    def load_from_json(self, json):
        if not isinstance(json, dict):
            raise Exception("json is not valid")
        self.__id = json['id']
        self.__first_name = json['first_name']
        self.__date_of_birth = json['date_of_birth']
        self.__genre = json['genre']
        self.__eyes_color = json['eyes_color']


    '''Declaring a get method for all private Person attributes'''
    def get_id(self):
        return self.__id

    def get_first_name(self):
        return self.__first_name

    def get_date_of_birth(self):
        return self.__date_of_birth

    def get_genre(self):
        return self.__genre

    def get_eyes_color(self):
        return self.__eyes_color

    '''Start of task 1 base class description'''
    def __str__(self):
        return self.__first_name + ' ' + self.last_name

    '''Check if attribute 'genre' is male or not'''
    def is_male(self):
        if self.__genre is not "Male":
            return False

    # 05/20/2016
    '''Comparing the date_of_birth to 05/20/2016 to find out the Person age'''
    def age(self):
        if self.__date_of_birth[0] > 5:
            return 2016 - self.__date_of_birth[2] - 1

    '''Comparitor Overloading'''
    def __gt__(self, other):
        return self.age() > other.age()

    def __ge__(self, other):
        return self >= other

    def __lt__(self, other):
        return self < other

    def __le__(self, other):
        return self <= other

    def __eq__(self, other):
        return self == other


    '''Task 2: declaring methods to be overloaded by individual child classes'''
    def can_run(self):
        return False

    def need_help(self):
        return False

    def is_young(self):
        return False

    def can_vote(self):
        return False

    '''Marriage methods'''
    def can_be_married(self):
        return False

    def is_married(self):
        return False

    def divorce(self, p):
        return False

    def just_married_with(self, p):
        return False


# can_run(self) => return True if the Class is Teenager or Adult
# need_help(self) => return True if the Class is Baby or Senior
# is_young(self) => return True if the Class is Baby or Teenager
# can_vote(self) => return True if the Class is Adult or Senior

'''Task 2: new classes to inherit Person class'''
class Baby(Person):
    def need_help(self):
        return True

    def is_young(self):
        return True

class Teenager(Person):
    def can_run(self):
        return True

    def is_young(self):
        return True

class Adult(Person):
    def can_run(self):
        return True

    def can_vote(self):
        return True

    def can_be_married(self):
        return True

class Senior(Person):
    def need_help(self):
        return True

    def can_vote(self):
        return True

    def can_be_married(self):
        return True


def save_to_file(list, filename):
    if not isinstance(filename, str) or not os.path.isfile(filename):
        raise Exception("filename is not valid or doesn't exist")
    else:
        list_json = []
    for i in list:
        list_json.append(i.json())
    with open(filename, 'w') as outfile:
        json.dump(list_json, outfile)


def load_from_file(filename):
    if not isinstance(filename, str) or not os.path.isfile(filename):
        raise Exception("filename is not valid or doesn't exist")
    else:
        with open(filename) as json_data:
            data = json.load(json_data)
            list = []
            for i in data:
                if i['kind'] == "Baby":
                    x = Baby(1, "X", [1, 1, 1111], "X", "X")
                if i['kind'] == "Senior":
                    x = Senior(1, "X", [1, 1, 1111], "X", "X")
                if i['kind'] == "Teenager":
                    x = Teenager(1, "X", [1, 1, 1111], "X", "X")
                if i['kind'] == "Adult":
                    x = Adult(1, "X", [1, 1, 1111], "X", "X")
                else:
                    x = Person(1, "X", [1, 1, 1111], "X", "X")
                x.load_from_json(i)
                list.append(x)
            return list
