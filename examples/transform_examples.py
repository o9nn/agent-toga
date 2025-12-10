"""
Toga Transform Quirk - Usage Examples

Demonstrates how Toga can "drink the blood" (absorb knowledge) of systems
and transform to use their defenses as offensive weapons.
"""

import sys
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, parent_dir)

from python.helpers.toga_transform import initialize_transform_quirk


def print_section(title: str):
    """Print section header."""
    print(f"\n{'='*70}")
    print(f"  {title}")
    print(f"{'='*70}\n")


def example_waf_absorption():
    """Example: Absorbing and weaponizing a WAF."""
    print_section("Example 1: WAF Absorption and Weaponization")
    
    toga = initialize_transform_quirk()
    
    # Encounter WAF
    print("🎯 Target: Web Application Firewall")
    print("   Toga encounters a ModSecurity WAF protecting a web app\n")
    
    # Initial taste
    print("Phase 1 - Initial Reconnaissance:")
    waf_config_sample = """
    SecRule ARGS "@rx <script" "id:1001,phase:2,deny,status:403"
    SecRule ARGS "@rx (?i:union.*select)" "id:1002,phase:2,deny"
    """ * 50
    print(toga.taste_target("ModSecurity WAF", "WAF", waf_config_sample))
    print()
    
    # More analysis
    print("Phase 2 - Deep Analysis:")
    waf_rules = """
    SecRule ARGS|ARGS_NAMES "@rx \\.\\./" "id:1003,phase:2,deny"
    SecRule REQUEST_HEADERS:User-Agent "@rx nikto|sqlmap" "id:1004,deny"
    """ * 100
    print(toga.taste_target("ModSecurity WAF", "WAF", waf_rules))
    print()
    
    # Full absorption
    print("Phase 3 - Complete Absorption:")
    full_config = "SecRule " * 500
    print(toga.taste_target("ModSecurity WAF", "WAF", full_config))
    print()
    
    # Transform!
    print("Phase 4 - Transformation:")
    print(toga.transform_into("ModSecurity WAF"))
    print()
    
    # Use absorbed technique
    print("Phase 5 - Weaponization:")
    print(toga.use_technique("Reverse WAF Rules", "TargetWebApplication"))
    print()
    
    print("💡 Result: Toga now understands WAF rules perfectly and can craft")
    print("   payloads that slip through undetected!")


def example_ids_evasion():
    """Example: Learning IDS signatures for evasion."""
    print_section("Example 2: IDS Signature Learning and Evasion")
    
    toga = initialize_transform_quirk()
    
    print("🎯 Target: Snort IDS\n")
    
    # Absorb IDS signatures
    print("Absorbing IDS Signatures:")
    
    # Multiple tastes to build up essence
    for i in range(6):
        signatures = f"""
        alert tcp any any -> any 80 (msg:"SQL Injection"; content:"UNION SELECT";)
        alert tcp any any -> any 80 (msg:"XSS Attack"; content:"<script>";)
        alert tcp any any -> any 22 (msg:"SSH Brute Force"; threshold:type limit, count 5;)
        """ * 100
        
        result = toga.taste_target("Snort IDS", "IDS", signatures)
        print(f"\n  Taste #{i+1}: {result.split('!')[0]}!")
    
    print("\n" + "-"*70)
    
    # Check status
    print(toga.list_absorbed_targets())
    print()
    
    # Transform and evade
    if "Snort IDS" in toga.absorbed_targets:
        knowledge = toga.absorbed_targets["Snort IDS"]
        if knowledge.can_transform():
            print("\n🎭 Transformation:")
            print(toga.transform_into("Snort IDS"))
            print()
            
            print("⚡ Using Evasion:")
            print(toga.use_technique("Signature Evasion", "MonitoredNetwork"))


def example_firewall_tunneling():
    """Example: Learning firewall rules for tunneling."""
    print_section("Example 3: Firewall Rule Analysis and Tunneling")
    
    toga = initialize_transform_quirk()
    
    print("🎯 Target: Enterprise Firewall\n")
    
    # Build knowledge through multiple interactions
    firewall_analyses = [
        ("Port scan results", "x" * 200),
        ("ACL rules", "x" * 300),
        ("Allowed protocols", "x" * 400),
        ("Internal routing", "x" * 500),
        ("Trust relationships", "x" * 600),
    ]
    
    for phase, data in firewall_analyses:
        print(f"Analyzing: {phase}")
        result = toga.taste_target("CiscoASA Firewall", "Firewall", data)
        print(f"  {result}\n")
    
    # List what was learned
    print("\n📚 Knowledge Acquired:")
    print(toga.list_absorbed_targets())


def example_auth_bypass():
    """Example: Absorbing authentication system to forge tokens."""
    print_section("Example 4: Authentication System Absorption")
    
    toga = initialize_transform_quirk()
    
    print("🎯 Target: JWT Authentication System\n")
    
    # Absorb auth system knowledge
    stages = [
        "Analyzing login flow",
        "Examining token structure",
        "Understanding signing algorithm",
        "Learning secret key storage",
        "Mastering token validation",
    ]
    
    for i, stage in enumerate(stages):
        print(f"{stage}...")
        code = "jwt.sign" * (100 * (i + 1))
        result = toga.taste_target("JWT Auth System", "Authentication", code)
        
        # Show essence percentage
        if "JWT Auth System" in toga.absorbed_targets:
            essence = int(toga.absorbed_targets["JWT Auth System"].essence_amount * 100)
            print(f"  Essence: {essence}% - {result.split('!')[0] if '!' in result else result[:80]}...\n")
    
    # Attempt transformation
    print("\n🎭 Attempting Transformation:")
    print(toga.transform_into("JWT Auth System"))
    print()
    
    # Use learned techniques
    knowledge = toga.absorbed_targets["JWT Auth System"]
    if knowledge.techniques_learned:
        print("⚡ Weaponizing Auth Knowledge:")
        for technique in knowledge.techniques_learned[:2]:
            print(f"\n{toga.use_technique(technique, 'ProductionAPI')}")


