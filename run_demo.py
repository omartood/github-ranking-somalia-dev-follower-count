#!/usr/bin/env python3
"""
Quick demo runner - shows the bot working without any setup
"""

import subprocess
import sys

def main():
    print("🇸🇴 Somali GitHub Developer Ranking Bot - Quick Demo")
    print("=" * 50)
    
    try:
        # Run the demo
        result = subprocess.run([sys.executable, 'demo_ranking.py'], 
                              capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ Demo completed successfully!")
            print("\n📄 Output:")
            print(result.stdout)
            
            # Show the generated file
            try:
                with open('README_demo.md', 'r') as f:
                    content = f.read()
                    lines = content.split('\n')
                    # Show first 15 lines
                    print("\n📋 Generated README_demo.md (first 15 lines):")
                    print("-" * 40)
                    for line in lines[:15]:
                        print(line)
                    if len(lines) > 15:
                        print("... (truncated)")
                        
            except FileNotFoundError:
                print("README_demo.md not found")
                
        else:
            print("❌ Demo failed:")
            print(result.stderr)
            
    except Exception as e:
        print(f"❌ Error running demo: {e}")

if __name__ == "__main__":
    main()