# README

Cruise (**CRU**civirus **I**teron **SE**arch) searches cressDNA virus genomes for iterons.

## Installation

CRUISE is written in Python3. In addition to the default libraries, the gffutils package must be installed:

`$ pip install gffutils`

Choose a working area and clone the CRUISE git repository to your local machine:

`$ git clone https://github.com/adamjnes/CRUISE`

### Folder structure

Source code is in the `src` folder:

- `args.py` CRUISE arguments and default values
- `cruise.py` CRUISE implementation
- `launch.py` CRUISE wrapper and "launch control"

Example GFF files are in the `examples` folder:

- Default folder in `args.py` for reading GFF input files is `gff-inputs`.
- Default folder in `args.py` for writing GFF output files is `gff-outputs`. 
- Expected GFF output files, useful for checking and testing, are in `gff-expected-outputs`.

GFF input and output folders can be overridden in the `args.py` file or on the command line.

Docker files `Dockerfile` and `requirements.txt` are contained at the top level.



## Running CRUISE from the command line

To run CRUISE from the command line, invoke Python from the CRUISE home folder:

`$ python src/launch.py`

To see CRUISE options and default arguments:

`$ python src/launch.py --help`

```
usage: launch.py [-h] [--help]
                [--inputFolder INPUTFOLDER]
                [--outputFolder OUTPUTFOLDER]
                [--minLength MINLENGTH] 
                [--maxLength MAXLENGTH] 
                [--range RANGE] 
                [--rank RANK]
                [--numberTopIterons NUMBERTOPITERONS] 
                [--maxScore MAXSCORE] 
                [--wiggle WIGGLE] 
                [--goodLength GOODLENGTH] 
                [--doStemLoop DOSTEMLOOP]
                [--doKnownIterons DOKNOWNITERONS] 
                [--maxDist MAXDIST] 
                [--bestDist BESTDIST] 
                [--scoreRange SCORERANGE]

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
## Note about StemLoopFinder

CRUISE requires genomes with the stem loop and nonanucleotide sequence annotated. The nonanucleotide should be annotated with the type "nonanucleotide" and the stem loop should be annotated with the type "stem_loop". The program has some flexibility in naming convention but not much. Examples of this annotation format are given in the example .gff input files.



