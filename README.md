# gltf2usd

This tool is a command-line Python script which converts glTF 2.0 models to USD, with the goal being simple pipeline conversion from glTF to usdz using Pixar's `usdzip` or Apple's `usdz_converter`.  

The tool is a **proof-of-concept**, to determine format conversion details, which could be useful for an actual C++ USD plugin.  It has been developed and tested on both Windows 10 and Mac OS 10.14 Mojave Beta, using USD v18.09 and is built against the USD Python API.

This tool currently only works on glTF 2.0 files with external textures, based on the core glTF 2.0 specification (no extensions).  

## Supported Features
- glTF nodes are mapped to USD `Xform`
- glTF `PbrMetallicRoughnessMaterial` is mapped to `USDPreviewSurface`
- glTF `PbrSpecularGlossiness` extension
- glTF Skeletal animation is mapped to `UsdSkel`
- glTF node animations are supported
- Currently supports `.gltf` conversion to `.usd`, `.usda`, `.usdc`, and `.usdz`


## Currently not implemented:
- `.glb` files
- glTF extensions
- Primitive modes (other than triangles)

## Note:
- The root node of the generated USD file is, by default, scaled by 100 to convert from glTF's meters to USD's centimeters.  This scale is purely to be able to see the glTF models when using ARKit, or otherwise, they are too small.
- There are several edge cases that have not been fully tested yet

## Dependencies:

- You will need to initially have [USD v18.09](https://github.com/PixarAnimationStudios/USD) installed on your system
and have the Python modules built
    - Linux users will need to build the tools themselves, or use [AnimalLogic's USD Docker Container](https://github.com/AnimalLogic/docker-usd) (recommended for non-CentOS users)
    - macOS users can use Apple's [Prebuilt USD Toolkit](https://developer.apple.com/go/?id=python-usd-library). Make sure you add the USD dir to your `PYTHONPATH`

### Python dependencies
You can install the following python dependencies using `pip install -r requirements.txt`:

- Pillow (Python module for image manipulation)
- enum34 (Python module for enums in Python 2.7)


## Help Menu:
```Shell
python gltf2usd.py -h
usage: gltf2usd.py [-h] --gltf GLTF_FILE [--fps FPS] --output USD_FILE
                   [--scale] [--verbose] [--arkit]

Convert glTF to USD

optional arguments:
  -h, --help            show this help message and exit
  --gltf GLTF_FILE, -g GLTF_FILE
                        glTF file (in .gltf format)
  --fps FPS             The frames per second for the animations (defaults to 24 fps)
  --output USD_FILE, -o USD_FILE
                        destination to store generated .usda file
  --scale SCALE, -s     Scale the resulting USDA model
  --verbose, -v         Enable verbose mode
  --arkit               Check USD with ARKit compatibility before making USDZ
                        file
```

## Sample usage:
```Shell
python gltf2usd.py -g ../path_to_read_glTF_file/file.gltf -o path_to_write_usd_file/file.usda
```
