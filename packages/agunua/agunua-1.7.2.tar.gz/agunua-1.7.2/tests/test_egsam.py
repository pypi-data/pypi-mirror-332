#!/usr/bin/env python3

import Agunua

import pytest

# 0
def test_start():
    me = Agunua.GeminiUri("gemini://egsam.glv.one/0.gmi")
    assert me.status_code == "20"
#1
def test_overview():
    me = Agunua.GeminiUri("gemini://egsam.glv.one/1.gmi")
    assert me.status_code == "20"

# 1.1 Awfully slow (again, the timeout problem)
def disabled_test_transactions():
    me = Agunua.GeminiUri("gemini://invalid.invalid/")
    assert not me.network_success
    me = Agunua.GeminiUri("gemini://pitr.ca/")
    assert not me.network_success
    me = Agunua.GeminiUri("gemini://egsam.glv.one/1.1.write.timeout")
    assert not me.network_success
    me = Agunua.GeminiUri("gemini://egsam.glv.one/1.1.no.close")
    assert not me.network_success

# 1.2
# No test?

# 2
# No test

# 3
def test_responses():
    # We accept bare LF even if the test says no because we're liberal
    me = Agunua.GeminiUri("gemini://egsam.glv.one/3.no.cr", get_content=True)
    assert me.network_success and me.status_code == "20" and me.payload.startswith("Fail if you see this")

# 3.1
def test_responses_headers():
    me = Agunua.GeminiUri("gemini://egsam.glv.one/3.1.bad.status")
    # We don't check statuses' syntax
    assert me.status_code == "hi"
    me = Agunua.GeminiUri("gemini://egsam.glv.one/3.1.no.space")
    assert not me.network_success
    me = Agunua.GeminiUri("gemini://egsam.glv.one/3.1.long.meta")
    assert me.status_code == "20" # TODO or check and raise an error?

# 3.2
def test_status_codes():
    me = Agunua.GeminiUri("gemini://egsam.glv.one/3.2.one.digit")
    assert not me.network_success
    me = Agunua.GeminiUri("gemini://egsam.glv.one/3.2.three.digits")
    assert not me.network_success
    me = Agunua.GeminiUri("gemini://egsam.glv.one/3.2.status.2")
    assert me.status_code == "29" # Invalid status code but we don't care
    me = Agunua.GeminiUri("gemini://egsam.glv.one/3.2.status.9")
    assert me.status_code == "99" # Invalid category, may be we should care

# 3.2.1
def test_input():
    me = Agunua.GeminiUri("gemini://egsam.glv.one/3.2.1.percent")
    assert me.status_code == "10" and me.meta.startswith("Please enter the following: 1% + #x")
    me = Agunua.GeminiUri("gemini://egsam.glv.one/3.2.1.long")
    assert me.status_code == "10" and me.meta.startswith("Please enter the input as instructed") # Too long, should we be pick and reject it?
        
# 3.2.2
def test_success():
    me = Agunua.GeminiUri("gemini://egsam.glv.one/3.2.2.text", get_content=True)
    assert me.status_code == "20" and me.mediatype == "text/plain" and me.payload.startswith("Pass")
    me = Agunua.GeminiUri("gemini://egsam.glv.one/3.2.2.html", get_content=True)
    assert me.status_code == "20" and me.mediatype == "text/html" and me.payload.startswith("<marquee>Pass")
    me = Agunua.GeminiUri("gemini://egsam.glv.one/3.2.2.jpg")
    assert me.status_code == "20" and me.mediatype == "image/jpeg"
    me = Agunua.GeminiUri("gemini://egsam.glv.one/3.2.2.jpg.bad")
    assert me.status_code == "20" and me.mediatype == "image/jpeg"

# 3.2.3
def test_redirect():
    me = Agunua.GeminiUri("gemini://egsam.glv.one/3.2.3.redirect", follow_redirect=False)
    assert me.status_code == "30" and me.meta == "3.2.3.redirect.1"
    me = Agunua.GeminiUri("gemini://egsam.glv.one/3.2.3.redirect", follow_redirect=True, get_content=True)
    assert me.status_code == "20" and me.payload.startswith("Pass")

# 3.2.4 and 3.2.5
def test_failure():
    me = Agunua.GeminiUri("gemini://egsam.glv.one/3.2.4.fail")
    assert me.status_code == "40" and me.meta.startswith("If you see this")
    me = Agunua.GeminiUri("gemini://egsam.glv.one/3.2.5.fail")
    assert me.status_code == "50" and me.meta.startswith("If you see this")

# 3.3
def test_mime():
    me = Agunua.GeminiUri("gemini://egsam.glv.one/3.3/utf-8")
    assert me.status_code == "20" and me.charset == "utf-8"
    me = Agunua.GeminiUri("gemini://egsam.glv.one/3.3/ebcdicatde")
    assert me.status_code == "20" and me.charset == "ebcdicatde"
    # This test is currently (2020-01-07) broken "50 open static/encodings/utf-16.bad.txt: no such file or directory"
    #me = Agunua.GeminiUri("gemini://egsam.glv.one/3.3/utf-16.bad")
    #assert me.status_code == "20" and me.charset == "utf-16"

# 3.4
def test_body():
    me = Agunua.GeminiUri("gemini://egsam.glv.one/3.4.text.unknown", get_content=True)
    assert me.mediatype.startswith("text/") and me.payload.startswith("Pass")

# 4
def test_tls():
    me = Agunua.GeminiUri("gemini://egsam.glv.one/4.gmi", get_content=True)
    assert me.status_code == "20" and me.payload.startswith("# 4 TLS")
    me = Agunua.GeminiUri("gemini://egsam.glv.one/4.gmi", get_content=True, send_sni=False)
    assert not me.network_success
    # 4.1 :
    me = Agunua.GeminiUri("gemini://egsam.glv.one/4.1.gmi", get_content=True)
    assert me.status_code == "20" and me.payload.startswith("# 4.1 Version requirements")

    
