cat << 'EOF' > test3.md
# Test
EOF

ex -s test3.md << 'VIMEOF'
set hidden
argdo call append('$', ['', '## Maintenance', '', 'Note that this file should be updated if outdated or steps/examples are not working.']) | update
qa!
VIMEOF

cat test3.md
