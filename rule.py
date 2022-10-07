# -*- encoding:utf-8 -*-

# 找出去过吉普岛却没有去过新西兰的人

# 去过普吉岛的人员数据
users_visited_phuket = [
    {"first_name": "Sirena", "last_name": "Gross", "phone_number": "650-568-0388", "date_visited": "2018-03-14"},
    {"first_name": "James", "last_name": "Ashcraft", "phone_number": "412-334-4380", "date_visited": "2014-09-16"},
]

# 去过新西兰的人员数据
users_visited_nz = [
    {"first_name": "Justin", "last_name": "Malcom", "phone_number": "267-282-1964", "date_visited": "2011-03-13"},
    {"first_name": "Albert", "last_name": "Potter", "phone_number": "702-249-3714", "date_visited": "2013-09-11"},
    {"first_name": "James", "last_name": "Ashcraft", "phone_number": "412-334-4380", "date_visited": "2014-09-15"},
]

# 实际上就是去过吉普岛的人员集合 - 去过新西兰的人员集合


class VisitedData(object):
    def __init__(self, first_name, last_name, phone_number, date_visited) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.phone_name = phone_number
        self.date_visited = date_visited
    
    def __hash__(self) -> int:
        return hash(self.first_name + self.last_name)
    
    def __str__(self) -> str:
        return self.first_name + ':' + self.last_name
    
    def __repr__(self) -> str:
        return self.first_name + ':' + self.last_name
    
    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, VisitedData) and hash(__o.first_name + __o.last_name) == hash(self.first_name + self.last_name):
            return True

        return False


if __name__ == '__main__':
    phuket = {VisitedData(**d) for d in users_visited_phuket}
    nz = {VisitedData(**d) for d in users_visited_nz}
    print(phuket - nz)
