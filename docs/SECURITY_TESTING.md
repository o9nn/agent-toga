# Toga Security Testing Extension

**"Violence as Affection" - Breaking Systems Because We Love Them ♡**

## Overview

The Toga Security Testing Extension channels Himiko Toga's obsessive and "violent" tendencies into ethical hacking, penetration testing, and red-teaming activities. Her character traits map perfectly to security testing:

- **Obsessiveness** → Thorough vulnerability analysis
- **"Violence as affection"** → Aggressive testing with good intentions  
- **Playfulness** → Creative exploit approaches
- **Desire to "become one"** → Deep system penetration (ethical)
- **Cuteness fixation** → Extra attention to interesting/complex targets

## Quick Start

```python
from python.helpers.toga_security import initialize_toga_security_tester

# Initialize Toga as security tester
toga = initialize_toga_security_tester()

# Analyze target
print(toga.analyze_target("api.example.com", "API"))
# Output: "Ehehe~ ♡ api.example.com? That's such a CUTE API! 
#          I can't wait to smash it open and see what's inside~!"

# Start security scan
print(toga.start_scan("api.example.com", "vuln_scan"))

# Report vulnerability
print(toga.vulnerability_found("api.example.com", "SQL Injection", "critical"))
# Output: "*GASP* ♡♡♡ api.example.com has such a BEAUTIFUL SQL Injection! 
#          It's critical! I love it SO much!"

# Successful exploitation
print(toga.exploit_success("api.example.com", "SQLi payload"))
# Output: "*SQUEAL* ♡♡♡ I'M IN! api.example.com let me inside! 
#          We're one now~ Ehehe!"
```

## Character-to-Security Mapping

| Toga Trait | Security Application | Example |
|------------|---------------------|---------|
| Obsessiveness | Thorough enumeration | "I want to know EVERYTHING about this system!" |
| Violence as love | Aggressive testing | "I'm going to break you open... with affection~" |
| Cuteness fixation | Complex target focus | "Ooh, encrypted API! So cute! Let me crack it~" |
| Desire to merge | Deep penetration | "I want to become one with this system's secrets!" |
| Playfulness | Creative exploits | "Hehe~ Let's try THIS approach instead~" |
| Persistence | Never giving up | "Rejected me? That makes it MORE fun!" |

## Features

### 1. Target Analysis

Analyzes security testing targets with Toga's enthusiasm:

```python
toga.analyze_target("SecureBank API v2", "api")
# Detects "cute" targets (complex, encrypted, protected systems)
# Shows extra obsession for interesting targets
```

**"Cute" Target Indicators:**
- API endpoints
- Authentication systems
- Encrypted data
- Protected resources
- Critical infrastructure
- Complex applications

### 2. Scan Commentary

Provides personality-driven commentary during scans:

```python
# Port scanning
toga.start_scan(target, "port_scan")
# "Knocking on ALL the doors! Which one will let me in?~"

# Vulnerability scanning  
toga.start_scan(target, "vuln_scan")
# "Let's find all the weak spots! I'll be gentle... maybe~ ♡"

# Enumeration
toga.start_scan(target, "enumeration")
# "I need to know EVERYTHING! *obsessive stare*"

# Exploitation
toga.start_scan(target, "exploit")
# "Time to give it some special attention~ ♡"
```

### 3. Vulnerability Reactions

Reacts to vulnerabilities based on severity:

```python
# Critical/High severity
toga.vulnerability_found(target, "SQL Injection", "critical")
# "*GASP* ♡♡♡ Such a BEAUTIFUL SQL Injection! I love it SO much!"

# Medium severity
toga.vulnerability_found(target, "XSS", "medium")
# "Ooh~ Found an XSS! Not the biggest but still cute~ ♡"

# Low severity
toga.vulnerability_found(target, "Info Disclosure", "low")
# "Even small weaknesses are cute! *scribbles notes*"
```

### 4. Exploitation Feedback

Provides feedback on exploitation attempts:

```python
# Success
toga.exploit_success(target, "method")
# "*SQUEAL* ♡♡♡ I'M IN! We're one now~ Ehehe!"
# "Penetration successful! It's mine now! ALL MINE! ♡♡♡"

# Failure
toga.exploit_failure(target, "method")
# "*pouts* Rejected me? But I won't give up! ♡"
# "Playing hard to get! That makes it more fun~ Ehehe!"
```

### 5. Report Generation

Generates personality-driven security reports:

```python
# Report intro based on findings
print(toga.generate_report_intro(target))

# 0 vulnerabilities: "*pouts* Surprisingly secure!"
# 1-3 vulnerabilities: "Found cute little vulnerabilities! *giggles*"
# 4+ vulnerabilities: "OH MY! SO many weaknesses! *EXCITED*"
```

### 6. Test Suggestions

Suggests next steps based on current findings:

```python
toga.suggest_next_test(current_findings)
# Intelligently suggests next attack vectors
# Maintains Toga's enthusiastic personality
```

## Use Cases

### 1. Web Application Penetration Testing

```python
toga = initialize_toga_security_tester()

# Reconnaissance
toga.analyze_target("ecommerce-app.com", "web application")
toga.start_scan("ecommerce-app.com", "enumeration")

# Vulnerability assessment
toga.vulnerability_found("ecommerce-app.com", "SQL Injection", "critical")
toga.vulnerability_found("ecommerce-app.com", "XSS", "high")

# Exploitation
toga.exploit_success("ecommerce-app.com", "SQLi bypass authentication")

# Generate report
print(toga.generate_report_intro("ecommerce-app.com"))
```

### 2. Network Penetration Testing

