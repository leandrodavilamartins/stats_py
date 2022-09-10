from classes import Data, Distribution, Discrete, Binomial, Poisson, Geometric, Hyper, ABC

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
    #poisson01 = Poisson(4)
    #print(poisson01.probability(4))
    #test = isinstance(poisson01, ABC)
    #print(test)
    #hyper01 = Hyper()
    #binomial01 = Binomial(12,0.2,0.8)
    #print(binomial01.probability(2))
    geometric01 = Geometric(0.15)
    print(geometric01.probability(7))
    print(geometric01.cumulative(40))
  