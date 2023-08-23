# Inventory Management System (Storage)

Inventory items can divided into categories having category-specific properties which can be custom-added by the user.

This is basicaly a CRUD system for Floor, Room, Category, Item and User.

It also has an advanced filter page with intuitive tables and add/edit/delete facility from the table itself.

CSV files are also available for download.



### Usage

- `pip install -r requirements.txt`
- `python manage.py makemigrations`
- `python manage.py migrate`
- `python manage.py createsuperuser` and add an admin user
- `python manage.py insert_fromCSV` to bulk upload data from csv
- `python manage.py runserver`
- Open 127.0.0.1:8000 on your browser and login with admin credentials

### Features
- Add Item
    - An item can be added  directly to any location or to **Store** by default. One can select it's category or add new category for the item.
    - Not selecting any Rooom options will directly assign location to store.
    - Unique value for an item's **name and model** is maintained while adding new item.
- Advanced Search
  - **Filtering by Floor, Room, and Category:** You can filter items by selecting a floor, room, or category from the dropdown menus.
  - **Searching by Item Name:** Use the search bar to find items by their name. Also can be used to search items by room,model's name. As you type, the system will display items that match the search query.
  - **Sorting Items:** Items can be sorted based on name, model, room, cost, verification date, working items number .

  - **Actions**
      - Adding Items: To add a new item, click the "Add" button on the "Actions" column  of items.
        
      - Editing Items: Edit an item's details by clicking the "Edit" button on "Actions" column  of items.. Update the necessary information and save the changes.
        
      - Verifying Items: Ensure the accuracy of item details by verifying them. Click the "Verify" button on "Actions" column  of items.to mark the item as verified. It will also show verification logs for verified items.
        
      - Deleting Items: If you have the required permissions, you can delete items by clicking the "Delete" button on "Actions" column  of items. Be cautious, as this action is irreversible.
        
      - Reallocating Items: Reallocate an item to a different room by clicking the "Reallocate" button on "Actions" column  of items. Select the new room and save the changes. If that item's already in the destination room, the quantity will simply add up.
- Settings        
  - Floor Management:

    **Add:** Clicking on "Add" allows you to create a new floor.    
   **Edit:** Redirects to the page where you can edit existing floor details.    
    **Delete:** Opens a page where you can delete a floor.

  - Room Management:

    **Add:** Enables you to create a new room.    
    **Edit:** Takes you to a page for editing room information.     
    **Delete:** Redirects to a page where you can delete a room.

  - Category Management:

    **Add:** Clicking on "Add" allows you to create a new category.    
    **Edit:** Redirects to a page for editing category details.    
    **Delete:** Opens a page where you can delete a category.
    

  - Admin Settings:
    
    Update Info: Clicking on "Update Info" takes you to a page where you can edit your admin account information.
- Download
  
    User can download CSV file  for each cateogry. It includes all the item details in a csv format.
    
     
### Screenshots
 



![0](https://user-images.githubusercontent.com/83212553/180799227-f6754db0-b6b8-424d-9d65-6039e5449a8e.png)
![1](https://user-images.githubusercontent.com/83212553/180799238-4f67ef05-136f-4511-8b0f-b4246cebe601.png)
![2](https://user-images.githubusercontent.com/83212553/180799249-01d5b372-2e19-4fae-bb48-e110ea5b4e7d.png)
![3](https://user-images.githubusercontent.com/83212553/180799264-6281cb84-5709-4c51-a740-2b5024feff33.png)


