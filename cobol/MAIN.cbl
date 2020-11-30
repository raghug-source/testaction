      IDENTIFICATION DIVISION.                      
      PROGRAM-ID.     MAIN.                         
                                              
      DATA DIVISION.                                
      WORKING-STORAGE SECTION.                   
       COPY STUDCPY.                              
      PROCEDURE DIVISION.                           
      CALL 'UTIL' USING BY CONTENT FS-STUDENT-ID
                BY CONTENT FS-STUDENT-NAME.   
      DISPLAY 'STUDENT FID:' WS-STUDENT-ID       
      DISPLAY 'STUDENT-FNAME:' WS-STUDENT-NAME   
      STOP RUN.                                 
