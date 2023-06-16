class parking_spot:
    __item = {}
    def __init__(self, name, city, district, ptype, longitude, latitude):
        self.__item = {'name':str(name), 'city':str(city), 'district':str(district), #프로그램 실행과 동시에 가져온 파일의 '순번'을 제외해서 출력해 주는 프로그램이다
                       'ptype':str(ptype), 'longitude':float(longitude), 'latitude':float(latitude)}
    def get(self, keyword = 'name'):
        return self.__item[keyword]
        

    def __str__(self):
        item = self.__item
        s  = f"[{item['name']}({item['ptype']})] "
        s += f"{item['city']} {item['district']}"
        s += f"(lat:{item['latitude']}, long:{item['longitude']})"
        return s
    
def str_list_to_class_list(str_list): #'순번'을 제외한 나머지 데이터를 ','로 나누어서 연속적으로 값을 가져와 주는 함수이다
    str_list1 = []
    for i in str_list:
        b = i.split(',')
        name = b[1]
        city = b[2]
        district = b[3]
        ptype = b[4]
        longitude = b[5]
        latitude = b[6]
        a = parking_spot(name, city, district, ptype, longitude, latitude)
        str_list1.append(a)
    return str_list1
def print_spots(spots): #spots의 길이를 알려주는 함수 이다
    print(f"---print elements({len(spots)})---")
    for i in spots:
        print(i)


# 각 단계별로 테스트 (테스트할때 주석해제 후 사용)
if __name__ == '__main__':
    print("Testing the module...")
    # version#2
    import file_manager
    str_list = file_manager.read_file("./input/free_parking_spot_seoul.csv")
    spots = str_list_to_class_list(str_list)
    print_spots(spots)

    # version#3
    # spots = filter_by_district(spots, '동작')
    # print_spots(spots)
    
    # version#4
    # spots = sort_by_keyword(spots, 'name')
    # print_spots(spots)
