#!/usr/bin/env python3

import Agunua

import pytest

import datetime

def test_arguments():
    with pytest.raises(Agunua.WrongParameters):
        me = Agunua.GeminiUri("gemini://gemini.bortzmeyer.org/", force_ipv4=True, force_ipv6=True)
    with pytest.raises(Agunua.WrongParameters):
        me = Agunua.GeminiUri("gemini://gemini.bortzmeyer.org/", parse_content=True, binary=True)
    with pytest.raises(Agunua.WrongParameters):
        me = Agunua.GeminiUri("gemini://gemini.bortzmeyer.org/", clientcert="foo/bar")
                       
def test_mycapsule():
    me = Agunua.GeminiUri("gemini://gemini.bortzmeyer.org/")
    assert me.network_success and me.status_code == "20"
    
def test_referencesite():
    me = Agunua.GeminiUri("gemini://gemini.circumlunar.space/", insecure=True) # Self-signed certificate
    assert me.network_success and me.status_code == "20"

def test_invalid():
    me =  Agunua.GeminiUri("gemini://gemini.invalid")
    assert not me.network_success

def test_meta():
    me = Agunua.GeminiUri("gemini://gemeaux.bortzmeyer.org/")
    assert me.network_success and me.status_code == "20" and me.mediatype == "text/gemini" and me.lang == "fr"

def test_tls():
    # Anyone knows an old capsule with only 1.2?
    #me = Agunua.GeminiUri("gemini://gemeaux.bortzmeyer.org/")
    #assert me.network_success and me.tls_version == "TLSv1.2"
    me = Agunua.GeminiUri("gemini://gemini.circumlunar.space/", insecure=True)
    assert me.network_success and me.tls_version == "TLSv1.3"

# 2021-11-28: test removed, see https://framagit.org/bortzmeyer/agunua/-/issues/50
# You can test the servers with 'gnutls-cli --insecure -p 1965
# gemini.circumlunar.space' and check for a "Peer has closed the
# GnuTLS connection" at the end. If you get "*** Fatal error: The TLS
# connection was non-properly terminated. *** Server has terminated
# the connection abnormally.", it means the server did not return a
# TLS close notify.
#def test_close_notify():
#    # Obviously, this test will have to be modified when these capsules will upgrade to newer versions
#    me = Agunua.GeminiUri("gemini://gemeaux.bortzmeyer.org/", get_content=True) # gemserv doesn't send the close_notify
#    assert me.network_success and me.no_shutdown
#    me = Agunua.GeminiUri("gemini://gemini.circumlunar.space/", get_content=True, insecure=True) # MollyBrown does it
#    assert me.network_success and not me.no_shutdown
    
def test_certificate():
    me = Agunua.GeminiUri("gemini://gemeaux.bortzmeyer.org/")
    assert me.network_success and me.status_code == "20" and \
        me.cert_not_after > datetime.datetime.now() + datetime.timedelta(days=3)
    
def test_content():
    me = Agunua.GeminiUri("gemini://gemini.bortzmeyer.org/presto/", get_content=True)
    assert me.network_success and me.status_code == "20" and "Solar Influences Data analysis Center" in me.payload
    me = Agunua.GeminiUri("gemini://gemini.bortzmeyer.org/presto/", get_content=False)
    assert me.network_success and me.status_code == "20" and me.payload is None
    
def test_iri():
    me = Agunua.GeminiUri("gemini://gémeaux.bortzmeyer.org/café.gmi")
    assert me.network_success and me.status_code == "20"    
    me = Agunua.GeminiUri("gemini://café.mozz.us/files/𝒻𝒶𝓃𝒸𝓎.txt", insecure=True)
    assert me.network_success and me.status_code == "20"

# For all tests with a wrong name or a literal IP address, it
# currently (2021-11-29) fails since Stargazer closes abruptly the TLS
# session instead of returning a Gemini error code (typically 53)
# <https://todo.sr.ht/~zethra/stargazer/25>. TODO

def test_wrong_name():
    me = Agunua.GeminiUri("gemini://radia.bortzmeyer.org/")
    assert not me.network_success

