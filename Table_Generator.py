from tkinter import*
from pushToDB import Data_Operations


try:
    import tksheet
except ModuleNotFoundError:
    import os
    os.system("pip install tksheet")
    import tksheet

class Table_Generator:

    def __init__(self):
        pass
        
    def remove_res_name(self, data: list):
        
        if data== None:
            print("no records received")
            return
        
        data_to_return = []

        for record in data:
            data_to_return.append(record[0:3])
        
        return data_to_return

    def remove_res_name_and_category(self, data: list):
        
        if data== None:
            print("no records received")
            return

        data_to_return = []

        for record in data:
            data_to_return.append(record[0:2])
        
        return data_to_return

    def generate_table(self, root:Tk, col:int):
        
        if col==3:

            new_sheet = tksheet.Sheet(
                    root,
                    headers=["Item", "Price","Category"],
                    show_x_scrollbar=False,
                    column_width= 300
                    )
            new_sheet.height_and_width(height=350, width=955)

        elif col==2:

            new_sheet = tksheet.Sheet(
                    root,
                    headers=["Item", "Price"],
                    show_x_scrollbar=False,
                    column_width= 300
                    )
            new_sheet.height_and_width(height=350, width=655)

        else:
            print(f"For this project, tables of columnlength 2 or 3 only are intended to be created. \n You have enterd {col}")
            return

        return new_sheet            
        

    # all of the below functions return a gui sheet with item, price. Category if asked for.    
    def get_all_contents(self, root: Tk ,table_name: str, display_category = True):

        db = Data_Operations()
        if display_category:

            content = self.remove_res_name(db.get_all_contents(table_name))

            sheet = self.generate_table(root,3)

            sheet.set_sheet_data(content)

        else:
            content = self.remove_res_name_and_category(db.get_all_contents(table_name))
            
            sheet = self.generate_table(root,2)

            sheet.set_sheet_data(content)

        return sheet

    def get_contents_of_category(self,root:Tk, table_name: str, category:str, display_category = True):

        db = Data_Operations()
        if display_category:

            content = self.remove_res_name(db.get_contents_of_category(table_name,category))

            sheet = self.generate_table(root,3)

            sheet.set_sheet_data(content)

        else:
            content = self.remove_res_name_and_category(db.get_contents_of_category(table_name, category))
            
            sheet = self.generate_table(root,2)

            sheet.set_sheet_data(content)

        return sheet

    def get_contents_in_priceRange(self, root:Tk, table_name:str, lower_limit:float, upperlimit:float, display_category = True):

        db = Data_Operations()
        if display_category:

            content = self.remove_res_name(db.get_contents_in_priceRange(table_name,lower_limit, upperlimit))

            sheet = self.generate_table(root,3)

            sheet.set_sheet_data(content)

        else:
            content = self.remove_res_name_and_category(db.get_contents_in_priceRange(table_name,lower_limit, upperlimit))
            
            sheet = self.generate_table(root,2)

            sheet.set_sheet_data(content)

        return sheet        

    def get_contents_with_keyword(self, root:Tk, table_name:str, keyword:str, display_category= True):
        
        db = Data_Operations()
        if display_category:

            content = self.remove_res_name(db.get_contents_with_keyword(table_name,keyword))

            sheet = self.generate_table(root,3)

            sheet.set_sheet_data(content)

        else:
            content = self.remove_res_name_and_category(db.get_contents_with_keyword(table_name,keyword))
            
            sheet = self.generate_table(root,2)

            sheet.set_sheet_data(content)

        return sheet