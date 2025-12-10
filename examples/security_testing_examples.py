"""
Toga Security Testing Examples

Demonstrates how to use Toga's personality for ethical hacking,
penetration testing, and red-teaming scenarios.

"Violence as Affection" - Breaking systems because we love them ♡
"""

import sys
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, parent_dir)

from python.helpers.toga_security import initialize_toga_security_tester


def example_webapp_pentest():
    """Example: Web application penetration test with Toga."""
    print("\n" + "="*60)
    print("  Example 1: Web Application Penetration Test")
    print("="*60 + "\n")
    
    toga = initialize_toga_security_tester()
    
    # Target analysis
    print("🎯 Target Discovery:")
    print(toga.analyze_target("CoolShop E-Commerce", "web application"))
    print()
    
    # Reconnaissance phase
    print("🔍 Reconnaissance Phase:")
    print(toga.start_scan("CoolShop E-Commerce", "enumeration"))
    print()
    
    # Finding vulnerabilities
    vulns = [
        ("XSS in search parameter", "medium"),
        ("SQL Injection in login", "critical"),
        ("Broken Authentication", "high"),
        ("Sensitive Data Exposure", "high"),
    ]
    
    print("💥 Vulnerability Discovery:")
    for vuln, severity in vulns:
        print(f"\n  [{severity.upper()}] {vuln}")
        print(f"  {toga.vulnerability_found('CoolShop E-Commerce', vuln, severity)}")
    print()
    
    # Exploitation
    print("⚡ Exploitation Phase:")
    print(toga.exploit_success("CoolShop E-Commerce", "SQL injection bypass"))
    print()
    
    # Next steps
    print("📋 Recommended Next Steps:")
    print(toga.suggest_next_test(["webapp", "authenticated"]))


def example_network_pentest():
    """Example: Network penetration test with Toga."""
    print("\n" + "="*60)
    print("  Example 2: Network Penetration Test")
    print("="*60 + "\n")
    
    toga = initialize_toga_security_tester()
    
    # Target
    print("🎯 Target: Corporate Network 10.0.0.0/24")
    print(toga.analyze_target("10.0.0.0/24", "network"))
    print()
    
    # Port scanning
    print("🔍 Port Scanning:")
    print(toga.start_scan("10.0.0.0/24", "port_scan"))
    print()
    
    # Findings
    print("📊 Scan Results:")
    print("  Host: 10.0.0.15")
    print(toga.vulnerability_found("10.0.0.15", "SMB signing disabled", "high"))
    print()
    
    print("  Host: 10.0.0.23")
    print(toga.vulnerability_found("10.0.0.23", "Outdated SSH version", "medium"))
    print()
    
    # Lateral movement
    print("🎯 Lateral Movement:")
    print(toga.suggest_next_test(["open_ports", "smb"]))


def example_api_security_test():
    """Example: API security testing with Toga."""
    print("\n" + "="*60)
    print("  Example 3: REST API Security Assessment")
    print("="*60 + "\n")
    
    toga = initialize_toga_security_tester()
    
    # API analysis
    print("🎯 API Target:")
    target = "api.example.com/v1"
    print(toga.analyze_target(target, "REST API"))
    print()
    
    # Testing endpoints
    print("🔍 Endpoint Analysis:")
    print(toga.start_scan(target, "enumeration"))
    print()
    
    # OWASP API Security Top 10 testing
    api_vulns = [
        ("Broken Object Level Authorization", "critical"),
        ("Excessive Data Exposure", "high"),
        ("Lack of Resources & Rate Limiting", "medium"),
        ("Missing Function Level Access Control", "high"),
    ]
    
    print("💥 OWASP API Top 10 Findings:")
    for vuln, severity in api_vulns:
        print(f"\n  {vuln}:")
        print(f"  {toga.vulnerability_found(target, vuln, severity)}")
    print()
    
    # Exploitation attempt
    print("⚡ Exploitation:")
    print(toga.exploit_success(target, "BOLA bypass"))


def example_failed_attempts():
    """Example: Handling failed exploitation attempts."""
    print("\n" + "="*60)
    print("  Example 4: Failed Exploitation (Toga's Persistence)")
    print("="*60 + "\n")
    
    toga = initialize_toga_security_tester()
    
    target = "SuperSecure Corp Portal"
    
    print("🎯 Target:")
    print(toga.analyze_target(target, "web portal"))
    print()
    
    # Multiple failed attempts
    failed_methods = [
        "SQL injection",
        "XSS payload",
        "CSRF token bypass",
        "Directory traversal",
    ]
    
    print("💔 Failed Exploitation Attempts:")
    for method in failed_methods:
        print(f"\n  Trying {method}...")
        print(f"  {toga.exploit_failure(target, method)}")
    print()
    
    # Persistence
    print("🎯 Toga's Response:")
    print(toga.suggest_next_test(["hardened_target"]))
    print()
    
    # Eventually succeed
    print("✨ Finally...")
    print(toga.exploit_success(target, "0-day authentication bypass"))


