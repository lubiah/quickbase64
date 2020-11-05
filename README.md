# Quick Base64

Quick Base64 is an application which can convert files into Base64 format.
It can also convert base64 text to it's original format.

When decoding base64 files to it's original format, it uses the [file command](https://en.wikipedia.org/wiki/File_(command)) to determine the mime-type of the data.
It then decodes and write the data according to the mime-type's extension.

It is available in a GUI and a CLI. Currently, it is running on Windows only but I am hoping to compile it on Linux very soon.

## Aim
* Quick Base64 is meant to be fast and easy to use.
* Minimalistic interface but with great features.   

## How it Works
When the application is opened, the mode is set to 'encode' by default.
Then a user will drop a file onto the surface and that will initialize the encoding.
It has no start, encode or decode button. The application only runs when a file is dropped 
onto it's surface.

## How it decodes
When the mode is set to decode, a file can only be decoded if a file is dropped onto it's surface.
Then file is then checked to verify if it's in base64 format. It is rejected if not.
The decoded data is written to a temporary file. Then the *file* command is used on the temporary file to determine the 
type of output file.
It first tries using the command `file  --extension tempoary_file`, if it doesn't get any output.
It finally then tries the comand `file --mime-type temporary_file` to get the mime type. An extension is then
generated from the mime-type.
Then an extension is generated according to the file type and the decoded data is now.

Website : [https://www.eakloe.com/quickbase64](https://www.eakloe.com/quickbase64)