def test_insecure():
    me = Agunua.GeminiUri("gemini://radia.bortzmeyer.org/", insecure=True)
    assert me.network_success

def test_connect_to():
    me = Agunua.GeminiUri("gemini://gemini.bortzmeyer.org/", connect_to="radia.bortzmeyer.org")
    assert me.network_success

# 2022-07-21 Test disabled since Stargazer sends a fatal TLS alert
# when using raw IP addresses as SNI :-(
#def test_literal_addresses():
    # These are today's (2021-04-17) addresses of
    # gemini.bortzmeyer.org. Obviously, the certificate will appear
    # wrong, hence the insecure=True.
#    me = Agunua.GeminiUri("gemini://193.70.85.11/", insecure=True)
#    assert me.network_success
#    me = Agunua.GeminiUri("gemini://[2001:41d0:302:2200::180]/", insecure=True)
#    assert me.network_success
#def test_literal_addresses_and_ports():
    # These are today's (2021-04-17) addresses of
    # gemini.bortzmeyer.org. Obviously, the certificate will appear
    # wrong, hence the insecure=True.
#    me = Agunua.GeminiUri("gemini://193.70.85.11:1965/", insecure=True)
#    assert me.network_success
#    me = Agunua.GeminiUri("gemini://[2001:41d0:302:2200::180]:1965/", insecure=True)
#    assert me.network_success

def test_links():
    me = Agunua.GeminiUri("gemini://gemini.bortzmeyer.org/", parse_content=True)
    assert "gemini://gemeaux.bortzmeyer.org/" in me.links

def test_size():
    size = 30
    me = Agunua.GeminiUri("gemini://gemini.bortzmeyer.org/", get_content=True, binary=True, maxsize=size)
    assert len(me.payload) == size
    me = Agunua.GeminiUri("gemini://gemeaux.bortzmeyer.org/valleuse-antifer.jpg", get_content=True, maxsize=None)
    assert me.size == 2414113
    assert len(me.payload) == 2414113
    me = Agunua.GeminiUri("gemini://gemeaux.bortzmeyer.org/valleuse-antifer.jpg", get_content=True, maxsize=1000)
    assert me.size == 1000
    me = Agunua.GeminiUri("gemini://gemeaux.bortzmeyer.org/test-size.gmi", get_content=True, binary=True) # If
    # we retrieve as text, end-of-lines may be different. See issue
    # #42.
    assert me.size == 111
    assert len(me.payload) == 111
    me = Agunua.GeminiUri("gemini://gemeaux.bortzmeyer.org/test-size.gmi", get_content=True, maxlines=2)
    assert me.size < 111 # See also issue #42.

def test_mime():
    me = Agunua.GeminiUri("gemini://gemini.bortzmeyer.org/software/")
    assert me.mediatype == "text/gemini"
    me = Agunua.GeminiUri("gemini://gemeaux.bortzmeyer.org/valleuse-antifer.jpg")
    assert me.mediatype == "image/jpeg"
    
def test_decoding():
    # 2022-07-21 decoding error. They changed the encoding?
    # me = Agunua.GeminiUri("gemini://egsam.glv.one/3.3/utf-16le", get_content=True, binary=False)
    #assert me.network_success and me.binary and me.error != ""
    me = Agunua.GeminiUri("gemini://gemini.spam.works/mirrors/textfiles/anarchy/werehere.mad", get_content=True, binary=False)
    assert me.binary and me.error != ""

def test_client_certificate():
    # 2022-07-21 down :-(
    #me = Agunua.GeminiUri("gemini://xj-ix.luxe:1969/bin/fingerprint", insecure=True,
    #                      get_content=True,
    #                      clientcert="sample-cert-user.pem",
    #                      clientkey="sample-key-user.pem")
    #assert me.network_success and "cn=User" in me.payload
    # 2022-07-21 down :-(
    #me = Agunua.GeminiUri("gemini://ondollo.com/internal/test?showCert", insecure=True,
    #                       get_content=True,
    #                      clientcert="sample-cert-user.pem",
    #                      clientkey="sample-key-user.pem")
    #assert me.network_success and "User:" in me.payload
    assert True # As long as we don't find a capsule with client certificate testing
