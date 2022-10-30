class temparatureConverter:
    def __init__(self,temparature):
        self.temparature = temparature

    def convertCelciusToFahrenheit(self):
        return (self.temparature * 9/5) + 32

    def convertFahrenhitToCelcius(self):
        return (self.temparature - 32) * (5/9)
