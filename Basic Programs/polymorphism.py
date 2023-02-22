class India():
    def name(self):
        print("This is for India:")
    def capital(self):
        print("New Delhi")
    def language(self):
        print("Hindi")
    def type(self):
        print("Developing country\n")
class USA():
    def name(self):
        print("This is for USA:")
    def capital(self):
        print("Washington D.C")
    def language(self):
        print("English")
    def type(self):
        print("Developed country\n")  
class Bangladesh():
    def name(self):
        print("This is for Bangladesh")
    def capital(self):
        print("Dhaka")
    def language(self):
        print("Bangla")
    def type(self):
        print("Developing country\n")  
india=India()
usa=USA()
bang=Bangladesh()
#access using for loop 
'''for country in (india,usa,bang):
    country.name()
    country.capital()
    country.language()
    country.type()  '''
#access using userdefined function
def func(obj):
    obj.name()
    obj.capital()
    obj.language()
    obj.type() 
func(india)
func(usa)
func(bang)                                             