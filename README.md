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

Test files are in the `examples` folder:

- `test.fasta` is the .fasta file containing the sequences for analysis.
- `out.gff` is the .gff file associated with the above fasta file, containing essential annotations for CRUISE's operation, taken from the output of StemLoop-Finder.
- `finaloutput.gff` is the final output CRUISE produces, with selected annotations controlled through the `args.py` file (see below)

Arguments can be overridden in the `args.py` file or on the command line.

Docker files `Dockerfile` and `requirements.txt` are contained at the top level.



## Running CRUISE from the command line

To run CRUISE from the command line, invoke Python from the CRUISE home folder:

`$ python src/launch.py`

To see CRUISE options and default arguments:

`$ python src/launch.py --help`

```
usage: launch.py [-h] [--help]
                [--inputFasta INPUTFASTA]
                [--inputGFF INPUTGFF]
                [--outputGFF OUTPUTGFF]
                [--outputAnnotations OUTPUTANNOTATIONS]
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
  --inputFasta INPUTFASTA
                        relative path for input FASTA file with all sequences
  --inputGFF INPUTGFF
                        relative path for associated input GFF file
  --outputGFF OUTPUTGFF
                        relative path for output GFF file
  --outputAnnotations OUTPUTANNOTATIONS
                        identifiers to selectively preserve annotations, see documentation for details                                         
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

CRUISE requires genomes with the stem loop and nonanucleotide sequence annotated. As such, the program was designed to work with files processed by a sister program called StemLoopFinder which locates and annotates these structures. CRUISE is still designed to run alone, but requires that the nonanucleotide be annotated with the type "nonanucleotide" and the stem loop be annotated with the type "stem_loop". The program has some flexibility in naming convention but not much. Examples of this annotation format are given in the example .gff input files.

## Note about --outputAnnotations

This argument accepts a specially-formatted string of identifiers, space-separated. The first value is an integer: -1 to preserve all annotations, 1-9 to preserve based on position index. For example, the argument "2 CRUISE Stem-Loop_Finder Geneious" will preserve all annotations with one of those three sources (CRUISE, Stem-Loop_Finder, and Geneious), as source is the value stored in the second position index. See general .gff3 format documentation for all position indeces and their values.



