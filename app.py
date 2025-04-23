from flask import Flask, render_template, request, jsonify
import stripe

app = Flask(__name__)

# Cấu hình Stripe API Key
stripe.api_key = "sk_test_...your_stripe_api_key_here..."

# Mẫu dữ liệu trận đấu
matches = [
    {"id": 1, "team1": "Vietnam", "team2": "Thailand", "date": "2025-04-25", "stadium": "My Dinh"},
    {"id": 2, "team1": "Brazil", "team2": "Argentina", "date": "2025-04-26", "stadium": "Maracanã"}
]

@app.route('/')
def index():
    return render_template('index.html', matches=matches)

@app.route('/book_ticket', methods=['POST'])
def book_ticket():
    match_id = request.form['match_id']
    # Logic để xử lý đặt vé
    # Thêm logic thanh toán tại đây (Stripe API)
    return jsonify({"message": "Đặt vé thành công cho trận đấu!"})

@app.route('/payment', methods=['POST'])
def payment():
    token = request.form['stripeToken']
    amount = 5000  # Giá vé (ví dụ: 5000 VND)

    try:
        charge = stripe.Charge.create(
            amount=amount,
            currency='vnd',
            description='Football match ticket',
            source=token
        )
        return jsonify({"message": "Thanh toán thành công!"})
    except stripe.error.StripeError:
        return jsonify({"error": "Đã xảy ra lỗi khi thanh toán!"})

if __name__ == '__main__':
    app.run(debug=True)
