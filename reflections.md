# 2.5 Reflection - Phản ánh quá trình thực hiện dự án

---

## 1. Những khó khăn gặp phải (Difficulties Encountered)

###  Thành viên 1: [Thái Khắc Anh Tuấn - 23120112]
| Khó khăn | Mô tả chi tiết |
|----------|----------------|
| **Kiến thức domain về khí hậu học** | Cần tìm hiểu và nắm vững nhiều khái niệm chuyên ngành để có thể đặt câu hỏi và giải thích kết quả một cách khoa học, bao gồm: |
| → Hiệu ứng điều hòa của biển (Sea Breeze) | Hiểu cơ chế gió biển làm mát vùng ven biển (Cần Giờ → Quận 7) vào buổi chiều |
| → Vi khí hậu đô thị (Urban Microclimate) | Phân biệt đặc điểm 5 vùng khí hậu của TP.HCM: trung tâm, phía Đông, phía Nam, Tây Bắc, ven biển |
| → Hiệu ứng Đảo Nhiệt Đô Thị (UHI) | Hiểu tại sao khu vực đô thị (Quận 1) nóng hơn ngoại ô (Củ Chi), đặc biệt vào ban đêm |
| → Quán tính nhiệt (Thermal Inertia) | Giải thích tại sao bê tông/nhựa đường giữ nhiệt lâu hơn đất/cây xanh, dẫn đến "cú đấm đêm" (nocturnal heat pulse) |

###  Thành viên 2: [Hà Quốc Kiên - 23120056]
| Khó khăn | Mô tả chi tiết |
|----------|----------------|
| **Hyperparameter Tuning cho Random Forest** | Không gian tham số rất rộng, quá trình Grid Search tiêu tốn hơn 30 phút mỗi lần chạy. Phải giới hạn phạm vi tìm kiếm nhỏ hơn để tiết kiệm thời gian, dẫn đến rủi ro bỏ lỡ các tổ hợp tham số tối ưu hơn. |
| **Các vấn đề với mô hình ARIMA** | Việc xác định bậc (p,d,q) phù hợp cho từng khu vực là thách thức lớn. RMSE trên tập kiểm định liên tục ở mức cao (~3°C) - gấp 3 lần so với các mô hình ML. Chỉ số R² âm (-3 đến -7) ở ngưỡng dự báo 6 giờ ban đầu gây hoang mang, nhưng sau nghiên cứu đã hiểu đây là hiện tượng hợp lệ khi mô hình kém hơn baseline. |
| **Đảm bảo tính công bằng khi so sánh mô hình** | So sánh giữa ARIMA (chuỗi thời gian đơn biến) và các mô hình ML (đa biến) đòi hỏi thiết kế chiến lược đánh giá cẩn trọng để tránh thiên kiến, đồng thời giữ nguyên đặc thù riêng của từng mô hình. |

###  Thành viên 3: [Nguyễn Hoàng Minh Trí - 23120179]
| Khó khăn | Mô tả chi tiết |
|----------|----------------|
| **Data Leakage** | Đây là thách thức lớn nhất. Phải xử lý rất kỹ việc dịch chuyển (shift) dữ liệu để đảm bảo không vô tình dùng thông tin tương lai cho việc huấn luyện. |
| **Feature Engineering** | Việc tìm ra bộ đặc trưng tối ưu (Lag features, Cyclical features) đòi hỏi thử nghiệm liên tục để mô hình hiểu được tính chu kỳ của thời tiết. |
| **Đồng bộ dữ liệu đa vùng** | Xử lý nhiễu và dữ liệu khuyết cho 5 vùng riêng biệt mà vẫn giữ được tính tổng quát của quy trình là bài toán khó. |


---

## 2. Bài học kinh nghiệm (What We Learned)

###  Thành viên 1: [Thái Khắc Anh Tuấn - 23120112]

