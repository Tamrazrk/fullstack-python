class Family:
    def __init__(self, members, last_name):
        self.members = members
        self.last_name = last_name

    def born(self, **new_member):
        print(f"Congratulations to the entire family on the arrival of your newest member: {new_member['name']}!")
        self.members.append(new_member)

    def is_18(self, member_name):
        try:
            member = list(filter(lambda mem: mem['name'] == member_name,
                                self.members))[0]
            return member['age'] >= 18
        except IndexError:
            raise Exception(f"member with name {member_name} not found!")

    def family_presentation(self):
        print(f"{self.last_name}'s family:", end=' ')
        print(', '.join([mem['name'] for mem in self.members]))


if __name__ == '__main__':
    smith = Family(
        [
            {'name':'Michael','age':35,'gender':'Male','is_child':False},
            {'name':'Sarah','age':32,'gender':'Female','is_child':False}
        ],
        'Smith'
    )

    smith.born(**{'name':'Brad','age': 0,'gender':'Male','is_child':True})
    smith.born(**{'name':'Angelina','age': 0,'gender':'Female','is_child':True})

    print("Michael is over 18:", smith.is_18('Michael'))
    print("Brad is over 18:", smith.is_18('Brad'))
    # print(smith.is_18('No_member'))

    smith.family_presentation()