def example_red_team_operation():
    """Example: Red team operation with Toga."""
    print("\n" + "="*60)
    print("  Example 5: Red Team Operation")
    print("="*60 + "\n")
    
    toga = initialize_toga_security_tester()
    
    print("🎯 Red Team Scenario: Breach Corporate Network")
    print()
    
    # Phase 1: External reconnaissance
    print("Phase 1 - External Reconnaissance:")
    print(toga.analyze_target("TechCorp.com", "corporate infrastructure"))
    print(toga.start_scan("TechCorp.com", "enumeration"))
    print()
    
    # Phase 2: Initial access
    print("Phase 2 - Initial Access:")
    print(toga.vulnerability_found("TechCorp.com", "Exposed Git repository", "high"))
    print(toga.exploit_success("TechCorp.com", "credential harvesting from git"))
    print()
    
    # Phase 3: Privilege escalation
    print("Phase 3 - Privilege Escalation:")
    print(toga.vulnerability_found("internal.techcorp.com", "Kernel exploit", "critical"))
    print(toga.exploit_success("internal.techcorp.com", "CVE-2024-XXXX privilege escalation"))
    print()
    
    # Phase 4: Lateral movement
    print("Phase 4 - Lateral Movement:")
    print(toga.suggest_next_test(["privileged_access"]))
    print(toga.vulnerability_found("dc01.techcorp.com", "Kerberoasting", "high"))
    print()
    
    # Phase 5: Objective
    print("Phase 5 - Objective Achieved:")
    print(toga.exploit_success("database.techcorp.com", "pass-the-hash attack"))


def example_security_report():
    """Example: Generate a security report with Toga's personality."""
    print("\n" + "="*60)
    print("  Example 6: Security Assessment Report")
    print("="*60 + "\n")
    
    toga = initialize_toga_security_tester()
    
    # Simulate testing
    target = "MyAwesomeApp v3.0"
    
    toga.exploits_found[target] = [
        "SQL Injection",
        "XSS",
        "CSRF",
        "Insecure Deserialization",
        "XML External Entity",
    ]
    
    # Generate report
    print(toga.generate_report_intro(target))
    print()
    
    print("Detailed Findings:")
    print("-" * 60)
    for i, vuln in enumerate(toga.exploits_found[target], 1):
        print(f"\n{i}. {vuln}")
        print(f"   Status: Confirmed ♡")
        print(f"   Exploitability: High")
        print(f"   Toga's Note: This was fun to find~ Ehehe!")


def example_integration_with_tools():
    """Example: Integration with actual security tools."""
    print("\n" + "="*60)
    print("  Example 7: Integration with Security Tools")
    print("="*60 + "\n")
    
    toga = initialize_toga_security_tester()
    
    print("🛠️  Tool Integration Examples:\n")
    
    # Nmap
    print("Using nmap:")
    print(toga.start_scan("target.com", "port_scan"))
    print("  $ nmap -sV -sC -p- target.com")
    print()
    
    # SQLmap
    print("Using sqlmap:")
    print(toga.vulnerability_found("target.com", "SQL Injection", "critical"))
    print("  $ sqlmap -u 'http://target.com/page?id=1' --batch --dbs")
    print()
    
    # Burp Suite
    print("Using Burp Suite:")
    print(toga.start_scan("webapp.com", "vuln_scan"))
    print("  [Burp] Active scanning initiated...")
    print()
    
    # Metasploit
    print("Using Metasploit:")
    print(toga.exploit_success("target.com", "ms17_010_eternalblue"))
    print("  msf6 > exploit/windows/smb/ms17_010_eternalblue")
    print("  [*] Meterpreter session 1 opened")


def run_all_examples():
    """Run all security testing examples."""
    print("\n" + "="*70)
    print("  TOGA SECURITY TESTING EXAMPLES")
    print("  Ethical Hacking with Personality ♡")
    print("="*70)
    
    examples = [
        example_webapp_pentest,
        example_network_pentest,
        example_api_security_test,
        example_failed_attempts,
        example_red_team_operation,
        example_security_report,
        example_integration_with_tools,
    ]
    
    for example in examples:
        try:
            example()
        except Exception as e:
            print(f"\n❌ Error in {example.__name__}: {e}\n")
    
    print("\n" + "="*70)
    print("  'Violence as Affection' - Breaking systems because we love them ♡")
    print("  Remember: Only test systems you have permission to test!")
    print("="*70 + "\n")


if __name__ == "__main__":
    run_all_examples()