####  Về kiến thức domain khí hậu học
| Khái niệm | Bài học rút ra |
|-----------|----------------|
| **Hiệu ứng Đảo Nhiệt (UHI)** | UHI mạnh nhất vào ban đêm (0h-6h), không phải ban ngày như nhiều người nghĩ. Nguyên nhân: bê tông giữ nhiệt và tỏa ra vào đêm |
| **Sea Breeze Effect** | Gió biển từ Cần Giờ làm mát Quận 7 vào buổi chiều (14h-18h), giải thích tại sao vùng ven biển mát hơn trung tâm |
| **Vai trò của mây** | Mây có vai trò kép: "ô che nắng" ban ngày (giảm UHI) nhưng "chăn bông" ban đêm (tăng UHI) |
| **Mùa khô vs Mùa mưa** | UHI mạnh hơn vào mùa khô (~0.5°C) so với mùa mưa (~0.2°C) do mưa làm mát bề mặt |

####  Về phương pháp phân tích
- **Đặt câu hỏi có ý nghĩa (Meaningful Questions):** Thay vì chạy mô hình một cách máy móc, cần đặt các câu hỏi có ý nghĩa thực tiễn để khám phá dữ liệu
- **Kết hợp thống kê và trực quan:** Dùng kiểm định thống kê (t-test, ANOVA) để chứng minh, dùng biểu đồ để storytelling
- **Domain knowledge + Data Science:** Sự kết hợp giữa kiến thức chuyên ngành và kỹ năng phân tích dữ liệu tạo ra insights có giá trị thực sự
  

###  Thành viên 2: [Hà Quốc Kiên - 23120056]
####  Về thuật toán Machine Learning
- **Trade-off giữa Random Forest (Bagging) và XGBoost (Boosting):**
  - Random Forest: Giảm phương sai (variance) tốt, ổn định (robust), nhưng làm mượt các giá trị cực trị
  - XGBoost: Giảm độ lệch (bias) hiệu quả hơn, nhưng dễ overfit
  - Kết quả RMSE chỉ chênh 0.01°C → cả hai đều là strong learners

- **Error Propagation trong ARIMA:** Sai số ở mỗi bước dự báo tích lũy và ảnh hưởng đến các bước sau. Các mô hình ML dùng direct forecasting nên tránh được vấn đề này → ARIMA xuất sắc ở ngưỡng 1 giờ nhưng kém hiệu quả ở ngưỡng 24 giờ.

####  Về Feature Engineering
- Lag features trong 48 giờ đóng vai trò quan trọng nhất
- Mã hóa chu kỳ (cyclical encoding) dạng sin/cos hiệu quả hơn one-hot
- Domain knowledge (ví dụ: thêm feature gió cho vùng ven biển) có tác động rất đáng kể
- **Bài học:** "Đặc trưng tốt hơn" quan trọng hơn "nhiều dữ liệu hơn"

####  Về lựa chọn mô hình
Việc lựa chọn mô hình phải dựa trên yêu cầu cụ thể - không có giải pháp "one-size-fits-all":
| Mô hình | Phù hợp khi |
|---------|-------------|
| XGBoost | Cần độ chính xác cao nhất |
| Random Forest | Cân bằng tốc độ và độ chính xác |
| ARIMA | Dự báo đơn giản, ngắn hạn (1 giờ) |


###  Thành viên 3: [Nguyễn Hoàng Minh Trí - 23120179]
####  Về xử lý chuỗi thời gian
- **Time-series Split là bắt buộc:** Dữ liệu chuỗi thời gian phải cắt theo trục "Quá khứ → Tương lai", tuyệt đối không dùng `train_test_split` ngẫu nhiên
- **Sức mạnh của XGBoost:** Gradient Boosting xử lý tốt các mối quan hệ phi tuyến tính, Feature Importance giúp giải thích mô hình

