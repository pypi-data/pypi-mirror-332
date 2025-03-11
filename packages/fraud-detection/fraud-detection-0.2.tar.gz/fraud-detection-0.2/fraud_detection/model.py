import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

def train_fraud_model():
    # Đọc dữ liệu
    df = pd.read_csv("dataset.csv")

    # Kiểm tra và đổi tên cột nhãn nếu cần
    if "Hợp lệ" in df.columns and "Gian lận" not in df.columns:
        df.rename(columns={"Hợp lệ": "Gian lận"}, inplace=True)

    # Xóa cột không cần thiết (như "Mã khách hàng")
    df = df.drop(columns=["Mã khách hàng"], errors="ignore")

    # Chuyển cột "Ngày giao dịch" thành timestamp (giây kể từ 01/01/1970)
    df["Ngày giao dịch"] = pd.to_datetime(df["Ngày giao dịch"]).astype(int) / 10**9  # Chuyển thành giây

    # Xử lý dữ liệu: One-Hot Encoding
    df = pd.get_dummies(df, columns=["Loại giao dịch", "Địa điểm"])

    # Tách feature & label
    X = df.drop(columns=["Gian lận"])
    y = df["Gian lận"]

    # Huấn luyện mô hình
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)

    # Lưu mô hình và danh sách feature
    joblib.dump((model, X.columns.tolist()), "fraud_model.pkl")

    print("✅ Mô hình đã huấn luyện và lưu thành công!")

if __name__ == "__main__":
    train_fraud_model()
