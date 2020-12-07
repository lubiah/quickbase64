# Quick Base64

-----------------------------------------------------------------

Can I get a star :star: - I would really appreciate it. :smile:

-------------------

 [![Website shields.io](https://img.shields.io/website-up-down-green-red/http/eakloe.com.svg)](http://www.eakloe.com)    [![Github all releases](https://img.shields.io/github/downloads/biah/quickbase64/total.svg)](https://GitHub.com/Biah/quickbase64/releases/)

![](https://forthebadge.com/images/badges/open-source.svg) [![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

[![GitHub forks](https://img.shields.io/github/forks/biah/quickbase64.svg?style=social&label=Fork&maxAge=2592000)](https://GitHub.com/Biah/quickbase64/network/)
[![GitHub stars](https://img.shields.io/github/stars/Biah/quickbase64.svg?style=social&label=Star&maxAge=2592000)](https://GitHub.com/Biah/Quickbase64/stargazers/)

--------------------------------

## *Cool Features*

 ![](readme\auto_detect_gif.gif)

*Quick Base64's auto-detection mode allows the application to automatically detect the mode for your file. It switches the mode to encode if your file needs to be encoded or switches it to decode if your file needs to be decoded.*

![Loading a file with Quick Base64](readme/loading_file.png)

_Many ways to load a file with Quick Base64. You can drop a file, load a file using windows file selector, load a file from your clipboard or even load a text from your clipboard. Just right-click the panel._

![Saving a file with Quick Base64](readme/saving_file.png)

_Also, many ways to save a file, you can let it guess the extension and save it, provide file extension yourself or copy the raw results._

![Coping in HTML/CSS](readme/copy_html_css.png)

_I didn't also forget the web developers, if you encode an image, audio or video, Quick Base64 will allow you to copy the results in HTML or CSS format. For example, copying an encoded image "picture.png" in Copy (HTML) will produce the format "data:image/png;base46,base64contents" . You don't need to tell it that your file is an image/picture/video, it knows. Isn't that cool :cool:"_

Before we get started, let us know what __Base64__ is first.

## What is Base64? 

According to Wikipedia,
> __Base64__ is a group of binary-to-text encoding schemes that represent binary data (more specifically a sequence of 8-bit bytes)
> in  an ASCII string format by translating it into a radix-64 representation. 

## Why do I need to encode in Base64?

* Encoding in base64 allows you to embed binaries in text.

* It ensures that data remains intact without modification during transport.

* Embedding base64 encoded images into your web page, makes the page load faster.

* Enables you to pass complex data over SSH.

  

## What is Quick Base64?

 It is an application which encodes your text and files into base64 format.
Not only can it encode, it can also decode your base64 contents to it's original format. :cool:

As you can see from it's name, it's *Quick*, that's why it's named Quick Base64.

![Screenshot of the application](readme/screenshot.png)

​														__Screenshot of the application__

The application has a minimalistic interface but has great features. The reason is to make it's use simple for normal encoding and decoding, whiles been able to become complex when the need arises.

You might be wondering, "Where is the start, encode or decode button?". The answer is, it has none. So then, how does it encode or decode. The answer is simple, everything is initialized when a file is dropped or loaded into the application.

### How it Works

On application start, the default mode is always set to encode, unless changed by the user.  The magic happens when a file or piece of text is dropped onto it's surface or loaded using the context menu. When an object is dropped or loaded, it first checks the mode to see if it is on encode or decode.

If mode is:
* Encode:

   ​	First of all, it checks to see if the object dropped was a file, folder or text. It displays an error if a folder is dropped.
   
   ​	The contents of the file is read and encoded into Base64 format.
   
   ​	If the encoded data is greater than 20000 bytes, only the first 20000 bytes are displayed. Reason is that, if the data to be displayed is more than that, it causes the application to [hang](https://www.wikipedia.org/wiki/Hang_(computing)).
   
* Decode:

   ​	When an object is dropped, it checks to see if it is a file or folder. An error is raised if object is a folder.

   ​	If the object is a file, it's contents are read. It is then checked, if it is a valid Base64 text.

   ​	If it is, it then decodes the Base64 text. In order to know the file type of the decoded data. It uses the [file]('https://www.en.wikipedia.com/wiki/File_(command)') command to find the file type.

   ​	It first tries the command `file --extension temporary_file` , if it doesn't get the extension from this command. It tries to get the 

   ​	mime-type using the command `file --mime-type temporary_file` . An extension is then generated from the mime-type of the contents.

## Why use Quick Base64?

There are many base64 encoders out there. The reason why Quick Base64 is unique is that:
* It's simple to use.
* Can encode and decode base64 contents.
* It can become complex when you want it to. :wink:

## Donation 

You can donate into my bitcoin account. 

<img src="readme\bitcoin.png" style="zoom: 60%;display:inline;text-align:left" />


