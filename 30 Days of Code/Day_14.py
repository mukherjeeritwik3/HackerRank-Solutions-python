
    # Add your code here
    def computeDifference(self):
        max = 0
        for i in range(len(self.__elements)):
            for j in range(len(self.__elements)):
                absolute = abs(self.__elements[i] - self.__elements[j])
                if absolute>max:
                    max = absolute
        self.maximumDifference= max    

