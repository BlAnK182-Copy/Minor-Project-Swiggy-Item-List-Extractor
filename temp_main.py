from pushToDB import Data_Operations

#This is a temporary script which can be used for calling functions of the Data_operations class
# NOT INTENDED TO BE IN FINAL DRAFT

obj = Data_Operations()

table_name= "burger_king"
filename= "burger_king"

obj.createTable(table_name)
obj.add_items_to_table(table_name,filename)
#print(obj.get_all_contents(table_name))
##obj.delete_table(table_name)

category_list = obj.get_categories(table_name)
print(category_list)


category_name= category_list[3]
print(obj.get_contents_of_category(table_name, category_name))

#print(obj.get_contents_in_priceRange(table_name,200,400))

'''
keyword= "burger"
print(obj.get_contents_with_keyword(table_name,keyword))
'''