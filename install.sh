#!/bin/bash

# Colors for beautiful output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}==========================================${NC}"
echo -e "${BLUE}       Installing Coode-Rubika Tool       ${NC}"
echo -e "${BLUE}==========================================${NC}"

# 1. Check if Python exists
echo -e "${YELLOW}[*] Checking Python...${NC}"
if ! command -v python &> /dev/null; then
    echo -e "${RED}[!] Python not found. Installing Python...${NC}"
    pkg install python -y
else
    echo -e "${GREEN}[+] Python is already installed.${NC}"
fi

# 2. Create storage directory in Local Bin
echo -e "${YELLOW}[*] Setting up directory...${NC}"
mkdir -p $HOME/.local/bin

# 3. Move main file (assumes the file name is coode_rt.py)
echo -e "${YELLOW}[*] Moving script to system path...${NC}"
if [ -f "coode_rt.py" ]; then
    cp coode_rt.py $HOME/.local/bin/coode_rt.py
    echo -e "${GREEN}[+] Script moved to $HOME/.local/bin/coode_rt.py${NC}"
else
    echo -e "${RED}[!] Error: coode_rt.py not found in current directory!${NC}"
    exit 1
fi

# 4. Create Alias with custom name: fitrey
echo -e "${YELLOW}[*] Creating command 'fitrey'...${NC}"
# Check if this Alias was already added (to prevent duplicates)
if ! grep -q "alias fitrey=" ~/.bashrc; then
    echo "alias fitrey='python $HOME/.local/bin/coode_rt.py'" >> ~/.bashrc
    echo -e "${GREEN}[+] Command 'fitrey' added successfully!${NC}"
else
    echo -e "${YELLOW}[!] Command 'fitrey' already exists in .bashrc.${NC}"
fi

echo -e "${BLUE}==========================================${NC}"
echo -e "${GREEN}   INSTALLATION COMPLETE!${NC}"
echo -e "${GREEN}   Now type: source ~/.bashrc${NC}"
echo -e "${GREEN}   Then you can use: fitrey${NC}"
echo -e "${BLUE}==========================================${NC}"
