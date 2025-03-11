import pandas as pd
from sklearn.model_selection import train_test_split

def load_and_preprocess_data(file_path="dataset.csv"):
    """Đọc dữ liệu, xử lý NaN và chuẩn bị tập train/test"""
    df = pd.read_csv(file_path)

    # Chuyển đổi cột "Ngày giao dịch" thành số ngày tính từ mốc đầu tiên
    df["Ngày giao dịch"] = pd.to_datetime(df["Ngày giao dịch"])
    df["Ngày giao dịch"] = (df["Ngày giao dịch"] - df["Ngày giao dịch"].min()).dt.days

    # Chuyển đổi cột danh mục (Loại giao dịch, Địa điểm) sang dạng số
    df = pd.get_dummies(df, columns=["Loại giao dịch", "Địa điểm"], drop_first=True)

    # Chia tập dữ liệu
    X = df.drop(columns=["ID", "Mã khách hàng", "Hợp lệ"])
    y = df["Hợp lệ"]

    return train_test_split(X, y, test_size=0.2, random_state=42)

