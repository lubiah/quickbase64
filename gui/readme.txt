        =====================
            QUICK BASE64
        =====================

A simple and easy to use application which can encode your files
to base64 format and can decode base64 contents back to it's original format.

It's cool auto-detecting feature allows you to encode and decode with ease. Just drop a file, it will detect the mode and perform the action.

MODES
-------
Encode : This mode encodes an object into base64 format.
Decode : This mode decodes an object from base64 format into it's original format.
auto-detect : This mode will automatically set the mode to encode if your file 
needs to be encoded and set the mode to decode if your file needs to be decoded.

HOW TO USE
-------------
1. Set a mode,
NB: If auto-detect is active, it will overide your default mode and choose a mode depending on the type of the object.
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
To overide this feature, select the option 'Save (Give ext.)', this options allows you yourself to generate a filename with your prefered extension.

SETTINGS
-----------

General settings
..................

Default mode: This allows you to set the mode you want on application start.
This mode is very useful if you want to encode or decode a file before opening the application.
The best mode for this is 'auto-detect'. For instance, if the mode is on auto-detect, and you drop a file on Quick Base64's exe, it will determine the mode and encode/decode. This way, the application will start with the results, saving you a bunch of time.

Drop file and work on application start? : This option allows you to disable the ability of a file being encoded or decoded when dropped on Quick Base64's exe while's it's closed. 
If set to 'yes', when a file is dropped on Quick Base64's exe, a command will be executed, command being either encode or decode.
If set to 'no', when a file is dropped on Quick Base64's exe, it will just open the application.

Paths
..............

Output directory : This enables you to specify a default directory, where all encoded/decoded files will be saved.

Temporary file directory : This allows you to specify the temporary directory Quick Base64 will use.
Whenever you close Quick Base64, the temporary files are deleted, but on a case of an application crash, these temporary files, wont be deleted and they will occupy space.
When you specify the temporary directory, it gives you more control of the temporary files.

HOW TO COPY RESULTS
---------------------
Quick Base64 provides you three ways in which you want to recieve the results.

1. Copy
This option just copies the raw contents to your clipboard.

2. Copy (HTML)
NB: This only works if mode is set to encode AND file's type is either a picture, audio or video.
Do note that this will copy the results including the html tag to your clipboard.
example:
picture => <img src="data:image/extension_type;base64, base64_contents">
audio => <audio controls src="data:audio/extension_type;base64, base64_contents">
video => <video controls src="data:video/extension_type;base64, base64_contents"></video>

3. Copy (CSS)
This option only works for images. IN CSS, you can use a base64 encoded image as the background-image of an element.
Quick base64 will provide the results in the following syntax.
url("data:image/image_type;base64,base64_contents")
======================================================================================
Report bugs to support@eakloe.com or make an issue on github at github.com/biah/quickbase64