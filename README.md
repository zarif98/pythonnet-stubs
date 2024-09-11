# stubgen

Generate stubs for .NET libraries

Python.NET Stub Generator

## Usage:

    usage: stubgen [-h] [-v] [--verbose] [-o OUTPUT_DIR] [-m] command ...

    A library for generating stubs of .NET libraries

    positional arguments:
        command
            extract             extract types from assemblies to json
            build               build stub file tree

    options:
        -h, --help            show this help message and exit
        -v, --version         show program's version number and exit
        --verbose             set log level to DEBUG
        -o OUTPUT_DIR, --output-dir OUTPUT_DIR
                              path to output directory [default: .]
        -m, --multi-threaded  flag to use multi threading

## Extract:

Generates a skeleton file for each assembly and a doc file for each namespace.

    usage: stubgen extract [-h] [-s] [-p PATH] [-a | -b | -c] [-w] [assemblies ...]

    positional arguments:
        assemblies            names of dll assemblies to process

    options:
        -h, --help            show this help message and exit
        -s, --skip-failed     skips failed assemblies
        -p PATH, --path PATH  additional directories to add to the path
        -a, --all             process all assemblies
        -b, --built_in        process built-in assemblies
        -c, --core            process core assemblies
        -w, --overwrite       overwrite existing files

## Build Usage:

Generates stub files for each namespace in the skeleton files provided. Can optionally include doc strings provided in doc files.

    usage: stubgen build [-h] [-l LINE_LENGTH] [-f] skeletons docs

    positional arguments:
        skeletons             glob to the skeleton files
        docs                  glob to the doc files

    options:
        -h, --help            show this help message and exit
        -l LINE_LENGTH, --line-length LINE_LENGTH
                              process core assemblies
        -f, --format-files    format generated stub files


## Examples:

    python -m stubgen -o output extract --overwrite mscorlib System System.Core

    python -m stubgen -o stubs build -f output/*_skeleton.json output/*_doc.json

    python -m stubgen --verbose -m -o ../../stubs_output build -f ..\..\output\*_skeleton.json ..\output\*_doc.json

    python -m stubgen --verbose -m -o "C:\repos\CommonDev\Lotus\Cougar\Net\Scripts\DiagnosticsWrappers\Stubs" build -f "C:\repos\CommonDev\Lotus\Cougar\Net\Scripts\DiagnosticsWrappers\StubsSkeletonOutput\*_skeleton.json" "C:\repos\CommonDev\Lotus\Cougar\Net\Scripts\DiagnosticsWrappers\StubsSkeletonOutput\*_doc.json"



    ** must be in: PS C:\Users\zrahman\OneDrive - KLA Corporation\Documents\GitHub\pythonnet-stubs\src\stubgen>

python -m stubgen -o ../output --dll-directory "C:\Users\zrahman\OneDrive - KLA Corporation\Documents\GitHub\pythonnet-stubs\Dlls" extract

python -m stubgen --verbose -m -o ..\..\output\ extract -s "C:\repos\CommonDev\BuildOutputs\Output\Run\Exec\Bin\KLATencor.Lotus.AppLogic.Vacuum.dll"

python -m stubgen -o ..\..\output extract --overwrite -s C:\repos\CommonDev\BuildOutputs\Output\Run\Exec\Bin\KLATencor.eCP.Infras.dll



