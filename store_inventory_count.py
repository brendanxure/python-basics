##################################################################
#  Program title:         Store Inventory Count
#  Program Author:        Brendan Obilo
#  Date:                  19/04/2024
#
#  Description:           A function that accepts the product number
#                         and quantity of t-shirt sold and returns a
#                         list of updated inventory.
###########################################################

# delcare variables
# product_number = ['252567', '786539', '231568', '231568']
product_number = ['252567', '786539', '231568', '231568']
# product_description = ['Got Code', 'I Heart Code', 'Im with code', 'Born to Code']
product_description = ['Got Code', 'I Heart Code', 'Im with code', 'Born to Code']
# quantity = [25, 25, 25, 25]
quantity = [25, 25, 25, 25]


# def stock_inventory(product_number_parameter: int, quantity_parameter: int)
def stock_inventory(product_number_parameter: str, quantity_parameter: int):
    try:
        # input_product_code = str(product_number_parameter)
        input_product_code = str(product_number_parameter)
        # input_quantity = int(quantity_parameter)
        input_quantity = int(quantity_parameter)
        # returnUpdatedList = quantity
        returnUpdatedList = quantity
        # for element in product_number:
        for element in product_number:
            # if element == input_product_code:
            if element == input_product_code:
                # product_quantity = quantity[product_number.index(element)]
                product_quantity = quantity[product_number.index(element)]
                # product_quantity = product_quantity - input_quantity
                product_quantity = product_quantity - input_quantity
                # quantity[product_number.index(element)] = product_quantity
                quantity[product_number.index(element)] = product_quantity
        return returnUpdatedList
    # except ValueError:
    except ValueError:
        # return returnUpdatedList
        return returnUpdatedList
    
# print(stock_inventory('252567', 10))
print(stock_inventory('252567', -10))
