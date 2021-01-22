# credstuffing - Credential Stuffing

:skull: A simple script that performs **credential stuffing** on HTTP Basic authentication.

## Usage
1. `git clone https://github.com/santosfilipe/credstuffing`

2. Alter the following lines to reflect the actual files of users and passwords:
```python
username_file = open('users file goes here')
password_file = open('passwords file goes here')
```

3. Alter the following line to configure the actual application you are testing:
```python
tryAuthentication("application URL goes here", user, password)
```

4. Make the script executable:
`chmod +x credential_stuffing.py`

5. Run the script:
`python3 credential_stuffing.py`
