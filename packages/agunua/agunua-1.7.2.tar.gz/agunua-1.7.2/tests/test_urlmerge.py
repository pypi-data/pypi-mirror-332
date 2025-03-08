#!/usr/bin/env python3

import sys

BASE_NOPATH = "gemini://capsule.example"
BASE_NOPATH_SLASH = "gemini://capsule.example/"
BASE_SHORTPATH_NOSLASH = "gemini://capsule.example/dir1"
BASE_SHORTPATH_SLASH = "gemini://capsule.example/dir1/"
BASE_LONGPATH_NOSLASH = "gemini://capsule.example/dir1/dir2"
BASE_LONGPATH_SLASH = "gemini://capsule.example/dir1/dir2/"
MYQUERY="test=0"
BASE_WITH_QUERY = "gemini://capsule.example/dir1?%s" % MYQUERY
BASE_WITH_FRAGMENT = "gemini://capsule.example/dir1#nope"
BASE_IRI = "gemini://gémeaux.bortzmeyer.org/"
REFERENCE = "gemini://foo.example.com/bar"
REFERENCE_FRAG = "gemini://foo.example.com/bar#ignoreme"

from Agunua.urltinkering import urlmerge, sanitize, pathmerge

def test_abs_reference():
    assert urlmerge(BASE_SHORTPATH_NOSLASH, REFERENCE) == REFERENCE
    assert urlmerge(BASE_SHORTPATH_NOSLASH, REFERENCE_FRAG) == REFERENCE_FRAG
    
def test_trivial_absolute():
    assert urlmerge(BASE_NOPATH, "/foo.gmi") == "%s/foo.gmi" % (BASE_NOPATH)

def test_trivial_relative():
    assert urlmerge(BASE_NOPATH, "foo.gmi") == "%s/foo.gmi" % (BASE_NOPATH)

def test_network_path(): # RFC 3986, section 4.2. See also issue #44
    assert urlmerge(BASE_NOPATH_SLASH, "//foo.example/thing.gmi") == "gemini://foo.example/thing.gmi"
    
def test_leading_dot():
    assert urlmerge(BASE_NOPATH, "./foo.gmi") == "%s/foo.gmi" % (BASE_NOPATH)

def test_leading_slashdot():
    assert urlmerge(BASE_NOPATH, "/./foo.gmi") == "%s/foo.gmi" % (BASE_NOPATH)

def test_with_query():
    assert urlmerge(BASE_SHORTPATH_SLASH, "foo.gmi?test=true") == "%sfoo.gmi?test=true" % (BASE_SHORTPATH_SLASH)
    
def test_leading_dots_nopath():
    assert urlmerge(BASE_NOPATH, "../foo.gmi") == "%s/foo.gmi" % (BASE_NOPATH)

def test_leading_slashdots_nopath():
    assert urlmerge(BASE_NOPATH, "/../foo.gmi") == "%s/foo.gmi" % (BASE_NOPATH)

def test_shortpath_noslash_absolute():
    assert urlmerge(BASE_SHORTPATH_NOSLASH, "/foo.gmi") == "%s/foo.gmi" % (BASE_NOPATH)

def test_shortpath_noslash_relative():
    assert urlmerge(BASE_SHORTPATH_NOSLASH, "foo.gmi") == "%s/foo.gmi" % (BASE_NOPATH)

def test_leading_dots_shortpath_noslash():
    assert urlmerge(BASE_SHORTPATH_NOSLASH, "../foo.gmi") == "%s/foo.gmi" % (BASE_NOPATH)

def test_shortpath_slash_absolute():
    assert urlmerge(BASE_SHORTPATH_SLASH, "/foo.gmi") == "%s/foo.gmi" % (BASE_NOPATH)

def test_shortpath_slash_relative():
    assert urlmerge(BASE_SHORTPATH_SLASH, "foo.gmi") == "%sfoo.gmi" % (BASE_SHORTPATH_SLASH)

def test_leading_dots_shortpath_slash():
    assert urlmerge(BASE_SHORTPATH_SLASH, "../foo.gmi") == "%s/foo.gmi" % (BASE_NOPATH)

def test_longpath_noslash_absolute():
    assert urlmerge(BASE_LONGPATH_NOSLASH, "/foo.gmi") == "%s/foo.gmi" % (BASE_NOPATH)

def test_longpath_noslash_relative():
    assert urlmerge(BASE_LONGPATH_NOSLASH, "foo.gmi") == "%s/foo.gmi" % (BASE_SHORTPATH_NOSLASH)

def test_longpath_dot():
    assert urlmerge(BASE_LONGPATH_NOSLASH, ".") == "%s" % (BASE_SHORTPATH_NOSLASH)
    assert urlmerge(BASE_LONGPATH_SLASH, ".") == "%s" % (BASE_LONGPATH_NOSLASH)

def test_longpath_dotdot():
    assert urlmerge(BASE_LONGPATH_NOSLASH, "..") == "%s" % (BASE_NOPATH)
    assert urlmerge(BASE_LONGPATH_SLASH, "..") == "%s" % (BASE_SHORTPATH_NOSLASH)

def test_leading_dots_longpath_noslash():
    assert urlmerge(BASE_LONGPATH_NOSLASH, "../foo.gmi") == "%s/foo.gmi" % (BASE_NOPATH)

