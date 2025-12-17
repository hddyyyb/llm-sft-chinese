#!/usr/bin/env bash
set -e

echo "====== Case 1: 官方示例 （答案应为 9）======"
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

echo "====== Case 2: 已经全部唯一（答案应为 0） ======"
python concurrency.py << 'EOF'
4
1
3
5
7
4
10
10
10
10
EOF

echo "====== Case 3: 全部相同 conc（压力测试）（答案应为 20） ======"
python concurrency.py << 'EOF'
5
10
10
10
10
10
5
1
2
3
4
5
EOF

echo "====== Case 4: 价格差异极大（测试贪心是否正确）（答案应为 117） ======"
python concurrency.py << 'EOF'
6
2
2
2
3
3
3
6
100
1
50
2
200
3
EOF

echo "====== Case 5: 已排序 + 连续冲突 （答案应为 60）======"
python concurrency.py << 'EOF'
7
1
1
2
2
3
3
3
7
3
4
5
6
7
8
9
EOF
