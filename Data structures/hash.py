class Hash:
    def __init__(self, size=7):
        self.data_map=[None]*size

    def __hash(self, key):
        my_hash=0
        for letter in key:
            my_hash=(my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash

    def print_table(self):
        for index, data in enumerate(self.data_map):
            print(index, ": ", data)

    def set(self, key, value):
        index=self.__hash(key)
        if self.data_map[index]==None:
            self.data_map[index]=[]
        self.data_map[index].append([key, value])

    def get(self, key):
        index=self.__hash(key)
        data=self.data_map[index]
        if data is None: return None
        for item in data:
            if item[0]==key:
                return item[1]
        return None

    def keys(self):
        keys_list=[]
        for data in self.data_map:
            if data is None: continue
            for item in data:
                keys_list.append(item[0])
        return keys_list







hashvar=Hash()
hashvar.set("tên", "Phú")
hashvar.set("tuổi", "26")
hashvar.set("trình độ", "12/12")
hashvar.set("dân tộc", "kinh")
hashvar.set("Quốc tịch", "Việt Nam")
hashvar.set("tôn giáo", "Công giáo")
hashvar.set("Nghề nghiệp", "IT")
hashvar.print_table()
print(hashvar.get("dân tộc"))
keys=hashvar.keys()
print(keys)