def test_longpath_slash_absolute():
    assert urlmerge(BASE_LONGPATH_SLASH, "/foo.gmi") == "%s/foo.gmi" % (BASE_NOPATH)

def test_longpath_slash_relative():
    assert urlmerge(BASE_LONGPATH_SLASH, "foo.gmi") == "%sfoo.gmi" % (BASE_LONGPATH_SLASH)

def test_leading_dots_longpath_slash():
    assert urlmerge(BASE_LONGPATH_SLASH, "../foo.gmi") == "%s/foo.gmi" % (BASE_SHORTPATH_NOSLASH)

def test_query_with_abs_path():
    assert urlmerge(BASE_WITH_QUERY, "/foo.gmi") == "%s/foo.gmi" % (BASE_NOPATH)

def test_query_with_abs_path_and_query():
    assert urlmerge(BASE_WITH_QUERY, "/foo.gmi?stuff") == "%s/foo.gmi?stuff" % (BASE_NOPATH)

def test_query_with_rel_path():
    assert urlmerge(BASE_WITH_QUERY, "foo.gmi") == "%s/foo.gmi" % (BASE_NOPATH)

def test_query_with_rel_path_and_query():
    assert urlmerge(BASE_WITH_QUERY, "foo.gmi?stuff") == "%s/foo.gmi?stuff" % (BASE_NOPATH)

def test_fragment_with_abs_path():
    assert urlmerge(BASE_WITH_FRAGMENT, "/foo.gmi") == "%s/foo.gmi" % (BASE_NOPATH)

def test_fragment_with_rel_path():
    assert urlmerge(BASE_WITH_FRAGMENT, "foo.gmi") == "%s/foo.gmi" % (BASE_NOPATH)

def test_iri():
    assert urlmerge(BASE_IRI, "café.gmi") == "%scafé.gmi" % (BASE_IRI)
    
def test_slash_end():
    # Real-world case, at gemini://caolan.uk/weather/
    assert urlmerge("gemini://caolan.uk/weather/", "/weather/ee/") == "gemini://caolan.uk/weather/ee/"

def test_sanitize_simple():
    assert sanitize("/foo/bar") == ("foo/bar", True)
    assert sanitize("foo/bar") == ("foo/bar", False)

def test_sanitize_special():
    assert sanitize("/foo/bar?baz") == ("foo/bar_baz", True)
    assert sanitize("foo/bar$baz") == ("foo/bar_baz", False)

def test_sanitize_unicode():
    assert sanitize("/foo/barré/clé") == ("foo/barré/clé", True)
    assert sanitize("foo/barré/clé") == ("foo/barré/clé", False)

def test_sanitize_dir():
    assert sanitize("/foo/bar/") == ("foo/bar/index.gmi", True)
    assert sanitize("foo/bar/") == ("foo/bar/index.gmi", False)

def test_pathmerge():
    assert pathmerge("gemini.bortzmeyer.org/", "gemini.bortzmeyer.org/foo/bar.gmi", "/") == "../index.gmi"
    assert pathmerge("gemini.bortzmeyer.org", "gemini.bortzmeyer.org/foo/bar.gmi", "/") == "../index.gmi"
    assert pathmerge("gemini.bortzmeyer.org/foo/", "gemini.bortzmeyer.org/foo/bar.gmi", "/") == "index.gmi"
    assert pathmerge("gemini.bortzmeyer.org/", "gemini.bortzmeyer.org/foo.gmi", "/") == "index.gmi"
    assert pathmerge("gemini.bortzmeyer.org/", "gemini.bortzmeyer.org/stuff/foo.gmi", "/bar/baz.gmi") == \
        "../bar/baz.gmi"

def test_pathmerge_dir():
    assert pathmerge("gemini.bortzmeyer.org/", "gemini.bortzmeyer.org/foo.gmi", "bar/") == "bar/index.gmi"

def test_pathmerge_ignore():
    assert pathmerge("gemini.bortzmeyer.org/", "gemini.bortzmeyer.org/foo.gmi", "../bar.gmi") == "../bar.gmi"
    assert pathmerge("gemini.bortzmeyer.org/", "gemini.bortzmeyer.org/foo.gmi", "bar.gmi") == "bar.gmi"
    assert pathmerge("gemini.bortzmeyer.org/", "gemini.bortzmeyer.org/baz/foo.gmi", "bar.gmi") == "bar.gmi"
    assert pathmerge("gemini.bortzmeyer.org/", "gemini.bortzmeyer.org/foo.gmi", "gemini://truc.example/") == \
        "gemini://truc.example/"
    assert pathmerge("gemini.bortzmeyer.org/", "gemini.bortzmeyer.org/presto/", "2021-04-29.gmi") == "2021-04-29.gmi"
    assert pathmerge("gemini.bortzmeyer.org/", "gemini.bortzmeyer.org/presto/index.gmi", "2021-04-29.gmi") == "2021-04-29.gmi"

def test_pathmerge_special():
    assert pathmerge("gemini.bortzmeyer.org/", "gemini.bortzmeyer.org/foo.gmi", "bar.gmi?3") == "bar.gmi_3.gmi"

