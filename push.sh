#!/bin/bash

# 检查是否提供了参数
if [ $# -eq 0 ]; then
    echo "请提供提交信息"
    exit 1
fi

# 获取参数作为提交信息
commit_message="$*"

git pull
git add .
git commit -m "$commit_message"
git push