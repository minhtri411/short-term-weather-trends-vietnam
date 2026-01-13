# TP.HCM Urban Microclimate Dataset & Analysis (2024–2025)

## Mục lục
1. [Tổng quan dự án](#1-tổng-quan-dự-án)
2. [Nguồn và mô tả dữ liệu](#2-nguồn-và-mô-tả-dữ-liệu)
   - [2.1 Chủ đề dữ liệu](#21-chủ-đề-dữ-liệu)
   - [2.2 Nguồn dữ liệu](#22-nguồn-dữ-liệu)
   - [2.3 Giấy phép sử dụng](#23-giấy-phép-sử-dụng)
   - [2.4 Phương pháp thu thập dữ liệu](#24-phương-pháp-thu-thập-dữ-liệu)
   - [2.5 Chiến lược lựa chọn điểm đại diện & độ phân giải](#25-chiến-lược-lựa-chọn-điểm-đại-diện--độ-phân-giải)
3. [Cấu trúc thư mục](#3-cấu-trúc-thư-mục)
4. [Hướng dẫn chạy dự án](#4-hướng-dẫn-chạy-dự-án)
5. [Thư viện và công nghệ sử dụng](#5-thư-viện-và-công-nghệ-sử-dụng)

---

## 1. Tổng quan dự án

### Tên dự án
**Phân tích vi khí hậu đô thị, hiệu ứng đảo nhiệt đô thị (Urban Heat Island – UHI)  
và dự báo nhiệt độ ngắn hạn tại Thành phố Hồ Chí Minh (2024–2025)**

### Mục tiêu
- Xây dựng bộ dữ liệu thời tiết theo giờ cho TP.HCM phục vụ phân tích vi khí hậu đô thị.
- So sánh đặc trưng khí hậu giữa các khu vực đô thị lõi, đô thị mở rộng, vùng chuyển tiếp nông thôn và ven biển.
- Cung cấp nền tảng dữ liệu cho nghiên cứu đảo nhiệt đô thị (UHI), cảnh báo nhiệt và hỗ trợ quy hoạch đô thị thích ứng khí hậu.

### Phạm vi thời gian
- Thời gian: **01/01/2024 – 31/12/2025**
- Độ phân giải thời gian: **Theo giờ (hourly)**

---

## 2. Nguồn và mô tả dữ liệu

### 2.1 Chủ đề dữ liệu
Dữ liệu thời tiết lịch sử theo giờ của TP.HCM, được trích xuất tại **5 điểm đại diện** cho các vùng khí hậu – đô thị đặc trưng, dựa trên dữ liệu tái phân tích khí hậu (*reanalysis*).

| Vùng đại diện | Tọa độ (lat, lon) | Loại vùng khí hậu |
|--------------|------------------|------------------|
| Quận 1 | 10.7769, 106.7009 | Urban Core |
| TP. Thủ Đức | 10.8443, 106.7725 | Urban Expansion |
| Củ Chi | 11.0067, 106.5132 | Rural Transition |
| Quận 7 | 10.7028, 106.7226 | Planned Urban |
| Cần Giờ | 10.4114, 106.9546 | Coastal |

---

### 2.2 Nguồn dữ liệu
- **Open-Meteo Historical Weather API**  
  https://open-meteo.com/

Dữ liệu được xây dựng từ các mô hình tái phân tích khí hậu **ERA5 / IFS (ECMWF)**, phù hợp cho phân tích khí hậu quy mô đô thị và khu vực.

---

### 2.3 Giấy phép sử dụng
- Dữ liệu Open-Meteo được sử dụng miễn phí cho mục đích nghiên cứu và phi thương mại.
- Khi công bố kết quả, cần trích dẫn **Open-Meteo** và **ECMWF (ERA5)** theo quy định nguồn dữ liệu.

---

### 2.4 Phương pháp thu thập dữ liệu
- Truy vấn dữ liệu theo tọa độ địa lý (*latitude, longitude*) thông qua Open-Meteo API.
- Độ phân giải không gian xấp xỉ **9 × 9 km**, tương ứng với một ô lưới khí hậu.

---

### 2.5 Chiến lược lựa chọn điểm đại diện & độ phân giải
- TP.HCM có địa hình thấp, bằng phẳng → tương quan không gian cao trong bán kính **10–15 km**.
- Một ô lưới khí hậu (~81 km²) có thể đại diện cho nhiều đơn vị hành chính.
- Lựa chọn **5 điểm đại diện cho 5 cơ chế khí hậu khác nhau**, thay vì phủ toàn bộ 22 quận nhằm:
  - Tránh trùng lặp thông tin
  - Giảm đa cộng tuyến trong phân tích
  - Phù hợp với bản chất dữ liệu khí hậu dạng lưới
- Độ phân giải ~9 km đạt cân bằng giữa:
  - Khả năng phân biệt vi khí hậu đô thị
  - Độ tin cậy vật lý của dữ liệu reanalysis
  - Hiệu quả tính toán và mô hình hóa

---

## 3. Cấu trúc thư mục

```text
project-folder/
├── data/
│   ├── hcm_weather_overview.csv
│   └── hcm_weather_processed.csv
│
├── notebooks/
│   ├── 01_data_collection.ipynb
│   ├── 02_data_exploration.ipynb
│   ├── 03_feature_engineering.ipynb
│   ├── 04_meaningful_questions.ipynb
│   └── 05_data_modeling.ipynb
│
├── src/
│   └── preprocessing_utils.py
│
├── environment.yml
├── LICENSE
└── README.md
```

## Mô tả chi tiết

### data/
- **hcm_weather_overview.csv**  
  Dữ liệu thời tiết theo giờ từ Open-Meteo cho 5 điểm đại diện (chưa xử lý).

- **hcm_weather_processed.csv**  
  Dữ liệu đã làm sạch, chuẩn hóa thời gian, gắn nhãn vùng khí hậu và tạo biến phục vụ phân tích & mô hình hóa.

### notebooks/
- **01_data_collection.ipynb** – Thu thập dữ liệu từ Open-Meteo API.  
- **02_data_exploration.ipynb** – Khám phá và so sánh đặc trưng khí hậu theo vùng.  
- **03_feature_engineering.ipynb** – Xây dựng biến thời gian và đặc trưng khí hậu dẫn xuất.  
- **04_meaningful_questions.ipynb** – Xây dựng và phân tích các câu hỏi mô hình hóa có ý nghĩa.  
- **05_data_modeling.ipynb** – Huấn luyện, đánh giá và so sánh mô hình dự báo nhiệt độ.

### src/
- **preprocessing_utils.py** – Hàm tiện ích dùng chung cho làm sạch và chuẩn hóa dữ liệu.

### Các file khác
- **environment.yml** – Môi trường Conda và thư viện.  
- **LICENSE** – Giấy phép sử dụng.  
- **README.md** – Tài liệu tổng quan dự án.

---

## 4. Hướng dẫn chạy dự án

### Bước 1: Clone repository
Chạy lệnh sau trong Terminal (Ubuntu hoặc Terminal của VS Code):
```bash
git clone <repository-url>
```
### Bước 2: Di chuyển vào thư mục dự án
Chạy trong Terminal (Ubuntu hoặc Terminal của VS Code):
```bash
cd <project-folder>
```
### Bước 3: Tạo môi trường Conda
Chạy trong Terminal (Ubuntu hoặc Terminal của VS Code):
```bash
conda env create -f environment.yml
conda activate environment
```
### Bước 4: Chạy notebook
Mở Jupyter Notebook, JupyterLab hoặc Visual Studio Code (VS Code), sau đó chạy lần lượt các notebook trong thư mục notebooks/:
```bash
- 01_data_collection.ipynb

- 02_data_exploration.ipynb

- 03_feature_engineering.ipynb

- 04_meaningful_questions.ipynb

- 05_data_modeling.ipynb
```
**Lưu ý:**
  - Nếu chạy notebook trong VS Code, hãy chắc chắn đã chọn đúng Python Interpreter / Conda environment.
  - Trên Ubuntu, có thể mở notebook bằng lệnh jupyter notebook hoặc jupyter lab.
### 5. Thư viện và công nghệ sử dụng
- **Python**: 3.11.5

- **Core & Data Handling**:
  - pandas 2.1.1
  - numpy 1.26.0
  - scipy 1.11.3
  - openpyxl 3.1.2

- **Machine Learning**:
  - scikit-learn 1.3.1
  - xgboost 3.1.2
  - statsmodels 0.14.0  # cho ARIMA và time series

- **Visualization**:
  - matplotlib 3.8.0
  - seaborn 0.13.0
  - plotly 5.17.0

- **Jupyter & Extensions**:
  - JupyterLab 4.0.7
  - jupyter_contrib_nbextensions 0.7.0
  - ipywidgets 8.1.1
  - nbdime 3.2.1
  - ipython  # để dùng display, HTML

- **Version Control & Utilities**:
  - git 2.42.0
  - pip 23.3
  - jupyter-black (formatter)


