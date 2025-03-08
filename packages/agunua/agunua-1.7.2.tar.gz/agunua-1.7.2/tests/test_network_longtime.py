#!/usr/bin/env python3

import Agunua

import pytest

def test_unreachable():
    me =  Agunua.GeminiUri("gemini://[2001:db8::1]")
    assert not me.network_success
    me =  Agunua.GeminiUri("gemini://192.0.2.1")
    assert not me.network_success
    me =  Agunua.GeminiUri("gemini://10.1.2.3")
    assert not me.network_success

