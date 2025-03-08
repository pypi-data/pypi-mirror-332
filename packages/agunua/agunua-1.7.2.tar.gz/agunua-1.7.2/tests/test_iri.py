#!/usr/bin/env python3

from Agunua.urltinkering import uri_to_iri,iri_to_uri
import Agunua

import pytest

def test_trivial_iri():
    assert iri_to_uri("gemini://gémeaux.bortzmeyer.org/café") == "gemini://xn--gmeaux-bva.bortzmeyer.org/caf%C3%A9"

def test_iri_with_query():
    assert iri_to_uri("gemini://gémeaux.bortzmeyer.org/café?plus=thé") == "gemini://xn--gmeaux-bva.bortzmeyer.org/caf%C3%A9?plus=th%C3%A9"

def test_iri_with_fragment():
    assert iri_to_uri("gemini://gémeaux.bortzmeyer.org/café#thé") == "gemini://xn--gmeaux-bva.bortzmeyer.org/caf%C3%A9#th%C3%A9"

def test_already_uri():
    assert iri_to_uri("gemini://gemeaux.bortzmeyer.org/cafe") == "gemini://gemeaux.bortzmeyer.org/cafe"

def test_iri_partially_encoded():
    assert iri_to_uri("gemini://gémeaux.bortzmeyer.org/café%20thé") == "gemini://xn--gmeaux-bva.bortzmeyer.org/caf%C3%A9%20th%C3%A9"

def test_iri_with_several_items_in_path():
    assert iri_to_uri("gemini://gémeaux.bortzmeyer.org/café/chocolat/thé") == "gemini://xn--gmeaux-bva.bortzmeyer.org/caf%C3%A9/chocolat/th%C3%A9"
    
def test_iri_with_port():
    assert iri_to_uri("gemini://gémeaux.bortzmeyer.org:666/café") == "gemini://xn--gmeaux-bva.bortzmeyer.org:666/caf%C3%A9"

def test_iri_literal_ipv4():
    assert iri_to_uri("gemini://192.0.3.1/café") == "gemini://192.0.3.1/caf%C3%A9"

def test_iri_literal_ipv4_with_port():
    assert iri_to_uri("gemini://192.0.3.1:666/café") == "gemini://192.0.3.1:666/caf%C3%A9"

def test_iri_literal_ipv6():
    assert iri_to_uri("gemini://[2001:db8::deca]/café") == "gemini://[2001:db8::deca]/caf%C3%A9"

def test_iri_literal_ipv6_with_port():
    assert iri_to_uri("gemini://[2001:db8::deca]:666/café") == "gemini://[2001:db8::deca]:666/caf%C3%A9"

def test_trivial_uri():
    assert uri_to_iri("gemini://xn--gmeaux-bva.bortzmeyer.org/caf%C3%A9") == "gemini://gémeaux.bortzmeyer.org/café"

def test_already_uri():
     with pytest.raises(Agunua.AlreadyIriOrWrongEncoding):
         uri_to_iri("gemini://gémeaux.bortzmeyer.org/café")

def test_slash_encoded():
    assert uri_to_iri("gemini://xn--gmeaux-bva.bortzmeyer.org/caf%C3%A9%2Fsucre") == "gemini://gémeaux.bortzmeyer.org/café/sucre"

def test_uri_with_port():
    assert uri_to_iri("gemini://xn--gmeaux-bva.bortzmeyer.org:666/caf%C3%A9") == "gemini://gémeaux.bortzmeyer.org:666/café"
    
def test_with_spaces():
    assert uri_to_iri("gemini://xn--gmeaux-bva.bortzmeyer.org/caf%C3%A9%20sucre") == "gemini://gémeaux.bortzmeyer.org/café sucre"
    # Spaces are not allowed even in IRI, it should not be done that
    # way. It works as long as we don't parse text containing these
    # IRIs.

def test_queries_with_question_marks():
    # Happens in the real world, see gemini://gus.guru/
    assert uri_to_iri("gemini://gus.guru/v/search/1?%3Fgus.guru/known-feeds") == "gemini://gus.guru/v/search/1?%3Fgus.guru/known-feeds"

# Bug with Molly Brown's redirections when there is no slash after the authority but a query
def test_noslash_query():
    assert(iri_to_uri("gemini://gemini.circumlunar.space?page=0") == "gemini://gemini.circumlunar.space?page=0")
    


