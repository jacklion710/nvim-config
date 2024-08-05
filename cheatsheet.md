# Neovim Custom Key Bindings Cheat Sheet

## File Explorer (NvimTree)

<leader>pv : Toggle NvimTree
<leader>e : Toggle NvimTree (duplicate)
<C-n> : Toggle focus between NvimTree and file content
<C-w>h : Move focus to NvimTree
<C-w>l : Move focus to file content
a : Add new file/directory
o : Create new file
O : Create new directory
d : Delete file/directory
r : Rename file/directory
m : Move file/directory (then navigate and press 'p')
x : Cut file/directory
p : Paste file/directory
y : Copy file/directory name
Y : Copy relative path
gy : Copy absolute path
<C-v> : Open file in vertical split
<C-x> : Open file in horizontal split
<C-t> : Open file in new tab
<CR> : Open file
R : Refresh NvimTree

## Movement and Editing

J (visual) : Move selected lines down
K (visual) : Move selected lines up
J (normal) : Join lines and keep cursor in place
<C-d> : Scroll down and center cursor
<C-u> : Scroll up and center cursor
n : Next search result and center view
N : Previous search result and center view
<leader>p : Paste without yanking deleted text
<leader>y : Yank to system clipboard
<leader>Y : Yank line to system clipboard
<leader>d : Delete without yanking
<C-c> : Exit insert mode (alternative to Esc)

## LSP and Formatting

<leader>zig : Restart LSP
<leader>f : Format buffer

## Navigation

<C-k> : Next quickfix item
<C-j> : Previous quickfix item
<leader>k : Next location list item
<leader>j : Previous location list item

## Search and Replace

<leader>s : Search and replace word under cursor

## File Operations

<leader>x : Make current file executable

## Code Snippets

<leader>ee : Insert error handling snippet (Go)

## Configuration

<leader>vpp : Open Packer configuration file
<leader>cs : Open this cheat sheet

## Miscellaneous

Q : No operation (disabled)
<C-f> : Open tmux sessionizer
<leader><leader> : Source current file
RunPython : Run current Python file

## Cellular Automaton Effects

<leader>mr : Trigger "make it rain" effect
<leader>mR : Reset file to last saved state

## Undo/Redo

u : Undo last change
<C-r>: Redo last undone change
g- : Go to older text state
g+ : Go to newer text state

## LSP Keybindings

gf : LSP finder
gD : Go to declaration
gd : Peek definition
gi : Go to implementation
<leader>ca : Code action
<leader>rn : Rename
<leader>D : Show line diagnostics
<leader>d : Show cursor diagnostics
[d : Jump to previous diagnostic
]d : Jump to next diagnostic
K : Hover documentation
<leader>o : Toggle outline
<leader>vws : Workspace symbol
<leader>vd : Open float
<leader>vrr : References
<C-h> (insert) : Signature help

## TypeScript Specific

<leader>rf : Rename file
<leader>oi : Organize imports
<leader>ru : Remove unused
