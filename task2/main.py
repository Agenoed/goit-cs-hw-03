from pymongo import MongoClient
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId
import os


MONGO_URI = "mongodb+srv://jamersong321:PhZoUlM5DXb4wGXQ@myfirstdatabase.oehyt.mongodb.net/?retryWrites=true&w=majority&appName=myFirstDatabase"


client = MongoClient(MONGO_URI, server_api=ServerApi('1'))
db = client["myFirstDatabase"]  
collection = db["cats"]  

def insert_cat(name, age, features):
    """Додає нового кота в колекцію."""
    try:
        result = collection.insert_one(
            {
                "name": name,
                "age": age,
                "features": features
            }
        )
        print(f"Cat added with id: {result.inserted_id}")
        return result.inserted_id
    except Exception as e:
        print(f"Error adding cat: {e}")
        return None


def get_all_cats():
    """Виводить інформацію про всіх котів в колекції."""
    try:
        cats = collection.find()
        for cat in cats:
            print(cat)
    except Exception as e:
        print(f"Error getting all cats: {e}")


def get_cat_by_name(name):
    """Виводить інформацію про кота за ім'ям."""
    try:
        cat = collection.find_one({"name": name})
        if cat:
            print(cat)
        else:
            print(f"Cat with name '{name}' not found.")
    except Exception as e:
        print(f"Error getting cat by name: {e}")


def update_cat_age(name, new_age):
    """Оновлює вік кота за ім'ям."""
    try:
        result = collection.update_one({"name": name}, {"$set": {"age": new_age}})
        if result.modified_count > 0:
            print(f"Cat '{name}' age updated to {new_age}")
        else:
            print(f"Cat with name '{name}' not found.")
    except Exception as e:
        print(f"Error updating cat age: {e}")


def add_cat_feature(name, new_feature):
    """Додає нову характеристику до списку features кота за ім'ям."""
    try:
        result = collection.update_one({"name": name}, {"$push": {"features": new_feature}})
        if result.modified_count > 0:
            print(f"Feature '{new_feature}' added to cat '{name}'")
        else:
            print(f"Cat with name '{name}' not found.")
    except Exception as e:
        print(f"Error adding cat feature: {e}")


def delete_cat_by_name(name):
    """Видаляє кота з колекції за ім'ям."""
    try:
        result = collection.delete_one({"name": name})
        if result.deleted_count > 0:
            print(f"Cat '{name}' deleted")
        else:
            print(f"Cat with name '{name}' not found.")
    except Exception as e:
        print(f"Error deleting cat: {e}")


def delete_all_cats():
    """Видаляє всі записи з колекції."""
    try:
        result = collection.delete_many({})
        print(f"Deleted {result.deleted_count} cats")
    except Exception as e:
        print(f"Error deleting all cats: {e}")


def main():
    while True:
        print("\nChoose an operation:")
        print("1. Add a cat")
        print("2. Get all cats")
        print("3. Get cat by name")
        print("4. Update cat age")
        print("5. Add cat feature")
        print("6. Delete cat by name")
        print("7. Delete all cats")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            name = input("Enter cat name: ")
            age = int(input("Enter cat age: "))
            features = input("Enter cat features (comma-separated): ").split(',')
            insert_cat(name, age, features)
        elif choice == '2':
            get_all_cats()
        elif choice == '3':
            name = input("Enter cat name: ")
            get_cat_by_name(name)
        elif choice == '4':
            name = input("Enter cat name: ")
            new_age = int(input("Enter new age: "))
            update_cat_age(name, new_age)
        elif choice == '5':
            name = input("Enter cat name: ")
            new_feature = input("Enter new feature: ")
            add_cat_feature(name, new_feature)
        elif choice == '6':
            name = input("Enter cat name: ")
            delete_cat_by_name(name)
        elif choice == '7':
            delete_all_cats()
        elif choice == '8':
            print("Exiting...")
            client.close()
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()