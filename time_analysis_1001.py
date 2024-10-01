import pandas as pd


file_path_excel = r"C:\Users\SM-PC\Desktop\2024_2\MEIT\08월 서울시 교통량 조사자료(2024).xlsx"


address_data = pd.read_excel(file_path_excel, sheet_name='수집지점 주소 및 좌표')
traffic_data = pd.read_excel(file_path_excel, sheet_name='2024년 08월')

def get_traffic_data_for_districts(districts, start_hour, end_hour):

    all_district_point_numbers = []
    for district in districts:
 
        cleaned_address_data = address_data.dropna(subset=['주소'])
        

        district_data = cleaned_address_data[cleaned_address_data['주소'].str.contains(district)]
        district_point_numbers = district_data['지점번호'].tolist()
        all_district_point_numbers.extend(district_point_numbers)  
    

    district_traffic_data = traffic_data[traffic_data['지점번호'].isin(all_district_point_numbers)]
    

    hourly_columns = [f'{i}시' for i in range(start_hour, end_hour + 1)]
    

    traffic_sum_per_hour = district_traffic_data[hourly_columns].sum()
    
    
    sorted_traffic = traffic_sum_per_hour.sort_values()
    
    return sorted_traffic


district_input = input("구 이름을 쉼표로 구분하여 입력하세요 (예: 종로구, 용산구): ")
districts_list = [district.strip() for district in district_input.split(",")]  
start_hour_input = int(input("분석할 시작 시간 (예: 9): "))
end_hour_input = int(input("분석할 종료 시간 (예: 17): "))


traffic_result = get_traffic_data_for_districts(districts_list, start_hour_input, end_hour_input)
print(traffic_result)
