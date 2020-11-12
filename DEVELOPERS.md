# README FOR DEVELOPERS

Readme for developers who want to contribute to Quick Base64. I will be glad if you contribute :wink:        

## Variables

* ```drop_type``` is a variable which stores information about how an object entered the drag area. ie. The left side frame which accepts drop and used for loading.

  ```drop_type``` can be one of, 'file' which shows that a file was dropped, 'load', which means the file was loaded using the right-click load command, 'text' which means a text was dragged onto the application drop area.

* ```results``` is a global variable which contains only encoded and decoded file contents.

## Functions used in the application and their functions.

* copy_to_clipboard :

  Parameters : None

  Use : This function takes text and copies it to clipboard.

  It uses a global variable called  ```results```.  ```results```  mostly contain strings in two types ```bytes & str``` 

  If ```type(results)``` is binary. It is decoded and copied to clipboard. Else if the ```type(results)``` is string,

  It is copied to clipboard without t any changes.

* save_file:

  Parameters : None

  Use : This function saves contents to a text file.

  First of all, it checks the mode to see if it is set to encode or decode.

  If drop_type is one of 'load' or 'file', it means the object has a filename.

  If the mode is set to encode:

  It checks the ```drop_type``` variable.

  * If drop_type is 'load' or 'file', 

    it checks for the value of ```file_path```. ```file_path``` will only contain a value if ```drop_type``` is 'load' or 'file'.

    It then writes the contents of  ```results``` to ```file_path```.
    
  * If drop_type is 'text':
  	It asks the user for a filename with an extension.
  	It then writes the contents of ```results``` to the filename.
    

If the mode is set to decode:
 It uses the same method as encode, but it writes contents in binary mode.
 example.
 ```python
 with open(filename, 'wb') as file:
 	file.write(results)
 ```


​    

* center_app:

  Parameters : master, width, height

  Use : Positions a window in the middle of the screen.

  