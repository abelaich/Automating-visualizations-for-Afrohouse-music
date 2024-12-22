import tkinter as tk

def main():
    # Create the main window
    root = tk.Tk()
    root.title("Afrohouse Visualization")
    
    # Make the window full screen
    root.attributes("-fullscreen", True)
    
    # Set the background to black
    root.configure(bg="black")
    
    # Disable resizing
    root.resizable(False, False)
    
    # Add a keybinding to exit full screen with "Esc"
    root.bind("<Escape>", lambda event: root.quit())
    
    # Run the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()
