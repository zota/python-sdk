from zotapaysdk.mg_requests.objects import MGRequestParam


def test_mg_request_pair_general_ok(monkeypatch):
    obj = MGRequestParam("test", "test", 10, True)
    ok, reason = obj.validate()
    assert ok


def test_mg_request_pair_value_length_fail(monkeypatch):
    obj = MGRequestParam("test", "testtesttest", 10, True)
    ok, reason = obj.validate()
    assert not ok


def test_mg_request_pair_required_field_ok(monkeypatch):
    obj = MGRequestParam("test", None, 10, False)
    ok, reason = obj.validate()
    assert ok


def test_mg_request_pair_required_field_fail(monkeypatch):
    obj = MGRequestParam("test", None, 10, True)
    ok, reason = obj.validate()
    assert not ok


def test_mg_request_pair_fields(monkeypatch):
    obj = MGRequestParam("test", "testtesttest", 10, True)
    assert obj.required is True
    assert obj.param_name == "test"
    assert obj.param_value == "testtesttest"
    assert obj.max_size == 10
