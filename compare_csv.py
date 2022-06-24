import csv

#Open two source files and three files where you will save three different output types
with open('product_inventory_before.csv', 'r') as csv1, open('product_inventory_after.csv', 'r') as csv2, open('Create.csv', 'w') as Create, open('Delete.csv', 'w') as Delete, open('Update.csv', 'w') as Update:  
    before_list = list(csv.DictReader(csv1))
    after_list = list(csv.DictReader(csv2))
    
    #Create a list of IDs from the first dataset
    indexes_before = []
    for x in range(0, len(before_list)):
        indexes_before.append(before_list[x]['id'])

    #Create a list of IDs from the second dataset    
    indexes_after = []
    for y in range(0, len(after_list)):
        indexes_after.append(after_list[y]['id'])
   
    #Create headers of your table
    fieldnames = before_list[0].keys()

    #New records to be created
    new_items = csv.DictWriter(Create, fieldnames=fieldnames, dialect='excel')
    new_items.writeheader()

    for row2 in after_list:
        if row2['id'] not in indexes_before:
            new_items.writerow(row2)
    print("New file with records to be created is ready!")

    #Records to be deleted
    delete_items = csv.DictWriter(Delete, fieldnames=fieldnames, dialect='excel')
    delete_items.writeheader()
    for row1 in before_list:
        if row1['id'] not in indexes_after:
                delete_items.writerow(row1)       
    print("New file with records to be deleted is ready!")

    #Records to be updated
    update_items = csv.DictWriter(Update, fieldnames=fieldnames, dialect='excel')
    update_items.writeheader()
    for row2 in after_list:
        if row2['id'] in indexes_before:
            update_items.writerow(row2)
    print("New file with records to be updated is ready!")

    
   

            
       

