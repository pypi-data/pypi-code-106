import sys, argparse, os
from PIL import Image
import numpy as np


def main(infile: str, outfile: str) -> int:
    if not os.path.isfile(infile):
        print(f"{infile} does not exists!")
        return -1
    
    im = Image.open(infile)

    if im.width > 255 or im.height > 255:
        print("Image must be 255x255 or smaller!")
        return -1
    
    if im.format != "BMP":
        print("Image must be a bitmap")
        return -1
    
    if im.mode != "1":
        print("Image must be monochrome 1-bit pixels")
        
    # Convert the image to a numpy array
    im_array = np.array(im)

    with open(outfile, 'wb') as out: 
        # Write out the width then height as the first two bytes
        out.write((im.width).to_bytes(1, byteorder='big'))
        out.write((im.height).to_bytes(1, byteorder='big'))

        # loop through the rows and pack the rows into arrays of bytes
        for row in im_array:
            bits = np.packbits(row, bitorder="little")
            # write out the bytes, but in reverse order
            out.write(bits.tobytes()[::-1])


def cli():
    parser = argparse.ArgumentParser(description='Convert Monochrome BMP to Duet3D Menu Image')
    parser.add_argument("bitmap", type=str, help="Input monochrome bitmap")
    parser.add_argument("output", type=str, help="Output filename")

    args = parser.parse_args()
    sys.exit(main(args.bitmap, args.output))  # next section explains the use of sys.exit


if __name__ == '__main__':
    cli()
