# CRUISE: CRUcivirus Iteron SEarch tool
Adam R. Jones, George W. Kasun, Nacho de la Higuera, Ken M. Stedman

In preparation for [*Microbiology Resource Announcements*](mra.asm.org)

---

*Cruciviruses* are unique ssDNA viruses with capsid genes that are homologous to RNA virus capsid genes, and replication protein genes that are homologous to DNA virus replication protein genes. The apparent hybrid nature of crucivirus genomes suggests recombination between DNA and RNA viruses. Iterons are short sequence repeats near stem-loop structures at the genomes' origin of replication. Iterons are involved in the replication process and are hypothesized to play a role in recombination events. Iteron identification is essential for the analysis of crucivirus genomes, and critical for the design of experiments aimed at investigating the origin of cruciviruses. The CRUcivirus Iteron SEarch (CRUISE) tool searches for iterons in crucivirus genomes.

CRUISE, written in Python 3, can be parameterized with iteron lengths, distance from nonanucleotide sequence, distance between repeats, number of repeats, and a database of previous known iterons. The tool is designed for integration with Geneious, importing crucivirus genome sequences and exporting the same sequences annotated with iteron candidates. CRUISE was applied to a database of 508 recently-discovered crucivirus genomes[1] with stem-loop structures, and 1275 iteron candidates were found in 487 genomes. Alternatively, without an iteron sequence database, CRUISE identified 893 novel iteron candidates in 475 genomes.

To our knowledge, no tool is currently available that can predict ssDNA iteron candidates, or even ssDNA origin-of-replication sites in general. CRUISE provides a novel way to automate an important part of ssDNA genome annotation. In fact, the process CRUISE uses is not limited to crucivirus genomes, but can be adapted to any cressDNA virus genome. We plan on making this tool publicly available along with a stem-loop structure identifying tool developed by another member of the lab, which should help other ssDNA researchers in genome analysis.

[1]: de la Higuera et. al., *mBio*, 2020