# ~/pmd-bin-6.0.0/bin/run.sh pmd -d src -R rulesets/java/unusedcode.xml -f text -r unusedcode.txt

# ~/pmd-bin-6.0.0/bin/run.sh pmd -d ./src/HelloWorld.java -R unusedcode.xml -f text -r unusedcode.txt

# ~/pmd-bin-6.0.0/bin/run.sh pmd -d ../../lucky/  -R unusedcode.xml -f text -r unusedcode.txt

~/pmd-bin-6.0.0/bin/run.sh pmd -d ../../lucky/  -R unusedcode.xml -f xml -r violation.xml


# ~/pmd-bin-6.0.0/bin/run.sh pmd -d AVLTree.java -R unusedcode.xml -f xml -r violation.xml

# cpd
# ~/pmd-bin-6.0.0/bin/run.sh cpd --minimum-tokens 100 --language php --files ../pmd-master --encoding utf-8 --format xml  > cpd.xml
# ~/pmd-bin-6.0.0/bin/run.sh cpd --minimum-tokens 100 --language php --files src --encoding utf-8 --format xml  > cpd.xml