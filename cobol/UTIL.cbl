IDENTIFICATION DIVISION.                                   
PROGRAM-ID.     UTIL.                                      
                                                           
DATA DIVISION.                                             
   LINKAGE SECTION.                                        
   COPY STUDCPY.                                           
PROCEDURE DIVISION USING WS-STUDENT-ID, WS-STUDENT-NAME.   
    DISPLAY 'IN RAMAUD PROGRAM'.                           
    EXIT PROGRAM.                                          