####  Về đánh giá mô hình
- Chỉ số RMSE là chưa đủ
- Cần biểu đồ so sánh Thực tế - Dự báo để phát hiện ngay các điểm trễ (lag)
- Kết hợp nhiều metrics: RMSE, MAE, R², MAPE





---

## 3. Định hướng phát triển (Future Work)

###  Tối ưu hóa mô hình hiện tại

| Hướng phát triển | Mô tả | Kỳ vọng cải thiện |
|------------------|-------|-------------------|
| **Bayesian Optimization** | Thay thế Grid Search bằng Optuna để tìm hyperparameter hiệu quả hơn | RMSE giảm 0.05-0.1°C |
| **Ensemble Stacking** | Kết hợp dự báo từ nhiều mô hình: 70% ARIMA + 30% XGBoost cho 1 giờ, 100% XGBoost cho 24 giờ | Tận dụng điểm mạnh từng mô hình |
| **Feature Engineering nâng cao** | Thêm features tương tác (nhiệt độ × độ ẩm), thống kê trượt (MA 7 ngày), mã hóa sự kiện thời tiết | Cải thiện khả năng dự báo cực trị |

###  Áp dụng Deep Learning

| Mô hình | Mục đích | Ưu điểm kỳ vọng |
|---------|----------|-----------------|
| **LSTM/GRU** | Mạng nơ-ron hồi quy cho chuỗi thời gian | Tự học phụ thuộc dài hạn, giảm công sức tạo feature thủ công |
| **Transformer** | So sánh với mô hình attention-based | Xử lý sequential patterns phức tạp |
| **So sánh với SARIMAX** | Benchmark với mô hình thống kê đa biến | Xác định ML có thực sự vượt trội khi thêm các biến exogenous |

###  Nâng cao chất lượng dự báo

| Hướng phát triển | Mô tả |
|------------------|-------|
| **Uncertainty Quantification** | Cung cấp khoảng dự báo thay vì chỉ point prediction. Ví dụ: "30°C ± 1.5°C với độ tin cậy 90%" thông qua Quantile Regression hoặc Conformal Prediction |
| **Model Interpretability** | Sử dụng SHAP để giải thích dự báo ở cấp độ từng mẫu dữ liệu, tăng độ tin cậy cho người dùng cuối |

###  Ứng dụng thực tế

| Hướng phát triển | Mô tả |
|------------------|-------|
| **Real-time Pipeline** | Xây dựng end-to-end pipeline: thu thập dữ liệu tự động → API serving → monitoring → auto-retraining khi hiệu suất suy giảm |
| **Tích hợp dữ liệu ngoài** | Bổ sung dữ liệu chất lượng không khí (AQI), chỉ số UV, ảnh vệ tinh (MODIS/Landsat) |
| **Mở rộng phạm vi** | So sánh UHI của TP.HCM với Hà Nội, Đà Nẵng để hiểu đặc trưng theo vùng miền |

---

## 4. Tổng kết

> **"Data Science không chỉ là chạy code - mà là sự kết hợp giữa kỹ thuật, thống kê và kiến thức chuyên ngành."**

Qua dự án phân tích xu hướng thời tiết và hiệu ứng Đảo Nhiệt Đô Thị tại TP.HCM, nhóm đã học được:

| Khía cạnh | Bài học chính |
|-----------|---------------|
|  **Kỹ thuật** | Xử lý chuỗi thời gian, Feature Engineering, so sánh các thuật toán ML |
|  **Thống kê** | Kiểm định giả thuyết, đánh giá mô hình, tránh data leakage |
|  **Domain** | Hiệu ứng UHI, Sea Breeze, vi khí hậu đô thị, quán tính nhiệt |
|  **Teamwork** | Phân chia công việc, review code, tổng hợp kết quả |

Những kỹ năng này sẽ là nền tảng vững chắc cho các dự án Data Science phức tạp hơn trong tương lai.

---

*Hoàn thành: Tháng 1/2026*
*Môn học: Nhập môn Khoa học Dữ liệu - VNU-HCMUS*