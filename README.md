sling-git
=========

Say you have two git repositories that you want to keep up to date in separate
places for some reason--like, say, Dropbox--and you'll only ever
update one or the other and you'll never want two versions at once.

So basically, you want to sling your git repository from one computer to
another, and then you'll probably want to slang it back. And that's what
sling-git does.

How to Use It
-------------
1. Initialize a bare repository, and clone it in two different places on the same computer (eg, Dropbox and a local copy), `dir1` and `dir2`, say. Add these in the script.
2. Every time you update something in `dir1`, run `sling`; every time you update something in `dir2`, run `sling slang`.
3. A timestamped commit will be made every time in `dir1`, and this commit will be slung to `dir2`.

Specifying `dir1` and `dir2`
----------------------------
1. There's a default.
2. Or run `sling -s dir1 -d dir2` or `sling -s dir1 -d dir2 slang`, depending.
