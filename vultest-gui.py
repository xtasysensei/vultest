import os
import sys
import subprocess
import threading
import tkinter as tk
from tkinter import ttk, messagebox

# Global variable to store the subprocess
scan_process = None

def run_xss_scan(url):
    """Runs the XSS scan using a subprocess."""
    global scan_process
    script_path = os.path.join('main', 'anti-xss.py')
    try:
        scan_process = subprocess.Popen([sys.executable, script_path, '-u', url])
        scan_process.wait()
        if scan_process.returncode == 0:
            messagebox.showinfo("Scan Complete", "XSS Scan completed successfully.")
        else:
            messagebox.showerror("Error", f"XSS Scan failed with return code {scan_process.returncode}.")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"XSS Scan failed: {e}")
    finally:
        enable_buttons()

def run_sql_injection_scan(url):
    """Runs the SQL Injection scan using a subprocess."""
    global scan_process
    script_path = os.path.join('main', 'sqlifinder.py')
    try:
        scan_process = subprocess.Popen([sys.executable, script_path, '-d', url])
        scan_process.wait()
        if scan_process.returncode == 0:
            messagebox.showinfo("Scan Complete", "SQL Injection Scan completed successfully.")
        else:
            messagebox.showerror("Error", f"SQL Injection Scan failed with return code {scan_process.returncode}.")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"SQL Injection Scan failed: {e}")
    finally:
        enable_buttons()

def run_scan_in_thread(scan_func, url):
    """Runs the scan in a separate thread to prevent GUI freezing."""
    disable_buttons()
    threading.Thread(target=scan_func, args=(url,)).start()

def on_scan_button_click(scan_type):
    """Handles button click to start a scan."""
    url = url_entry.get().strip()
    if not url:
        messagebox.showwarning("Input Error", "Please enter a valid URL.")
        return

    if scan_type == 'xss':
        run_scan_in_thread(run_xss_scan, url)
    elif scan_type == 'sql':
        run_scan_in_thread(run_sql_injection_scan, url)

def cancel_scan():
    """Cancels the currently running scan."""
    global scan_process
    if scan_process and scan_process.poll() is None:  # If process is still running
        scan_process.terminate()
        messagebox.showinfo("Scan Canceled", "The scan has been canceled.")
    else:
        messagebox.showwarning("No Scan Running", "There is no scan running to cancel.")
    enable_buttons()

def disable_buttons():
    """Disable the scan buttons and enable the cancel button."""
    xss_button.config(state=tk.DISABLED)
    sql_button.config(state=tk.DISABLED)
    cancel_button.config(state=tk.NORMAL)

def enable_buttons():
    """Enable the scan buttons and disable the cancel button."""
    xss_button.config(state=tk.NORMAL)
    sql_button.config(state=tk.NORMAL)
    cancel_button.config(state=tk.DISABLED)

# GUI setup
root = tk.Tk()
root.title("Web Vulnerability Scanner")
root.geometry("600x300")
root.resizable(True, True)

# Define style
style = ttk.Style()
style.configure('TLabel', font=('Helvetica', 14), background='#f7f7f7', foreground='#333')
style.configure('TButton', font=('Helvetica', 12), padding=10, background="#4CAF50", foreground='white')
style.configure('TEntry', padding=10)

# Main frame for content
frame = tk.Frame(root, bg="#f7f7f7", bd=5)
frame.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.9, relheight=0.6)

# URL input field
url_label = tk.Label(frame, text="Enter URL:", font=('Helvetica', 14), bg='#f7f7f7')
url_label.grid(row=0, column=0, padx=20, pady=(10, 10), sticky=tk.W)
url_entry = tk.Entry(frame, font=('Helvetica', 12), bd=2, relief="groove")
url_entry.grid(row=0, column=1, padx=20, pady=(10, 10), sticky=tk.EW)

# XSS Scan button
xss_button = tk.Button(frame, text="Start XSS Scan", font=('Helvetica', 12), command=lambda: on_scan_button_click('xss'),
                       bg="#4CAF50", fg='white', relief='raised', bd=3)
xss_button.grid(row=1, column=0, padx=20, pady=(10, 10), sticky=tk.W)

# SQL Injection Scan button
sql_button = tk.Button(frame, text="Start SQL Injection Scan", font=('Helvetica', 12), command=lambda: on_scan_button_click('sql'),
                       bg="#2196F3", fg='white', relief='raised', bd=3)
sql_button.grid(row=1, column=1, padx=20, pady=(10, 10), sticky=tk.W)

# Cancel Scan button
cancel_button = tk.Button(frame, text="Cancel Scan", font=('Helvetica', 12), command=cancel_scan,
                          bg="#f44336", fg='white', relief='raised', bd=3, state=tk.DISABLED)
cancel_button.grid(row=2, column=0, columnspan=2, pady=(10, 10), sticky=tk.EW)

# Exit button
exit_button = tk.Button(root, text="Exit", command=root.quit, font=('Helvetica', 12),
                        bg="#f44336", fg='white', relief='raised', bd=3)
exit_button.place(relx=0.5, rely=0.95, anchor="s", y=-20)

# Make sure URL entry expands horizontally
frame.grid_columnconfigure(1, weight=1)

root.mainloop()
