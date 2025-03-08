#!/usr/bin/env python3

from Agunua import parse_text

def test_empty():
    assert parse_text("") == []
    
def test_nolinks():
    assert parse_text("""
# Title

Text
""") == []

def test_relative_with_query():
    assert parse_text("""With a query

=> target?thing=stuff
""",  url="gemini://test.example/dir/file") == ["gemini://test.example/dir/target?thing=stuff"]

def test_bug_merging_query():
    assert parse_text("""Without a slash after the hostname

=> /post/180
""",  url="gemini://test.example?page=0") == ["gemini://test.example/post/180"]

def test_absolute_links():
    assert parse_text("""
# Title

Text => gemini://MUSTNOTAPPEAR.example/ Not a real link

=> gemini://gemini.circumlunar.space/ Real link

=> https://www.afnic.fr/ Web link

=>gemini://empty.example/ No space

=>     gemini://something.example/gaz A lot of spaces

=> gemini://gémeaux.bortzmeyer.org/thé IRI

=> gemini://xn--gmeaux-bva.bortzmeyer.org/caf%C3%A9 URI to transform in IRI

""") == ["gemini://gemini.circumlunar.space/", "gemini://empty.example/", "gemini://something.example/gaz",
         "gemini://gémeaux.bortzmeyer.org/thé",
         "gemini://gémeaux.bortzmeyer.org/café"]

def test_relative_links():
    assert parse_text("""

=> foo.gmi

=> ../foo.gmi

=> ./foo.gmi

=> ././././foz.gmi

=> ../../../../foo.gmi

=> /foo.gmi

=> .

=> ..

""", url="gemini://test.example/dir/file") == ["gemini://test.example/dir/foo.gmi",
                                               "gemini://test.example/foo.gmi",
                                               "gemini://test.example/dir/foo.gmi",
                                               "gemini://test.example/dir/foz.gmi",
                                               "gemini://test.example/foo.gmi",
                                               "gemini://test.example/foo.gmi",
                                               "gemini://test.example/dir",
                                               "gemini://test.example"]

# Bug #12
def test_link_last_line():
    assert parse_text("""
# Title

=> gemini://foobar.example/ Last""") == ["gemini://foobar.example/"]
    
# Bug #16
def test_broken_url():
    assert parse_text("""
# Title

=> gemini://[illegaldrugs.net/cgi-bin/motm](http://illegaldrugs.net/cgi-bin/motm/boards
""") == []
    
def test_empty_link():
    assert parse_text("""
# Title

=> 
""", url="gemini://test.example/") == [] # Must be ignored
    
def test_repeated_link():
    assert parse_text("""
# Title

=> gemini://foobar.example/ One
=> gemini://foobar.example/ Two
   
""") == ["gemini://foobar.example/"]
    
# Bug #19
def test_iri():
    assert parse_text("""

=> café.gmi Link for IRI
=> caf%C3%A9%20th%C3%A9 Link percent-encoded
""", url="gemini://gémeaux.bortzmeyer.org/") == ["gemini://gémeaux.bortzmeyer.org/café.gmi",
                                                 "gemini://gémeaux.bortzmeyer.org/café thé"]

# Bug #26
def test_preformatted():
    assert parse_text("""

=> ok.gmi

```
This is preformatted

=> error.gmi Must be ignored
```

=> ok2.gmi
""", url="gemini://gem.example/") == ["gemini://gem.example/ok.gmi",
                                      "gemini://gem.example/ok2.gmi"]
    
    
