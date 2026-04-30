# Configuration and constants for the Scientific Calculator

# Calculator Configuration
CALC_CONFIG = {
    'DECIMAL_PLACES': 10,      # Maximum decimal places in results
    'MAX_HISTORY': 10,          # Maximum history items to display
    'ANGLE_MODE': 'degrees',    # 'degrees' or 'radians'
    'PRECISION': 1e-10,         # Tolerance for floating point comparisons
}

# UI Configuration
UI_CONFIG = {
    'PAGE_TITLE': 'Scientific Calculator',
    'PAGE_ICON': '🧮',
    'LAYOUT': 'wide',
    'INITIAL_SIDEBAR_STATE': 'expanded',
    'DISPLAY_FONT_SIZE': 28,
    'COLUMN_RATIO': [2, 1],     # Main content vs. History sidebar ratio
}

# Button Layouts
BUTTON_LAYOUTS = {
    'number_rows': [
        ['7', '8', '9', '÷'],
        ['4', '5', '6', '×'],
        ['1', '2', '3', '−'],
        ['0', '.', '=', '^'],
    ],
    'scientific': [
        ['sin', 'cos', 'tan', '√'],
        ['log', 'ln', 'x²', '1/x'],
    ],
    'top_row': ['C', '←', 'π', 'del'],
}

# Operation Symbols
OPERATIONS = {
    '+': 'add',
    '−': 'subtract',
    '*': 'multiply',
    '×': 'multiply',
    '/': 'divide',
    '÷': 'divide',
    '^': 'power',
    '%': 'modulo',
}

# CSS Styles
CUSTOM_CSS = """
    <style>
        .calculator-container {
            max-width: 500px;
            margin: 0 auto;
        }
        
        .result-display {
            background-color: #f0f2f6;
            padding: 20px;
            border-radius: 10px;
            text-align: right;
            font-size: 28px;
            font-weight: bold;
            margin-bottom: 20px;
            border: 2px solid #ddd;
            word-wrap: break-word;
            overflow: hidden;
            min-height: 60px;
            display: flex;
            align-items: center;
            justify-content: flex-end;
        }
        
        .history-item {
            background-color: #f9f9f9;
            padding: 10px;
            border-radius: 5px;
            margin-bottom: 8px;
            border-left: 4px solid #0066cc;
            font-size: 12px;
        }
        
        .history-timestamp {
            color: #666;
            font-size: 10px;
            margin-bottom: 4px;
        }
        
        .history-expression {
            color: #333;
            font-weight: 500;
        }
        
        .operation-indicator {
            font-size: 12px;
            color: #0066cc;
            font-weight: bold;
            margin-bottom: 5px;
            height: 16px;
        }
        
        .error-message {
            color: #d32f2f;
            font-size: 14px;
            padding: 10px;
            border-radius: 4px;
            background-color: #ffebee;
        }
    </style>
"""

# Error Messages
ERROR_MESSAGES = {
    'divide_by_zero': '⚠️ Cannot divide by zero!',
    'sqrt_negative': '⚠️ Cannot take square root of negative number!',
    'log_invalid': '⚠️ Logarithm undefined for non-positive numbers!',
    'ln_invalid': '⚠️ Natural logarithm undefined for non-positive numbers!',
    'invalid_input': '⚠️ Invalid input!',
    'invalid_operation': '⚠️ Invalid operation!',
    'overflow': '⚠️ Number too large!',
}
