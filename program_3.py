TotalSales = input("Total Sales: ")

def CalculateTax(TotalSales):
    StateSalesTax = float(TotalSales) * 0.05
    CountySalesTax = float(TotalSales) * 0.025
    TotalSalesTax = StateSalesTax + CountySalesTax
    return str("State Sales Tax: " + str(StateSalesTax) + "      County Sales Tax: "+ str(CountySalesTax) + "      total Sales Tax: " + str(TotalSalesTax))

print(CalculateTax(TotalSales))