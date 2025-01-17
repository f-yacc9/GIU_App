import tkinter as tk
from tkinter import filedialog, ttk
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

"""class PlotApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Browser and Plotting App")
        
        # File Selection
        self.file_label = tk.Label(root, text="No file selected")
        self.file_label.pack(pady=10)
        
        self.browse_button = tk.Button(root, text="Browse File", command=self.browse_file)
        self.browse_button.pack(pady=10)
        
        # Data Preview
        self.preview_label = tk.Label(root, text="Data Preview:")
        self.preview_label.pack(pady=5)
        
        self.text_preview = tk.Text(root, height=10, width=80)
        self.text_preview.pack(pady=10)
        
        # Plotting Options
        self.options_frame = tk.Frame(root)
        self.options_frame.pack(pady=10)
        
        self.x_label = tk.Label(self.options_frame, text="X-axis:")
        self.x_label.grid(row=0, column=0, padx=5)
        
        self.x_combobox = ttk.Combobox(self.options_frame, state="readonly")
        self.x_combobox.grid(row=0, column=1, padx=5)
        
        self.y_label = tk.Label(self.options_frame, text="Y-axis:")
        self.y_label.grid(row=0, column=2, padx=5)
        
        self.y_combobox = ttk.Combobox(self.options_frame, state="readonly")
        self.y_combobox.grid(row=0, column=3, padx=5)
        
        self.plot_button = tk.Button(root, text="Plot", command=self.plot_data)
        self.plot_button.pack(pady=10)
        
        # Plot Area
        self.plot_frame = tk.Frame(root)
        self.plot_frame.pack(pady=10)
        
    def browse_file(self):
        filepath = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv"), ("All files", "*.*"),("Text files","*.txt")])
        if filepath:
            self.file_label.config(text=filepath)
            self.load_data(filepath)
    
    def load_data(self, filepath):
        try:
            self.data = pd.read_csv(filepath)
            self.text_preview.delete("1.0", tk.END)
            self.text_preview.insert(tk.END, self.data.head().to_string())
            
            # Update combobox options
            columns = self.data.columns.tolist()
            self.x_combobox["values"] = columns
            self.y_combobox["values"] = columns
        except Exception as e:
            self.text_preview.delete("1.0", tk.END)
            self.text_preview.insert(tk.END, f"Error loading file: {e}")
    
    def plot_data(self):
        x_col = self.x_combobox.get()
        y_col = self.y_combobox.get()
        
        if not x_col or not y_col:
            self.text_preview.insert(tk.END, "\nPlease select X and Y columns!")
            return
        
        # Create plot
        fig, ax = plt.subplots(figsize=(5, 4))
        ax.plot(self.data[x_col], self.data[y_col], label=f"{y_col} vs {x_col}")
        ax.set_xlabel(x_col)
        ax.set_ylabel(y_col)
        ax.legend()
        
        # Clear previous plot and embed the new one
        for widget in self.plot_frame.winfo_children():
            widget.destroy()
        
        canvas = FigureCanvasTkAgg(fig, master=self.plot_frame)
        canvas.draw()
        canvas.get_tk_widget().pack()

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = PlotApp(root)
    root.mainloop()"""



root = tk.Tk()
#main = ttk.Frame(root)
#tk.Label(main, text="Hello, World!", bg="red").pack()

tk.Label(root, text="Hello, World!", bg="pink").pack(side="left", expand=True, fill="both")

root.mainloop()

