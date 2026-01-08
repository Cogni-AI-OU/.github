# Copilot Plus Agent - Usage Examples

This document demonstrates the key features and usage patterns of the Copilot Plus agent.

## Overview

Copilot Plus is an enhanced coding agent with:

- **Critical thinking**: Never gives up, tries alternatives when tools fail
- **Context awareness**: Checks file sizes before viewing, uses filtering for large outputs
- **Robust execution**: Attempts to install missing commands, handles errors gracefully
- **Self-improvement**: Updates documentation based on challenges encountered
- **Autonomous problem-solving**: Works through complex issues independently

## Key Features

### 1. Context-Aware File Viewing

Copilot Plus automatically checks file sizes before reading them to preserve context window:

**Before:**

```bash
cat large_file.log  # Dumps entire file, consuming context
```

**With Copilot Plus:**

```bash
# Check file size first
wc -l large_file.log
# For large files, use filtering
head -n 50 large_file.log  # View beginning
tail -n 50 large_file.log  # View ending
grep "ERROR" large_file.log | head -20  # Search for specific content
```

### 2. Smart Command Output Filtering

Handles commands that produce large output:

**Example: Package Installation**

```bash
# Check output size first
npm install 2>&1 | wc -l

# Filter to show only errors/warnings
npm install 2>&1 | grep -E "error|warn" -i || echo "Install successful"
```

**Example: Log Analysis**

```bash
# Don't dump entire log
docker logs container 2>&1 | grep -i error | head -50

# Show summary instead of everything
./run_tests.sh 2>&1 | grep -E "fail|error|pass" -i | head -30
```

### 3. Robust Command Execution

Automatically handles missing commands:

**Example: JSON Processing**

```bash
# Copilot Plus checks if jq exists
if ! command -v jq &> /dev/null; then
  echo "Installing jq..."
  apt-get update && apt-get install -y jq
fi

# If jq still not available, try alternative
jq . file.json 2>/dev/null || python3 -m json.tool < file.json
```

**Example: YAML Processing**

```bash
# Try yq, fallback to python
yq eval file.yaml 2>/dev/null || \
python3 -c "import yaml; print(yaml.safe_load(open('file.yaml')))"
```

### 4. Failure Recovery Patterns

Never gives up when facing challenges:

**Example: File Not Readable**

```bash
# Try reading file
if [ ! -r file.txt ]; then
  # Check permissions
  ls -la file.txt
  # Try to fix permissions
  chmod +r file.txt || sudo chmod +r file.txt
fi
cat file.txt
```

**Example: Command Not Found**

```bash
# Check if command exists
command -v tool_name &> /dev/null || {
  echo "Tool not found, trying to install..."
  apt-get update && apt-get install -y tool_name
}
```

### 5. Critical Thinking Workflow

Copilot Plus follows a structured approach:

1. **Deep Analysis**: Understand the core problem and constraints
2. **Planning**: Break down into testable steps with dependencies
3. **Validation**: Check prerequisites before executing
4. **Execution**: Use filtering and fallbacks
5. **Verification**: Test changes thoroughly
6. **Self-Improvement**: Update documentation based on lessons learned

## Usage Scenarios

### Scenario 1: Debugging a Large Log File

**Problem**: Application log is 10,000+ lines

**Copilot Plus Approach:**

```bash
# Check file size
wc -l app.log
# Output: 12543 app.log

# Don't dump entire file - search for errors
echo "Searching for errors in last 1000 lines..."
tail -1000 app.log | grep -i error | head -20

# Find exception stacktraces
echo "Looking for exceptions..."
grep -B 3 -A 10 "Exception" app.log | head -50

# Count error types
echo "Error summary:"
grep -i error app.log | awk '{print $NF}' | sort | uniq -c | sort -rn | head -10
```

### Scenario 2: Working with Missing Tools

**Problem**: Need to process JSON but jq is not installed

**Copilot Plus Approach:**

```bash
# Try jq first
if command -v jq &> /dev/null; then
  jq '.results[]' data.json
else
  echo "jq not found, installing..."
  apt-get update && apt-get install -y jq && jq '.results[]' data.json || \
  {
    echo "jq installation failed, using Python fallback..."
    python3 -c "import json; data=json.load(open('data.json')); print(data['results'])"
  }
fi
```

### Scenario 3: Exploring Large Codebase

**Problem**: Repository has 200+ files

**Copilot Plus Approach:**

```bash
# Get overview without dumping everything
echo "Repository structure:"
find . -type f -name "*.py" | wc -l
echo "Python files found"

# Find largest files
echo "Largest files:"
find . -name "*.py" -exec wc -l {} + | sort -rn | head -10

# Search for specific patterns
echo "Files containing TODO comments:"
grep -rl "TODO" --include="*.py" | head -20

# For files to read, check size first
for file in $(find . -name "*.py" -exec wc -l {} + | sort -rn | head -5 | awk '{print $2}'); do
  lines=$(wc -l < "$file")
  echo "$file: $lines lines"
  if [ $lines -gt 500 ]; then
    echo "  (too large, will read selectively)"
  fi
done
```

