from ratisbona_utils.colors.simple_color import RGBColor
from ratisbona_utils.colors.palette import Palette


def to_gimp_palette(palette: Palette[RGBColor]) -> str:
    """
    Convert a Palette object to a GIMP palette file format.

    Args:
        palette (Palette): The palette object to convert

    Returns:
        str: The GIMP palette file content
    """
    description = palette.description.replace('\n', ' ')
    lines = [
        "GIMP Palette",
        f"Name: {palette.name}",
        "Columns: 16",
        f"# Description: {description}",
        f"# Author: {palette.author}",
        f"# Created: {palette.creation_date}",
    ]
    for color, name in zip(palette.colors, palette.color_names):
        lines.append(f"{color[0]} {color[1]} {color[2]} {name}")
    return "\n".join(lines)


def parse_gimp_palette(palette_as_str: str) -> Palette:
    """
    Parse a GIMP palette file and return the Palette object.

    Args:
        palette_as_str (str): The GIMP palette file content as a string

    Returns:
        Palette: The parsed palette object
    """
    lines = palette_as_str.splitlines()
    lines = map(str.strip, lines)
    lines = list(filter(lambda s: s and not s.startswith("#"), lines))
    if not lines[0] == "GIMP Palette":
        raise ValueError("Not a GIMP palette file")
    if not lines[1].startswith("Name: "):
        raise ValueError("Invalid palette name line {line[1]}. Does not start with 'Name: '")
    name = lines[1][6:]
    money_shot_at = 3
    if not lines[2].startswith("Columns: "):
        money_shot_at = 2
        print("Warning: Invalid columns line {line[2]}. Does not start with 'Columns: '")


    colors = []
    names = []
    for line in lines[money_shot_at:]:
        if not line:
            continue
        color = line.split()
        colors.append((int(color[0]), int(color[1]), int(color[2])))
        names.append(color[3] if len(color) > 3 else "")
    return Palette(
        name=name,
        description="",
        author="",
        creation_date=None,
        colors=colors,
        color_names=names,
        color_types=["rgb"] * len(colors)
    )


