class Celsius(object):
    def __init__(self, value=0):
        print('调用了init')
        "init"
        self.temperature = value  ##  对self.temperature的赋值会触发property绑定的set_temperature方法

    def to_fahrenheit(self):
        print('调用了温度设置')
        return (self.temperature * 1.8) + 32  ##  对self.temperature的访问会触发property绑定的get_temperature方法

    def get_temperature(self):  ##  绑定到property的getter方法
        print("Getting value")
        return self.__temperature

    def set_temperature(self, value):  ##  绑定到property的setter方法
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print("Setting value")
        self.__temperature = value  ##  对属性进行封装和隐藏

    def del_temperature(self):
        print("del temperature")
        del self.__temperature

    temperature = property(get_temperature, set_temperature, del_temperature)

c = Celsius(9)
print('分隔符1')
print (c.temperature)
print('分隔符2')
c.temperature=230
print('分隔符3')
print (c.temperature)
del c.temperature