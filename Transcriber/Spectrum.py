"""
Author: Vishruth Raj
"""

#Imports necessary libraries
import re

#A class that holds data for each spectrum that is read from the SpectralLibrary class
class Spectrum:
    #Initializes all the necessary data stores
    attributes = {}
    peakList = []
    allSpecs = []
    
    #A parse method that takes a buffered list of lines and parses them into one dictionary and one list
    def parse( self, buffList ):
        #Sets a boolean flag variable
        flag = True
        
        #Resets attributes
        self.attributes = {}
        
        #Loops through each line in the buffered list
        for line in buffList:
            #Checks if the flag is true    
            if flag:
                #Sets key-value variables using the split() method, splits only by colon and only splits once               
                key, value = re.split( ":", line, 1 )
                
                #Adds the key-value pair to the dictionary
                self.attributes[ key ] = value
                
                #Checks if the key is a certain value
                if key == "Num peaks":
                    #Changes the flag to false
                    flag = False
                    
                #Checks if key is equal to another value
                if key == "Comment":
                    #Splits the comment values properly
                    commentItems = re.split( ",\D| ", value )
                    
                    #Runs through each comment in the commentItems list
                    for comment in commentItems:
                        #Checks if the length of comment is over two and if when it is split it has two elements in the list
                        if len( comment ) >= 2 and ( len( comment.split( "=" ) ) == 2 ):
                            #Splits each comment one more time
                            commentKey, commentValue = comment.split( "=" )
                        
                            #Store the key-value pair in the dictionary
                            self.attributes[ commentKey ] = commentValue
                    
            #If the flag is not true checks if the flag is false
            elif not flag:
                #Splits the line
                mz, intensity, interpretations = line.split( "\t" )
                
                #Adds the values into the list
                self.peakList.append( [ mz, intensity, interpretations ] )
        
        #Adds the peak list to the attributes dictionary then returns the attributes dictionary
        self.attributes[ "Peaks" ] = self.peakList        
        
        #Adds the attributes to the list of spectrums
        self.allSpecs.append( self.attributes )