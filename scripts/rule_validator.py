import yaml
import os
import sys

def validate_rule(file_path):
    print(f"Validating {file_path}...")
    try:
        with open(file_path, 'r') as stream:
            rule = yaml.safe_load(stream)
            
            # Basic schema validation
            required_fields = ['title', 'logsource', 'detection', 'level']
            for field in required_fields:
                if field not in rule:
                    print(f"  [ERROR] Missing required field: {field}")
                    return False
            
            # Check detection condition
            if 'condition' not in rule['detection']:
                 print(f"  [ERROR] Detection section missing 'condition' logic")
                 return False

            print("  [OK] Syntax is valid.")
            return True
            
    except yaml.YAMLError as exc:
        print(f"  [ERROR] YAML Parsing Logic: {exc}")
        return False
    except Exception as e:
        print(f"  [ERROR] Unexpected error: {e}")
        return False

def main():
    rules_dir = os.path.join(os.getcwd(), 'detection', 'rules')
    if not os.path.exists(rules_dir):
        print(f"Directory not found: {rules_dir}")
        return

    failed = 0
    passed = 0
    
    for filename in os.listdir(rules_dir):
        if filename.endswith(".yml") or filename.endswith(".yaml"):
            success = validate_rule(os.path.join(rules_dir, filename))
            if success:
                passed += 1
            else:
                failed += 1
    
    print("-" * 30)
    print(f"Validation Complete. Passed: {passed}, Failed: {failed}")

if __name__ == '__main__':
    main()
