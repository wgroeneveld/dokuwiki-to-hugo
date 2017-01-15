# dokuwiki-to-hugo

A DokuWiki to Hugo file exporter to quickly migrate your existing PHP wiki to Hugo

See https://www.dokuwiki.org/wiki:syntax

**How do I run this thing?**

Main wiring in `DokuWikiToHugo` - see the tests for an elaborate example.

```python
      DokuWikiToHugo().doku_to_hugo('some_dokuwiki_root_dir')
```

This generates files in a new folder called 'output' with the same directory structure.

## TOML File headers

Every converted file contains a TOML header with:

* datestamp - looking at the file modified date (transfer from your FTP using 'keep timestamps' option)
* draft automatically set to false
* tags: every subfolder is a tag, including the name of the file
* title: name of the file

See `test_hugo_file_config.py` for an example.

## Following Dokuwiki syntax converted:

### general

Things that needed some conversion:

* code, file, inlinecode with single quotes
* italic, strikethrough
* headings with equal sign
* linebreaks (double backslash) are at this moment replaced with HTML BRs.
* ordered lists using dash to markdown
* emoji following this cheat sheet: http://www.webpagefx.com/tools/emoji-cheat-sheet/ - don't forget to enable emoji in your hugo config.

Things that are **the same** anyway:

* horizontal rule (4 slashes VS 3 or more)
* bold stuff using double asteriks
* unordered lists as asteriks
* sub/sup

### embedding HTML

Since Hugo still supports html tags, we don't need to do anything but to remove the `<html/>` tags.

See also the `MarkdownInlineHtml` class in simplestyle module.

### links

Simple internal links are converted to relrefs like `[[mylink]]`. Local links with double colon are replaced by forward slash.

`[[sub:link]]` would become a link to the sub/link article.

If it's a HTTP(S) link, it stays that way.

#### interwiki

You'll have to come up with your own shortcodes for those.

See wp.html in the layouts directory. You could customize interwiki links from dokuwiki: `[[custom>somelink]]` would refer to some custom wiki.
Simply add custom.html and link to the website of your choice. Use Hugo's `{{ index .Params 0 }}` to get the link content.

### I want to create my own syntax conversion!

No problem, the project was made with extensibility in mind.

Simply drop a python script in the markdown submodule folder location and annotate it with the class decorator `@MarkdownConverter.Register`.
That way it's auto-loaded and wired in the main conversion.

## TODO

### styling

* Figure out image links ala http://php.net|{{wiki:dokuwiki-128.png}}
* Tables, should complex ones be supported or can I do a manual convert?
* no formatting (nowiki, %%) - should this just be a pre?

### Not supported and probably will never be

* embedding php - kill it with fire?
* macro's - kill it with fire?
* what to do with footnotes?