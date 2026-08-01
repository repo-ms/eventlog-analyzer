SEVERITY = {
    # Logon / Authentication
    4624: "INFO",       # Login Success
    4625: "WARNING",    # Login Failed
    4634: "INFO",       # Logoff
    4647: "INFO",       # User Initiated Logoff
    4648: "WARNING",    # Logon with Explicit Credentials (runas)
    4672: "WARNING",    # Special Privileges Assigned
    4776: "INFO",       # NTLM Authentication Success/Failed

    # Account Management
    4720: "ALERT",      # User Account Created
    4722: "INFO",       # User Account Enabled
    4723: "INFO",       # User Password Change Attempt
    4724: "WARNING",    # User Password Reset Attempt
    4725: "INFO",       # User Account Disabled
    4726: "ALERT",      # User Account Deleted
    4728: "ALERT",      # Member Added to Global Security Group
    4732: "ALERT",      # Member Added to Local Security Group
    4738: "WARNING",    # User Account Modified
    4740: "WARNING",    # User Account Locked Out
    4756: "ALERT",      # Member Added to Universal Security Group

    # Execution / Persistence
    4688: "INFO",       # Process Created
    4689: "INFO",       # Process Terminated
    4698: "ALERT",      # Scheduled Task Created
    4699: "INFO",       # Scheduled Task Deleted
    4700: "INFO",       # Scheduled Task Enabled
    4702: "INFO",       # Scheduled Task Updated
    7045: "ALERT",      # Service Installed

    # Policy / Audit
    1102: "CRITICAL",   # Audit Log Cleared
    4719: "WARNING",    # System Audit Policy Changed
    4907: "WARNING",    # Auditing Settings Changed

    # Object Access / File Share
    4656: "INFO",       # Handle Requested
    4663: "INFO",       # Object Access
    4697: "ALERT",      # Service Installed
    5140: "INFO",       # Network Share Object Accessed
    5145: "INFO",       # Network Share Object Checked
}

def get_severity(event_id: int) -> str:
    return SEVERITY.get(event_id, "INFO")