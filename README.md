# dokuwiki-to-hugo

A DokuWiki to Hugo file exporter to quickly migrate your existing PHP wiki to Hugo

See https://www.dokuwiki.org/wiki:syntax

## Following Dokuwiki syntax converted:

### general

* code, file, inlinecode with single quotes
* bold, italic, sub/sup, strikethrough
* headings with equal sign
* linebreaks (double backslash) are at this moment replaced with HTML BRs.
* unordered lists (already native MD), ordered lists using dash to markdown

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

## TODO

### styling

* Figure out image links ala http://php.net|{{wiki:dokuwiki-128.png}}
* Tables, should complex ones be supported or can I do a manual convert?
* emoticons
* no formatting (nowiki, %%) - should this just be a pre?

### structure

* build file structure - wire everything together
* build header TOML with timestamps, draft false etc

## Not supported and probably will never be

* embedding php - kill it with fire?
* macro's - kill it with fire?
* what to do with footnotes?