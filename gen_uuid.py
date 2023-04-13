import uuid

def generate_uuid(num_uuids):
    uuid_list = []
    for i in range(num_uuids):
        uuid_list.append(str(uuid.uuid4()))
    return uuid_list

# Example usage:
num_uuids = 2  # Change this number to generate more or fewer UUIDs
uuid_list = generate_uuid(num_uuids)
print(uuid_list)