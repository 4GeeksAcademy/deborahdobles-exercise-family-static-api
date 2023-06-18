from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        self._members = [
                        {
                "id": self._generateId(),
                "first_name": "John",
                "last_name": last_name,
                "age": 33,
                "lucky_numbers": [7, 13, 22]
            },
            {
                "id": self._generateId(),
                "first_name": "Jane",
                "last_name": last_name,
                "age": 35,
                "lucky_numbers": [10, 14, 3]
            },
            {
                "id": self._generateId(),
                "first_name": "Jimmy",
                "last_name": last_name,
                "age": 5,
                "lucky_numbers": [1]
            }
        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        new_member =  {
                "id": member["id"],
                "first_name": member["first_name"],
                "last_name": self.last_name,
                "age":member["age"],
                "lucky_numbers": member["lucky_numbers"]
            }
        return self._members.append(new_member)        

    def delete_member(self, id):
        # fill this method and update the return
        for member in self._members:
            if member['id'] == id:
                self._members.remove(member)
                return True  # Member found and deleted
        return False

    def get_member(self, id):
        # fill this method and update the return
        for member in self._members:
            if member['id'] == id:
                return member
        return False

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
