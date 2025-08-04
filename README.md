# Fundraising Bot

A Flask-based web application for managing fundraising campaigns with raffle ticket functionality.

## Features

- Donation management with minimum and maximum limits
- Raffle ticket system (1 ticket per $100 donated)
- Progress tracking with milestone notifications
- Prize management and winner selection
- Responsive user interface with error handling

## Requirements

- Python 3.x
- Flask
- Additional dependencies listed in `requirements.txt`

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd Fundraising-Bot
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app.py
```

The application will be available at `http://127.0.0.1:5000`

## Testing

Run the unit tests using:
```bash
python -m unittest test_fundraising_bot.py
```

## Features

### Donation System
- Input validation for donation amounts
- Minimum and maximum donation limits
- Real-time progress tracking
- Success/error message display

### Raffle System
- Automatic ticket assignment based on donation amount
- One ticket per $100 donated (rounded up)
- Prize management
- Random winner selection

### User Interface
- Responsive design
- Clear progress indicators
- Milestone notifications
- Raffle ticket display

## Development

- Written in Python using Flask framework
- Unit tested with Python's unittest module
- Styled with CSS for better user experience
- Error handling for invalid inputs
- Git version control

## License

See the LICENSE file for details.
