      IDENTIFICATION DIVISION.                      
      PROGRAM-ID.     MAIN.                         
                                              
      DATA DIVISION.                                
      WORKING-STORAGE SECTION.                   
       COPY STUDCPY.                              
      PROCEDURE DIVISION.                           
      CALL 'UTIL' USING BY CONTENT WS-STUDENT-ID
                BY CONTENT WS-STUDENT-NAME.   
      DISPLAY 'STUDENT FID:' WS-STUDENT-ID       
      DISPLAY 'STUDENT-FNAME:' WS-STUDENT-NAME   
      STOP RUN.                                 
