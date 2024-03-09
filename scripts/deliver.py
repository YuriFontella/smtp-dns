import smtplib
import dns.resolver

async def deliver(email):
    domain = email.split('@')[-1]
    try:
        mx = dns.resolver.resolve(domain, 'MX')
        record = str(mx[0].exchange)

        with smtplib.SMTP(record, timeout=10) as server:
            server.set_debuglevel(0)
            server.ehlo()
            server.mail('')
            code, message = server.rcpt(email)

            if code == 250:
                return True, 'Valid'
            else:
                print(code, message)
                return False, 'Invalid'

    except smtplib.SMTPConnectError as e:
        return False, f"Connection error when checking {email}: {e}"
    except smtplib.SMTPServerDisconnected as e:
        return False, f"SMTP server disconnected when checking {email}: {e}"
    except dns.resolver.NXDOMAIN as e:
        return False, f"Domain not found when checking {email}: {e}"
    except Exception as e:
        return False, f"Unknown error when checking {email}: {e}"
