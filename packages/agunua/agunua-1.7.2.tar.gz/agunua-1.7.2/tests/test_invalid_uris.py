#!/usr/bin/env python3

import pytest

import Agunua

# urllib.parse accepts very broken URIs :-(
#def test_parse():
#    with pytest.raises(Agunua.InvalidUri):
#        me = Agunua.GeminiUri("gemini://completey broken / URI /")

def test_notgemini():
    with pytest.raises(Agunua.NonGeminiUri):
        me = Agunua.GeminiUri("https://www.bortzmeyer.org/")

def test_broken_port():
    with pytest.raises(Agunua.InvalidUri):
        me = Agunua.GeminiUri("gemini://gemini.bortzmeyer.org:1:2")

def test_no_brackets():
    with pytest.raises(Agunua.InvalidUri):
        me = Agunua.GeminiUri("gemini://2001:db8::dada/")

def test_noscheme(): # Scheme has to be explicit, we don't use
                     # "gemini" as a default. See #30
    with pytest.raises(Agunua.NonGeminiUri):
        me = Agunua.GeminiUri("gemini.foobar.example")
    with pytest.raises(Agunua.NonGeminiUri):
        me = Agunua.GeminiUri("//gemini.foobar.example/with/path")

    
