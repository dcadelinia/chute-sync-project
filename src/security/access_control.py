import datetime

class ProprietaryAuditLogger:
    """ Logs data exposures to prove willful misappropriation under TUTSA/DTSA """
    def __init__(self, log_path="LEGAL/access_audit.log"):
        self.log_path = log_path

    def log_access(self, user_id: str, action: str, classification_level: str):
        timestamp = datetime.datetime.utcnow().isoformat()
        log_entry = f"[{timestamp}] USER: {user_id} | ACTION: {action} | CLASS: {classification_level}\n"
        
        # In production, route this directly to an immutable write-once read-many (WORM) storage node
        with open(self.log_path, "a") as log_file:
            log_file.write(log_entry)
