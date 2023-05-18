import pytest
import os
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from rgbi_gui_new import RGBI_GUI


@pytest.fixture
def gui():
    window = tk.Tk()
    return RGBI_GUI(window)

@pytest.mark.parametrize("input_dir, yolo_path, yolo_version, class_id, image_size, output_dir", [
    ("/path/to/input", "/path/to/yolo", "v8", 0, 640, "/path/to/output")])

def test_generate_output(gui, input_dir, yolo_path, yolo_version, class_id, image_size, output_dir):
    # Set the initial values in the GUI
    gui.entryInputPath.delete(0, "end")
    gui.entryInputPath.insert(0, input_dir)
    gui.entryyoloPath.delete(0, "end")
    gui.entryyoloPath.insert(0, yolo_path)
    gui.comboYolo.set(yolo_version)
    gui.entrycid.delete(0, "end")
    gui.entrycid.insert(0, str(class_id))
    gui.entrysize.delete(0, "end")
    gui.entrysize.insert(0, str(image_size))
    gui.entryOutputPath.delete(0, "end")
    gui.entryOutputPath.insert(0, output_dir)

# Test cases
def test_gui_components(gui):
    assert isinstance(gui.labelInput, ttk.Label)
    assert isinstance(gui.entryInputPath, ttk.Entry)
    assert isinstance(gui.btnBrowseIpDir, ttk.Button)
    assert isinstance(gui.comboYolo, ttk.Combobox)

def test_invalid_input_directory(gui, mocker):
    mocker.patch('tkinter.messagebox.showerror')
    gui.btnGenRes.invoke()
    messagebox.showerror.assert_called_once_with("Error", "Input Directory or Output Directory is not specified!")

def test_yolo_version_selection(gui):
    gui.comboYolo.set("v7")
    assert gui.comboYolo.get() == "v7"
