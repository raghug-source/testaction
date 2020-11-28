      IDENTIFICATION DIVISION.                      
      PROGRAM-ID.     MAIN.                         
                                              
      DATA DIVISION.                                
      WORKING-STORAGE SECTION.                   
       COPY STUDCPY.                              
      PROCEDURE DIVISION.                           
      CALL 'UTIL' USING BY CONTENT WS-STUDENT-ID
                BY CONTENT WS-STUDENT-NAME.   
      DISPLAY 'STUDENT WID:' WS-STUDENT-ID       
      DISPLAY 'STUDENT-WNAME:' WS-STUDENT-NAME   
      STOP RUN.                                 
