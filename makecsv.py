import csv

categories = [
    ['Computers'],
    ['Projectors'],
    ['Cables'],
    ['Benches'],
    ['Chairs']
]

floors = [
    [1],
    [2],
    [3]
]

rooms = [
    [101, 'Room 101', 1],
    [201, 'Room 201', 2],
    [301, 'Room 301', 3]
]

items = [
    [1, 1, 'Dell Laptop', 'Generic', 1200, 101, '2023-06-01', 5, 0, 0],
    [2, 2, 'Epson Projector', 'Generic', 1500, 201, '2023-06-01', 1, 0, 0],
    [3, 3, 'HDMI Cable', 'Generic', 10, 301, '2023-06-01', 20, 0, 0],
    [4, 4, 'Wooden Bench', 'Generic', 100, 101, '2023-06-01', 10, 2, 0],
    [5, 5, 'Office Chair', 'Generic', 80, 201, '2023-06-01', 15, 0, 1]
]

sub_items = [
    [1, 1, 'Keyboard', 10, 0, 0],
    [2, 1, 'Mouse', 10, 0, 0],
    [3, 2, 'Remote Control', 1, 0, 0],
    [4, 3, 'Power Cable', 20, 0, 0]
]

def write_to_csv(data, file_path):
    with open(file_path, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(data)

# Usage example
write_to_csv(categories, 'categories.csv')
write_to_csv(floors, 'floors.csv')
write_to_csv(rooms, 'rooms.csv')
write_to_csv(items, 'items.csv')
write_to_csv(sub_items, 'sub_items.csv')