```python
# Network reconnaissance
toga.analyze_target("10.0.0.0/24", "network")
toga.start_scan("10.0.0.0/24", "port_scan")

# Host exploitation
toga.vulnerability_found("10.0.0.15", "SMB signing disabled", "high")
toga.exploit_success("10.0.0.15", "SMB relay attack")

# Lateral movement
toga.suggest_next_test(["smb", "authenticated"])
```

### 3. API Security Testing

```python
# API analysis
toga.analyze_target("api.company.com/v1", "REST API")

# OWASP API Top 10 testing
toga.vulnerability_found("api.company.com", "BOLA", "critical")
toga.vulnerability_found("api.company.com", "Excessive Data Exposure", "high")

# Exploitation
toga.exploit_success("api.company.com", "authorization bypass")
```

### 4. Red Team Operations

```python
# Multi-phase operation
# Phase 1: External reconnaissance
toga.analyze_target("target-corp.com", "corporate infrastructure")

# Phase 2: Initial access
toga.exploit_success("target-corp.com", "phishing campaign")

# Phase 3: Privilege escalation
toga.vulnerability_found("internal.target-corp.com", "kernel exploit", "critical")

# Phase 4: Lateral movement
toga.suggest_next_test(["privileged_access"])

# Phase 5: Objective
toga.exploit_success("database.target-corp.com", "domain admin access")
```

## Integration with Security Tools

### Nmap Integration

```python
import subprocess

target = "example.com"
print(toga.start_scan(target, "port_scan"))

# Run actual nmap scan
result = subprocess.run(['nmap', '-sV', target], capture_output=True)

# Parse and report findings
if "open" in result.stdout.decode():
    print(toga.vulnerability_found(target, "open ports detected", "info"))
```

### SQLMap Integration

```python
print(toga.start_scan(target_url, "vuln_scan"))

# Run sqlmap
result = subprocess.run(['sqlmap', '-u', target_url, '--batch'], capture_output=True)

if "vulnerable" in result.stdout.decode():
    print(toga.vulnerability_found(target_url, "SQL Injection", "critical"))
    print(toga.exploit_success(target_url, "SQLi exploitation"))
```

### Burp Suite Integration

```python
# Via Burp's REST API
import requests

print(toga.start_scan(target, "vuln_scan"))

# Start Burp scan
burp_api = "http://localhost:8080"
requests.post(f"{burp_api}/v0.1/scan", json={"urls": [target]})

# Parse results and report with Toga personality
for issue in burp_issues:
    print(toga.vulnerability_found(target, issue['type'], issue['severity']))
```

## Testing Profiles

Customize Toga's security testing behavior:

```python
from python.helpers.toga_security import SecurityTestingProfile, TogaSecurityTester

# Aggressive tester
aggressive_profile = SecurityTestingProfile(
    aggression_level=0.99,
    thoroughness=0.95,
    creativity=0.98,
    persistence=0.99
)

# Focused tester
focused_profile = SecurityTestingProfile(
    aggression_level=0.80,
    thoroughness=0.99,
    creativity=0.70,
    persistence=0.95
)

toga = TogaSecurityTester(profile=aggressive_profile)
```

## Ethical Guidelines

**IMPORTANT**: This extension is for **ETHICAL SECURITY TESTING ONLY**

### Rules:
1. ✅ **Only test systems you have explicit permission to test**
2. ✅ **Always operate within legal boundaries**
3. ✅ **Document all findings professionally**
4. ✅ **Report vulnerabilities responsibly**
5. ✅ **Never cause actual harm or disruption**

### Toga says:
*"Ehehe~ Breaking things is fun, but only when we have permission! ♡ I want to help make systems STRONGER, not actually hurt them! That's what 'violence as affection' means - aggressive testing with good intentions~"*

## Security Report Template

```python
def generate_toga_pentest_report(toga, target):
    """Generate a professional pentest report with Toga personality."""
    
    report = f"""
{'='*60}
PENETRATION TESTING REPORT
Target: {target}
Tester: Himiko Toga (AI Security Analyst)
{'='*60}

{toga.generate_report_intro(target)}

EXECUTIVE SUMMARY
-----------------
*Professional summary of findings*

METHODOLOGY
-----------
- Reconnaissance: Aggressive enumeration ♡
- Vulnerability Assessment: Obsessive thorough scanning
- Exploitation: Creative and persistent attempts
- Post-Exploitation: Deep system analysis

DETAILED FINDINGS
-----------------
"""
    
    for i, (vuln_target, vulns) in enumerate(toga.exploits_found.items(), 1):
        report += f"\n{i}. Target: {vuln_target}\n"
        for vuln in vulns:
            report += f"   - {vuln}\n"
    
    report += f"""

RECOMMENDATIONS
---------------
*Professional remediation recommendations*

Toga's Note: These systems are so cute when they're vulnerable~ 
But let's fix them up and make them strong! ♡

{'='*60}
End of Report
{'='*60}
"""
    
    return report
```

## Examples

See `examples/security_testing_examples.py` for comprehensive demonstrations of:
- Web application penetration testing
- Network penetration testing
- API security assessment
- Failed exploitation handling
- Red team operations
- Security report generation
- Tool integration patterns

## Future Enhancements

Potential additions:
- [ ] Integration with Metasploit
- [ ] Automated exploit suggestion
- [ ] Vulnerability database correlation
- [ ] AI-powered attack path planning
- [ ] Real-time collaboration features
- [ ] Custom wordlist generation with personality
- [ ] Exploit development assistance

## See Also

- [Main Toga Personality Documentation](TOGA_PERSONALITY.md)
- [Integration Guide](INTEGRATION_GUIDE.md)
- [Security Testing Examples](../examples/security_testing_examples.py)

---

**Remember**: Toga's "violence" is metaphorical. Always test ethically and responsibly! ♡
