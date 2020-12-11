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
........................

Output directory : This enables you to specify a default directory, where all encoded/decoded files will be saved.

Temporary file directory : This allows you to specify the temporary directory Quick Base64 will use.
Whenever you close Quick Base64, the temporary files are deleted, but on a case of an application crash, these temporary files, wont be deleted and they will occupy space.
When you specify the temporary directory, it gives you more control of the temporary files.

HOW TO COPY RESULTS
--------------------------------
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

FILE EXTENSIONS
--------------------------
Whenever the application uses the mime type command to generate an extension, it first obtains the mime type,
then it looks inside data.yaml to get the associative extension of the mime type, if the extension for your mime type
is not determined, your file is saved with a '.txt' extension.
Also, you can add the mime type and extension inside the data.yaml file and the application will recognize it.
    Example. If the application doesn't get the extension for your file which has a mime type of "video/avi",
    you can add it to the application by opening 'data.yaml' and adding your extension in this format
    video/avi : .mp4 
After that, you do not need to restart the application, just drop your file again and the application will use the mime type
which you just added.

NB: I will be glad if you submit your "data.yaml" file to me after adding more extensions so I will include them in the next version.
Also, you name will be acknowledged if you contribute.
You can open a pull request at github with the changes you made to the data.yaml file or better still, send the "data.yaml" file to 
support@eakloe.com with your name so I will acknowledge your name in the next version.

Preview mode
================
This mode allows you to view the end results of an encoded or decode file.
If you preview base64 contents with Quick Base64, you will have a view of the original file.
For example, using the preview feature on a base64 encoded image will pop up the original image 
which will be derived from the base64 contents.

Report bugs to support@eakloe.com or make an issue on github at https://www.github.com/biah/quickbase64/issues  