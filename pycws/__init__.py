# module
# from zeep import Client. # needed for SOAP
import requests
import json
# import hashlib
# import datetime
import base64
import urlparse
import logging

logger = logging.getLogger(__name__)


def _member_by_user(url, login, pw, user):
    member_id = '__invalid_user_id__'
    members = fetch_members(url, login, pw)
    member_data = [x for x in members['members'] if x['accountName'] == user]
    if len(member_data) == 1:
        member_id = member_data[0]['memberId']
    elif len(member_data) == 0:
        logger.warning("No user found")
    else:
        logger.warning("More than one user found. This should not be possible")
    return member_id


def invite_member(url, login, pw, user):
    logger.info('Invite member %s' % user)
    endpoint = urlparse.urljoin(url, 'members/inviteMember')
    data = dict(accountName=login,
                credential=base64.b64encode(pw),
                newAccountName=user)
    headers = {'Content-type': 'application/json',
               'Accept': 'application/json'}
    response = requests.post(endpoint, data=json.dumps(data), headers=headers)
    logger.info(response.text)
    return json.loads(response.text)


def fetch_members(url, login, pw, user=None):
    logger.info('Fetch members')
    endpoint = urlparse.urljoin(url, 'members/fetchMembers')
    data = dict(accountName=login,
                credential=base64.b64encode(pw))
    if user is not None:
        member_id = _member_by_user(url, login, pw, user)
        data['memberId'] = member_id

    headers = {'Content-type': 'application/json',
               'Accept': 'application/json'}
    response = requests.post(endpoint, data=json.dumps(data), headers=headers)
    logger.info(response.text)
    return json.loads(response.text)


def delete_member(url, login, pw, user):
    logger.info('Delete member %s' % user)
    # temporary workaround until cws 1.2
    # need to resolve memberId by accountName
    member_id = _member_by_user(url, login, pw, user)

    endpoint = urlparse.urljoin(url, 'members/deleteMember')
    data = dict(accountName=login,
                credential=base64.b64encode(pw),
                memberId=member_id)
    headers = {'Content-type': 'application/json',
               'Accept': 'application/json'}
    response = requests.post(endpoint, data=json.dumps(data), headers=headers)
    logger.info(response.text)
    return json.loads(response.text)
