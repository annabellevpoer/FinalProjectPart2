# Name: Annabelle Poer
# ID: 1798854


#  item ID, manufacturer name, item type, price, service date, and list if it is damaged 
#  - sorted alphabetically by manufacturer

#  item ID, manufacturer name, price, service date, and list if it is damaged
#  - sorted by their item ID

#  item ID, manufacturer name, item type, price, service date, and list if it is damaged.
#  - order of service date from oldest to most recent

#  item ID, manufacturer name, item type, price, and service date.
#  - most expensive to least expensive

from datetime import date
from datetime import datetime
from os.path import exists


class ProjectPartOne:

    # puts every line from csv file into a list  
    with open("ManufacturerList.csv") as f:
        manufacturer_list = f.read().splitlines() 

    with open("PriceList.csv") as f:
        price_list = f.read().splitlines() 

    with open("ServiceDatesList.csv") as f:
        dates_list = f.read().splitlines() 


    id_dict = {}
    all_items = []
    m_set = set()
    it_set = set()


    # this loop splits each line of the file into a another list
    # it then creates a dictionary (id_dict):
    # the key of the dictionary is the itemID
    # the value is an array including manufacturer name, item type, the damaged indicator
    for x in manufacturer_list:
        file_line = x.split(',')
        itemID = file_line[0].strip()
        file_line.pop(0)
        id_dict[itemID]= file_line
        m_set.add(file_line[0].strip())
        it_set.add(file_line[1].strip())

        
        
    # appends price to array value of the map
    for x in price_list:
        file_line = x.split(',')
        id_dict[file_line[0]].append(file_line[1])

    # appends date to array value of the map
    for x in dates_list:
        file_line = x.split(',')
        id_dict[file_line[0]].append(file_line[1])


    #  now we have a map that holds all the fields from every input csv file given
    # the keys are the itemID string
    # the values are an array containing: manufacturer name, item type, the damaged indicator, price, date


    # this loop creates an array (all_items) from the map we created
    # the first element of the array is set as the map key itemID
    # then we can append the value of the map, which is an array, to the end
    #  so all_items contains (in this order) item ID, manufacturer name, item type, price, service date, damaged indicator.
    #       for every itemID listed in all the csv files 
    for x in id_dict:
        arr = id_dict[x]
        # print("arr: ", arr)
        arr.insert(0, x)
        arr.insert(5, arr.pop(3))
        all_items.append(arr)


    def outputOne(self):
        # --------- (1) SORTS BY MANUFACTUREER ------------ #
        # item ID, manufacturer name, item type, price, service date,  damaged.
        list_one = (sorted(self.all_items, key=lambda x:x[1])) #  sorts the list by manufacturer

        f = open("FullInventory.csv", "w") # opens the csv file to write to it 
        for line in list_one: # writes each element of the list the file
            f.write(",".join(line))
            f.write("\n")

        f.close()
        # --------- (1) SORTS BY MANUFACTUREER ------------ #

    def outputTwo(self):
        # ------------- (2) SORTS BY ID ---------------- #
        # newlist = all_items.copy()
        list_two = sorted(self.all_items, key=lambda x:x[0]) #  sorts the list by item id


        # what it looks like
        # item ID, manufacturer name, item type, the damaged indicator, price, date
        # item ID, manufacturer name, price,  date, the damaged indicator

        # print("\n--------- THE LIST ---------")
        # print(list_two)

        for line in list_two:
            filename = line[2] +".csv"
            f = open(filename, "w") # we want to make sure that each file is empty before we begin writing to it

        f.close()

        for line in (list_two):
            filename = line[2] +".csv"
            itemtype = line[2]
            (line).pop(2)  # remove the item type from the sorted array 
            # damagedindc = line[2] # the damaged indicator
            # (line).pop(2)  # remove the damaged indicator from the sorted array 
            # line.append(damagedindc) # add damagaed indicator to end of array
            # list_two.pop(2)
            # print("\n----------- LINE ------------")
            # print((line))
            f = open(filename, "a") # opens the file in append mode
            f.write(",".join(line))
            f.write("\n")
            line.insert(2, itemtype)

        f.close()

        # print("\n--------- THE LIST TWO ---------")
        # print(list_two)
        # ------------- (2) SORTS BY ID ---------------- #

    
    def outputThree(self):
        # -------------- (3) SORTS BY ORDER SERVICE DATE, OLDEST -> RECENT---------------- #
        # print("\n--------- THE LIST all_items---------")
        # print(all_items)

        list_three = sorted((self.all_items), key=lambda x:datetime.strptime(x[4], "%m/%d/%Y")) #  sorts the list by date
        f = open("PastServiceDateInventory.csv", "w")

        today = date.today()
        for line in list_three:
            date_obj = datetime.strptime(line[4], "%m/%d/%Y").date()
            if(date_obj>today): # only write to file if date is past today (the day you execute this program) 
                f.write(",".join(line))
                f.write("\n")

        f.close()
        # -------------- #3 SORTS BY ORDER SERVICE DATE, OLDEST -> RECENT---------------- #

    def outputFour(self):
        # -------------- (4) SORTS BY PRICE ---------------- #
        list_four = sorted(self.all_items, key=lambda x:x[4]) #  sorts the list by price

        f = open("DamagedInventory.csv", "w")
        for line in list_four:
            if(line[5] == 'damaged'):
                list(line).pop(5) # remove the damaged indicator from the array 
                f.write(",".join(line))
                f.write("\n")

        f.close()
        # -------------- (4) SORTS BY PRICE ---------------- #

    # def main():
    #     partOneObj = ProjectPartOne()
        
    #     partOneObj.outputOne()
    #     partOneObj.outputTwo()
    #     partOneObj.outputThree()
    #     partOneObj.outputFour()

    # if __name__ == "__main__":
    #     main()
    

