# README #

This repository holds the Nordling Lab Beamer template. It is identical to the PowerPoint and Keynote templates.

It is copyrighted 2018 by Nordling Lab.

## Installation ##

### Mac OS X ###

1. Open a Terminal window.
2. Check where TeXLive want you to install your own packages by issuing: ```kpsewhich -expand-var '$TEXMFHOME'```
3. Change to the folder where TeXLive want you to install your own packages. (If it does not exist, then create it and change to it.)
4. Change to the latex folder: ```cd tex/latex``` (If it does not exist, then create it: ```mkdir -p tex/latex```
5. Clone this GIT repository into the folder: ```git clone git@bitbucket.org:nordlinglab/nordlinglab-template-beamer.git```
6. Update the TeXLive data base: ```texhash```

Now you can use the template.

### Windows 10 ###

1. Open a Command line window.
2. You will need to create a local textmf tree to store the template. A good place to place this directory would be under this address ```C:/localtexmf/tex/latex/```
3. First change your current directory to C: and type on your command prompt ```mkdir localtexmf```
4. Follow by creating the sub tree tex/latex by typing ```mkdir localtexmf/tex``` followed by ```mkdir localtexmf/tex/latex```
5. Change your current directory to the recently created folder by ```cd localtexmf/tex/latex```
5. Clone this GIT repository into the folder: ```git clone https://bitbucket.org/nordlinglab/nordlinglab-template-beamer.git```
6. Open your MiKTeX settings (Admin) and under the Roots tab add the path for the localtexmf folder
6. Refresh the file name database by simply returning to the General tab and clicking on ```Refresh FNDB```

### Linux ###

1. Open a Terminal window.
2. Check where TeXLive want you to install your own packages and change to the folder by issuing: ```cd $(kpsewhich -var-value $TEXMFHOME)```
3. Change to the latex folder: ```cd tex/latex``` (If it does not exist, then create it: ```sudo mkdir -p tex/latex```
4. Clone this GIT repository into the folder: ```sudo git clone https://bitbucket.org/nordlinglab/nordlinglab-template-beamer.git```
5. Update the TeXLive data base: ```sudo texhash```

## Usage ##

To use the template, please, see the example *NordlingLab_template_beamer.tex*, which is found in this GIT repository.

To use the 16:9 template, make sure to change the aspect ratio of your beamer presentation to 16:9 by changing to the line:
```\documentclass[aspectratio=169]{beamer}``` instead of ```\documentclass{beamer}```.
Also change your theme to ```NordlingLab169``` instead of ```NordlingLab```.
