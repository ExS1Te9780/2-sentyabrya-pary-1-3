class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')
    
    def insert(self, data):
        for row in data:
            values = row.split()
            record = {}
            for i, field in enumerate(self.FIELDS):
                record[field] = values[i]
            self.lst_data.append(record)
    
    def select(self, a, b):
        if b >= len(self.lst_data):
            b = len(self.lst_data) - 1
        return self.lst_data[a:b+1]