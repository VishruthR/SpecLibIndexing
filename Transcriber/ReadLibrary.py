"""
Author: Vishruth Raj
"""

#Imports necessary libraries
from SpectralLibrary import SpectralLibrary
import argparse

#Creates a parser
parser = argparse.ArgumentParser( description = 'Enter in the file to read, file to write to, and all the columns, separated by spaces.' )

#Adds the argument to the parser
parser.add_argument( 'Inputs', 
                     metavar = 'N', 
                     type = str, 
                     nargs = '+', 
                     help = 'Reads from file and then writes into another file using the entered columns' )

#Creates a list of arguments which will be stored in appropriate variables later
args = parser.parse_args()

#Stores the file name in a variable
fileName = args.Inputs[ 0 ]

#Stores the name of the file to write into in a variable
fileNameWrite = args.Inputs[ 1 ]

#Removes unnecessary elements from the list
args.Inputs.remove( fileName )
args.Inputs.remove( fileNameWrite )

#Stores the columns into a list
columns = args.Inputs

#Creates an instance of the SpectralLibrary object, passing the variable that holds the file name
library = SpectralLibrary( fileName );

#Calls the SpectralLibrary's read method and stores the result in a list
spectrumList = library.read()

#Calls the library's write() method passing on the spectrumList
library.write( spectrumList, columns, fileNameWrite )

