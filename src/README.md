== Text Segmentation == 
Date: June 8th, 2023 
Software: Text Segmentation, Version 1.0 
Contact: Mivili Suganthan (613-790-9641) or email: mivili.suganthan@gmail.com 
Author: Mivili Suganthan

== Description == 
This software focuses on text segmentation where a folder path is given 
as input, which is then used to process the photos within the folder. 
The software recognizes text within the images and draws rectangles around 
the borders of each word detected. This software also uses the text recognized 
to write each word detected within an ias file and includes the location of each 
word as well.

== Dependencies == 
Python (Python Software Foundation License)
Pytesseract (Apache License 2.0)
Pillow (HPND License)


== Installation == 
To begin installation unzip the folder and open the TEXT_UI.py file in the directory 
that is desired. Installation requires pytesseract, python 3.11, and python pillow. 
Further instructions on how to install these dependencies on Windows 11 can be found here:
https://acrobat.adobe.com/link/review?uri=urn:aaid:scds:US:12a76aa0-6630-3e0a-aa4a-496101b87c28 
or Installation.pdf file. 

== Drawbacks == 
This software is unable to encode multiple languages within a folder or a png file at once. 
The language that is present within the png files must be specified. For more information on 
which languages are supported through this software and the three language codes for those languages
can be found here: https://tesseract-ocr.github.io/tessdoc/Data-Files-in-different-versions.html

== Credits == 
text_recognition.py: Mivili Suganthan 
TEXT_UI.py: Mivili Suganthan
Work Log Sheet - Mivili Suganthan.pdf: Mivili Suganthan
Research History_References.pdf: Mivili Suganthan
Test History and Status.pdf: Mivili Suganthan
Installation.pdf: Mivili Suganthan
lang_codes.csv: Mivili Suganthan

== License ==
MIT License

Copyright (c) 2023, Mivili Suganthan

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the
\"Software\"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be included
in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
