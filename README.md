The acquisition of the melting temperature (Tm) is a straightforward process. 

Nevertheless, this data holds significant importance as it enables us to compare the Tm values of samples with unknown genotypes to those of the "Standards" (samples with known genotypes). This comparative analysis allows us to determine the alleles present in mosquitoes for both positions.

For instance, if a randomly selected sample shows a Tm of 73.3 for position 1016 and 82.9 for position 1534, we can conclude that the mosquito is Sensitive for position 1016 and Resistant for position 1534, as its Tm values resemble the Standard values. Therefore, the genotype of this mosquito would be R1R1.

The objective is to replicate this entire procedure in the developed program (called GENOMOS) so that, by providing the Standard Tm values as a reference point and loading the Tm values of samples with unknown genotypes, the program can determine both the genotype for each position and the resulting genotype for both positions.

GENOMOS is a desktop application that has been entirely developed in the Python programming language, designed with Qt Creator using the PySide2 module. PySide2 is the official Python module of the Qt project. On the other hand, Qt Creator is a cross-platform Integrated Development Environment (IDE) programmed in C++, JavaScript, and QML, developed by Trolltech. This IDE is part of the SDK used for the development of applications with Graphical User Interfaces (GUI). Additionally, SQLite was employed as the database manager. 

To download the project, you can visit the following link:


The program allows the reading of databases in both Excel (.xlsx) and CSV (.csv) formats. To ensure correct data integration and prevent errors in the program, it is necessary for the columns to be arranged in the following order:

Samples of melting temperatures for allele 1016 (with the column name 'temperature_melting_1016').
Samples of melting temperatures for allele 1534 (with the column name 'temperature_melting_1534').
Standard temperature for allele 1016 associated with the 'SS' or sensitive genotype (with the column name 'temperature_melting_1016_SS').
Standard temperature for allele 1016 associated with the 'SR' or heterozygous genotype (with the column name 'temperature_melting_1016_SR').
Standard temperature for allele 1016 associated with the 'RR' or resistant genotype (with the column name 'temperature_melting_1016_RR').
Standard temperature for allele 1534 associated with the 'SS' or sensitive genotype (with the column name 'temperature_melting_1534_SS').
Standard temperature for allele 1534 associated with the 'SR' or heterozygous genotype (with the column name 'temperature_melting_1534_SR').
Standard temperature for allele 1534 associated with the 'RR' or resistant genotype (with the column name 'temperature_melting_1534_RR').

To incorporate this data, simply click on the "Open Data" button. If the column names and their order are correct, a message will appear in the console indicating that the data has been successfully incorporated.

The program provides the option to manually add samples through the 'New Sample' button, edit a sample using the 'Edit Sample' button, and delete samples with the 'Delete Sample' button. Additionally, it is possible to save the data in the input table by selecting 'Save Data', and delete all data from the database with the 'Delete Data' option. To view the results of genotype classification, simply click on the 'Results' button. When accessing the 'Results' interface, we can observe the status for both allele 1016 and allele 1534, along with the resulting genotype. These results can be downloaded in Excel (*xslx) or CSV (*csv) format. In addition to presenting these results, the program also provides the genotype distribution and the allele sum in a pie chart. Both charts are downloadable.




