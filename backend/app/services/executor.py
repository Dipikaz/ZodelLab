import subprocess

def safe_execute(code_str):
    with open("temp_script.py", "w") as f:
        f.write(code_str)
    
    # Timeout prevents infinite loops
    res = subprocess.run(
        ["python3", "temp_script.py"], 
        capture_output=True, 
        text=True, 
        timeout=10 
    )
    return res.stdout # This should be the JSON for Plotly