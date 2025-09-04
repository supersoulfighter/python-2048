"""
Asset loader
============
*This module makes working with assets (images, sounds, fonts) easier by preloading and accessing each asset with a string path.*

- Images are converted to ``pygame.Surfaces``.
- Sounds to ``pygame.Sounds``.
- Fonts are left as ``Path`` references (see Fonts below).
- If multiple assets are found in a folder, they are added to a tuple (see Images below).
- It is recommended that you use a top-level folder for each asset type: "images", "sounds", "fonts".

Initialization
--------------
The ``load_assets()`` function takes a root asset directory and loads all assets, recursively looking in subfolders. Call this function before you access any assets.

If you do a standard import of this module: ``import assets``, the assets variable will be global, meaning assets are loaded once and shared between all files. Other importing methods, like ``from assets import *``, could be used to load separate asset collections. Presumably, each would be created by supplying different root directories to ``load_assets()``.

Usage
-----
All assets are loaded into a single dictionary, the ``assets`` variable. The keys are the paths to the assets, e.g., "images/player/jump". So in any file, import assets, then access an asset with ``assets["images/player/jump"]``.

Images
------
To access a single image (Surface), for example: ``self.image = assets["images/player/idle"]``. If multiple images are found in a folder, they are added to a tuple. This makes it easier to have a set of animation frames. So to set a Sprite's image to the fifth (file) animation frame, use ``self.image = assets["images/player/run"][4]``.

Sounds
------
Example way to play a Sound: ``assets["sounds/bleep"].play()``

Fonts
-----
A ``pygame.Font`` must be created for each font size, so this module won't know what sizes are needed ahead of time. Therefore, Fonts are not actually loaded until you use code like this example:
``pygame.font.Font(assets["fonts/SomeFont/regular"], SOME_FONT_SIZE)``
"""
from pathlib import Path

import pygame

# Single dictionary for all assets
assets = {}


def load_assets(assets_relative_path: str):
    """
    load_assets
    ===========

    *Load assets into the ``assets`` global variable.*

    Parameters
    ----------
        ``assets_relative_path``: This should be the root directory of all assets, relative to the project folder. For example, "./assets".
    """
    # This little hack is needed for PyCharm as it treats the root directory as the current directory.
    a = Path(assets_relative_path)
    if not a.exists():
        assets_relative_path = "../" + a.stem
        a = Path(assets_relative_path)

    for directory in a.rglob("*"):
        if not directory.is_dir():
            continue
            
        # Skip certain directories
        if any(skip in str(directory) for skip in ["__pycache__", ".git"]):
            continue
        
        # Get all files in this directory
        files = [f for f in directory.iterdir() if f.is_file()]
        if not files:
            continue
        
        # Group files by type
        images = [f for f in files if f.suffix.lower() in [
            '.bmp',
            '.gif',
            '.jpg',
            '.jpeg',
            '.lbm',
            '.pcx',
            '.pbm',
            '.pgm',
            '.png',
            '.pnm',
            '.ppm',
            '.svg',
            '.tga',
            '.tiff',
            '.webp',
            '.xpm',
        ]]
        sounds = [f for f in files if f.suffix.lower() in [
            '.wav',
            '.mp3',
            '.ogg'
        ]]
        fonts = [f for f in files if f.suffix.lower() in [
            '.ttf',
            '.otf'
        ]]
        
        # Create relative path key
        rel_path = directory.relative_to(assets_relative_path).as_posix()
        
        # Load images
        if images:
            surfaces = tuple(pygame.image.load(str(img)).convert_alpha() for img in sorted(images))
            assets[rel_path] = surfaces[0] if len(surfaces) == 1 else surfaces
        
        # Load sounds
        if sounds:
            sound_effects = tuple(pygame.mixer.Sound(str(snd)) for snd in sorted(sounds))
            assets[rel_path] = sound_effects[0] if len(sound_effects) == 1 else sound_effects
        
        # Load fonts
        if fonts:
            assets[rel_path] = fonts[0] if len(fonts) == 1 else sorted(fonts)



def print_assets():
    """Print all loaded assets for debugging."""
    print("\nLoaded Assets:")
    for path, asset in assets.items():
        asset_type = "image(s)" if isinstance(asset, (pygame.Surface, tuple)) and isinstance(asset[0] if isinstance(asset, tuple) else asset, pygame.Surface) else \
                    "sound(s)" if isinstance(asset, (pygame.mixer.Sound, tuple)) and isinstance(asset[0] if isinstance(asset, tuple) else asset, pygame.mixer.Sound) else \
                    "font(s)"
        count = len(asset) if isinstance(asset, tuple) else 1
        print(f"  {path}: {count} {asset_type}")
