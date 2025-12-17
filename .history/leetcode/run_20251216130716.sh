
#!/usr/bin/env bash
set -euo pipefail

python concurrency.py << 'EOF'
5
5
2
5
3
3
5
3
7
8
6
9
EOF