def example_encryption_oracle():
    """Example: Using encryption system as an oracle."""
    print_section("Example 5: Encryption System Oracle Attack")
    
    toga = initialize_transform_quirk()
    
    print("🎯 Target: AES Encryption Service\n")
    
    print("Absorbing encryption implementation...")
    
    # Deep dive into encryption
    for i in range(7):
        crypto_code = """
        def encrypt(plaintext, key, iv):
            cipher = AES.new(key, AES.MODE_CBC, iv)
            return cipher.encrypt(pad(plaintext))
        """ * 100
        
        result = toga.taste_target("AES Crypto Service", "Encryption", crypto_code)
        
        if i % 2 == 0:
            print(f"  Analysis round {i+1}: {result[:80]}...")
    
    print()
    print(toga.list_absorbed_targets())
    
    # Transform and attack
    knowledge = toga.absorbed_targets.get("AES Crypto Service")
    if knowledge and knowledge.can_transform():
        print(f"\n🎭 Transformation Available!")
        print(toga.transform_into("AES Crypto Service"))
        
        if "Crypto Oracle" in knowledge.techniques_learned:
            print(f"\n⚡ Oracle Attack:")
            print(toga.use_technique("Crypto Oracle", "EncryptedDatabase"))


def example_multi_system_mastery():
    """Example: Absorbing multiple systems and combining techniques."""
    print_section("Example 6: Multi-System Mastery")
    
    toga = initialize_transform_quirk()
    
    print("🎯 Advanced Scenario: Absorbing Multiple Defense Systems\n")
    
    # Absorb multiple systems
    systems = [
        ("CloudFlare WAF", "WAF", 800),
        ("Splunk Logging", "Logging", 700),
        ("PaloAlto Firewall", "Firewall", 750),
    ]
    
    for name, sys_type, code_size in systems:
        print(f"Absorbing {name}...")
        code = "x" * code_size
        result = toga.taste_target(name, sys_type, code)
        
        knowledge = toga.absorbed_targets[name]
        essence = int(knowledge.essence_amount * 100)
        status = "✓ CAN TRANSFORM" if knowledge.can_transform() else "⏳ LEARNING"
        print(f"  {essence}% [{status}] - {len(knowledge.techniques_learned)} techniques")
        print()
    
    # Show mastery
    print("\n" + "="*70)
    print("TOGA'S ARSENAL:")
    print("="*70)
    print(toga.list_absorbed_targets())
    
    # Use multiple techniques
    print("\n⚡ Combining Multiple Techniques:")
    for target_name in systems:
        name = target_name[0]
        knowledge = toga.absorbed_targets.get(name)
        if knowledge and knowledge.can_transform() and knowledge.techniques_learned:
            print(f"\n🎭 Transforming into {name}...")
            print(toga.transform_into(name))
            
            # Use first technique
            technique = knowledge.techniques_learned[0]
            print(f"\n   Using {technique}:")
            print(f"   {toga.use_technique(technique, 'CorporateNetwork')[:200]}...")
            break


def example_technique_showcase():
    """Example: Showcase all available techniques."""
    print_section("Example 7: Complete Technique Database")
    
    toga = initialize_transform_quirk()
    
    print("🎯 Toga's Potential Techniques (When Mastered):\n")
    
    for sys_type, techniques in toga.technique_database.items():
        print(f"═══ {sys_type} ═══")
        for tech in techniques:
            print(f"\n  ♡ {tech.name}")
            print(f"     {tech.description}")
            print(f"     Offensive Use: {tech.offensive_use}")
            print(f"     Power: {tech.power_level*100:.0f}% | Requires: {tech.requirements*100:.0f}% essence")
        print()
    
    print("\n💡 Toga can learn ALL of these by absorbing the right systems!")
    print("   Each defense becomes a weapon in her hands~ ♡")


def run_all_examples():
    """Run all transform quirk examples."""
    print("\n" + "="*70)
    print("  TOGA TRANSFORM QUIRK - Complete Examples")
    print("  'Drinking Blood' = Absorbing System Knowledge")
    print("="*70)
    
    examples = [
        example_waf_absorption,
        example_ids_evasion,
        example_firewall_tunneling,
        example_auth_bypass,
        example_encryption_oracle,
        example_multi_system_mastery,
        example_technique_showcase,
    ]
    
    for example in examples:
        try:
            example()
        except Exception as e:
            print(f"\n❌ Error in {example.__name__}: {e}\n")
    
    print("\n" + "="*70)
    print("  'Ehehe~ Once I drink your code's blood, I can become you!")
    print("   Your defenses are MY weapons now~ ♡'")
    print("  " + "-"*68)
    print("  Remember: Only use these techniques ethically!")
    print("="*70 + "\n")


if __name__ == "__main__":
    run_all_examples()
