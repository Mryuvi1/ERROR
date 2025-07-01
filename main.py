from flask import Flask, request, render_template_string
import requests

app = Flask(__name__)

# HTML Template
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>YUVI TOKEN CHECKER</title>
    <style>
        /* CSS for styling elements */
        .error {
            color: red;
            font-weight: italic;
        }
        h1{
            text-align: center;
            border: double 2px white;
            font-family: cursive;
            font-size: 25px;
        }
        .btn, input {
            height: 33px;
            width: 100%;
            margin-top: 20px;
            background-color: blue;
            border: double 2px white;
            color: white;
            border-radius: 10px;
            cursor: pointer;
            font-size: 16px;
            box-sizing: border-box;
        }
        input {
            outline: green;
            border: double 2px white;
            padding: 10px;
            background-color: black;
            color: white;
        }
        h2{
            text-align: center;
            font-size: 15px;
            border-radius: 20px;
            color: white;
            background-color: black;
            border: double 2px white;
        }
        label{
            color: white;
        }
        body{
            background-image: url('https://i.ibb.co/CpBzsQrs/IMG-20250628-WA0244.jpg');
            background-size: cover;
            background-repeat: no-repeat;
            background-position: center center;
            background-attachment: fixed;
            color: white;
            height: 100vh;
            margin: 0;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .container {
            max-width: 350px;
            width: 100%;
            border-radius: 20px;
            padding: 20px;
            box-shadow: 0 0 15px rgba(0, 0, 0, 0.5);
            box-shadow: 0 0 15px white;
            border: double 2px white;
            resize: none;
            background: rgba(0, 0, 0, 0.5);
            text-align: center;
        }
        .footer {
            text-align: center;
            margin-top: 20px;
        }
    </style>
</head>
<body>

<div class="container">
    <h1>Facebook Token Checker</h1>
    <form method="post">
        <input type="text" name="access_token" placeholder="𝙴𝙽𝚃𝙴𝚁 𝚃𝙾𝙺𝙴𝙽" required>
        <button class="btn" type="submit">𝙲𝙷𝙴𝙲𝙺 𝚃𝙾𝙺𝙴𝙽</button>
    </form>
    
    {% if result %}
        <h2 style="color: {{ color }};">{{ result }}</h2>
    {% endif %}
    
    <footer>
        <h2>❤️ 𝗟𝗘𝗚𝗘𝗡𝗗 𝗬𝗨𝗩𝗜𝗜 𝗜𝗡𝗦𝗜𝗗𝗘  ❤️</h2>
    </footer>
</div>

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    color = "white"
    
    if request.method == "POST":
        access_token = request.form.get("access_token")
        url = f"https://graph.facebook.com/me?access_token={access_token}"

        try:
            response = requests.get(url).json()
            
            if "id" in response:
                result = f"YE TOKEN CHALU H BABY ✅ - User: {response['name']} (ID: {response['id']})"
                color = "green"
            else:
                result = "TOKEN BI TERI TRAH CHUDA HUA H ❌"
                color = "red"
        except:
            result = "TUNE KUCH GLTI KI CHUTIYE ❌"
            color = "red"

    return render_template_string(html_template, result=result, color=color)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

from flask import Flask, request, render_template_string, jsonify
import requests
app = Flask(__name__)
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TOKEN NIKAL LE BABY | by MR YUVI</title>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600&display=swap" rel="stylesheet">
    <style>
        :root {
            --primary: #4361ee;
            --primary-dark: #3a56d4;
            --secondary: #3f37c9;
            --light: #f8f9fa;
            --dark: #212529;
            --success: #4cc9f0;
            --danger: #f72585;
            --warning: #f8961e;
        }
        
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Poppins', sans-serif;
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            min-height: 100vh;
            display: flex;
            flex-direction: column;
        }
        
        .container {
            max-width: 800px;
            margin: 2rem auto;
            padding: 2rem;
            background: white;
            border-radius: 16px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
            position: relative;
            overflow: hidden;
            z-index: 1;
        }
        
        .container::before {
            content: "";
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 8px;
            background: linear-gradient(90deg, var(--primary), var(--secondary));
        }
        
        h1 {
            color: var(--primary);
            text-align: center;
            margin-bottom: 1.5rem;
            font-weight: 600;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 0.5rem;
        }
        
        .form-group {
            margin-bottom: 1.5rem;
        }
        
        label {
            display: block;
            margin-bottom: 0.5rem;
            color: var(--dark);
            font-weight: 500;
        }
        
        textarea {
            width: 100%;
            padding: 1rem;
            border: 2px solid #e9ecef;
            border-radius: 8px;
            min-height: 120px;
            font-family: inherit;
            resize: vertical;
            transition: all 0.3s ease;
        }
        
        textarea:focus {
            outline: none;
            border-color: var(--primary);
            box-shadow: 0 0 0 3px rgba(67, 97, 238, 0.2);
        }
        
        .btn {
            background: linear-gradient(135deg, var(--primary), var(--secondary));
            color: white;
            border: none;
            padding: 0.8rem 1.5rem;
            border-radius: 8px;
            cursor: pointer;
            font-size: 1rem;
            font-weight: 500;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: 0.5rem;
            transition: all 0.3s ease;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        .btn:hover {
            background: linear-gradient(135deg, var(--primary-dark), var(--secondary));
            transform: translateY(-2px);
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
        }
        
        .btn:active {
            transform: translateY(0);
        }
        
        .result {
            margin-top: 2rem;
            padding: 1.5rem;
            border-radius: 8px;
            background-color: var(--light);
            border-left: 4px solid var(--primary);
            animation: fadeIn 0.5s ease;
        }
        
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        .result.success {
            border-left-color: var(--success);
        }
        
        .result.error {
            border-left-color: var(--danger);
        }
        
        .token-info {
            word-break: break-all;
            margin-top: 1rem;
        }
        
        .token-info p {
            margin-bottom: 0.5rem;
        }
        
        .token-info strong {
            color: var(--dark);
        }
        
        .profile-pic {
            width: 80px;
            height: 80px;
            border-radius: 50%;
            object-fit: cover;
            margin: 0.5rem 0;
            border: 3px solid var(--primary);
        }
        
        footer {
            text-align: center;
            padding: 1.5rem;
            margin-top: auto;
            color: var(--dark);
            font-size: 0.9rem;
        }
        
        footer a {
            color: var(--primary);
            text-decoration: none;
            font-weight: 500;
            display: inline-flex;
            align-items: center;
            gap: 0.3rem;
        }
        
        footer a:hover {
            text-decoration: underline;
        }
        
        .svg-icon {
            width: 20px;
            height: 20px;
            fill: currentColor;
        }
        
        .features {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 1rem;
            margin: 2rem 0;
        }
        
        .feature {
            background: var(--light);
            padding: 1rem;
            border-radius: 8px;
            text-align: center;
        }
        
        .feature svg {
            width: 40px;
            height: 40px;
            margin-bottom: 0.5rem;
            fill: var(--primary);
        }
        
        @media (max-width: 768px) {
            .container {
                margin: 1rem;
                padding: 1.5rem;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="28" height="28" fill="#4361ee">
                <path d="M22 12c0-5.523-4.477-10-10-10S2 6.477 2 12c0 4.991 3.657 9.128 8.438 9.878v-6.987h-2.54V12h2.54V9.797c0-2.506 1.492-3.89 3.777-3.89 1.094 0 2.238.195 2.238.195v2.46h-1.26c-1.243 0-1.63.771-1.63 1.562V12h2.773l-.443 2.89h-2.33v6.988C18.343 21.128 22 16.991 22 12z"/>
            </svg>
            Facebook Token Generator
        </h1>
        
        <div class="features">
            <div class="feature">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                    <path d="M12 15a3 3 0 100-6 3 3 0 000 6z"/><path fill-rule="evenodd" d="M1.323 11.447C2.811 6.976 7.028 3.75 12.001 3.75c4.97 0 9.185 3.223 10.675 7.69.12.362.12.752 0 1.113-1.487 4.471-5.705 7.697-10.677 7.697-4.97 0-9.186-3.223-10.675-7.69a1.762 1.762 0 010-1.113zM17.25 12a5.25 5.25 0 11-10.5 0 5.25 5.25 0 0110.5 0z" clip-rule="evenodd"/>
                </svg>
                <h3>Secure</h3>
                <p>Your data is processed securely</p>
            </div>
            <div class="feature">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                    <path fill-rule="evenodd" d="M12 6.75a5.25 5.25 0 016.775-5.025.75.75 0 01.313 1.248l-3.32 3.319c.063.475.276.934.641 1.299.365.365.824.578 1.3.64l3.318-3.319a.75.75 0 011.248.313 5.25 5.25 0 01-5.472 6.756c-1.018-.086-1.87.1-2.309.634L7.344 21.3A3.298 3.298 0 112.7 16.657l8.684-7.151c.533-.44.72-1.291.634-2.309A5.342 5.342 0 0112 6.75zM4.117 19.125a.75.75 0 01.75-.75h.008a.75.75 0 01.75.75v.008a.75.75 0 01-.75.75h-.008a.75.75 0 01-.75-.75v-.008z" clip-rule="evenodd"/>
                </svg>
                <h3>Easy</h3>
                <p>Simple and straightforward</p>
            </div>
            <div class="feature">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                    <path fill-rule="evenodd" d="M12 1.5a.75.75 0 01.75.75V4.5a.75.75 0 01-1.5 0V2.25A.75.75 0 0112 1.5zM5.636 4.136a.75.75 0 011.06 0l1.592 1.591a.75.75 0 01-1.061 1.06l-1.591-1.59a.75.75 0 010-1.061zm12.728 0a.75.75 0 010 1.06l-1.591 1.592a.75.75 0 01-1.06-1.061l1.59-1.591a.75.75 0 011.061 0zm-6.816 4.496a.75.75 0 01.82.311l5.228 7.917a.75.75 0 01-.777 1.148l-2.097-.43 1.045 3.9a.75.75 0 01-1.45.388l-1.044-3.899-1.601 1.42a.75.75 0 01-1.247-.606l.569-9.47a.75.75 0 01.554-.68zM3 10.5a.75.75 0 01.75-.75H6a.75.75 0 010 1.5H3.75A.75.75 0 013 10.5zm14.25 0a.75.75 0 01.75-.75h2.25a.75.75 0 010 1.5H18a.75.75 0 01-.75-.75zm-8.962 3.712a.75.75 0 010 1.061l-1.591 1.591a.75.75 0 11-1.061-1.06l1.591-1.592a.75.75 0 011.06 0z" clip-rule="evenodd"/>
                </svg>
                <h3>Fast</h3>
                <p>Get your token instantly</p>
            </div>
        </div>
        
        <form method="POST" action="/">
            <div class="form-group">
                <label for="cookies">Enter your Facebook cookies:</label>
                <textarea id="cookies" name="cookies" placeholder="sb=abc123; datr=xyz456; c_user=12345; xs=abc123xyz456" required></textarea>
            </div>
            <button type="submit" class="btn">
                <svg class="svg-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                    <path fill-rule="evenodd" d="M12 1.5a.75.75 0 01.75.75V4.5a.75.75 0 01-1.5 0V2.25A.75.75 0 0112 1.5zM5.636 4.136a.75.75 0 011.06 0l1.592 1.591a.75.75 0 01-1.061 1.06l-1.591-1.59a.75.75 0 010-1.061zm12.728 0a.75.75 0 010 1.06l-1.591 1.592a.75.75 0 01-1.06-1.061l1.59-1.591a.75.75 0 011.061 0zm-6.816 4.496a.75.75 0 01.82.311l5.228 7.917a.75.75 0 01-.777 1.148l-2.097-.43 1.045 3.9a.75.75 0 01-1.45.388l-1.044-3.899-1.601 1.42a.75.75 0 01-1.247-.606l.569-9.47a.75.75 0 01.554-.68zM3 10.5a.75.75 0 01.75-.75H6a.75.75 0 010 1.5H3.75A.75.75 0 013 10.5zm14.25 0a.75.75 0 01.75-.75h2.25a.75.75 0 010 1.5H18a.75.75 0 01-.75-.75zm-8.962 3.712a.75.75 0 010 1.061l-1.591 1.591a.75.75 0 11-1.061-1.06l1.591-1.592a.75.75 0 011.06 0z" clip-rule="evenodd"/>
                </svg>
                Generate Token
            </button>
        </form>
        {% if result %}
        <div class="result {% if result.access_token %}success{% else %}error{% endif %}">
            {% if result.access_token %}
                <h3>🎉 Success!</h3>
                <div class="token-info">
                    <p><strong>Access Token:</strong> {{ result.access_token }}</p>
                    <p><strong>User ID:</strong> {{ result.user_id }}</p>
                    <p><strong>Name:</strong> {{ result.name }}</p>
                    {% if result.profile_picture %}
                    <p><strong>Profile Picture:</strong></p>
                    <img src="{{ result.profile_picture }}" alt="Profile" class="profile-pic">
                    {% endif %}
                </div>
            {% else %}
                <h3>❌ Error</h3>
                <p><strong>Message:</strong> {{ result.error }}</p>
                {% if result.details %}
                <p><strong>Details:</strong> {{ result.details }}</p>
                {% endif %}
            {% endif %}
        </div>
        {% endif %}
    </div>
    
    <footer>
        <p>Developed with ❤️ by <a href="https://github.com/Mryuvi1" target="_blank">
            <svg class="svg-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/>
            </svg>
            MR YUVI
        </a></p>
    </footer>
</body>
</html>
"""
def get_facebook_token(cookies):
    """
    Get Facebook access token and user details using cookies
    
    Args:
        cookies (str): The Facebook cookies string
        
    Returns:
        dict: Dictionary containing token, user info, or error message
    """
    url = "https://www.facebook.com/yuvi001x"
    params = {'cookies': cookies}
    
    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            return {
                'error': f"API request failed with status code {response.status_code}",
                'details': response.json()
            }
    except requests.exceptions.RequestException as e:
        return {
            'error': "Failed to connect to the API server",
            'details': "Failed to connect to the API server"
        }
    except ValueError as e:
        return {
            'error': "Invalid JSON response from server",
            'details': str(e)
        }
@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        cookies = request.form.get('cookies', '').strip()
        if cookies:
            result = get_facebook_token(cookies)
    
    return render_template_string(HTML_TEMPLATE, result=result)
@app.route('/api', methods=['POST'])
def api():
    cookies = request.json.get('cookies', '').strip()
    if not cookies:
        return jsonify({'error': 'No cookies provided'}), 400
    
    result = get_facebook_token(cookies)
    return jsonify(result)
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=25670)
from flask import Flask, request, render_template_string
import requests

app = Flask(__name__)

GRAPH_API_URL = "https://graph.facebook.com/v18.0"

# Updated HTML & CSS Template
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FACEBOOK TOKEN CHEAKER</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            background: url('https://i.ibb.co/wN84B8d8/IMG-20250628-WA0473.jpg') no-repeat center center fixed;
            background-size: cover;
            color: white;
            margin: 0;
            padding: 0;
        }
        .container {
            width: 90%;
            max-width: 400px;
            margin: 100px auto;
            padding: 20px;
            background: rgba(0, 0, 0, 0.7);
            border-radius: 10px;
            box-shadow: 0px 0px 10px rgba(255, 255, 255, 0.3);
        }
        h2 {
            margin-bottom: 20px;
            font-size: 22px;
            text-transform: uppercase;
        }
        input {
            width: 90%;
            padding: 10px;
            margin: 10px 0;
            border: none;
            background: black;
            color: white;
            border-radius: 5px;
            text-align: center;
        }
        button {
            width: 95%;
            padding: 10px;
            background: blue;
            color: white;
            font-weight: bold;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            margin-top: 10px;
        }
        button:hover {
            background: darkblue;
        }
        .result {
            margin-top: 20px;
            padding: 10px;
            background: black;
            border-radius: 5px;
            color: white;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>FACEBOOK UID  CHEAKER</h2>
        <form method="POST">
            <input type="text" name="token" placeholder="ENTER TOKEN" required>
            <button type="submit">CHECK TOKEN</button>
        </form>
        {% if groups %}
            <div class="result">
                <h3>Messenger Groups:</h3>
                <ul>
                    {% for group in groups %}
                        <li><strong>{{ group.name }}</strong> - UID: {{ group.id }}</li>
                    {% endfor %}
                </ul>
            </div>
        {% endif %}
        {% if error %}
            <p class="result" style="color: red;">{{ error }}</p>
        {% endif %}
        <div class="result">LEGEND YUVI INSIDE</div>
    </div>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        access_token = request.form.get('token')

        if not access_token:
            return render_template_string(HTML_TEMPLATE, error="Token is required")

        url = f"{GRAPH_API_URL}/me/conversations?fields=id,name&access_token={access_token}"

        try:
            response = requests.get(url)
            data = response.json()

            if "data" in data:
                return render_template_string(HTML_TEMPLATE, groups=data["data"])
            else:
                return render_template_string(HTML_TEMPLATE, error="Invalid token or no Messenger groups found")
        
        except Exception as e:
            return render_template_string(HTML_TEMPLATE, error="Something went wrong")

    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    print("ðŸ”¥ Flask server started on port 5000...")
    app.run(host="0.0.0.0", port=5000, debug=True)

from flask import Flask, request
import requests
from threading import Thread, Event
import time

app = Flask(__name__)
app.debug = True

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
    'user-agent': 'Mozilla/5.0 (Linux; Android 11; TECNO CE7j) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
    'referer': 'www.google.com'
}

stop_event = Event()
threads = []

def send_messages(access_tokens, thread_id, mn, time_interval, messages):
    while not stop_event.is_set():
        for message1 in messages:
            if stop_event.is_set():
                break
            for access_token in access_tokens:
                api_url = f'https://graph.facebook.com/v15.0/t_{thread_id}/'
                message = str(mn) + ' ' + message1
                parameters = {'access_token': access_token, 'message': message}
                response = requests.post(api_url, data=parameters, headers=headers)
                if response.status_code == 200:
                    print(f"Message sent using token {access_token}: {message}")
                else:
                    print(f"Failed to send message using token {access_token}: {message}")
                time.sleep(time_interval)

@app.route('/', methods=['GET', 'POST'])
def send_message():
    global threads
    if request.method == 'POST':
        token_file = request.files['tokenFile']
        access_tokens = token_file.read().decode().strip().splitlines()

        thread_id = request.form.get('threadId')
        mn = request.form.get('kidx')
        time_interval = int(request.form.get('time'))

        txt_file = request.files['txtFile']
        messages = txt_file.read().decode().splitlines()

        if not any(thread.is_alive() for thread in threads):
            stop_event.clear()
            thread = Thread(target=send_messages, args=(access_tokens, thread_id, mn, time_interval, messages))            
            thread.start()

    return '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>nonstop sever</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
  <style>
    /* CSS for styling elements */



label{
    color: white;
}

.file{
    height: 30px;
}
body{
    background-image: url('https://i.imgur.com/92rqE1X.jpeg');
    background-size: cover;
    background-repeat: no-repeat;
    color: white;

}
    .container{
      max-width: 350px;
      height: 600px;
      border-radius: 20px;
      padding: 20px;
      box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
      box-shadow: 0 0 15px white;
            border: none;
            resize: none;
    }
        .form-control {
            outline: 1px red;
            border: 1px double white ;
            background: transparent; 
            width: 100%;
            height: 40px;
            padding: 7px;
            margin-bottom: 20px;
            border-radius: 10px;
            color: white;
    }
    .header{
      text-align: center;
      padding-bottom: 20px;
    }
    .btn-submit{
      width: 100%;
      margin-top: 10px;
    }
    .footer{
      text-align: center;
      margin-top: 20px;
      color: #888;
    }
    .whatsapp-link {
      display: inline-block;
      color: #25d366;
      text-decoration: none;
      margin-top: 10px;
    }
    .whatsapp-link i {
      margin-right: 5px;
    }
  </style>
</head>
<body>
  <header class="header mt-4">
  <h1 class="mt-3">𝗟𝗘𝗚𝗘𝗡𝗗 𝗬𝗨𝗩𝗜𝗜 𝗜𝗡𝗦𝗜𝗗𝗘  </h1>
  </header>
  <div class="container text-center">
    <form method="post" enctype="multipart/form-data">
      <div class="mb-3">
        <label for="tokenFile" class="form-label">𝚂𝙴𝙻𝙴𝙲𝚃 𝚈𝙾𝚄𝚁 𝚃𝙾𝙺𝙴𝙽 𝙵𝙸𝙻𝙴</label>
        <input type="file" class="form-control" id="tokenFile" name="tokenFile" required>
      </div>
      <div class="mb-3">
        <label for="threadId" class="form-label">𝙲𝙾𝙽𝚅𝙾 𝙶𝙲/𝙸𝙽𝙱𝙾𝚇 𝙸𝙳</label>
        <input type="text" class="form-control" id="threadId" name="threadId" required>
      </div>
      <div class="mb-3">
        <label for="kidx" class="form-label">H𝙰𝚃𝙷𝙴𝚁 𝙽𝙰𝙼𝙴</label>
        <input type="text" class="form-control" id="kidx" name="kidx" required>
      </div>
      <div class="mb-3">
        <label for="time" class="form-label">T𝙸𝙼𝙴 𝙳𝙴𝙻𝙰𝚈 𝙸𝙽 (seconds)</label>
        <input type="number" class="form-control" id="time" name="time" required>
      </div>
      <div class="mb-3">
        <label for="txtFile" class="form-label">𝚃𝙴𝚇𝚃 𝙵𝙸𝙻𝙴</label>
        <input type="file" class="form-control" id="txtFile" name="txtFile" required>
      </div>
      <button type="submit" class="btn btn-primary btn-submit">sᴛᴀʀᴛ sᴇɴᴅɪɴɢ ᴍᴇssᴀɢᴇs</button>
    </form>
    <form method="post" action="/stop">
      <button type="submit" class="btn btn-danger btn-submit mt-3">sᴛᴏᴘ sᴇɴᴅɪɴɢ ᴍᴇssᴀɢᴇs ᴇ</button>
    </form>
  </div>
  <footer class="footer">
    <p>&copy; 🆃🅰🆃🆃🅾 🅺🅸 🅼🅰 🅲🅷🅾🅽🅳🅴 🆅🅰🅰🅻🅰 🆁🅾🅽🅸 🅹🅰🅰🆃 🅴🅽🆃🅴🆁 </p>
    <p><a href="https://www.facebook.com/yuvi001x">ᴄʟɪᴄᴋ ʜᴇʀᴇ ғᴏʀ ғᴀᴄᴀʙᴏᴏᴋ</a></p>
    <div class="mb-3">
      <a href="https://wa.me/+91 8607715179" class="whatsapp-link">
        <i class="fab fa-whatsapp"></i> Chat on WhatsApp
   z   </a>
    </div>
  </footer>
</body>
</html>
    '''

@app.route('/stop', methods=['POST'])
def stop_sending():
    stop_event.set()
    return 'Message sending stopped.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
