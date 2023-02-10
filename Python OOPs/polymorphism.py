class India:
    def capital(self):
        print("Capital is New Delhi")
    def language(self):
        print("Official language is Hindi")
    def type(self):
        print("It is a Developing Country")
class USA:
    def capital(self):
        print("Capital is Washington D.C")
    def language(self):
        print("Official language is English")
    def type(self):
        print("It is a Developed Country")
class Bangladesh:
    def capital(self):
        print("Capital is Dhaka")
    def language(self):
        print("Official language is Bangla")
    def type(self):
        print("It is a Under Developing Country")
obj_ind=India()
obj_usa=USA()
obj_bang=Bangladesh()
#access these element using type1

for country in (obj_ind,obj_usa,obj_bang):
    print("-----------------------------------------")
    country.capital()
    country.language()
    country.type()
#access these element using type2

def count(obj):
    obj.capital()
    obj.language()
    obj.type()
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
count(obj_ind)
print("*****************************************************")
count(obj_usa)
print("*****************************************************")
count(obj_bang)
