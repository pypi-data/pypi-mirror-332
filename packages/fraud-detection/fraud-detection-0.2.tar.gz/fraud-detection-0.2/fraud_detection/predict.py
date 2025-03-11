import pandas as pd
import joblib

# Load mô hình và danh sách feature đã huấn luyện
model, feature_names = joblib.load("fraud_model.pkl")

def predict_fraud(df):
    """
    Hàm dự đoán gian lận hay không cho tất cả các giao dịch trong DataFrame.
    
    - df: DataFrame chứa tất cả các giao dịch cần dự đoán
    - Trả về: DataFrame với kết quả dự đoán (Hợp lệ/Gian lận) cho mỗi giao dịch
    """
    
    # Chuyển cột "Ngày giao dịch" thành timestamp (giây kể từ 01/01/1970)
    df["Ngày giao dịch"] = pd.to_datetime(df["Ngày giao dịch"]).astype(int) / 10**9  # Chuyển thành giây

    # Xóa cột "Mã khách hàng" nếu có
    df = df.drop(columns=["Mã khách hàng"], errors="ignore")

    # One-Hot Encoding cho các cột danh mục (giống lúc huấn luyện)
    df = pd.get_dummies(df, columns=["Loại giao dịch", "Địa điểm"])

    # Đồng bộ hóa feature: Nếu thiếu cột nào, điền giá trị 0
    df = df.reindex(columns=feature_names, fill_value=0)

    # Dự đoán cho tất cả các giao dịch trong DataFrame
    df["Dự đoán"] = model.predict(df)

    # Chuyển đổi giá trị dự đoán thành "Gian lận" hoặc "Hợp lệ"
    df["Dự đoán"] = df["Dự đoán"].apply(lambda x: "Gian lận" if x == 0 else "Hợp lệ")
    
    return df

if __name__ == "__main__":
    # Ví dụ: Đọc file dữ liệu
    df = pd.read_csv("dataset.csv")  # Đọc file dữ liệu chứa các giao dịch

    # Dự đoán cho tất cả các giao dịch trong file
    result = predict_fraud(df)

    # In kết quả hoặc lưu lại vào file mới
    print(result)
    result.to_csv("result_predictions.csv", index=False)  # Lưu kết quả vào file CSV mới
