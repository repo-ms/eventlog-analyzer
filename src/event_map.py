EVENT_MAP = {
    # Logon / Authentication
    4624: "Login Success",
    4625: "Login Failed",
    4634: "Logoff",
    4647: "User Initiated Logoff",
    4648: "Logon with Explicit Credentials (runas)",
    4672: "Special Privileges Assigned",
    4776: "NTLM Authentication Success/Failed",

    # Account Management
    4720: "User Account Created",
    4722: "User Account Enabled",
    4723: "User Password Change Attempt",
    4724: "User Password Reset Attempt",
    4725: "User Account Disabled",
    4726: "User Account Deleted",
    4728: "Member Added to Global Security Group",
    4732: "Member Added to Local Security Group",
    4738: "User Account Modified",
    4740: "User Account Locked Out",
    4756: "Member Added to Universal Security Group",

    # Execution / Persistence
    4688: "Process Created",
    4689: "Process Terminated",
    4698: "Scheduled Task Created",
    4699: "Scheduled Task Deleted",
    4700: "Scheduled Task Enabled",
    4702: "Scheduled Task Updated",
    7045: "Service Installed",

    # Policy / Audit
    1102: "Audit Log Cleared",
    4719: "System Audit Policy Changed",
    4907: "Auditing Settings Changed",

    # Object Access / File Share
    4656: "Handle Requested (File/Object Access)",
    4663: "An attempt was made to access an object",
    4697: "A service was installed in the system",
    5140: "Network Share Object Accessed",
    5145: "Network Share Object Checked for Access",
}