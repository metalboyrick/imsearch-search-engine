import sqlite3

def populate_image(conn):
    
    with open("./imsearch/data/url_mappings.csv", "r", encoding="utf8") as f:
        is_first = True
        lines = f.readlines()
        for line in lines:
            if is_first:
                is_first = False
                continue
            cursor = conn.cursor()
            split_line = line.split(",")
            img_id = split_line[0]
            img_name = f'{img_id}.jpg'
            cursor.execute(f'INSERT INTO search_service_image VALUES ("{img_id}", "{img_name}")')
            cursor.close()

def populate_label(conn):

    with open("./imsearch/data/class_descriptions.csv", "r", encoding="utf8") as f:
        lines = f.readlines()

        for line in lines:
            cursor = conn.cursor()
            split_line = line.split(",")
            label_id = split_line[0]
            label_name = split_line[1]
            cursor.execute(f'insert into search_service_label values ("{label_id}", "{label_name}")')
            cursor.close()

    with open("./imsearch/data/attributes_descriptions.csv", "r", encoding="utf8") as f:
        lines = f.readlines()

        for line in lines:
            cursor = conn.cursor()
            split_line = line.split(",")
            label_id = split_line[0]
            label_name = split_line[1]
            cursor.execute(f'insert into search_service_label values ("{label_id}", "{label_name}")')
            cursor.close()

def populate_image_labels(conn):

    with open("./imsearch/data/image_annotations.csv", "r", encoding="utf8") as f:
        lines = f.readlines()
        is_first = True
        count = 1
        for line in lines:
            if is_first:
                is_first = False
                continue
            cursor = conn.cursor()
            split_line = line.split(",")
            image_id = split_line[0]
            label_id = split_line[2]
            cursor.execute(f'insert into search_service_imagelabels values ({count}, "{image_id}", "{label_id}")')
            cursor.close()
            count += 1
 

def populate_image_relationships(conn):

    with open("./imsearch/data/relationships.csv", "r", encoding="utf8") as f:
        lines = f.readlines()
        count = 1
        for line in lines[1:]:
            cursor = conn.cursor()
            split_line = line.split(",")
            label_1 = split_line[0]
            label_2 = split_line[1]
            relationship = split_line[2]
            cursor.execute(f'insert into search_service_imagerelationship values ({count},"{label_1}", "{label_2}", "{relationship}")')
            cursor.close()
            count += 1

def main():
    connection = sqlite3.connect('./imsearch/db.sqlite3')
    with connection:
        populate_image(connection)
        populate_label(connection)
        populate_image_labels(connection)
        populate_image_relationships(connection)
    pass

if __name__ == "__main__":
    main()
