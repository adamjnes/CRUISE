import argparse

parser = argparse.ArgumentParser(description = 'Search for iterons around CRESS stem-loops in GFF files')

parser.add_argument("--inputFasta",
                    help = "relative path for input FASTA file with all sequences",
                    default = "examples/test.fasta")

parser.add_argument("--inputGFF",
                    help = "relative path for associated input GFF file",
                    default = "examples/out.gff")

parser.add_argument("--outputGFF",
                    help = "relative path for output GFF file",
                    default = "examples/finaloutput.gff")

parser.add_argument("--outputAnnotations",
                    help = "identifiers to selectively preserve annotations, see documentation for details",
                    default = "2 CRUISE")
                    #accepts string of identifiers, space-separated
                    #first value is an integer, -1 to preserve all annotations, 1-9 to preserve based on position index
                    #another default: "2 CRUISE Stem-Loop_Finder Geneious"                    

parser.add_argument("--minLength",
                    help = "Minimum iteron length",
                    type = int,
                    default = 5)

parser.add_argument("--maxLength",
                    help = "Maximum iteron length",
                    type = int,
                    default = 12)

parser.add_argument("--range", \
                    help = "Number of base pairs around nona to search",
                    type = int,
                    default = 65)                    

parser.add_argument("--rank", \
                    help = "Use ranking system",
                    type = bool,
                    default = True)

parser.add_argument("--numberTopIterons",
                    help = "The number of iterons returned in rank order",
                    type = int,
                    default = 5)                    

parser.add_argument("--maxScore",
                    help = "Maximum score allowed for iterons if rank = False",
                    type = int,
                    default = 40)

parser.add_argument("--wiggle",
                    help = "Max difference between iteron length and distance allowed before score detriment",
                    type = int,
                    default = 5)

parser.add_argument("--goodLength",
                    help = "The highest favorable iteron length ",
                    type = int,
                    default = 11)

parser.add_argument("--doStemLoop",
                    help = "Whether to annotate stem-loop repeats",
                    type = bool,
                    default = True)

parser.add_argument("--doKnownIterons",
                    help = "Whether to annotate known iterons",
                    type = bool,
                    default = True)

parser.add_argument("--maxDist", \
                    help = "Maximum allowed distance between iterons",
                    type = int,
                    default = 20)
                    # below may be redundant

parser.add_argument("--bestDist",
                    help = "Optimal maximum distance between iterons",
                    type = int,
                    default = 10)

parser.add_argument("--scoreRange",
                    help = "Score range between outputted candidates (recommended 50)",
                    type = int,
                    default = 50)
