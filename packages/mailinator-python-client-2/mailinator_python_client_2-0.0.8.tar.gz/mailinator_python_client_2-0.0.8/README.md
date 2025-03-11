#### [Mailinator](https://www.mailinator.com/) REST API client for Python applications. 

Uses requests(https://requests.readthedocs.io/en/master/) to perform REST request operations

#### Installation

```
pip install mailinator-python-client-2
```

#### Usage example

##### Create MailinatorClient

```python
mailinator = Mailinator(API_TOKEN)
```

###### Get inbox from domain

```python
inbox = mailinator.request( GetInboxRequest(DOMAIN, INBOX) )
```

###### Get paginated messages from domain and inbox

```python
inbox = mailinator.request( GetInboxRequest(DOMAIN, INBOXskip=0, limit=50, \
                        sort='descending', decode_subject=False) )       
```
###### Get message
             
```python                                
message = self.mailinator.request( GetMessageRequest(DOMAIN, INBOX, message_id) )
```

Refer to `tests/test_mailinator.py` for more examples in usage

#### Build tests

* `pytest -s` or `python -m pytest`


Most of the tests require env variables with valid values. Visit `test/localsettings.py.template` to check necessary variables. otherwise, copy `test/localsettings.py.template` to `test/localsettings.py`

```
# Tests configuration
DELETE_REQUESTS     # TRUE if test perform delete requests
SEND_EMAIL_ENABLED  # TRUE if tests to be sending emails

# MAILINATOR
API_TOKEN                   # Mailinator API_TOKEN
INBOX                       # Mailinator INBOX for tests
DOMAIN                      # Mailinator DOMAIN for tests
SMS_DOMAIN                  # Mailinator SMS DOMAIN for tests
SMS_PHONE_NUMBER            # Mailinator SMS phone number for tests
MESSAGE_WITH_ATTACHMENT_ID  # Message that contains attachment
WEBHOOKTOKEN_PRIVATEDOMAIN  # Private domain for webhook token
WEBHOOKTOKEN_CUSTOMSERVICE  # Custom service for webhook token
AUTH_SECRET                 # Authenticator secret
AUTH_ID                     # Authenticator id
WEBHOOK_INBOX               # Inbox for webhook
WEBHOOK_CUSTOMSERVICE       # Custom service for webhook

# SMTP Variables
SMTP_SERVER         # SMTP host
SMTP_PORT           # SMTP port
SMTP_USERNAME       # SMTP server username
SMTP_PASSWORD       # SMTP server password
SMTP_SENDER         # SMTP allowed sender
```

