from audioop import findfactor
import os
import cruise as cruise
import args
import time


start = time.time()
a = args.parser.parse_args()

Total = 0
FileCount = 0
totalFileCount = 0
RealTotal = 0
IteronCount = 0

def inputConvert(inputFastaFile,inputGFF,inputFolder):
    inputFasta = open(inputFastaFile, 'r')
    sequence = True
    fastaDict = {}
    for line in inputFasta:
        if ">" in line:
            name = line[1:-1]
        else:
            sequence = line.strip()
            fastaDict.update({name:sequence})
    inputGFF = open(inputGFF,'r')
    for name in fastaDict:
        with open(inputFolder + name + ".gff", 'w') as fout:
            sequence = fastaDict[name]
            fout.write("##gff-version 3\n##source-version geneious 2020.1.2\n##sequence-region\t")
            fout.write(name + "\t1\t" + str(len(sequence)+1) + "\n")
            fout.write(name + "\tGeneious\tregion\t1\t" + str(len(sequence)+1) + "\t.\t+\t0\tIs_circular=true\n")
            for line in inputGFF:
                if name in line:
                    thisline = line.replace("   ","\t")
                    fout.write(thisline)
                else:
                    break
            fout.write("##FASTA\n>" + name + "\n")
            fout.write(sequence)
         
def outputConvert(outputFolder, outputGFF,outputAnnotations):
    annotationSourceList = outputAnnotations.split(" ")
    positionIndex = int(annotationSourceList[0])
    if positionIndex == -1:
        filter = False
    elif positionIndex not in range(1,10):
        print("Annotations filter argument is faulty! Preserving all annotations")
        filter = False
    else:
        filter = True
    annotationSourceList.pop(0)
    with os.scandir(outputFolder) as folder:
        with open(outputGFF,'w') as output:
            for entry in folder:
                if entry.name.endswith('.gff') and entry.is_file():
                    fin = open(entry.path,'r')
                    start = False
                    for line in fin:
                        if "##FASTA" in line:
                            break
                        elif "##sequence-region" in line:
                            start = True
                        elif start == True:
                            if filter == True:
                                featureList = line.split()
                                featureOfInterest = featureList[positionIndex-1]
                                if featureOfInterest in annotationSourceList:
                                    output.write(line)
                            else:
                                output.write(line)

#replace a.inputFolder and a.outputFolder w constants

#ghost folders for internal operation
internalFolder = "internal/"
inputFolder = internalFolder + "gff-split-inputs/"
outputFolder = internalFolder + "gff-split-outputs/"
try:
    os.makedirs(inputFolder)
except OSError:
    print("Folder 'internal/gff-split-inputs' exists, delete it or modify internal folders")
try:
    os.makedirs(outputFolder)
except OSError:
    print("Folder 'internal/gff-split-outputs' exists, delete it or modify internal folders")

inputConvert(a.inputFasta,a.inputGFF,inputFolder)
with os.scandir(inputFolder) as folder:
    directory = os.getcwd()
    inputFolder = directory + "/" + inputFolder #creating same object twice
    for entry in folder:
        if entry.name.endswith('.gff') and entry.is_file():
            outputFile = cruise.getOutputFile(entry, outputFolder)

            #print(f"\nInput file:  {inputFolder + entry.name}")
            #print(f"Output file: {outputFile}")

            Data = cruise.findPosIterons(
                inputFolder + entry.name, 
                outputFile, 
                a.minLength, 
                a.maxLength,
                a.range,
                a.wiggle,
                a.rank,
                a.numberTopIterons,
                a.maxScore,
                a.goodLength,
                a.doStemLoop,
                a.doKnownIterons,
                a.maxDist,
                a.bestDist,
                a.scoreRange
            )

            if not Data == None:
                foundIterons = Data[0]
                newIteronCount = Data[1]
                totalFileCount += 1
            else:
                foundIterons = False
                newIteronCount = 0

            if not (foundIterons == False or foundIterons == 0):
                FileCount += 1
            IteronCount += newIteronCount

            #     Total += stats[0]
            #     RealTotal += stats[1]
            #     FileCount += 1
            # for x in stats:
            #     print(x.sequence, x.positions, x.score)

outputConvert(outputFolder,a.outputGFF,a.outputAnnotations)

with os.scandir(inputFolder) as folder:
    for file in folder:
        os.remove(file)

with os.scandir(outputFolder) as folder:
    for file in folder:
        os.remove(file)

os.rmdir(inputFolder)
os.rmdir(outputFolder)
os.rmdir(internalFolder)

print("\nDone: " + str(IteronCount) +
      " iteron candidates found in " + str(FileCount) +
      " out of " + str(totalFileCount) +
      " genomes (" + str(round(100*FileCount/totalFileCount, 3)) + "%)")

# if not a.rank:
#     print("Average Number of Candidates: " + str(Total/FileCount))
#     print("Average Number of Real Candidates: " + str(RealTotal/FileCount))

end = time.time()
print(str(round(end-start, 3)) + " seconds elapsed")
