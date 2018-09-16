"""
Author: Vishruth Raj
"""

#Imports all necessary classes
from Spectrum import Spectrum

#A class that reads a file and passes on data to another class
class SpectralLibrary:
    #Initializes all necessary variables for the class
    fileName = ""
    
    #Creates an initializer method that takes a file name
    def __init__( self, fileName ):
        #Sets the classes own fileName variable
        self.fileName = fileName
        
    #A method that reads all the lines of a file and passes them individually to a Spectrum object
    def read( self ):
        #Initializes a list that holds all of the buffered lines objects
        buffList = []
        
        #Creates a spectrum object with the buffered list 
        spec = Spectrum()
        
        #Opens the file using a with-loop
        with open( self.fileName, "r" ) as file:
            #Runs through the file line-by-line:
            for line in file:
                #Checks if line is empty
                if line in [ '\n', '\r\n' ]:            
                    #Calls the Spectrum objects parse() method passing the buffered list as an argument
                    spec.parse( buffList )
                    
                    #Resets the buffered list
                    buffList = []
                                        
                #If the line is not empty
                else:
                    #Adds the line to the list
                    buffList.append( line )
    
        #Returns the spectrum list
        return spec.allSpecs
    
    #A method that writes each of the objects's attributes from the spectrumList into a .tsv file
    def write( self, spectrumList, columns, fileName ):
        #Opens the file using a with-loop
        with( open( fileName, "w" ) ) as file:            
            #Runs through all of the spectrums in the spectrum list
            for spectrum in spectrumList:                     
                #Adds a new line
                file.write( '\n' )    
                       
                #Runs through all of the columns
                for column in columns:
                    #Gets rid of any new line characters in the string
                    spectrum[ column ] = spectrum[ column ].replace( '\n', '' )
                    
                    #Checks if the column is a key in the dictionary
                    if column in spectrum:
                        #Writes the line 
                        file.write( spectrum[ column ] + "\t\t" )
                        
                    #If the column is not their writes a statement in the file that tells the user
                    else:
                        file.write( "Column not found"  + "\t\t" )