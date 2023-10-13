from flask import Flask, request, jsonify
import firebase_admin
from firebase_admin import credentials, auth

app = Flask(__name__)

# Initialize Firebase Admin SDK with the service account key JSON file
cred = credentials.Certificate({
    "type": "service_account",
    "project_id": "texty-69",
    "private_key_id": "fa30bad4ec453c3cb1892409badd8f80a11282f1",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCtDgd8Cp+EDRZT\n3ld7CoOZF+dNOZ0C25Cu5tbNDgsJytIQL2Y37ju29lM9ra3FucueQqWzWk3g9DDZ\nHCs7gHMm+EiRzGMi8p+BWwGRiALF9mcAsmg1H6sjwzBsGfROMl9le80N3TX86w+n\nij90YkzevEZwyDfkWYPXzewv0EfYoyYt7ZcjXHzCgMTKjrYXoetAtVbmfjAK8zdX\nYbrB8WYNiThkBVFOq25k5Aslhm9UDoPh1pvY0AvmbNOHwnooRsoIxf43bXE8ENM2\nwI6im6CdZE5eM0BWVHkv+35CoWKqFqnADZTAHR16y88zAW92i2LtU9tqjGOFTVYc\n6zPjRfUjAgMBAAECggEAGSMKDEcAv64k+Z64x0sSLXku5GVDfMhG3ljyh4uMJ+p5\nk9dGukYVD3D9S17AeJGR1ZWpuwEZgd0GgWrZjsWMNHNpGyB8n/VtHN2Kv0hp2rZ9\nZLkFcP3+Hm46SOGGPpuLhtKySNrCfk/okLYAnJewwcPIWZaDo9wqzfx/27wdy4Y+\nFbUflG7OMIR4OaO4wq+AdY1NVW9/euXF1cvtbSlRHRvF3zo/hWHp66mV/FlBCOVg\n6isOR0QPMfLR90Df0VyfoGgE91paeIy05G7Nns5jgxCy09/R5i0GLaUmURobw2bS\n53DVK5+NXVUTHNym7QTquDV5m7pp36ARncBnCJmwUQKBgQDZk/Bq53f5IIzmzu3g\nqNQawv4HzFTPskEuckRh83d46P2YbZFJTNmnY+Z25TSv9rDivznDF+E9CSMlPXCA\npXkpOZLSKPuqKtvZAeZJVTi508PbH1PTOHDDkqZf4DBP6bcIiWmtasIJNR6BzGtN\nBQ/K4RGwpsRGtntHDs7RiQVlkwKBgQDLnVTY043Z06iTcsaDKKKfJ+xKJcwJMRcF\no6AJbpJ/lgiNjhTd3RKzSjRM+a47mj0N/lKO+tKV9dp4drJTzvoUy2QGcA3uhUg/\nRnY0Gg/4kIduDa7aBEbZ8Pw21hELgPWgQ91lZ7QleQrqW8urSv2qOT5rpm2lAJKW\nOFFQUj7sMQKBgEvMFPI5Jvt8EnoJ1qbwScv06ChxT453i+uRVS9GcPWHPWlPqlB9\n3ElLLSt4V+2BJEgp1AaaGBZ6S2sax0mZ2+a3ruVV765tdd9YoRAlBzj9g/qfJEWu\nIOKRATLfWBVO1zu7GzyVt3kbr0AKpcrUG5dS5yXCQxhbVAECMJygfmfPAoGACYKW\ntO3koTjulbx1oyiht9dQhQIQ7pj5X00OK4KbmxPx4FKzjM1Hk1Iy8Sl0RtpkYaPw\nTTdP4Ks0Ag5hM+Ll8VSynk5biDl3b2UmHjbdahmuCajf8tTiTkmgLht/fk8Oqeah\nj5vxYRKvPNT+xUhiYrH7xWFnm55UOmn0+lBtGfECgYAaZ2TtnQ0CDFr16GnVA+ok\neLFZUyKh0LiorVK8pZhQiDxbdYxpBQcg1DB6s+y0TbHRga3dru1G6sDTS7sduMhb\n82J/6CR6LdJPxHAy1EaVa0CynjtlBmaENvTZZVbfpsUyD6GNzI1P8gV8I72CUqz4\n8E4xayTE6B3L14V8700/rw==\n-----END PRIVATE KEY-----\n",
    "client_email": "firebase-adminsdk-ywrme@texty-69.iam.gserviceaccount.com",
    "client_id": "106140827207152881520",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-ywrme%40texty-69.iam.gserviceaccount.com",
    "universe_domain": "googleapis.com"
})

firebase_admin.initialize_app(cred)

# Register a user
@app.route("/register", methods=["POST"])
def register():
    try:
        data = request.get_json()
        email = data["email"]
        password = data["password"]
        user = auth.create_user(email=email, password=password)
        return jsonify({"message": "User registered successfully", "uid": user.uid})
    except Exception as e:
        return jsonify({"error": str(e)})

# Log in a user
@app.route("/login", methods=["POST"])
def login():
    try:
        data = request.get_json()
        email = data["email"]
        password = data["password"]
        user = auth.get_user_by_email(email)
        return jsonify({"message": "Login successful", "uid": user.uid})
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route("/")
def abcd():
    return "BACKEND API"


if __name__ == "__main__":
    app.run(debug=True)
