# md2stie

Site Generator from Markdown files

## Install

    python3 -m venv .
    ./bin/pip install --upgrade pip
    ./bin/pip install -r requirements.txt

## Usage

Puts md files in content directory and run the script.

    md2site run --content=<path_to_content_dir> --output=<path_to_output_dir> --log=<path_to_logs_dir>

ex:

    md2site run --content=./content --output=./output --log=./logs

## Disclaimer:

This is a small system that I wrote to manage my documentation, there is not much support for css and the like, I'm making it public just in case it could be of use to someone but without any guarantees.
To modify the result it is necessary to edit the layout.html file.
Happy coding.
