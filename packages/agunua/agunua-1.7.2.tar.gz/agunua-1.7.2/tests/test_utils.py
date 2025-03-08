#!/usr/bin/env python3

import netaddr

import Agunua.utils

def test_ip_address():
    assert Agunua.utils.is_valid_ip_address("192.0.2.1") == (True, 4)
    assert Agunua.utils.is_valid_ip_address("2001:db8::fada") == (True, 6)
    assert not Agunua.utils.is_valid_ip_address("101.1:3")[0]
    assert not Agunua.utils.is_valid_ip_address("foobar.example")[0]

def test_canonicalize():
    assert Agunua.utils.canonicalize("FOOBAR.Example") == "foobar.example"
    assert Agunua.utils.canonicalize("CAFÉ.Example") == "xn--caf-dma.example"
    
