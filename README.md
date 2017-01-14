# dokuwiki-to-hugo

A DokuWiki to Hugo file exporter to quickly migrate your existing PHP wiki to Hugo

See https://www.dokuwiki.org/wiki:syntax

## TODO

* Figure out image links ala http://php.net|{{wiki:dokuwiki-128.png}}
* Tables, should complex ones be supported or can I do a manual convert?
* build file structure - wire everything together
* build header TOML with timestamps, draft false etc
* lists
* emoticons
* no formatting (nowiki) - should this just be a pre?
* code hilighting (inline and multiline and downloadable)
* embedding html - remove html tag and done?

## Not supported and probably will never be

* embedding php - kill it with fire?
* macro's - kill it with fire?
* what to do with footnotes?