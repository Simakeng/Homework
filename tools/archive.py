import zipfile
import argparse
import os
parser = argparse.ArgumentParser(description="Archive maker ver 1.0")

parser.add_argument('input_files', metavar='files', type=str, nargs='+',
                    help='file to pack')
parser.add_argument('-o', dest='file',help="output file path")
args = parser.parse_args()

print(f'Creating zip file {args.file}...')
print(args.file)
print(args.input_files)
zfile = zipfile.ZipFile(args.file,'w')
for file in args.input_files:
    print(file)
    zfile.write(file,file.split(os.path.sep)[-1],compress_type=zipfile.ZIP_LZMA)

zfile.close()