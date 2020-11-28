      IDENTIFICATION DIVISION.                      
      PROGRAM-ID.     MAIN.                         
                                              
      DATA DIVISION.                                
      WORKING-STORAGE SECTION.                   
       COPY STUDCPY.                              
      PROCEDURE DIVISION.                           
      CALL 'UTIL' USING BY CONTENT WS-STUDENT-ID
                BY CONTENT WS-STUDENT-NAME.   
      DISPLAY 'STUDENT ID:' WS-STUDENT-ID       
      DISPLAY 'STUDENT-NAME:' WS-STUDENT-NAME   
      STOP RUN.                                 
