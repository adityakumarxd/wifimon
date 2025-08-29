# WiFi Monitoring Project

This project is a Flask-based web application designed for monitoring network devices and capturing traffic data. It provides a user-friendly interface to view connected devices, analyze traffic logs, and manage network activity in real-time.

## Project Structure

```
wifimon/
├── app/
│   ├── static/                # CSS, JS, images for UI
│   ├── templates/             # HTML Flask templates
│   │   ├── base.html          # Base template
│   │   ├── login.html         # Login page
│   │   ├── dashboard.html     # Main dashboard showing devices
│   │   └── device_detail.html # Device-specific traffic logs
│   ├── __init__.py            # Initialize Flask app
│   ├── routes.py              # Flask routes and views
│   ├── auth.py                # Login & authentication logic
│   ├── network_scan.py        # Functions to scan network devices
│   ├── traffic_sniffer.py     # Sniffer to capture and parse traffic
│   ├── utils.py               # Helper functions
│   └── socketio_server.py     # For real-time communication (with Flask-SocketIO)
├── config.py                  # Configuration (router creds, flask secret key)
├── requirements.txt           # Python dependencies
├── run.py                     # Entry point to run Flask app
└── README.md                  # Project overview and setup instructions
```

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/adityakumarxd/wifimon.git
   cd wifimon
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Configure your router credentials and Flask secret key in `config.py`.

## Usage

To run the application, execute the following command:
```
python run.py
```

Visit `http://localhost:5000` in your web browser to access the application.

## Features

- User authentication for secure access.
- Real-time monitoring of network devices.
- Detailed traffic logs for each device.
- Intuitive dashboard for easy navigation.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.