# Test json api

import pycws

URL = "http://cws.quaivecloud.com/cws/"

''' The admin accesses the system and prepares a user to support encryption.
To do so, a temporary certificate is generated, saved to cws and passed to the
user. The certificate serves as token so that the user is allowed to set her
initial password.
'''


def test_fetch_members():
    data = pycws.fetch_members(URL, 'admin', 'admin')
    assert len(data['members']) > 0
    assert data["returnCode"] == 200


def test_invite_delete_member():

    data = pycws.fetch_members(URL, 'admin', 'admin', 'test_user')
    assert len(data['members']) == 0
    assert data["returnCode"] == 406

    data = pycws.invite_member(URL, 'admin', 'admin', 'test_user')
    assert data["returnCode"] == 200

    # Now there should be one test user
    data = pycws.fetch_members(URL, 'admin', 'admin', 'test_user')
    assert len(data['members']) == 1
    assert data["returnCode"] == 200

    # reinvite the same user and check that we get a failure
    data = pycws.invite_member(URL, 'admin', 'admin', 'test_user')
    assert data["returnCode"] == 595

    # Clean up again
    data = pycws.delete_member(URL, 'admin', 'admin', 'test_user')
    assert data["returnCode"] == 200

    data = pycws.fetch_members(URL, 'admin', 'admin', 'test_user')
    assert len(data['members']) == 0
    assert data["returnCode"] == 406


''' A user has been informed that he can now upgrade her profile to support
encryption. To do so she has to visit her profile page, agree to the terms,
specify a password and upload her encryption certificate '''
