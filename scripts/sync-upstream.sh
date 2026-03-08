#!/bin/bash
# Agent-Reach-Kr Upstream Sync Script
# 업스트림 변경을 가져와 충돌을 정리하고 검증까지 수행합니다.

set -euo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

TARGET_BRANCH=$(git rev-parse --abbrev-ref HEAD)
AUTO_PUSH="${AUTO_PUSH:-0}"

echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}Agent-Reach-Kr Upstream Sync${NC}"
echo -e "${BLUE}========================================${NC}"
echo ""

echo -e "${YELLOW}[1/6]${NC} Fetching upstream changes..."
git fetch upstream main
echo -e "${GREEN}✓${NC} Upstream fetched"
echo ""

echo -e "${YELLOW}[2/6]${NC} Checking upstream status..."
if git merge-base --is-ancestor upstream/main HEAD; then
    echo -e "${GREEN}✓${NC} Current branch already contains upstream/main"
    exit 0
fi

MERGE_BASE=$(git merge-base HEAD upstream/main || true)
if [ -n "${MERGE_BASE}" ]; then
    echo -e "${BLUE}Merge base:${NC} ${MERGE_BASE}"
else
    echo -e "${YELLOW}No merge-base found.${NC} This will be treated as an unrelated-history bootstrap sync."
fi
echo ""

echo -e "${YELLOW}[3/6]${NC} Upstream change summary:"
python3 scripts/build_sync_report.py --base "${MERGE_BASE}" --upstream upstream/main
echo ""

echo -e "${YELLOW}[4/6]${NC} Preparing merge..."
if git merge --allow-unrelated-histories --no-commit --no-ff upstream/main 2>/dev/null; then
    echo -e "${GREEN}✓${NC} Merge applied without conflicts"
else
    echo -e "${RED}✗${NC} Merge conflicts detected"
    echo -e "${YELLOW}Resolving conflicts with fork policy...${NC}"

    git diff --name-only --diff-filter=U | while read -r file; do
        echo -e "${BLUE}Processing:${NC} ${file}"
        case "$file" in
            README.md|CHANGELOG.md|CONTRIBUTING.md|docs/*.md|agent_reach/guides/*.md|agent_reach/skill/SKILL.md|TRANSLATION_STATUS.md)
                echo "  → Keeping fork documentation version"
                git checkout --ours "$file"
                git add "$file"
                ;;
            *.py|pyproject.toml|constraints.txt|tests/*.py|scripts/*.sh)
                echo "  → Accepting upstream code/config version"
                git checkout --theirs "$file"
                git add "$file"
                ;;
            *)
                echo "  → Manual resolution required for ${file}"
                ;;
        esac
    done

    if [ -n "$(git diff --name-only --diff-filter=U)" ]; then
        echo -e "${RED}Unresolved conflicts remain.${NC}"
        echo "Resolve them manually, then run: git commit"
        exit 1
    fi
fi
echo ""

echo -e "${YELLOW}[5/6]${NC} Running sync validation..."
python3 scripts/validate_sync.py
echo -e "${GREEN}✓${NC} Validation passed"
echo ""

echo -e "${YELLOW}[6/6]${NC} Creating merge commit..."
git commit --no-edit
echo -e "${GREEN}✓${NC} Merge committed on ${TARGET_BRANCH}"
echo ""

if [ "${AUTO_PUSH}" = "1" ]; then
    echo -e "${YELLOW}Pushing current branch to origin...${NC}"
    git push origin "${TARGET_BRANCH}"
    echo -e "${GREEN}✓${NC} Pushed to origin/${TARGET_BRANCH}"
else
    echo -e "${BLUE}Auto-push disabled.${NC} Review the merge, then push manually if everything looks right."
    echo "To push now: git push origin ${TARGET_BRANCH}"
fi
