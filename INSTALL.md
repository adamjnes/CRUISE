# Installation and Usage

Clone the git repository to your local machine:

`git clone https://github.com/adamjnes/CRUISE`

CRUISE reqiurs Python3. In addition to the default libraries, the gffutils package must be installed:

`pip install gffutils`

## Folder structure

The repository is organized as follows:

Docker files `Dockerfile` and `requirements.txt` are contained at the top level.

Source code is in `src`:

- `args.py` default values for CRUISE arguments
- `cruise.py` CRUISE implementation
- `launch.py` wrapper file for CRUISE

Example GFF files are in `examples`:

- GFF files for analysis are in `gff-inputs`.
- The default location for writing GFF output files is `gff-outputs`. 
- Expected GFF output files for checking and testing are in `gff-expected-outputs`.

GFF input and output folders can be overridden in the `args.py` file or on the command line.

## Interfacing with Genious

TBD

## Running CRUISE from the command line

To run CRUISE from the command line, invoke Python from the CRUISE home folder:

`python src/launch.py`

To see CRUISE options and default arguments:

`python src/launch.py --help`

```
usage: launch.py [-h] [--inputFolder INPUTFOLDER] [--outputFolder OUTPUTFOLDER] [--minLength MINLENGTH] [--maxLength MAXLENGTH] [--range RANGE] [--rank RANK]
                 [--numberTopIterons NUMBERTOPITERONS] [--maxScore MAXSCORE] [--wiggle WIGGLE] [--goodLength GOODLENGTH] [--doStemLoop DOSTEMLOOP]
                 [--doKnownIterons DOKNOWNITERONS] [--maxDist MAXDIST] [--bestDist BESTDIST] [--scoreRange SCORERANGE]

Search for iterons around CRESS stem-loops in GFF files

optional arguments:
  -h, --help            show this help message and exit
  --inputFolder INPUTFOLDER
                        Folder to read GFF files
  --outputFolder OUTPUTFOLDER
                        Folder to write GFF files
  --minLength MINLENGTH
                        Minimum iteron length
  --maxLength MAXLENGTH
                        Maximum iteron length
  --range RANGE         Number of base pairs around nona to search
  --rank RANK           Use ranking system
  --numberTopIterons NUMBERTOPITERONS
                        The number of iterons returned in rank order
  --maxScore MAXSCORE   Maximum score allowed for iterons if rank = False
  --wiggle WIGGLE       Max difference between iteron length and distance allowed before score detriment
  --goodLength GOODLENGTH
                        The highest favorable iteron length
  --doStemLoop DOSTEMLOOP
                        Whether to annotate stem-loop repeats
  --doKnownIterons DOKNOWNITERONS
                        Whether to annotate known iterons
  --maxDist MAXDIST     Maximum allowed distance between iterons
  --bestDist BESTDIST   Optimal maximum distance between iterons
  --scoreRange SCORERANGE
                        Score range between outputted candidates (recommended 50)
```
## Running CRUISE in Docker

Docker must be  [installed](https://www.docker.com/products/docker-desktop) on the host. To create a Docker container from the CRUISE home folder:

`docker build --tag cruise .`

To run Docker interactively:

`docker run -it cruise`

This will execute `launch.py` on the default files, writing results *in the docker container*. The the results must be copied from the Docker container back into the host filesystem. See Docker documentation for more information. If you wish to use Docker in a batch mode, you can launch it with the `--mount` option. Replace `<cruise-home-folder>` below with the full path to the CRUISE home folder:

`docker run -it --mount type=bind,source=<cruise-home-folder>\examples\gff-outputs,target=/cruise/test-genomes/output-gff cruise`

On Windows, you can avoid typing the full path with:

`docker run -it --mount type=bind,source=%cd%\examples\gff-outputs,target=/cruise/examples/gff-outputs cruise`

This will run CRUISE on the GFF files in  `examples/gff-inputs` and write new GFF files to `examples/gff-outputs`.






