from typing import TypedDict


class _PALETTE_TYPE(TypedDict):
    main: str
    dark: str
    light: str


_RGB_TYPE = tuple[int, int, int] | tuple[int, int, int, int]


def rgb_to_hex(rgb: _RGB_TYPE) -> str:
    return "#" + "".join(f"{int(255*c):02X}" for c in rgb)


def get_brightness(rgb: _RGB_TYPE) -> float:
    return sum(rgb) / 3


def rgb_to_rgba(rgb: _RGB_TYPE) -> _RGB_TYPE:
    """Convert a RGB color to a RGBA color."""
    return (rgb + (1,)) if len(rgb) == 3 else rgb


def hex_to_rgb(hex: str) -> _RGB_TYPE:
    """Convert a hex color to a RGB color."""
    if hex.startswith("#"):
        hex = hex[1:]
    if len(hex) == 3:
        return tuple(int(hex[i] * 2, 16) / 255 for i in (0, 1, 2))
    elif len(hex) == 4:
        return tuple(int(hex[i : i + 2], 16) / 255 for i in (0, 1, 2, 3))
    elif len(hex) == 6:
        return tuple(int(hex[i : i + 2], 16) / 255 for i in (0, 2, 4))
    elif len(hex) == 8:
        return tuple(int(hex[i : i + 2], 16) / 255 for i in (0, 2, 4, 6))
    else:
        raise ValueError(f"Invalid hex color: {hex}")


def check_rgba(rgba: _RGB_TYPE) -> bool:
    if len(rgba) == 3:
        rgba = rgba + (1,)

    if len(rgba) != 4:
        return False

    return all(not (c < 0 or c > 1) for c in rgba)


def raise_if_rgba_is_invalid(rgba: _RGB_TYPE) -> _RGB_TYPE:
    if not check_rgba(rgba):
        raise ValueError(f"Invalid rgba color: {rgba}")
    return rgba


def change_brightness_relatively(rgba: _RGB_TYPE, brightness: float) -> _RGB_TYPE:
    """Change the brightness of a color.

    Args:
        rgb (_RGB_TYPE): The color to change.
        brightness (float): The final brightness of the color.
            From 0 to 1. where 0 is black and 1 is white and 0.5 is the original color.

    Returns:
        _RGB_TYPE: The color with the new brightness.
    """
    # Ensure brightness is between 0 and 1
    brightness = max(0, min(1, brightness))
    rgb = rgba[:3]

    # Calculate relative brightness compared to current brightness
    # current_brightness = get_brightness(rgb)
    if brightness < 0.5:
        # Darken: interpolate between black (0,0,0) and current color
        factor = 2 * brightness
        new_rgb = tuple(c * factor for c in rgb[:3])
    else:
        # Lighten: interpolate between current color and white (255,255,255)
        factor = 2 * (brightness - 0.5)
        new_rgb = tuple(c + (1 - c) * factor for c in rgb[:3])

    # Preserve alpha if it exists
    if len(rgba) == 4:
        return new_rgb + (rgba[3],)
    return new_rgb


def change_brightness_absolutely(rgba: _RGB_TYPE, brightness: float) -> _RGB_TYPE:
    """Change the brightness of a color.

    Args:
        rgb (_RGB_TYPE): The color to change.
        brightness (float): The final brightness of the color.
            From 0 to 1, where 0 is black and 1 is white.

    Returns:
        _RGB_TYPE: The color with the new brightness.
    """
    # Ensure brightness is between 0 and 1
    brightness = max(0, min(1, brightness))
    rgb = rgba[:3]

    # Scale each RGB component to match target brightness
    # Average of RGB components should equal target brightness * 255
    current_brightness = get_brightness(rgb)
    if current_brightness == 0:
        # Handle black color case
        new_rgb = tuple(brightness for _ in range(3))
    else:
        # Scale RGB values to achieve target brightness
        scale = (brightness * 3) / sum(rgb)
        new_rgb = tuple(min(1, c * scale) for c in rgb)

    # Preserve alpha if it exists
    if len(rgba) == 4:
        return new_rgb + (rgba[3],)
    return new_rgb


