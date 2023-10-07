# mandarin
My personal course and research notes on learning Mandarin Chinese.

# LaTeX Setup

Requires support for Mandarin and fonts.  Also uses some packages from CTAN for exercise sheets and other layout.

Note that to list packages for TeX depends on the TeX distro, which in turn can depend on the Linux distro.
For TeX Live installed on Debian, some basic skills with the `tlmgr` (native TeX Live Manager) can be apparently
attractive, but in fact `/usr/share/doc/texlive-base/README.tlmgr-on-Debian.md` recommends avoiding it unless
an independent installation from the upstream TeXLive repo has been installed.  This is because apt packaged
versions of the upstream are designed to work without recourse to the TeX Live internal tools.

TeX packaging is quite complex.

See [overleaf article](https://www.overleaf.com/learn/latex/Articles/An_introduction_to_Kpathsea_and_how_TeX_engines_search_for_files#TeX_engines_don%E2%80%99t_search_for_files%E2%80%A6_really!?)

## TeX Live Internals

TeX Live upstream via tlmgr (not recommended if using apt) will look for system installed (admin installed) packages in TEXMFHOME, and will require sudo privilege 
to install packages in this location for all users.  In `USER MODE` it can manage installations to a separate
location writable by a specific user at a usertree rooted at TEXMFHOME


## Ubuntu 22.04

Using TeX Live 2022 (Debian) pdfTeX version 3.141592653-2.6-1.40.22 with Ubuntu Studio 2022.04 as of 2023-10-06 it was 
necessary to install the following packages to be able to compile the OULC-MT notes I have made.

As per my comments in e.g. `lesson-er.tex` the following packages are recommended to be installed

 ```
# For the CJKutf8 and CJK packages
 sudo apt-get install cjk-all
# For ucs : package installed to /usr/share/texlive/texmf-dist/tex/latex/ucs/ via texlive-latex-extra
sudo apt-get install texlive-latex-extra
#
# For xpinyin
TBA
# For Chou recommended CTAN packages
TBA
```

# Copyright

Module OULC (Oxford University Language Centre)

In the primary content : Oxford University Language Centre, and Dr Wenbing (Wendy) Che specifically.

In the typesetting, addition content, formatting and so forth, Dr. Adam Vercingetorix Stephen.

Module MyWorksheets

In all respects - content, generation, typesetting Dr. Adam Vercingetorix Stephen.


# LICENSE

The pedagogical material in the course notes is Copyright 2018 OULC/Dr Che/Dr Stephen as noted above.   Any scripts, processing logic and the like will be licensed under the LGPL except where use of third party software implies a separate licensing condition.  The license conditions for any specific file in this repository shall be clearly stated within each individual file as a commented copyright and license statement on a per case basis.   When I get around to writing a nice licensing auto-wrapper.  In the meantime - as described above.


