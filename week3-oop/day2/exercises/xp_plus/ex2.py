from ex1 import Family

class TheIncredibles(Family):
    def use_power(self, member_name):
        if not self.is_18(member_name):
            raise Exception(f"{member_name} is not over 18 years old!")

        member = list(filter(lambda mem: mem['name'] == member_name,
                             self.members))[0]
        print(f"{member_name} power: {member['power']}")

    def incredible_presentation(self):
        self.family_presentation()
        print('\n'.join([f"{mem['incredible_name']} --> {mem['power']}"
                         for mem in self.members]))


if __name__ == '__main__':
    incredible_family = TheIncredibles(
        [
            {'name':'Michael','age':35,'gender':'Male','is_child':False,'power': 'fly','incredible_name':'MikeFly'},
            {'name':'Sarah','age':32,'gender':'Female','is_child':False,'power': 'read minds','incredible_name':'SuperWoman'}
        ],
        'Smith'
    )

    incredible_family.incredible_presentation()
    incredible_family.born(
        name='Jack',
        age=0,
        gender='Male',
        is_child=True,
        power='Unknown Power',
        incredible_name='UnknownMan'
    )
    incredible_family.incredible_presentation()
