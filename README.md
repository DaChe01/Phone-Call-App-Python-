# 📞 Twilio Phone Call App (Python)

Easily make automated voice calls using Twilio's Voice API in a Python project. Perfect for learning APIs, automation, and real-time communication. 🚀

---

## 📁 Project Structure

```
phone_call/
├── images/               📸 Optional images or assets
├── .env                  🔐 Secret credentials (excluded from Git)
├── .gitignore            📄 Git ignore rules
├── call.py               🐍 Main Python script
├── requirements.txt      📦 Python dependencies
└── README.md             📘 Project documentation
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/DaChe01/Phone-Call-App-Python-.git
cd phone_call
```

### 2️⃣ (Optional) Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Set Up Environment Variables
Create a `.env` file in the root directory:
```env
TWILIO_ACCOUNT_SID=your_account_sid
TWILIO_AUTH_TOKEN=your_auth_token
TWILIO_PHONE_NUMBER=your_twilio_number
```

### 5️⃣ Run the App
```bash
python call.py
```
Enter the recipient's phone number when prompted (include country code, e.g., `+91XXXXXXXXXX`).

---

## 🔐 Notes
- If you're using a **Twilio trial account**, you can only call verified phone numbers.
- All credentials are securely loaded from `.env` using `python-dotenv`.

---

## 💡 Features
- 📞 Make automated calls with Twilio
- 🔐 Secure environment variable usage
- 📦 Lightweight and easy to set up
- 👤 User input for flexible calling

---

## 📃 License
This project is licensed under the **MIT License**.

---

Made with ❤️ using [Twilio](https://www.twilio.com/) and Python 🐍

