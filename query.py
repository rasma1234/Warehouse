"""Command line interface to query the stock.

To iterate the source data you can use the following structure:

for item in warehouse1:
    # Your instructions here.
    # The `item` name will contain each of the strings (item names) in the list.
"""


def search_item( item_name, warehouse1, warehouse2):
        found_items = []
        for item in warehouse1 + warehouse2:
            if item_name.lower() in item.lower():
                found_items.append(item)
        return found_items


def print_warehouse(warehouse1, warehouse2):
    print('Items in warehouse 1:')
    for item in warehouse1:
        print('-', item)

    print('Items in warehouse 2:')
    for item in warehouse2:
        print('-', item)


warehouse1 =[
    "Brand new laptop", "Exceptional monitor", "Cheap tablet", "Funny laptop", "Second hand smartphone",
    "Brand new smartphone", "Cheap router", "Second hand laptop", "Elegant tablet", "Funny tablet",
    "Second hand headphones", "Exceptional tablet", "Brand new smartphone", "Cheap mouse", "Elegant headphones",
    "Brand new headphones", "Second hand smartphone", "High quality smartphone", "Brand new keyboard",
    "Second hand headphones", "Elegant router", "Exceptional router", "Second hand smartphone",
    "Exceptional monitor", "Almost new tablet", "High quality monitor", "Second hand monitor", "Brand new keyboard",
    "Almost new keyboard", "High quality headphones", "Elegant laptop", "Elegant router", "Almost new monitor",
    "Almost new headphones", "Second hand keyboard", "Brand new tablet", "Elegant laptop", "Almost new keyboard",
    "Exceptional router", "High quality keyboard", "Exceptional router", "Elegant router", "Cheap keyboard",
    "High quality monitor", "High quality keyboard", "Funny keyboard", "Cheap mouse", "Cheap monitor",
    "Funny headphones", "Elegant mouse", "Cheap smartphone", "High quality mouse", "Funny keyboard",
    "Second hand monitor", "Almost new router", "Almost new mouse", "Elegant smartphone", "Second hand router",
    "Second hand mouse", "Second hand tablet", "Exceptional tablet", "High quality smartphone",
    "Brand new headphones", "Exceptional monitor", "Elegant mouse", "Cheap laptop", "High quality smartphone",
    "Cheap monitor", "Funny monitor", "Almost new mouse", "Elegant headphones", "Cheap mouse",
    "Exceptional smartphone", "Cheap monitor", "Exceptional tablet", "Almost new tablet",
    "Second hand headphones", "Cheap tablet", "Elegant mouse", "Second hand mouse", "Cheap laptop",
    "Cheap keyboard", "Elegant router", "Elegant headphones", "Second hand monitor", "Funny router",
    "Elegant mouse", "Elegant headphones", "Brand new mouse", "Exceptional tablet", "Funny router",
    "Second hand headphones", "Brand new laptop", "Second hand router", "Cheap mouse", "Funny keyboard",
    "Elegant headphones", "Brand new laptop", "Elegant laptop", "Second hand mouse", "Test"
]

warehouse2 =[
    "High quality tablet", "Second hand headphones", "Second hand laptop", "Exceptional tablet",
    "Exceptional headphones", "Brand new smartphone", "Elegant laptop", "High quality tablet",
    "Brand new headphones", "Exceptional mouse", "Cheap mouse", "Cheap headphones", "High quality headphones",
    "Brand new keyboard", "Brand new smartphone", "Almost new mouse", "Second hand router", "High quality monitor",
    "High quality smartphone", "Second hand headphones", "Elegant monitor", "High quality mouse",
    "Almost new keyboard", "Exceptional headphones", "High quality smartphone", "Exceptional smartphone",
    "High quality tablet", "Cheap mouse", "Cheap monitor", "Funny monitor", "Elegant monitor",
    "Funny smartphone", "Second hand mouse", "Almost new headphones", "Cheap headphones", "High quality router",
    "Exceptional keyboard", "Funny keyboard", "Exceptional laptop", "Cheap keyboard", "Second hand mouse",
    "Elegant router", "Cheap router", "Funny mouse", "Funny laptop", "Elegant tablet", "Exceptional mouse",
    "Funny headphones", "Elegant tablet", "Second hand laptop", "Brand new headphones", "Second hand headphones",
    "Cheap router", "Exceptional mouse", "Elegant router", "Exceptional monitor", "Exceptional keyboard",
    "Funny headphones", "Second hand headphones", "Almost new router", "Brand new tablet", "Funny mouse",
    "Elegant mouse", "High quality router", "Second hand keyboard", "Second hand router", "Brand new monitor",
    "Funny mouse", "Funny tablet", "Elegant keyboard", "Cheap router", "Funny router", "Second hand monitor",
    "Elegant smartphone", "Brand new monitor", "Second hand monitor", "Second hand keyboard", "Cheap mouse",
    "Brand new keyboard", "Exceptional mouse", "Elegant router", "Brand new mouse", "Exceptional keyboard",
    "Elegant smartphone", "Exceptional tablet", "Second hand keyboard", "Almost new headphones",
    "Brand new tablet", "Brand new tablet", "Exceptional headphones", "Funny smartphone", "Funny smartphone",
    "Second hand tablet", "Cheap router", "Almost new keyboard", "Elegant router", "Brand new tablet",
    "High quality tablet", "Almost new router", "High quality monitor", "Test1"
]


user_name = input('What is your user name?: ')
print('Hello', user_name, '!')
print('What would you like to do?')
print('Menu:')
print('1. List items by warehouse')
print('2. Search for an item and place an order')
print('3. Quit')

choice =input('Type the number of the operation: ')
   

while True:
    if choice == '1':
        print_warehouse(warehouse1, warehouse2)
        break

    elif choice == '2':
        item_name = input('What is the name of the item?: ')
        found_items = search_item(item_name, warehouse1, warehouse2)
        print('Amount available:', len(found_items))
        if item_name in warehouse1 and warehouse2:
            print('Location: Both Warehouse')
            count1=0
            count2=0
            for item in warehouse1:
                if item_name in item:
                    count1+=1
            for item in warehouse2:
                if item_name in item:
                    count2+=1    
            if count1 < count2:
                print('Maximum availability:', count2, 'in Warehouse 2')
            else:
                print('Maximum availability:', count1, 'in Warehouse 1')    
        elif item_name in warehouse2:
            print('Location: Warehouse 2')
        elif item_name in warehouse1:
            print('Location: Warehouse 1')
        else:
            print('Location: Not in Stock')    
            print('Thank you for your visit, ', user_name)
            break 

        order=input('Would you like to order this item?(y/n): ')
        if order == 'n':
            print('Thank you for your visit, ', user_name)
            break
        elif order == 'y':
            amount_of_order=int(input('How many would you like?: '))
            len=int(len(found_items))
            if amount_of_order > len:
                print('******************************************************************************')
                print('There are not this many available. The maximum amount that can be ordered is ', len)
                print('******************************************************************************')
                available=input('Would you like to order the maximum available?(y/n): ')
                if available == 'n':
                    print('Thank you for your visit, ', user_name)
                    break
                elif available == 'y':
                    print(len,' ', item_name, 'have been ordered.')
                    print('Thank you for your visit, ', user_name)
        break

    elif choice == '3':
        print('Thank you for your visit, ', user_name)
        break
  
    else:
        print('***********************************')
        print(choice, 'is not a valid operation.')
        print('***********************************')
        print('Thank you for your visit, ', user_name)
        break