def change_alpha(rgb: _RGB_TYPE, alpha: float) -> _RGB_TYPE:
    """Change the alpha of a color.

    Args:
        rgb (_RGB_TYPE): The color to change.
        alpha (float): The final alpha of the color.
    """
    return rgb[:3] + (alpha,)


_POSSIBLE_COLOR_INIT_TYPES = (
    _PALETTE_TYPE | str | tuple[int, int, int] | tuple[int, int, int, int]
)


def convert_to_rgb(
    color: str | tuple[int, int, int] | tuple[int, int, int, int] | dict,
) -> _RGB_TYPE:
    if isinstance(color, str):
        return raise_if_rgba_is_invalid(hex_to_rgb(color))
    elif isinstance(color, tuple):
        return raise_if_rgba_is_invalid(color)
    elif isinstance(color, dict):
        return raise_if_rgba_is_invalid(convert_to_rgb(color["main"]))
    elif color is None:
        return (1, 1, 1)
    else:
        raise ValueError(f"Invalid color: {color}")


def convert_to_palette(palette: _POSSIBLE_COLOR_INIT_TYPES) -> _PALETTE_TYPE:
    if isinstance(palette, dict):
        for key, value in palette.items():
            palette[key] = convert_to_rgb(value)
        return palette

    return {"main": convert_to_rgb(palette)}


class ColorClass(tuple):
    def __new__(cls, palette: _POSSIBLE_COLOR_INIT_TYPES | None = None, **kwargs):
        main_color = convert_to_rgb(palette)
        return super().__new__(cls, main_color)

    def __init__(
        self,
        palette: _PALETTE_TYPE | str | None = None,
        background_color: _RGB_TYPE | None = None,
    ):
        self.palette = convert_to_palette(palette)
        self.main_color = self.palette["main"]
        self._background_color = (
            convert_to_rgb(background_color) if background_color else (1, 1, 1)
        )

    @property
    def dark(self):
        if "dark" in self.palette:
            return self._new_color(self.palette["dark"])
        else:
            return self.brightness(0.35)

    @property
    def light(self):
        if "light" in self.palette:
            return self._new_color(self.palette["light"])
        else:
            return self.brightness(0.65)

    @property
    def main(self):
        return self

    @property
    def hex(self):
        return rgb_to_hex(self.main_color)

    @property
    def rgba(self):
        return rgb_to_rgba(self.main_color)

    @property
    def rgb(self):
        if len(self.main_color) > 3 and self.main_color[3] < 1.0:
            # Alpha compositing with white background
            alpha = self.main_color[3]
            rgb = self.main_color[:3]
            # Formula: final_color = alpha * foreground + (1-alpha) * background
            # Where background is white (1,1,1)
            return tuple(
                c * alpha + (1 - alpha) * self._background_color[i]
                for i, c in enumerate(rgb)
            )
        return self.main_color[:3]

    def alpha(self, alpha: float, background_color: _RGB_TYPE | None = None):
        return self.opacity(alpha, background_color)

    def opacity(self, opacity: float, background_color: _RGB_TYPE | None = None):
        return self._new_color(
            change_alpha(self.main_color, opacity), background_color=background_color
        )

    def brightness(self, brightness: float):
        """Change the brightness of a color.

        Args:
            brightness (float): The final brightness of the color.
                From 0 to 1, where 0 is black and 1 is white.
        """
        return self._new_color(
            change_brightness_relatively(self.main_color, brightness)
        )

    def absolute_brightness(self, brightness: float):
        """Change the brightness of a color.

        Args:
            brightness (float): The final brightness of the color.
                From 0 to 1, where 0 is black and 1 is white.
        """
        return self._new_color(
            change_brightness_absolutely(self.main_color, brightness)
        )

    @property
    def transparent(self):
        return self._new_color(change_alpha(self.main_color, 0))

    def _new_color(self, color: _RGB_TYPE, background_color: _RGB_TYPE | None = None):
        if background_color is None:
            background_color = self._background_color
        return self.__class__(color, background_color=background_color)
