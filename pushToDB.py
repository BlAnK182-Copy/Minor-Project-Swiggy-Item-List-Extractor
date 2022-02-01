import sqlite3

class Data_Operations :

    def createTable(self, table_name):
        #creates a table in the db with the given table name.

        conn = sqlite3.connect("restraunt_items")
        Mycursor = conn.cursor()

        Mycursor.execute(f"""CREATE TABLE {table_name}(
            item_name varchar, 
            price decimal(6,2),
            category text, 
            restraunt text    
        )
        """)
        conn.commit()
        conn.close()

    def add_items_to_table(self, table_name: str, filename: str):
        #adds data into the specified table from the specified textfile.
        # name of textfile SHOULD NOT HAVE AN EXTENSION.

        conn = sqlite3.connect("restraunt_items")
        Mycursor = conn.cursor()

        datafile = open(filename+".txt", "r")
        
        before_header_space= True
        after_header_space = False
        c=0
        header= "blank"

        for line in datafile:

            if before_header_space:
                header = line.strip()
                after_header_space = True
                before_header_space=False


            elif line.isspace() and not after_header_space :
                before_header_space = True

            elif line.isspace() and after_header_space:
                after_header_space= False
                continue

            else:
                item_and_price = line.split("        ")
                item = item_and_price[0].strip()
                price = float((item_and_price[-1].strip()))

                #print(c)
                #print([item,price])
                Mycursor.execute(f"INSERT INTO {table_name} VALUES (:item_name, :price, :category, :restraunt)",
                {
                    "item_name" : item,
                    "price" : price,
                    "category": header,
                    "restraunt" : table_name,
                    
                }
                )
                
                c+=1
                

        datafile.close()

        print(f"{c} records added")

        conn.commit()
        conn.close()

    def delete_table(self, table_name):
        #d

        conn = sqlite3.connect("restraunt_items")
        Mycursor = conn.cursor()

        Mycursor.execute(f"DROP TABLE {table_name}")

        print(f"table {table_name} deleted")

        conn.commit()
        conn.close()

    def get_all_contents(self, table_name: str):
        # This function returns a list containing tuples, each tuple contianing one record.

        conn = sqlite3.connect("restraunt_items")
        Mycursor = conn.cursor()

        Mycursor.execute(f"""SELECT * FROM {table_name}
        """)

        received_data = Mycursor.fetchall()
        print (len(received_data))

        conn.commit()
        conn.close()

        return received_data


        
    def get_categories(self, table_name: str):
        # returns a list of all the categories in this table.

        conn = sqlite3.connect("restraunt_items")
        Mycursor = conn.cursor()

        Mycursor.execute(f""" SELECT DISTINCT category FROM {table_name}
        """)

        recieved_data = Mycursor.fetchall()

        categories = [x[0] for x in recieved_data]    

        conn.commit()
        conn.close()

        return  categories
            
    def get_contents_of_category(self, table_name, category_name):
        #Only records of the mentioned category will be returned
        # returns a list containing tuples with each tuple containg a record. 

        conn = sqlite3.connect("restraunt_items")
        Mycursor = conn.cursor()
        
        Mycursor.execute(f"""SELECT * from {table_name} where category = '{category_name}'
        """)

        recieved_data = Mycursor.fetchall()

        print(f"{len(recieved_data)} records returned")

        conn.commit()
        conn.close()

        return (recieved_data)

    def get_contents_in_priceRange(self, table_name, lower_limit: float, upperlimit: float):
        #Only records within the price limmit (inclusive of both limits) will be returned.
        # returns a list containing tuples with each tuple containg a record. 

        conn = sqlite3.connect("restraunt_items")
        Mycursor = conn.cursor()

        Mycursor.execute(f"""SELECT * from {table_name} WHERE price <= {upperlimit} and price >= {lower_limit} and category !='Recommended'
        """)

        recieved_data = Mycursor.fetchall()

        print(f"{len(recieved_data)} records returned")

        conn.commit()
        conn.close()

        return recieved_data

    def get_contents_with_keyword(self, table_name: str, keyword:str):
        #Returns all records where the item has the keyword in it.
        #Returns a list of tuples where each tuple is a record.

        conn = sqlite3.connect("restraunt_items")
        Mycursor = conn.cursor()

        Mycursor.execute(f"""SELECT * from {table_name} WHERE item_name LIKE '%{keyword}%' and category != 'Recommended'
        """)

        recieved_data = Mycursor.fetchall()

        print(f"{len(recieved_data)} records returned")

        conn.commit()
        conn.close()

        return recieved_data

