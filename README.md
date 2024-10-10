# Turtle Dot Art (Hirst Painting)

This Python program uses the Turtle module to create a dot painting, randomly selecting colors from a predefined color list. The turtle moves in a grid-like pattern and places colored dots at specific coordinates.

## Features

- The turtle draws a 10x10 grid of colored dots.
- The colors for the dots are chosen randomly from a pre-set color palette.
- The turtle moves quickly, with the speed set to "fastest" for efficient drawing.

## Setup Instructions

### 1. Clone the GitHub Repository

To get started, clone the repository to your local machine:

```bash
git clone https://github.com/Selorme/dot_art_turtle.git
```

Navigate into the project directory:

```bash
cd turtle-dot-art
```

### 2. Install Dependencies

Make sure you have Python 3.x installed. You can check your version using:

```bash
python --version
```

The code primarily relies on the `turtle` module, which is built into Python, and `colorgram.py` if you want to use the optional color extraction feature.

To install the optional `colorgram.py` library, use:

```bash
pip install colorgram.py
```

### 3. Run the Script

Run the `turtle_dot_art.py` script to generate the dot painting:

```bash
python turtle_dot_art.py
```

This will open a Turtle graphics window where the turtle will create the dot art.

## Code Breakdown

1. **Color Palette**: 
   The list `color_list` contains RGB color tuples, from which the program randomly selects the color for each dot.
   
2. **Grid Drawing**: 
   The turtle moves across a 10x10 grid, with each dot being placed 50 units apart. The position of each dot is calculated based on the current row and column.

3. **Turtle Setup**:
   - The turtle's color mode is set to 255 to use RGB values.
   - The turtle shape is set to a turtle, and the speed is set to "fastest" to reduce drawing time.

4. **Optional: Color Extraction**:
   The commented-out section includes code that uses the `colorgram` library to extract colors from an image. This could be used to update the color palette dynamically based on an image.

## How to Use the Color Extraction Feature

If you'd like to extract colors from an image, you can uncomment the code in the last section of the script. Replace `"image.jpg"` with the path to the image file from which you want to extract colors.

## Libraries Used

- **Turtle**: Built-in Python library for graphics.
- **colorgram.py** (Optional): Used for extracting colors from images.

## License

This project is licensed under the MIT License.