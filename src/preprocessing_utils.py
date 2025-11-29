# src/preprocessing_utils.py

import pandas as pd
import numpy as np

def load_data(filepath):
    """
    Đọc dữ liệu từ file CSV.
    """
    try:
        df = pd.read_csv(filepath)
        print(f" Đã load dữ liệu thành công từ {filepath}. Kích thước: {df.shape}")
        return df
    except FileNotFoundError:
        print(f" Không tìm thấy file tại {filepath}")
        return None

def initial_exploration(df):
    """
    In ra thông tin tổng quan về dữ liệu.
    """
    print("--- 5 dòng đầu tiên ---")
    display(df.head())
    print("\n--- Thông tin kiểu dữ liệu (Info) ---")
    print(df.info())
    print("\n--- Thống kê mô tả (Describe) ---")
    display(df.describe())

def handle_duplicates(df):
    """
    Kiểm tra và xóa dữ liệu trùng lặp.
    """
    initial_rows = len(df)
    df = df.drop_duplicates()
    deleted_rows = initial_rows - len(df)
    if deleted_rows > 0:
        print(f" Đã xóa {deleted_rows} dòng trùng lặp.")
    else:
        print(" Không có dữ liệu trùng lặp.")
    return df

def convert_datatypes(df):
    """
    Chuyển đổi kiểu dữ liệu cho cột thời gian và map weather code.
    """
    # 1. Chuyển đổi cột time sang datetime
    if 'time' in df.columns:
        df['time'] = pd.to_datetime(df['time'])
        print(" Đã chuyển cột 'time' sang kiểu datetime.")
    
    return df

def add_time_features(df, time_col='time'):
    """
    Tách các đặc trưng thời gian (Feature Engineering).
    """
    if time_col in df.columns:
        df['year'] = df[time_col].dt.year
        df['month'] = df[time_col].dt.month
        df['day'] = df[time_col].dt.day
        df['hour'] = df[time_col].dt.hour
        df['day_of_week'] = df[time_col].dt.day_name()
        print(" Đã thêm các cột: year, month, day, hour, day_of_week.")
    return df

def map_weather_code(df, code_col='weather_code'):
    """
    Thêm cột mô tả thời tiết dựa trên WMO code.
    """
    wmo_codes = {
        0: 'Clear sky', 1: 'Mainly clear', 2: 'Partly cloudy', 3: 'Overcast',
        45: 'Fog', 48: 'Depositing rime fog',
        51: 'Drizzle: Light', 53: 'Drizzle: Moderate', 55: 'Drizzle: Dense',
        61: 'Rain: Slight', 63: 'Rain: Moderate', 65: 'Rain: Heavy',
        71: 'Snow: Slight', 73: 'Snow: Moderate', 75: 'Snow: Heavy',
        80: 'Rain showers: Slight', 81: 'Rain showers: Moderate', 82: 'Rain showers: Violent',
        95: 'Thunderstorm: Slight or moderate',
        96: 'Thunderstorm with hail: Slight', 99: 'Thunderstorm with hail: Heavy'
    }
    
    if code_col in df.columns:
        df['weather_description'] = df[code_col].map(wmo_codes)
        print(" Đã thêm cột 'weather_description'.")
    return df

def handle_missing_values(df):
    """
    Xử lý giá trị thiếu bằng phương pháp nội suy tuyến tính (Linear Interpolation)
    phù hợp cho chuỗi thời gian (Time Series).
    """
    missing_count = df.isnull().sum().sum()
    if missing_count > 0:
        print(f" Phát hiện {missing_count} giá trị bị thiếu. Đang tiến hành nội suy...")
        # Nội suy tuyến tính theo thời gian
        df = df.interpolate(method='linear', limit_direction='both')
        print(" Đã xử lý xong giá trị thiếu.")
    else:
        print(" Không có giá trị bị thiếu (Missing values).")
    return df

def sanity_check(df):
    """
    Kiểm tra các giá trị vô lý trong dữ liệu.
    """
    print("\n--- Kiểm tra tính hợp lệ (Sanity Check) ---")
    issues = []
    
    # Kiểm tra độ ẩm
    if 'relative_humidity_2m' in df.columns:
        invalid_hum = df[(df['relative_humidity_2m'] < 0) | (df['relative_humidity_2m'] > 100)]
        if not invalid_hum.empty:
            issues.append(f" Có {len(invalid_hum)} dòng độ ẩm sai logic (0-100%).")
        else:
            print(" Dữ liệu Độ ẩm hợp lệ.")

    # Kiểm tra lượng mưa
    if 'precipitation' in df.columns:
        invalid_rain = df[df['precipitation'] < 0]
        if not invalid_rain.empty:
            issues.append(f" Có {len(invalid_rain)} dòng lượng mưa âm.")
        else:
            print(" Dữ liệu Lượng mưa hợp lệ.")
            
    if not issues:
        print("=> Bộ dữ liệu có vẻ hợp lý về mặt vật lý.")
    else:
        print("=> Cần xem xét lại các vấn đề trên.")

def save_data(df, filepath):
    """
    Lưu dữ liệu ra file CSV.
    """
    df.to_csv(filepath, index=False)
    print(f" Đã lưu dữ liệu đã xử lý vào: {filepath}")