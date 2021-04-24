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

with os.scandir(a.inputFolder) as folder:
    for entry in folder:
        if entry.name.endswith('.gff') and entry.is_file():
            outputFile = cruise.getOutputFile(entry, a.outputFolder)

            print(f"\nInput file:  {a.inputFolder + entry.name}")
            print(f"Output file: {outputFile}")

            Data = cruise.findPosIterons(
                a.inputFolder + entry.name, 
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

print("\nDone: " + str(IteronCount) +
      " iteron candidates found in " + str(FileCount) +
      " out of " + str(totalFileCount) +
      " genomes (" + str(round(100*FileCount/totalFileCount, 3)) + "%)")

# if not a.rank:
#     print("Average Number of Candidates: " + str(Total/FileCount))
#     print("Average Number of Real Candidates: " + str(RealTotal/FileCount))

end = time.time()
print(str(round(end-start, 3)) + " seconds elapsed")
