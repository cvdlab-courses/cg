## Example of slide generation using `Mark-Down` and `Pandoc`

*	Create the source file within the directory you are

		$ touch README.md
	
*	Write the file content using any ascii editor

*	Compile your file

		$ pandoc -t beamer --slide-level 2 -V theme:CambridgeUS -s  README.md -o README.pdf 
	
*	In case, look at [`http://pandoc.org/getting-started.html`](http://pandoc.org/getting-started.html)