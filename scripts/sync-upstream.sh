#!/bin/bash
# Agent-Reach-Kr Upstream Sync Script
# 업스트림 저장소의 변경사항을 가져와 한국어 번역을 보존하며 병합합니다

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}Agent-Reach-Kr Upstream Sync${NC}"
echo -e "${BLUE}========================================${NC}"
echo ""

# 1. Fetch upstream
echo -e "${YELLOW}[1/5]${NC} Fetching upstream changes..."
git fetch upstream
echo -e "${GREEN}✓${NC} Upstream fetched"
echo ""

# 2. Check if there are any changes
echo -e "${YELLOW}[2/5]${NC} Checking for upstream changes..."
LOCAL_COMMIT=$(git rev-parse HEAD)
UPSTREAM_COMMIT=$(git rev-parse upstream/main)

if [ "$LOCAL_COMMIT" = "$UPSTREAM_COMMIT" ]; then
    echo -e "${GREEN}✓${NC} Already up to date with upstream!"
    exit 0
fi

echo -e "${BLUE}Changes found:${NC}"
git log HEAD..upstream/main --oneline
echo ""

# 3. Show what files will change
echo -e "${YELLOW}[3/5]${NC} Files that will be modified:"
git diff --stat HEAD upstream/main
echo ""

# 4. Merge with strategy for Korean translations
echo -e "${YELLOW}[4/5]${NC} Merging upstream changes..."
echo -e "${BLUE}Strategy:${NC}"
echo "  - Python code files: Accept upstream changes"
echo "  - Korean translations: Preserve our versions"
echo "  - New files: Accept upstream additions"
echo ""

# Attempt merge with automatic conflict resolution
git merge -X theirs upstream/main --no-edit 2>/dev/null || {
    echo -e "${RED}✗${NC} Merge conflicts detected!"
    echo ""
    echo -e "${YELLOW}Resolving conflicts...${NC}"

    # Find and resolve conflicted files
    git diff --name-only --diff-filter=U | while read -r file; do
        echo -e "${BLUE}Processing: $file${NC}"

        case "$file" in
            README.md|CHANGELOG.md|CONTRIBUTING.md|docs/*.md|agent_reach/guides/*.md|agent_reach/skill/SKILL.md|TRANSLATION_STATUS.md)
                echo "  → Keeping Korean translation (ours)"
                git checkout --ours "$file"
                git add "$file"
                ;;
            *.py|pyproject.toml|constraints.txt|tests/*.py|scripts/*.sh)
                echo "  → Accepting upstream code (theirs)"
                git checkout --theirs "$file"
                git add "$file"
                ;;
            *)
                echo "  → Manual resolution required"
                ;;
        esac
    done

    # Complete the merge
    if [ -n "$(git diff --name-only --diff-filter=U)" ]; then
        echo -e "${YELLOW}Some conflicts require manual resolution${NC}"
        echo "Please resolve conflicts and run: git commit"
    else
        git commit --no-edit
    fi
}

echo -e "${GREEN}✓${NC} Merge completed"
echo ""

# 5. Push to origin
echo -e "${YELLOW}[5/5]${NC} Pushing to GitHub..."
git push origin main
echo -e "${GREEN}✓${NC} Pushed to origin/main"
echo ""

echo -e "${GREEN}========================================${NC}"
echo -e "${GREEN}Sync completed successfully!${NC}"
echo -e "${GREEN}========================================${NC}"
