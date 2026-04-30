import streamlit as st
import math
from datetime import datetime

# Set page config
st.set_page_config(
    page_title="Scientific Calculator",
    page_icon="🧮",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better UI
st.markdown("""
    <style>
        .calculator-container {
            max-width: 500px;
            margin: 0 auto;
        }
        .button-row {
            display: flex;
            gap: 10px;
            margin-bottom: 10px;
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
        }
        .history-item {
            background-color: #f9f9f9;
            padding: 10px;
            border-radius: 5px;
            margin-bottom: 8px;
            border-left: 4px solid #0066cc;
        }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if 'display' not in st.session_state:
    st.session_state.display = '0'
if 'history' not in st.session_state:
    st.session_state.history = []
if 'previous_value' not in st.session_state:
    st.session_state.previous_value = None
if 'operation' not in st.session_state:
    st.session_state.operation = None

# Title
st.title("🧮 Scientific Calculator")
st.markdown("---")

# Create two columns: calculator on left, history on right
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Calculator")
    
    # Display current value
    st.markdown(f"""
        <div class="result-display">
            {st.session_state.display}
        </div>
    """, unsafe_allow_html=True)
    
    # Helper functions
    def add_to_display(value):
        if st.session_state.display == '0':
            st.session_state.display = str(value)
        else:
            st.session_state.display += str(value)
    
    def clear_display():
        st.session_state.display = '0'
        st.session_state.previous_value = None
        st.session_state.operation = None
    
    def perform_operation(op):
        try:
            current = float(st.session_state.display)
            st.session_state.previous_value = current
            st.session_state.operation = op
            st.session_state.display = '0'
        except ValueError:
            st.error("Invalid input")
    
    def calculate_result():
        try:
            current = float(st.session_state.display)
            if st.session_state.previous_value is not None and st.session_state.operation:
                prev = st.session_state.previous_value
                op = st.session_state.operation
                
                if op == '+':
                    result = prev + current
                elif op == '-':
                    result = prev - current
                elif op == '*':
                    result = prev * current
                elif op == '/':
                    if current == 0:
                        st.error("Cannot divide by zero!")
                        return
                    result = prev / current
                elif op == '^':
                    result = prev ** current
                elif op == '%':
                    result = prev % current
                
                # Add to history
                expression = f"{prev} {op} {current} = {result}"
                st.session_state.history.append({
                    'expression': expression,
                    'timestamp': datetime.now().strftime("%H:%M:%S")
                })
                
                st.session_state.display = str(result)
                st.session_state.previous_value = None
                st.session_state.operation = None
        except Exception as e:
            st.error(f"Error: {str(e)}")
    
    def apply_scientific_function(func_name):
        try:
            value = float(st.session_state.display)
            
            if func_name == 'sin':
                result = math.sin(math.radians(value))
            elif func_name == 'cos':
                result = math.cos(math.radians(value))
            elif func_name == 'tan':
                result = math.tan(math.radians(value))
            elif func_name == 'sqrt':
                result = math.sqrt(value)
            elif func_name == 'log':
                result = math.log10(value)
            elif func_name == 'ln':
                result = math.log(value)
            elif func_name == 'abs':
                result = abs(value)
            elif func_name == '1/x':
                result = 1 / value if value != 0 else float('inf')
            elif func_name == 'x²':
                result = value ** 2
            elif func_name == 'x³':
                result = value ** 3
            elif func_name == 'π':
                if st.session_state.display == '0':
                    st.session_state.display = str(math.pi)
                else:
                    st.session_state.display += str(math.pi)
                return
            
            expression = f"{func_name}({value}) = {result}"
            st.session_state.history.append({
                'expression': expression,
                'timestamp': datetime.now().strftime("%H:%M:%S")
            })
            
            st.session_state.display = str(result)
        except Exception as e:
            st.error(f"Error: {str(e)}")
    
    # Button layout
    col_c1, col_c2, col_c3, col_c4 = st.columns(4)
    
    with col_c1:
        if st.button("C", use_container_width=True, key="clear"):
            clear_display()
            st.rerun()
    
    with col_c2:
        if st.button("←", use_container_width=True, key="backspace"):
            if len(st.session_state.display) > 1:
                st.session_state.display = st.session_state.display[:-1]
            else:
                st.session_state.display = '0'
            st.rerun()
    
    with col_c3:
        if st.button("π", use_container_width=True, key="pi"):
            apply_scientific_function('π')
            st.rerun()
    
    with col_c4:
        if st.button("÷", use_container_width=True, key="divide"):
            perform_operation('/')
            st.rerun()
    
    # Number buttons row 1
    col_n1, col_n2, col_n3, col_n4 = st.columns(4)
    with col_n1:
        if st.button("7", use_container_width=True, key="7"):
            add_to_display('7')
            st.rerun()
    with col_n2:
        if st.button("8", use_container_width=True, key="8"):
            add_to_display('8')
            st.rerun()
    with col_n3:
        if st.button("9", use_container_width=True, key="9"):
            add_to_display('9')
            st.rerun()
    with col_n4:
        if st.button("×", use_container_width=True, key="multiply"):
            perform_operation('*')
            st.rerun()
    
    # Number buttons row 2
    col_n1, col_n2, col_n3, col_n4 = st.columns(4)
    with col_n1:
        if st.button("4", use_container_width=True, key="4"):
            add_to_display('4')
            st.rerun()
    with col_n2:
        if st.button("5", use_container_width=True, key="5"):
            add_to_display('5')
            st.rerun()
    with col_n3:
        if st.button("6", use_container_width=True, key="6"):
            add_to_display('6')
            st.rerun()
    with col_n4:
        if st.button("−", use_container_width=True, key="subtract"):
            perform_operation('-')
            st.rerun()
    
    # Number buttons row 3
    col_n1, col_n2, col_n3, col_n4 = st.columns(4)
    with col_n1:
        if st.button("1", use_container_width=True, key="1"):
            add_to_display('1')
            st.rerun()
    with col_n2:
        if st.button("2", use_container_width=True, key="2"):
            add_to_display('2')
            st.rerun()
    with col_n3:
        if st.button("3", use_container_width=True, key="3"):
            add_to_display('3')
            st.rerun()
    with col_n4:
        if st.button("+", use_container_width=True, key="add"):
            perform_operation('+')
            st.rerun()
    
    # Number buttons row 4
    col_n1, col_n2, col_n3, col_n4 = st.columns(4)
    with col_n1:
        if st.button("0", use_container_width=True, key="0"):
            add_to_display('0')
            st.rerun()
    with col_n2:
        if st.button(".", use_container_width=True, key="decimal"):
            if '.' not in st.session_state.display:
                add_to_display('.')
            st.rerun()
    with col_n3:
        if st.button("=", use_container_width=True, key="equals"):
            calculate_result()
            st.rerun()
    with col_n4:
        if st.button("^", use_container_width=True, key="power"):
            perform_operation('^')
            st.rerun()
    
    # Scientific functions
    st.markdown("**Scientific Functions:**")
    sci_col1, sci_col2, sci_col3, sci_col4 = st.columns(4)
    
    with sci_col1:
        if st.button("sin", use_container_width=True, key="sin"):
            apply_scientific_function('sin')
            st.rerun()
    with sci_col2:
        if st.button("cos", use_container_width=True, key="cos"):
            apply_scientific_function('cos')
            st.rerun()
    with sci_col3:
        if st.button("tan", use_container_width=True, key="tan"):
            apply_scientific_function('tan')
            st.rerun()
    with sci_col4:
        if st.button("√", use_container_width=True, key="sqrt"):
            apply_scientific_function('sqrt')
            st.rerun()
    
    sci_col5, sci_col6, sci_col7, sci_col8 = st.columns(4)
    
    with sci_col5:
        if st.button("log", use_container_width=True, key="log"):
            apply_scientific_function('log')
            st.rerun()
    with sci_col6:
        if st.button("ln", use_container_width=True, key="ln"):
            apply_scientific_function('ln')
            st.rerun()
    with sci_col7:
        if st.button("x²", use_container_width=True, key="square"):
            apply_scientific_function('x²')
            st.rerun()
    with sci_col8:
        if st.button("1/x", use_container_width=True, key="reciprocal"):
            apply_scientific_function('1/x')
            st.rerun()

with col2:
    st.subheader("📋 History")
    
    if st.session_state.history:
        # Clear history button
        if st.button("Clear History", use_container_width=True):
            st.session_state.history = []
            st.rerun()
        
        # Display history
        for idx, item in enumerate(reversed(st.session_state.history[-10:])):  # Show last 10
            st.markdown(f"""
                <div class="history-item">
                    <small><strong>{item['timestamp']}</strong></small><br>
                    {item['expression']}
                </div>
            """, unsafe_allow_html=True)
    else:
        st.info("No calculations yet")
