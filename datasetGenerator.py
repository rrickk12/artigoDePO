#generate dataset 
import numpy as np
""" this following code generate the parameters 

orderCost : Price of the cost order given by the Supplier in Suppliers
rmHoldingCost : Holding Cost is given by function of set 'F' that is the subset of raw materieals
productHoldingCost : product Holding cost is given by 'J' that is the subset of produts

maximumCapacityRM : The maximum ammount of raw material in 'f' on dedicated tank
maximumCapacityProduct : The maximum ammount of raw material in 'j' on dedicated tank
generalInventory : The maximum capacity of multi-purpose tank in 'k' on set 'K'

discountRate : discount given by supplier 's' related to level 'd'
rmPurchasingCost : Purchasing Cost of raw material 'f' by supplier 's'
setupCost : Setup cost for task 't' in 'T' on production unity 'm'
productionCost : Production cost for task 't' in production unity 'm'

upperLimit : Upper limit of oder size for supplier 's' in discount level 'd'

batchTime : Time to produce one batch on task 't' in production unit 'm'
setupTime : Setup time for production task 't' in producion unit 'm'
processingTime : Avaliable processing time for 'm' in sub-period 'phi'

maximumBatchSize : Maximum batch size of task 't' produced in 'm'
minumumBatchSize : Minumum batch size of task 't' produced in 'm'

setupTimePacking : Setup time to start packing the product 'j' in packing unit 'n'
packingTime : Avaliable processing time for packint in unit 'n' in sub-period 'phi'

rmConsumption : Consumption of 'f' to produce one batch of task 't' in 'm'
participationInProduction : Percentile of 'j' produced by 't' in 'm'

bulkDemand : Demand of 'j' in sub-period 'phi'
packageDemand : Demand of packed product 'j' in period 'theta'

--random number generated  
alpha : Sufientily Big Number 
leadTime : delivery lead time of raw material 
"""

class Dataset():
    
    orderCost  = []
    rmHoldingCost  = []
    productHoldingCost  = []

    maximumCapacityRM  = [] 
    maximumCapacityProduct  = []
    generalInventory  = [] 

    discountRate  = [] 
    rmPurchasingCost  = []
    setupCost  = []
    productionCost  = [] 

    upperLimit  = []

    batchTime  = []
    setupTime  = []
    processingTime  = [] 

    maximumBatchSize  = [] 
    minumumBatchSize  = [] 

    setupTimePacking  = [] 
    packingTime  = [] 

    rmConsumption  = [] 
    participationInProduction  = [] 

    bulkDemand  = [] 
    packageDemand  = [] 

    alpha  = None
    leadTime  = None 
    """
        sensibility analisis proposes that 
        Suppliers size 4
        rawMaterials size 14
        DiscountLevels size 5
        ProductionTasks size 19        
        ProductionUnits size 3
        PackingUnits size 1
        Products size 10
        tanks size 11
        timePeriod size 4
        subPeriods size 8     
    """
    timePeriod = np.zeros((4,8))
    tanks = np.zeros(11)
    rawMaterials = np.zeros(14)
    Suppliers = np.zeros(4)
    DiscountLevels = np.zeros(5)
    ProductionTasks = np.zeros(19)
    ProductionUnits = np.zeros(3)
    PackingUnits = np.zeros(1) 
    Products = np.zeros(10) 

    def currentPeriod(self,phi):
        theta = None
        return theta

