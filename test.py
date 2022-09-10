from classes import Data, Distribution, Discrete, Poisson,ABC

if __name__=="__main__":
    data = [0,2,3,4,4,4,1,5,7,8] # maybe you should use a numpy array ? 

    myDataObj = Data(data) # creates the object 
    #print(myDataObj.contador())
    #print(myDataObj.soma())
    #print(myDataObj.media())
    #print(myDataObj.frequencia())
    #print(myDataObj.moda())
    #print(myDataObj.mediana())
    #print(myDataObj.ordenar())
    #print(myDataObj.variancia())
    #print(myDataObj.desvio())
    #print(myDataObj.cv())
    #print(myDataObj.percentil(8))
    #myDistribution = Distribution()
    #print(myDistribution.factorial[5])
    #discrete = Discrete();
    #discrete.probability();
    poisson01 = Poisson(6)
    print(poisson01.probability(6))
    test = isinstance(poisson01, ABC)
    print(test)
    
  