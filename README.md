# Scientific Calculator

A modern, web-based scientific calculator built with Streamlit. Perform basic arithmetic, advanced scientific calculations, and keep a history of your calculations.

## Features

✨ **Core Features:**
- Basic arithmetic operations (+, -, *, /)
- Advanced operations (power, modulo, reciprocal)
- Scientific functions (sin, cos, tan, sqrt, log, ln)
- Calculation history with timestamps
- Clean, responsive UI

🔢 **Number Handling:**
- Decimal point support with validation
- Automatic decimal precision (10 places)
- Leading zero handling
- Result formatting (removes trailing zeros)

🎯 **User Experience:**
- Pending operation indicator
- Real-time display updates
- Error handling with user-friendly messages
- One-click history clearing
- Keyboard-friendly button layout

## Installation

1. Clone the repository:
```bash
git clone https://github.com/mdaipayan/Simple-Calculator.git
cd Simple-Calculator
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the app:
```bash
streamlit run app.py
```

## Project Structure

```
├── app.py              # Main application file
├── calculator.py       # Core calculator logic
├── config.py          # Configuration and constants
├── ui_builder.py      # UI component builders
├── requirements.txt   # Python dependencies
├── LICENSE            # MIT License
└── README.md          # This file
```

## Architecture Improvements

This refactored version includes:

- **Modular Design**: Business logic separated from UI
- **Reduced Duplication**: Reusable button grid and component builders
- **Better Error Handling**: User-friendly error messages for domain errors
- **Configuration Management**: Centralized settings
- **Improved State Management**: Using `setdefault()` for cleaner initialization
- **Enhanced Validation**: Decimal and input validation
- **Operation Indicator**: Visual feedback for pending operations

## Usage Examples

### Basic Arithmetic
1. Click "5" + "3" + "=" → Result: 8
2. Click "10" ÷ "2" + "=" → Result: 5

### Scientific Functions
1. Click "30" then "sin" → Result: 0.5
2. Click "16" then "√" → Result: 4

### Using History
- All calculations are logged with timestamps
- View up to the last 10 calculations
- Click "Clear History" to reset

## Configuration

Edit `config.py` to customize:

```python
# Display precision
CALC_CONFIG['DECIMAL_PLACES'] = 10

# Maximum history items shown
CALC_CONFIG['MAX_HISTORY'] = 10

# UI layout and appearance
UI_CONFIG['LAYOUT'] = 'wide'
```

## Error Handling

The calculator handles:
- Division by zero
- Negative square roots
- Logarithms of non-positive numbers
- Invalid input formats
- Overflow conditions

## Requirements

- Python 3.7+
- Streamlit 1.0+

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Future Enhancements

- [ ] Keyboard input support
- [ ] Memory operations (M+, M-, MR, MC)
- [ ] Operator chaining
- [ ] Dark mode theme toggle
- [ ] Export calculation history
- [ ] Graphing capabilities
