        =====================
            QUICK BASE64
        =====================

A simple and easy to use application which can encode your files
to base64 format and can decode base64 contents back to it's original format.

It's cool auto-detecting feature allows you to encode and decode with ease. Just drop a file, it will detect the mode
and perform the action.


MODES
-------
Encode : This mode encodes an object into base64 format.
Decode : This function decodes an object from base64 format.
auto-detect : This function on it's own set the mode to encode if your file needs to be encoded.
It will also set the mode to decode if your file needs to be decoded. 

HOW TO USE
-------------
1. Set a mode,
NB: If auto-detect is active, it will overide your default mode and choose a mode depending on the object.
2. Drag and drop a file onto the application's left pane, 
the results will appear on the right side pane of the application.

HOW TO SAVE
------------    
The application allows you to save either the encoded or the decoded contents.
After either encoding or decoding, right-click on the right side pane, a pop-up menu will apppear,
select save.

NB: If you are saving a decoded file, the application automatically use the object's mime-type to 
generate an extension for your file, meaning, you don't have to know the file type of the contents
you are decoding.
To overide this feature, select the option 'Save (Give ext.)', this options allows you yourself
to generate a filename with your prefered extension.

SETTINGS
-----------

General settings
..................

Default mode: This allows you to set the mode you want on application start.
This mode is very useful if you want to encode or decode a file without opening the application.
The best mode for this is 'auto-detect'. For instance, if the mode is on auto-detect, and your drop
a file on Quick Base64's exe, it will determine the mode and encode/decode. This way, the application
will start with the results, saving you a bunch of time.

Drop file and work on application start? : This option allows you to disable the ability of a file being encoded or decoded when dropped on Quick Base64's exe while's it's closed. 
If set to 'yes', when a file is dropped on Quick Base64's exe, a command will be executed, command being
either encode or decode.
If set to 'no', when a file is dropped on Quick Base64's exe, it will just open the application.

Paths
..............

Output directory : This enables you to specify a directory where all encoded or decoded files will 
be saved. 

Temporary file directory : This allows you to specify the temporary directory Quick Base64 will use.
Whenever you close Quick Base64, the temporary files are deleted, but on a case of an application crash,
these temporary files, wont be deleted, specifying the temporary folder is useful as it gives you control over the temporary files.

Right-Click Context Menu on Right Panel.
 1. Save
 This option saves the encoded/decoded contents to a file.
 2. Save (Give ext.)
 This option allows you to determine the filename and extension of the file to be saved.
 3. Copy
 Copies the raw decoded/encoded contents to clipboard.
 4. Copy (HTML)
 Converts the encoded results into base64 format which you can embed in html.
 For example, if you encode a file 'picture.png', this option will produce the following 
 results, "data:image/png;base64,base64code".
 NB: The results is already wrapped in quotation marks so when coding it in HTML, 
 just write the tag <img src=(Press Ctrl+V) > to paste the results,
 wrong : <img src = "(Press Ctrl+V)".
 The results is already surrounded in quotation marks so don't specify it or else it work work.
 This option only works for images, videos and audios.
 5. Copy (CSS)
 This works like the Copy (HTML) command. This command converts your base64 contents into a css
 code which you can embed in your css file.
 The results it produces is in this format. => url(data:mime/type;base64, base64contents)
 This command works for files which are images only.

 Right-Click Context Menu on Left Panel.
 1.Load file:
 This option allows you to select a file using the windows file selector dialog.
 2. Clipboard (File):
 This enables you to embed a file which you have copied to clipboard into the application.
 NB: Quick Base64 is able to differentiate between text and files in clipboard.
 3. Clipboard (Text):
 This allows you to embed text in your clipboard into the application.



============================================================================================
Report bugs to support@eakloe.com or make an issue on github at github.com/biah/quickbase64