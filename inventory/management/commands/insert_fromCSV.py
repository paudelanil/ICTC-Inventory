import csv
from django.apps import apps
from django.core.management.base import BaseCommand
from datetime import datetime

class Command(BaseCommand):
    help = 'Inserts CSV data into the database'

    def handle(self, *args, **options):
        Categorie = apps.get_model('inventory', 'Categorie')
        Floor = apps.get_model('inventory', 'Floor')
        Room = apps.get_model('inventory', 'Room')
        Item = apps.get_model('inventory', 'Item')
        SubItem = apps.get_model('inventory', 'SubItem')

        with open('data.csv', 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                # Insert Categories
                category_name = row['category_name']
                Categorie.objects.get_or_create(category_name=category_name)

                # Insert Floors
                floor_number = int(row['floor_number'])
                floor, _ = Floor.objects.get_or_create(floor=floor_number)

                # Insert Rooms
                room_number = int(row['room_number'])
                room_name = row['room_name']
                Room.objects.get_or_create(room_no=room_number, room_name=room_name, floor=floor)

                # Insert Items
                category_name = row['category_name']
                category = Categorie.objects.get(category_name=category_name)
                item_name = row['item_name']
                item_model = row['item_model'] if (row['item_model']) else 0
                cost = row['cost_per_item']
                if cost:
                    cost_per_item = float(row['cost_per_item'])  
                else:
                    cost_per_item= None
                room_number = int(row['room_number']) if (row['room_number']) else 0
                date_of_acquire = row['date_of_acquire']                
                date_string = row['date_of_acquire']
                if date_string:
                    date_of_acquire = datetime.strptime(date_string, "%m/%d/%y").strftime("%Y-%m-%d")
                else:
                    date_of_acquire = None
                working = int(row['working']) if (row['working']) else 0
                in_maintenance = int(row['in_maintenance']) if (row['in_maintenance']) else 0
                out_of_order = int(row['out_of_order']) if row['out_of_order'] else 0
                itemSource = row['item_source']
                remarks = row['remarks']
                room = Room.objects.get(room_no=room_number)
                item = Item(category=category, name=item_name, model=item_model, cost_per_item=cost_per_item,
                            room=room, date_of_acquire=date_of_acquire, working=working,
                            in_maintenance=in_maintenance, out_of_order=out_of_order,remarks= remarks,itemSource=itemSource)
                item.save()

                # Insert SubItems
                # Insert SubItems
                # item_name = row['item_name']
                # items = Item.objects.filter(name=item_name)
                # if items.exists():
                #     item = items.first()
                #     sub_item_name = row['sub_item_name']
                #     sub_item_working = int(row['sub_item_working']) if (row['sub_item_working']) else 0
                #     sub_item_in_maintenance = int(row['sub_item_in_maintenance']) if (row['sub_item_in_maintenance']) else 0
                #     sub_item_out_of_order = int(row['sub_item_out_of_order']) if (row['sub_item_out_of_order']) else 0
                #     sub_item = SubItem(item=item, name=sub_item_name, working=sub_item_working,
                #                        in_maintenance=sub_item_in_maintenance, out_of_order=sub_item_out_of_order)
                #     sub_item.save()
                # else:
                #     # Handle the case when no matching Item object is found
                #     print(f"No matching Item object found for name: {item_name}. Skipping sub-item creation.")