### Scenario 4: Build Failure Diagnosis

**Problem**: Build fails with unknown error

**Copilot Plus Approach:**

```bash
# Run build with filtered output
echo "Running build and capturing errors..."
npm run build 2>&1 | tee build.log | grep -E "error|fail" -i || {
  echo "Build appears successful"
  exit 0
}

# Analyze failure
echo "Build failed. Analyzing errors..."
grep -i error build.log | head -20

# Check for missing dependencies
echo "Checking for dependency issues..."
grep -i "cannot find\|not found\|missing" build.log | head -10

# Try to identify and install missing tools
if grep -q "typescript.*not found" build.log; then
  echo "TypeScript missing, installing..."
  npm install -g typescript
  echo "Retrying build..."
  npm run build
fi
```

## Best Practices

### File Operations

1. **Always check size first**: `wc -l file.txt`
2. **Use head/tail for large files**: Show beginning and end only
3. **Search instead of dumping**: `grep pattern file.txt | head -20`
4. **Read in chunks**: `sed -n '100,200p' file.txt` for specific ranges

### Command Execution

1. **Check command exists**: `command -v tool &> /dev/null`
2. **Try to install if missing**: `apt-get install -y tool`
3. **Use fallback alternatives**: Try multiple tools that accomplish the same task
4. **Handle errors gracefully**: Use `||` for fallback commands

### Problem Solving

1. **Think before acting**: Plan approach and anticipate issues
2. **Never give up easily**: Try alternatives when primary approach fails
3. **Test thoroughly**: Verify changes work correctly
4. **Update documentation**: Record solutions for future reference

## Integration with Skills

Copilot Plus works seamlessly with the available skills:

- **[context-aware-ops](.github/skills/context-aware-ops/SKILL.md)**: Advanced
  patterns for managing large resources
- **[robust-commands](.github/skills/robust-commands/SKILL.md)**: Comprehensive
  command fallback and error recovery strategies
- **[git](.github/skills/git/SKILL.md)**: Non-interactive git operations
- **[github-actions](.github/skills/github-actions/SKILL.md)**: CI/CD debugging

## Common Patterns

### Pattern 1: Check-Try-Fallback

```bash
# Check if tool exists
if ! command -v tool &> /dev/null; then
  # Try to install
  apt-get update && apt-get install -y tool
fi

# If still not available, use alternative
tool command 2>/dev/null || alternative_command
```

### Pattern 2: Size-Check-Filter

```bash
# Check size
lines=$(wc -l < file.txt)

# Apply appropriate strategy
if [ $lines -gt 1000 ]; then
  # Large file - use filtering
  head -50 file.txt && echo "... ($lines lines total)"
else
  # Small file - show all
  cat file.txt
fi
```

### Pattern 3: Capture-Analyze-Fix

```bash
# Capture output
output=$(command 2>&1) || {
  # Analyze failure
  echo "$output" | grep -i error | head -10

  # Try to fix and retry
  fix_command
  command
}
```

## Self-Improvement Examples

After completing tasks, Copilot Plus updates documentation:

**Example 1: New Command Pattern**

If a new workaround is discovered:

```markdown
## Found New Pattern

When processing YAML files and yq is not available:

# Use Python with pyyaml
python3 -c "import yaml, json; print(json.dumps(yaml.safe_load(open('file.yaml'))))" | jq .
```

**Example 2: Common Pitfall**

If a common issue is encountered:

```markdown
## Avoid This Pitfall

When running npm install in CI environments, node_modules can be very large.
Always use: npm install --prefer-offline --no-audit 2>&1 | grep -E "error|warn" -i
```

## Troubleshooting

### Issue: Agent dumps large files

**Solution**: The agent should be checking file sizes first. If this happens, remind it to use
the context-aware-ops skill patterns.

### Issue: Agent gives up on command failures

**Solution**: The agent should try alternatives. Reference the robust-commands skill for
fallback patterns.

### Issue: Context window fills up

**Solution**: The agent should use filtering more aggressively. Suggest specific grep/head/tail
patterns for the situation.

## Summary

Copilot Plus is designed to be:

- **Autonomous**: Solves problems independently
- **Resourceful**: Finds workarounds when primary approaches fail
- **Efficient**: Manages context window wisely
- **Persistent**: Doesn't give up when facing challenges
- **Thorough**: Tests and verifies everything
- **Self-improving**: Updates documentation based on lessons learned

Use it for complex development tasks that require critical thinking and robust problem-solving!
