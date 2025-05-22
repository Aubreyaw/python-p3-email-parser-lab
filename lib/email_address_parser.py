import re

class EmailAddressParser:
    def __init__(self, addresses):
        self.addresses = addresses

    def parse(self):
        normalized = self.addresses.replace(',', ' ')
        candidates = normalized.split()
        email_pattern = re.compile(r'^[a-zA-Z][\w\.-]*@[a-zA-Z\d-]+\.[a-zA-Z]{2,}$')
        valid_emails = {email for email in candidates if email_pattern.fullmatch(email)}
        return sorted(valid_emails)