partOneObj = ProjectPartOne()
partOneObj.outputOne()
partOneObj.outputTwo()
partOneObj.outputThree()
partOneObj.outputFour()


# Please note, everything below is case sensitive  
def printCorrectOutput(dict_of_found_inventory_items, itemtype):
        #  the list containes everything in the itemtype csv
        today = date.today()

        new_dict={}
        new_dict = dict(sorted(dict_of_found_inventory_items.items(), key=lambda item: item[1][1], reverse=True))

        # print("didct: " , new_dict)
        for k,v in new_dict.items():
            damaged_indc = v[3].strip()
            dict_date = datetime.strptime(v[2], "%m/%d/%Y").date()
            if (damaged_indc != "damaged") and (dict_date>today):
                global price
                price = v[1]
                # print("PRINT: ", price)
                return_string = "Your item is: "+ k + ", " + v[0] + ", " + itemtype + ", " + v[1] + ", " + v[2] 
                return return_string

m_input = ''
while m_input != 'q':
    m_input = input("Please enter a manufacturer name and an item type name:, or enter 'q' to quit: ")
    manufacturer_itemtype_input = m_input.split()
    
    found = True
    price = 0
    


    # print("-------------\nchecking \n-----------")

    # print(ProjectPartOne.m_set)
    # print(ProjectPartOne.it_set)
    # print("-------------\nchecking 2\n-----------")

    m_count = 0
    it_count = 0
    filename = ""
    item_type_name = ""
    manufacturer_name = ""

    for x in manufacturer_itemtype_input:
        # print("X: ", x)
        if x in ProjectPartOne.m_set:
            m_count=m_count+1
            manufacturer_name = x
        if x in ProjectPartOne.it_set:
            it_count=it_count+1
            filename = x
            item_type_name = x

    # print(m_count)
    # print(it_count)
    # print("-------------\nchecking 3\n-----------")

    found_dict = {}

    if(m_count==1 & it_count==1): # they shoul donly be ONE manufacturer and ONE item type entered
        item_not_in_inventory = False
        with open(filename+".csv") as f:
            for line in f:
                        # print("line: ", line.split(","))
                line = line.split(",")
                # print("line: ", line)
                        # iterate through input and check every word of inupu to see if it exists in the file line, ignore case
                for y in manufacturer_itemtype_input:
                    # print("y: ", y, ", line[1]: ", line[1])
                    if (y == line[1].strip()): # if item type is found in the inventory...
                        # print("found it: ", y)
                        found_dict[line[0]] = line[1:6] 
                        item_not_in_inventory = False
                    else:
                        item_not_in_inventory = True
                        t = "a"

                        # print("No such item in inventory") #, " -- item typr not in inventory --")


        # print("DICTIONARY: ", found_dict)
        if(found_dict):
            # print("-------------\n RESULT \n-----------")       
            print("\n",printCorrectOutput(found_dict, filename))
            item_not_in_inventory = False
        else:
            item_not_in_inventory = True
            t = "b"

            # print("No such item in inventory") #, " -- corresct manufacturer+itemtype pair cannot be found --")

    else:
        item_not_in_inventory = True
        t = "c"
        # print("No such item in inventory") #," -- theres too many or too little or  manufacturer not in inventory-- ")
        #  if the  manufacturer is not in inventory, then it woul dhave caught that with the count
        
    if(item_not_in_inventory):
        print("No such item in inventory:")
    
   
    # print(printCorrectOutput(found_dict, filename))

    # print("\n ------ \nYOU MAY ASO CONSIDER \n-------")
    today = date.today()
    #  '1111111': ['Apple ', '700', '2/1/2024', '\n']

    file = open('FullInventory.csv', 'r')
    lines = file.readlines()
    distance = -1
    final = ""

#  checkign fo other entries to consider
    for index, line in enumerate(lines):
        # print("Line {}: {}".format(index, line.split(",")))  
        file_line = line.split(",")
        # print(item_type_name, file_line[1])
        if(item_type_name == file_line[2].strip()): # if we find a line that has the SAME ITEM
            # print("same: ", item_type_name, file_line[2])
            damaged_indc = file_line[5].strip()
            # print(file_line[4])
            dict_date = datetime.strptime(file_line[4], "%m/%d/%Y").date()

            # check for DIFFERENT manucaturer, NOT DAMAGED, and NOT PAST DATE
            if(manufacturer_name != file_line[1].strip() and (damaged_indc != "damaged") and (dict_date>today)):
                # print(manufacturer_name, file_line[1])
                # print("\n -- this line is good: ", line, price)
                # calculate distance from original price to this price
                # distance = abs(line[3] - price)
                # print(type(line[3]))
                if(distance == -1):
                    distance = abs(int(file_line[3]) - int(price))
                    # print("less distancde: ", distance, line)
                    
                    final = line
                elif(abs(int(file_line[3]) - int(price)) < distance):
                    # print("less distancd 2: ", distance, line)
                    distance = abs(int(file_line[3]) - int(price))
                    final = line

    # print(not final)

    if(final):
        print("You may, also, consider: ", final)
    else:
        print("there are no other considerations.")

    