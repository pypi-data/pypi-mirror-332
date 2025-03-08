"""Define classes and methods for working with JPEG files.
"""

import os
from tkinter import (
    Tk,
    Label,
    Button,
    Listbox,
    SINGLE,
    filedialog,
    Scale,
    HORIZONTAL,
    IntVar,
    Toplevel,
)
from PIL import Image


class JPEGToolSelector:
    """Main tool selector interface."""

    def __init__(self, master):
        self.master = master
        master.title("JPEG Tools")

        # Tool selection label
        self.label = Label(master, text="Select a JPEG Tool:")
        self.label.pack()

        # Tool listbox
        self.tool_listbox = Listbox(master, selectmode=SINGLE, height=5)
        self.tool_listbox.pack()

        # Add tools
        self.tools = ["Size Reduction"]
        for tool in self.tools:
            self.tool_listbox.insert("end", tool)

        # Launch button
        self.launch_button = Button(master, text="Launch Tool", command=self.launch_tool)
        self.launch_button.pack()

    def launch_tool(self):
        """Launch the selected tool."""
        selected_tool_index = self.tool_listbox.curselection()
        if not selected_tool_index:
            self.label.config(text="Please select a tool!", fg="red")
            return

        selected_tool = self.tools[selected_tool_index[0]]
        if selected_tool == "Size Reduction":
            self.run_size_reduction_tool()

    def run_size_reduction_tool(self):
        """Launch the Size Reduction tool."""
        SizeReductionTool(Toplevel(self.master))  # Open as a new window


class SizeReductionTool:
    """Size reduction tool interface."""

    def __init__(self, master):
        self.master = master
        master.title("JPEG Size Reducer")

        # File selection
        self.label = Label(master, text="Select a JPEG file:")
        self.label.pack()

        self.file_button = Button(master, text="Browse", command=self.select_file)
        self.file_button.pack()

        self.file_path_label = Label(master, text="", fg="blue")
        self.file_path_label.pack()

        # Quality slider
        self.quality_label = Label(master, text="Quality (1-100):")
        self.quality_label.pack()

        self.quality_var = IntVar(value=85)
        self.quality_slider = Scale(master, from_=1, to=100, orient=HORIZONTAL, variable=self.quality_var)
        self.quality_slider.pack()

        # Resize slider
        self.resize_label = Label(master, text="Resize percentage (10-100):")
        self.resize_label.pack()

        self.resize_var = IntVar(value=100)
        self.resize_slider = Scale(master, from_=10, to=100, orient=HORIZONTAL, variable=self.resize_var)
        self.resize_slider.pack()

        # Reduce button
        self.reduce_button = Button(master, text="Reduce Size", command=self.reduce_size)
        self.reduce_button.pack()

        # Status label
        self.status_label = Label(master, text="", fg="green")
        self.status_label.pack()

        self.file_path = None

    def select_file(self):
        """Select a JPEG file."""
        self.file_path = filedialog.askopenfilename(
            title="Select a JPEG file",
            filetypes=[("JPEG files", "*.jpg;*.jpeg")],
        )
        if self.file_path:
            self.file_path_label.config(text=os.path.basename(self.file_path))

    def reduce_size(self):
        """Reduce the size of the selected JPEG."""
        if not self.file_path:
            self.status_label.config(text="No file selected!", fg="red")
            return

        quality = self.quality_var.get()
        resize_percent = self.resize_var.get() / 100

        try:
            # Open the image
            img = Image.open(self.file_path)

            # Resize if applicable
            if resize_percent < 1.0:
                new_dimensions = (int(img.width * resize_percent), int(img.height * resize_percent))
                img = img.resize(new_dimensions, Image.ANTIALIAS)

            # Save reduced image
            save_path = filedialog.asksaveasfilename(
                title="Save Reduced JPEG",
                defaultextension=".jpg",
                filetypes=[("JPEG files", "*.jpg;*.jpeg")],
            )
            if save_path:
                img.save(save_path, quality=quality, optimize=True)
                self.status_label.config(text="File saved successfully!", fg="green")
            else:
                self.status_label.config(text="Save cancelled.", fg="orange")

        except Exception as e:
            self.status_label.config(text=f"Error: {e}", fg="red")


if __name__ == "__main__":
    root = Tk()
    app = JPEGToolSelector(root)
    root.mainloop()
